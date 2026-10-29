# A tall part on a steep slope

Part of [Terrain Precision Fix](../../../README.md), [parts lying alone](../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: on hold — read in the code; a first try found no part that both stands on the slope and is tall
enough to be sunk.**

*Why.* When `Vessel.CheckGroundCollision` puts a craft back onto a slope, it compares the drop to its lowest
point with the ground straight under its root, and sees a gap that is not there; past the 10 cm it
ignores, it sinks the craft into the slope. That does not depend on the ground this mod fixes: a part
lying alone on a steep slope could still start inside the ground, and still need the extra mass
([The fix: parts lying alone](../the-fix.md#for-every-part)).

*What counts is the height of the part, not its width.* The drop to the lowest point is measured from the
root along the normal of the slope: for a part lying alone, it is about half its height above the slope.
The gap seen is that height times `1/cos α − 1`, or `sin²α / cos α` once it goes past 10 cm, for a slope
of `α`. On a slope of 20°, it goes past the 10 cm ignored only for a part whose root stands more than about
1.6 m above the slope: a part more than 3 m tall, standing on it. A flat part, however wide, is never sunk.

*The first try.* An M-2x2 Structural Panel, 2 m wide, set flat on a slope of the Mun read at 30° from the
game's terrain, slid about 130 m down and came to rest, flat, on a slope of 21.9°. A panel lying flat
stands only 3 cm above the slope, far under the 10 cm ignored: there was nothing to measure, and the try
went no further.

*The test still to play.* On the Mun, a part that fits in an inventory, at least 3 m tall, standing on a
slope of 20° or more without tipping over or sliding; save, reload ten times. With this mod and
`fixLonePartMass = false`, then with this mod as installed. None of the stock parts that fit in an
inventory is an obvious candidate: the long ones are tubes, tanks and engines, which roll or tip over on a
slope.

*What should happen.* No more sliding or popping with this mod as installed than with
`fixLonePartMass = false`.
