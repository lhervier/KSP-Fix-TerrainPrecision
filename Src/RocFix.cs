using System;
using System.Collections.Generic;
using System.Reflection;
using HarmonyLib;
using UnityEngine;

namespace com.github.lhervier.ksp.fix.terrainprecision
{
    /// <summary>
    /// Places Breaking Ground's surface features (ROCs) on the ground they were built on, at the same height
    /// at every load.
    ///
    /// Stock KSP places them as it places the terrain scatter (see <see cref="ScatterFix"/>): each feature at
    /// a vertex of its quad, in the quad's own coordinates, under a holder that hangs from the body's terrain
    /// sphere with a local position hundreds of kilometres long. The holder is drawn with a matrix rounded
    /// otherwise than the quad's position, and unlike stock rocks the features carry a collider: they move,
    /// for the eye and for the physics, by a few centimetres from load to load. The terrain fix moves the
    /// quad, not the holder, so it does not settle this.
    ///
    /// Here each holder hangs from its own quad, at no offset. Stock gives surface features to the quads of
    /// the highest subdivision level only. It moves stock objects, the holders, away from where other mods
    /// may look for them: it has a setting of its own to turn it off.
    /// </summary>
    internal static class RocFix
    {
        // Set once the patches are in place. A holder is only ever moved while it is set.
        private static bool _active;

        // The stock holder of the surface features of a quad. Internal to KSP, as are the fields read here,
        // hence the reflection.
        private static Type _holderType;

        // Fields of the holder: its quad, cleared by stock when the holder goes back to its pool.
        private static AccessTools.FieldRef<object, PQ> _holderQuad;

        // Private field of LandClassROC: the object its holders hang from while they are not in use.
        private static AccessTools.FieldRef<LandClassROC, GameObject> _rocParent;

        // Spheres already reported, so that this message appears once per body and per session.
        private static readonly HashSet<PQS> _announced = new HashSet<PQS>();

        // Whether the missing pool container has been reported already.
        private static bool _warnedNoContainer;

        /// <summary>
        /// Applies the patches of the surface features, and turns them on once both are in place. Throws when
        /// a patch cannot be applied: the surface features are then left exactly as stock places them.
        /// </summary>
        public static void Install(Harmony harmony)
        {
            _holderType = AccessTools.TypeByName("PQSMod_ROCScatterQuad")
                ?? throw new MissingMemberException("PQSMod_ROCScatterQuad not found");
            _holderQuad = AccessTools.FieldRefAccess<PQ>(_holderType, "quad");
            _rocParent = AccessTools.FieldRefAccess<LandClassROC, GameObject>("rocParent");
            harmony.CreateClassProcessor(typeof(SetupPatch)).Patch();
            harmony.CreateClassProcessor(typeof(DestroyQuadPatch)).Patch();
            _active = true;
        }

        // ==========================================================================
        // A holder is given a quad
        // ==========================================================================

