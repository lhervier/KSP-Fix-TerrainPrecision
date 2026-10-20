# Scene changes and time warp, with Jeb on the scatter

Part of [Terrain Precision Fix](../../../../README.md), [the scatter](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned.**

*Why.* [Scene changes](../../../statics/non-regression/stock/scene-changes.md) and
[Time warp](../../../statics/non-regression/stock/time-warp.md) are checked on the statics of the KSC. The
scatter fix hangs each holder from its quad, and hangs it back in its pool when the quad goes: a scene
change drops every quad, and time warp on rails moves the floating origin at every frame. Stock scatter has
no collider, but with Kopernicus a rock can carry one
([Kopernicus: scatter with colliders](../../non-regression/kopernicus/scatter-with-colliders.md)), and a
kerbal standing on it would show it moving.

*The test.* Jebediah Kerman standing on a rock that carries a collider, read by
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) and
[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter): the sequence of
[Scene changes](../../../statics/non-regression/stock/scene-changes.md#the-test), then time warp on the
ground and a pass in time warp on rails as in [Time warp](../../../statics/non-regression/stock/time-warp.md),
on stock and with this mod.

*What should happen.* With this mod, the rock should come back where it was, and Jeb on it, after every
scene change and every time warp.
