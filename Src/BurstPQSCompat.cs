using System;
using System.Collections.Generic;
using System.Reflection;
using HarmonyLib;
using UnityEngine;

namespace com.github.lhervier.ksp.terrainprecisionfix
{
    /// <summary>
    /// Tells the terrain and scatter fixes which bodies BurstPQS places the terrain of, so that they leave the
    /// terrain to it there and keep the scatter on it.
    ///
    /// BurstPQS builds the terrain in place of stock, in Burst-compiled jobs, and since its 1.0.26 places every
    /// quad in double precision itself: on the bodies it builds, the ground no longer moves, which is what the
    /// terrain fix does. With both, each would place the same quads, in two postfixes of PQ.SetupQuad that run
    /// in an order nothing fixes. So, on those bodies only:
    /// - the terrain fix steps back. BurstPQS gives a whole body back to stock when one of its terrain mods has
    ///   no Burst version (the Earth, the Moon and Mars of Real Solar System 20.1.3 do): there the terrain fix
    ///   goes on correcting the ground, as without BurstPQS;
    /// - the scatter fix hangs a holder from its quad whatever the quad hangs from. Stock keeps every quad that
    ///   carries scatter in the sphere's local space storage, which the scatter fix relies on; BurstPQS puts
    ///   quads there only once the world turns with the body, so the quads built as a scene opens, those
    ///   around the craft, hang from the sphere when their scatter is set up. BurstPQS builds the mesh of a
    ///   quad against the quad's own transform wherever it hangs, so a holder drawn with that transform is
    ///   drawn with the ground.
    /// The statics and ground anchor fixes do not depend on who places the terrain.
    ///
    /// BurstPQS puts its component, BurstPQS.BatchPQS, on every terrain sphere, and keeps whether it gave the
    /// sphere back to stock in an internal property, Fallback, read here by reflection. Should that property be
    /// missing or unreadable, every sphere carrying the component is taken as placed by BurstPQS: the terrain
    /// fix then steps back on all of them, and never places a quad BurstPQS places too.
    /// </summary>
    internal static class BurstPQSCompat
    {
        private const string BatchPQSTypeName = "BurstPQS.BatchPQS";
        private const string FallbackPropertyName = "Fallback";

        // Null when BurstPQS is not installed.
        private static readonly Type _batchPQSType;

        // The getter of BatchPQS.Fallback, or null when it could not be found.
        private static readonly MethodInfo _fallbackGetter;

        // Spheres already reported, so that this message appears once per body and per session.
        private static readonly HashSet<PQS> _announced = new HashSet<PQS>();

        // Whether a failed read of Fallback has been reported already.
        private static bool _warnedUnreadable;

        static BurstPQSCompat()
        {
            _batchPQSType = AccessTools.TypeByName(BatchPQSTypeName);
            if (_batchPQSType == null)
            {
                return;
            }
            MethodInfo getter = AccessTools.PropertyGetter(_batchPQSType, FallbackPropertyName);
            if (getter != null && getter.ReturnType == typeof(bool) && getter.GetParameters().Length == 0)
            {
                _fallbackGetter = getter;
                Log.Info("BurstPQS installed: the terrain fix leaves it the bodies it builds");
            }
            else
            {
                Log.Warning($"BurstPQS installed, but {BatchPQSTypeName}.{FallbackPropertyName} was not found:"
                    + " the terrain fix leaves it every body, including those it gives back to stock");
            }
        }

        /// <summary>
        /// Whether BurstPQS places the terrain of <paramref name="sphere"/> itself. False when BurstPQS is not
        /// installed, or has given that sphere back to stock.
        /// </summary>
        public static bool PlacesTerrain(PQS sphere)
        {
            if (_batchPQSType == null || sphere == null)
            {
                return false;
            }
            Component batchPQS = sphere.GetComponent(_batchPQSType);
            if (batchPQS == null)
            {
                return false;
            }

            // BurstPQS decides once all of the sphere's terrain mods are set up, before it builds any quad, and
            // again if they are set up again: read each time rather than kept.
            bool places = !IsFallback(batchPQS);
            if (_announced.Add(sphere))
            {
                // Named after its body, as the terrain fix names it: a sphere keeps the name of the stock body
                // it was made from (Kerbin for the Earth of Real Solar System).
                CelestialBody body = PlanetFrame.BodyOf(sphere);
                string name = body != null ? body.bodyName : sphere.name;
                Log.Info(places
                    ? $"{name}: terrain placed by BurstPQS"
                    : $"{name}: terrain given back to stock by BurstPQS");
            }
            return places;
        }

        /// <summary>
        /// Whether BurstPQS gave its sphere back to stock. False when that cannot be read, which makes the
        /// sphere count as placed by BurstPQS.
        /// </summary>
        private static bool IsFallback(Component batchPQS)
        {
            if (_fallbackGetter == null)
            {
                return false;
            }
            try
            {
                return (bool)_fallbackGetter.Invoke(batchPQS, null);
            }
            catch (Exception e)
            {
                if (!_warnedUnreadable)
                {
                    _warnedUnreadable = true;
                    Log.Warning($"Could not read {BatchPQSTypeName}.{FallbackPropertyName}, the sphere is taken as"
                        + $" placed by BurstPQS: {e.Message}");
                }
                return false;
            }
        }
    }
}
