# Scene changes and time warp, with Jeb on a ROC

Part of [Terrain Precision Fix](../../../README.md), [the ROCs](../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned.**

*Why.* [Scene changes](../../statics/non-regression/stock/scene-changes.md) and
[Time warp](../../statics/non-regression/stock/time-warp.md) are checked on the statics of the KSC. A
surface feature hangs from a holder under the terrain sphere, like the scatter, and carries a collider: a
scene change builds its quad again, and time warp on rails moves the floating origin at every frame, so a
kerbal standing on one would show it moving.

*The test.* Jebediah Kerman standing on a surface feature with a collider (a small one, on the Mun), read by
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel): the sequence of
[Scene changes](../../statics/non-regression/stock/scene-changes.md#the-test), then time warp on the ground
and a pass in time warp on rails as in [Time warp](../../statics/non-regression/stock/time-warp.md), on
stock and with this mod.

*What should happen.* Unknown until the surface features have a fix of their own
([The ROCs](../README.md)): on stock, the feature, and Jeb on it, may come back aside after each.
