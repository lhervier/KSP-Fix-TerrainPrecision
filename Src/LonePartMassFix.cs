using HarmonyLib;

namespace com.github.lhervier.ksp.fix.terrainprecision
{
    /// <summary>
    /// Lets a part lying alone on the ground settle with its own mass.
    ///
    /// Every time a craft of a single part goes off rails landed or on the launch pad, stock makes the part much
    /// heavier for its kinematic delay, 3 seconds by default (ModuleCargoPart.MakePartSettle): 4 t between
    /// 0.8 g and 1.1 g, 20 t below. On a ground rebuilt at another height at every load, that softened the pops
    /// of a part reloaded inside the ground; on the ground this mod fixes, no part starts inside it any more.
    /// What is left is a part with a suspension tuning it to the extra mass, and thrown up when its own mass
    /// comes back. Here the part gets its own mass back as soon as stock raises it.
    /// </summary>
    internal static class LonePartMassFix
    {
        /// <summary>
        /// Applies the patch that gives a part lying alone its own mass back. Throws when the patch cannot be
        /// applied: parts are then made heavier as stock makes them.
        /// </summary>
        public static void Install(Harmony harmony)
        {
            harmony.CreateClassProcessor(typeof(UnpackPatch)).Patch();
        }

        // MakePartSettle keeps the part's mass in preSettlingPrefabMass and raises prefabMass before its first
        // yield, so both are set when OnPartUnpack returns; at the end of its wait, it sets prefabMass back to
        // preSettlingPrefabMass, which is then the mass already given back. Breaking Ground's deployed
        // experiments override OnPartUnpack without calling it, and are left alone.
        [HarmonyPatch(typeof(ModuleCargoPart), nameof(ModuleCargoPart.OnPartUnpack))]
        private static class UnpackPatch
        {
            private static readonly AccessTools.FieldRef<ModuleCargoPart, float> PreSettlingPrefabMass =
                AccessTools.FieldRefAccess<ModuleCargoPart, float>("preSettlingPrefabMass");

            private static void Postfix(ModuleCargoPart __instance)
            {
                Part part = __instance.part;
                float own = PreSettlingPrefabMass(__instance);
                if (part == null || own <= 0f || part.prefabMass == own)
                {
                    return;
                }
                Log.Debug($"Lone part mass fix: '{part.partInfo?.title}' given back its own mass, {own:F3} t,"
                    + $" instead of {part.prefabMass:F0} t");
                part.prefabMass = own;
            }
        }
    }
}
