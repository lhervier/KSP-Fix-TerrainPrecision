# The scatter fix without the terrain fix

Part of [Terrain Precision Fix](../../../../README.md), [the scatter](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned.** The scatter fix, on by default, is installed whether the terrain fix is on or not ([The fix: the scatter](../../the-fix.md)), but it has only been measured with it
([Checking the scatter: loading the same save](../../checking/loading.md)).
On its own, it should keep the scatter on the stock ground, which still comes back at a different height
at every load.

*To test:* the series of [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter), on its two
saves, twelve loads each, with `fixTerrain = false` and `fixScatter = true`. Every holder should be
drawn on its quad, and the objects should move with the ground under them, by as much as the stock
ground moves, and no more.