        /// <summary>
        /// Hangs a holder of surface features from the quad it was just set up for, at no offset, when the
        /// quad allows it. Otherwise, or if anything fails, the holder stays where stock placed it.
        /// </summary>
        private static void HangFromQuad(MonoBehaviour holder, PQ quad)
        {
            if (!_active || holder == null || quad == null)
            {
                return;
            }
            if (!Utils.CanHangFrom(quad))
            {
                if (Log.IsDebugEnabled)
                {
                    Log.Debug($"surface feature '{holder.name}' on quad '{quad.name}': left where stock places it");
                }
                return;
            }
            try
            {
                PQS sphere = quad.sphereRoot;
                bool announce = !_announced.Contains(sphere);

                // Everything that is only needed for the log is computed first, while the holder is still
                // where stock put it.
                double offsetMm = announce || Log.IsDebugEnabled
                    ? Utils.DrawnOffsetMm(holder.transform, quad) : 0.0;

                // The features are placed at quad.verts, in the quad's own frame, and their up direction is
                // computed from the holder's rotation, which stays the sphere's either way. The features are
                // built after this, on the first update of a visible quad, so they are placed under the
                // holder already moved.
                Transform holderTransform = holder.transform;
                holderTransform.SetParent(quad.transform, false);
                holderTransform.localPosition = Vector3.zero;
                holderTransform.localRotation = Quaternion.identity;
                holderTransform.localScale = Vector3.one;

                if (announce)
                {
                    _announced.Add(sphere);
                    Log.Info($"{sphere.name}: surface features drawn from their terrain quads"
                        + $" (first holder was {offsetMm:+0.00;-0.00;0.00} mm off)");
                }
                if (Log.IsDebugEnabled)
                {
                    Log.Debug($"surface feature '{holder.name}' on quad '{quad.name}':"
                        + $" hung from its quad, was drawn {offsetMm:+0.00;-0.00;0.00} mm off it");
                }
            }
            catch (Exception e)
            {
                Log.Error($"Could not hang a surface feature holder from quad '{quad.name}',"
                    + $" it is left as stock places it: {e}");
            }
        }

        [HarmonyPatch]
        private static class SetupPatch
        {
            private static MethodBase TargetMethod()
            {
                return AccessTools.Method(_holderType, "Setup");
            }

            // After the stock method, which gives the holder its quad and its 600 km local position.
            private static void Postfix(MonoBehaviour __instance, PQ quad)
            {
                HangFromQuad(__instance, quad);
            }
        }

        // ==========================================================================
        // A holder goes back to its pool
        // ==========================================================================

        /// <summary>
        /// Hangs a holder that <see cref="HangFromQuad"/> moved back from the container of its pool, at the
        /// identity. Does nothing to any other holder.
        /// </summary>
        private static void ReturnToPool(LandClassROC roc, MonoBehaviour holder)
        {
            // No check on _active: this only undoes what HangFromQuad did, recognised by the hierarchy itself.
            // Unity objects are compared with == on purpose, which also catches destroyed ones.
            if (holder == null)
            {
                return;
            }
            PQ quad = _holderQuad(holder);
            if (quad == null || holder.transform.parent != quad.transform)
            {
                return;
            }
            try
            {
                // Stock calls this from the quad's onDestroy, before the quad itself goes back to the PQS
                // cache, where it is deactivated and later reused elsewhere. The holder must not go with it:
                // stock takes its holders back from its pool and sets them up again under that container.
                GameObject container = _rocParent(roc);
                Transform back;
                if (container != null)
                {
                    back = container.transform;
                }
                else
                {
                    // Not expected. The sphere is where stock creates that container, at the identity, so a
                    // holder hung there is placed the same way.
                    back = quad.sphereRoot.transform;
                    if (!_warnedNoContainer)
                    {
                        _warnedNoContainer = true;
                        Log.Warning($"surface feature '{roc.rocName}' has no pool container,"
                            + " its holders are handed back to the terrain sphere instead");
                    }
                }

                Transform holderTransform = holder.transform;
                holderTransform.SetParent(back, false);
                holderTransform.localPosition = Vector3.zero;
                holderTransform.localRotation = Quaternion.identity;
                holderTransform.localScale = Vector3.one;

                if (Log.IsTraceEnabled)
                {
                    Log.Trace($"surface feature '{roc.rocName}' on quad '{quad.name}': holder back in its pool");
                }
            }
            catch (Exception e)
            {
                Log.Error($"Could not hand a surface feature holder of quad '{quad.name}' back to its pool: {e}");
            }
        }

        [HarmonyPatch(typeof(LandClassROC), "DestroyQuad")]
        private static class DestroyQuadPatch
        {
            // Before the stock method, not after: it clears the holder's quad before anything else is done.
            private static void Prefix(LandClassROC __instance, MonoBehaviour q)
            {
                ReturnToPool(__instance, q);
            }
        }
    }
}
