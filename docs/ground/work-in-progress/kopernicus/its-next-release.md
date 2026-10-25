# Kopernicus: its next release

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on Kopernicus.

**Status: planned — to play once Kopernicus releases the version after 1.12.1-251.** Read in its source,
not measured. Kopernicus patches `FlightDriver.Start`: when a save is resumed into flight, it places the
floating origin from the focused craft's orbit, in double, instead of the craft's position in float.
Up to release 1.12.1-251, a landed or splashed craft is left out and keeps the stock placement. On the
Kopernicus master branch, that exception is gone.

For a landed craft, the orbit it reads has not been written yet at that moment: `ProtoVessel.Load` creates
its `OrbitDriver` without setting its position, and the first one written comes from `OrbitDriver.Start`,
after the floating origin is placed. So, with that release, the floating origin of a landed craft
reloaded in flight starts at the centre of its body, a whole radius away, then moves to the craft.

This mod's terrain fix places the quads in double, but from where the game builds them. If it does not
hold across that first move, a landed craft would be seen moving or bouncing as the flight loads, or the
ground around it would open along the borders of its quads for the first seconds.

*To test:* once that release is out, the campaigns of
[The craft, over six loads](../../checking/loading.md#the-craft-over-six-loads) and
[The ground, over six loads](../../checking/loading.md#the-ground-over-six-loads), with that release of
Kopernicus, without this mod and then with it. By hand: land a craft, quicksave, quickload, and watch the
craft and the ground around it while the flight loads.
