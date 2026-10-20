# Promised Worlds: its bodies

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on Promised Worlds.

**Status: planned — read in the source, not played.** [Promised Worlds](https://github.com/PromisedWorlds/PromisedWorlds)
is a planet pack that recreates the star systems planned for KSP 2, Debdeb and Tuun, through
[Kopernicus](https://github.com/Kopernicus/Kopernicus). Three things set it apart from the planet pack of
[Kopernicus: a body from a planet pack](../kopernicus/a-body-from-a-planet-pack.md), and each touches the
terrain this mod places.

**Terrain mods of its own.** It ships PQSMods that shape its bodies: `VertexHeightOblateAdvanced`, which
flattens Axod and Gup at the poles, `VertexMitchellNetravaliHeightMap`, and `VertexHeightDeformity` and
`VertexHeightMap16` from Kopernicus Expansion. Read in their source, all of them only write the height of a
vertex (`OnVertexBuildHeight`). This mod reads that height after them, in `PQS.BuildVertexSurfaceRelative`,
exactly as stock does, so the shape they give should be kept. If it were not, the ground would no longer be
where the game computes it: a craft would sink into it or float above it on landing.

**Star systems far from the Sun.** Debdeb orbits the Sun at 2.554 × 10¹⁴ m and Tuun at 3.771 × 10¹⁴ m, a
hundred times more with the pack's `DistanceFactor = 100`. At that distance a double only holds a position
to 31 to 62 mm, the very size of the defect this mod removes. Read in the stock code, it does not reach the
ground under a craft: `OrbitPhysicsManager.setDominantBody` reverses the orbit of the body the craft is
near and of all its parents, and `OrbitDriver.updateFromParameters` then works out each parent from its
child. The rounding falls on the Sun, not on the body this mod places the terrain of.

**Rescaled bodies.** With [Sigma Dimensions](https://github.com/Sigma88/Sigma-Dimensions), the pack's
`Rescale` makes every body 2.5 or 10 times larger, and forces 10 times with Real Solar System. The
[safeguard](../../../common/safeguard.md) grows with the radius of a body, as it does on the Earth of Real
Solar System.

*What the player would see if this mod broke something:* a craft landed on one of these bodies that jumps
or sinks at each load, or a terrain this mod leaves alone, with one safeguard warning per body in the log.

*The test.* An install with Kopernicus, KSP Community Fixes, Promised Worlds with its Debdeb system, and
this mod. A craft landed on Gurdamma, whose 580 km radius gives a float the same 62.5 mm step as Kerbin's,
then one on Axod, flattened at the poles: each loaded six times, as in
[Checking the ground: loading the same save](../../checking/loading.md#the-craft-over-six-loads), without
this mod and with it. The log should carry `Gurdamma: terrain placed in double precision` and the same line
for Axod, and no safeguard warning. Then the same on Gurdamma with `DistanceFactor = 100` in
`PromisedWorldsSettings.cfg`.

*What should happen.* With this mod, the craft should stand at the same height at every load, on both
bodies and at both distances.
