# Scene changes, with a capsule on the ground

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned.**

*Why.* [Scene changes](../../../statics/non-regression/stock/scene-changes.md) is checked on the
launchpad, a static that this mod takes out of its sphere and puts back before every scene change. The
ground under a craft landed on bare ground goes through the same scene changes, and is built again after
each one: the quads this mod corrects are not checked through them yet.

*The test.* The same sequence as [Scene changes](../../../statics/non-regression/stock/scene-changes.md#the-test),
with a capsule landed on bare ground instead of a craft on the launchpad, read by
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) and
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) after each way of leaving
the flight and coming back, on stock and with this mod.

*What should happen.* With this mod, the ground under the capsule should come back where it was after every
scene change, as it does after [loading the same save](../../checking/loading.md).
