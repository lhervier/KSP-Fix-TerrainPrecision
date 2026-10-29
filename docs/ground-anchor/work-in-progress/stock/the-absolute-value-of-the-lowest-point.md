# The absolute value of the lowest point

Part of [Terrain Precision Fix](../../../../README.md), [the ground anchor](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned — seen on another part, read in the code; nothing changed yet.**

## Why it is a question

The model fix of this mod gives the stock ground anchor a new collider, because `Vessel.CheckGroundCollision`
takes the absolute value of the lowest point of a craft: with its origin below its collider, the anchor is
put back 4.2 cm higher than it was placed ([The anchor's model](../../the-culprit.md#the-anchors-model)).

The anchor is not the only part it moves. In
[Checking parts lying alone: on the runway](../../../lone-parts/checking/runway.md), two OX-STAT photovoltaic
panels lying alone on the runway go 107 mm up and fall back at every load, with this mod as installed and
with `fixLonePartMass = false` alike. `KSP.log` names the pass each time, 20 lines in each of the two
sessions, one per panel and per load
([`runway-fix.log`](../../../../diag/lone-parts/checking/runway/runway-fix.log)):

```
[Panneaux photovoltaïques OX-STAT]: ground contact! - error. Moving Vessel  up 0.107m
```

Read in the code, on a flat runway, only one case gives that line: a part whose origin lies below its
colliders. A part resting on the runway has its lowest point on it; the pass would leave it there if it took
that point with its sign. With the absolute value, it puts the origin as far above the runway as it was
below it: twice the depth of the origin, here about 107 mm, past the 10 cm the pass ignores. A part whose
origin lies less than 5 cm below its colliders is left alone; the anchor, at the root of its craft, is
moved whatever the distance.

## What is already known

- **The lift is set by the part, not by the ground.** With this mod, the line reads `up 0.107m` 39 times
  out of 40 and `up 0.108m` once, over the two sessions: the runway comes back where it was, and the lift is
  the same at every load. On stock, the same line reads from `up 0.101m` to `up 0.135m`, 18 times out of 20
  ([`runway-stock.log`](../../../../diag/lone-parts/checking/runway/runway-stock.log)): the runway moving at
  every load adds to the lift or takes from it, and at the load where it came back lower, the move fell under
  the 10 cm the pass ignores and the panels were left where they were.
- **It depends on how the part lies.** A part has its origin below its colliders in one position only: a
  panel lying the other way round, or standing, keeps its origin above its lowest point, and the pass leaves
  it alone. None of the six parts lying alone on the Mun, in
  [Checking parts lying alone: loading the same save](../../../lone-parts/checking/loading.md), has the line in
  [`loading-fix.log`](../../../../diag/lone-parts/checking/loading/loading-fix.log).
- **Not measured yet**, and to be read with an instrument: that the panel is lifted in one step, at its first
  physics step, rather than pushed out by the physics; and how deep its origin lies below its collider, which
  the reading above puts at half of 107 mm.

## A fix to the pass itself

Taking the lowest point with its sign would put every such part back where it rested: the anchor, a panel on
its back, any part of a mod built the same way. One patch to the stock pass would then stand for the anchor's
new collider, and cover the parts no one has listed. The anchor would keep resting as stock places it, its
base 2 cm into the ground, and would no longer move at a load.

The model fix could not simply be dropped for it, though. An anchor placed with the model fix rests with its
origin on the ground; loaded with the stock collider and a pass that takes the sign, it would be put back with
its origin 2 cm below the ground, and riveted there: every anchored base of an existing save would sink by
2 cm once. Whichever way is chosen, what it does to anchors already placed is part of the change.

## Why the absolute value is there

Before taking it away, what it is for has to be found. It is not written anywhere.

- **It only matters for a craft whose origin lies below all of its colliders.** `Vessel.getLowestPoint`
  returns the height of the craft's origin above its lowest collider point; for an ordinary craft, resting
  on colliders around or below its origin, it is positive, and the absolute value changes nothing. It turns
  negative for a part lying alone in a way that leaves its origin below it, the anchor or a panel on its
  back.
- **It is older than the anchor.** In KSP 1.8.1, before KSP 1.11 brought EVA construction and the ground
  anchor, the pass already takes the absolute value. It was not added for the anchor.
- **The pass guards against values it does not trust.** Right before, it sets the height above the terrain
  to zero when it is negative; it ignores moves under 10 cm (20 cm in KSP 1.8.1); and it moves a ground part
  at the root of its craft whatever the distance, which KSP 1.8.1 did not.
- **One reading: a guard against the moving ground.** The ground KSP rebuilds at a load is never at the same
  height twice ([The culprit: the ground](../../../ground/the-culprit.md)). A part lying alone and put back
  higher than it rested starts above the ground even when the ground comes back a few centimetres higher;
  on stock's ground, that is what keeps it from being pushed out. If that is what the absolute value is for,
  it is no longer needed with this mod's ground, as for
  [the extra mass of the parts lying alone](../../../lone-parts/the-culprit.md#the-extra-mass).
- **Against that reading:** the lowest point is measured on the craft alone, not against the ground, and the
  pass already finds the ground with a ray cast at load. What the absolute value adds depends on the part's
  model, not on how far the ground moved, and it only reaches the parts whose origin lies below their
  colliders.

## To test

**First, why it is there.** Find which parts and which cases stock meant it for: the releases that changed
the pass (KSP 1.8.1 against 1.12.5), the parts that have their origin below their colliders, and what happens
to them on stock's ground with the absolute value taken away.

**Then, the fix.** With the pass taking the lowest point with its sign: the anchor alone and with a battery,
as in [Checking the culprit: anchoring a base](../../checking/anchoring.md), without the model fix; the
OX-STAT panels of the runway, reloaded ten times; and a craft of several parts, loaded for the first time,
on the ground and on the runway.

*What should happen.* The anchor and the panels come back where they rested, and the log no longer has their
*Moving Vessel* line; nothing else moves more than with the absolute value.
