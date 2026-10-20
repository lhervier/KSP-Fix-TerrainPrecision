# Promised Worlds: its monuments and its frozen lake

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#work-in-progress): one point of the work in progress, on Promised Worlds.

**Status: planned — read in its configs, not played.** [Promised Worlds](https://github.com/PromisedWorlds/PromisedWorlds)
places its statics with the `City2` node of [Kopernicus](https://github.com/Kopernicus/Kopernicus), which
builds a `PQSCity2`, the kind of static of the launch sites of Making History. This mod takes them out of
their sphere in flight the same way, as checked on the Desert Launch Site in
[Checking the culprit: launching from a launch pad of Making History](../../checking/launch-pad.md).

They are:
- a monument on Bis, and one on Charr;
- on Merbel, a frozen lake made of eleven copies of one model stacked 5 m apart (`Merbel_FrozenLake`, then
  `Merbel_FrozenLake_Level-1` to `-10`), each scaled to 5 000 × 500 × 5 000.

All of them are set to `snapToSurface`: `PQSCity2.Orientate` puts them on the ground, and this mod puts them
back under their sphere while it does. Whether their models carry a collider has not been read. Without one,
nothing stands on them, and only their place on the ground can be watched.

*What the player would see if this mod broke something:* a monument that floats above the ground or sinks
into it, a lake drawn away from its basin, or, if the lake has a collider, a craft on its ice that jumps at
each load or after flying away and back.

*The test.* An install with Kopernicus, KSP Community Fixes, Promised Worlds with its Debdeb and Tuun
systems, and this mod. First, near each of them,
[KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders) shows whether it has a collider.
Then a craft landed by each monument, and one on the lake if it can be stood on, loaded twice, then flown
more than 30 km away and back, without this mod and with it.

*What should happen.* Each static should be in the same place without this mod and with it, and a craft on
the lake should stand as it did.
