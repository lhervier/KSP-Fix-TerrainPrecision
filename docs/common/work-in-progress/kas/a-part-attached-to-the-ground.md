# KAS: a part attached to the ground

Part of [Terrain Precision Fix](../../../../README.md), [what the fixes share](../../README.md#work-in-progress): one point of the work in progress, on KAS.

**Status: planned — read in the source, not played.** [Kerbal Attachment System](https://github.com/ihsoft/KAS)
links parts and crafts with joints of its own, and some of its parts hold on to the ground. KAS has no
Harmony patch and does not touch the terrain, the statics or the scatter. Three of its features meet what
this mod changes.

**The harpoon in the ground.** The HP-01 Harpoon (`KASModuleDart`) attaches to the ground, or to a building,
when it hits a collider that has no rigidbody. It then holds on with a joint that has no connected body:
pinned to a point of the world, not to the terrain quad nor to the building. This mod places that quad more
precisely, and moves the statics out of the terrain sphere in flight; neither changes what the joint holds.
KAS does not keep a surface attachment across a load (`CheckSettingsConsistency` resets it), so a load
cannot move it either.

**Docking two crafts with a KAS link.** When a KAS link docks two crafts (the TJ-1 and TJ-2 telescopic
joints in docking mode, `LinkUtilsImpl.CoupleParts`), KAS first removes the joint the game adds to hold a
landed craft still once it has stopped (`Vessel.AddRBAnchor`). That joint is not the stock Ground Anchor's
rivet, which this mod's [ground anchor fix](../../../ground-anchor/README.md) touches. A craft that carries a
Ground Anchor is still riveted after the docking, and this mod handles it at the next load like any anchored
craft.

**The pylons.** The GP-20 and BGP-400 pylons are ordinary cargo parts, without the module of the Ground
Anchor (`ModuleGroundPart`): set on the ground, each is a landed craft like any other, and rests on the
corrected ground as one.

*What the player would see if this mod broke something:* a harpoon that pulls loose or drags the craft it
tethers as soon as it bites into the ground or a building; a base docked by a KAS link to an anchored craft
that jumps or sinks at each load; a pylon that jumps at each load.

*The test.* An install with KSP Community Fixes, KAS and this mod, on Kerbin, by the KSC:

1. A rover with a W-50 winch and an HP-01 Harpoon: fire it into the ground, then into the side of a
   building, and pull on the cable with the winch.
2. A small base with a Ground Anchor, and a second craft linked to it by a TJ-1 in docking mode, then the
   save loaded six times, as in
   [Checking the culprit: anchoring a base](../../../ground-anchor/checking/anchoring.md#the-protocol).
3. A GP-20 pylon set on the ground in EVA, then the save loaded six times.

Each without this mod, then with it.

*What should happen.* With this mod as without it, the harpoon should hold where it bit. With this mod, the
docked base and the pylon should stand at the same height at every load.
