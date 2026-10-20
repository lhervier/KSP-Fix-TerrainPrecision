# Scene changes, with a capsule on the runway

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned.**

*Why.* [Scene changes](../../non-regression/stock/scene-changes.md) is checked on the launchpad. The
runway is a static of its own, placed apart from the launchpad and from the ground beside it
([Checking the statics: loading the same save](../../checking/loading.md)); a capsule resting on it has not
been watched through the same scene changes.

*The test.* The same sequence as [Scene changes](../../non-regression/stock/scene-changes.md#the-test), with
a capsule on the runway instead of a craft on the launchpad, read by
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) and
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) after each way of leaving
the flight and coming back, on stock and with this mod.

*What should happen.* With this mod, the deck of the runway should come back where it was after every scene
change, as the launchpad does.
