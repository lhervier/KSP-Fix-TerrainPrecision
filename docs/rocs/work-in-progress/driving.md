# Driving on while the world moves, by a ROC

Part of [Terrain Precision Fix](../../../README.md), [the ROCs](../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned.**

*Why.* Every 500 m the craft you fly travels, KSP moves the floating origin back onto it, and with it the
terrain sphere, which carries the ground and the holders of the surface features alike. With the terrain
fix alone, the ground no longer jumps at that move, but the holders still do, as the scatter's do
([Checking the scatter: driving on while the world moves](../../scatter/checking/driving.md)).

*The test.* A rover alone, driven to stop by a surface feature just short of 500 m from where it
started, then crept on until the origin moves, filmed before and after the move: with this mod and
`fixRocs = false`, then with this mod as installed. No other craft may stand landed nearby: while one is
loaded, KSP does not move the origin.

*What should happen.* With the fix of the surface features off, the feature jumps against the ground at the
move, by a few centimetres; with this mod as installed, nothing jumps.
