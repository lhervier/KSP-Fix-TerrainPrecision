# A large part on a steep slope

Part of [Terrain Precision Fix](../../../README.md), [parts lying alone](../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned — read in the code, not measured; the fix is not written yet.**

*Why.* When `Vessel.CheckGroundCollision` puts a craft back onto a slope, it compares the drop to its lowest
point with the ground straight under its root, and sees a gap that is not there; past the 10 cm it
ignores, it sinks the craft into the slope. That does not depend on the ground this mod fixes: a large part
lying alone on a steep slope could still start inside the ground, and still need the extra mass
([The fix: parts lying alone](../the-fix.md#for-every-part)).

*The test.* On the Mun, a part as wide as a rover wheel or more, dropped on a slope of 25° or more; save,
reload ten times. With this mod and `fixLonePartMass = false`, then with this mod as installed.

*What should happen.* No more sliding or popping with this mod as installed than with
`fixLonePartMass = false`.
