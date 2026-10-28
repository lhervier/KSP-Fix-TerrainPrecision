# Parts lying alone on the ground

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned — read in the code and seen in play; the fix is not written yet.**

## Why it is a question

Seen in a sandbox game, next to the runway: a rover wheel taken off a rover in EVA construction and dropped
on the grass lies still for about 3 seconds, then flies several metres up and lands tens of metres away.
Wheels already lying on the ground do it again at every load. It happens with and without this mod.

Read in the code, the jump comes from a stock behaviour that looks like a patch over the moving ground this
mod fixes: with this mod, it seems to protect from nothing any more, and only throws the wheels. This mod
could then turn it off.

## What is already known

- **A part alone on the ground is made heavier for 3 seconds every time it goes off rails.** When a craft
  of a single part goes off rails landed (or on the launch pad), `ModuleCargoPart.OnPartUnpack` starts
  `MakePartSettle`, which raises the part's mass to **4 t** on a body between 0.8 g and 1.1 g, and to
  **20 t** below 0.8 g, then gives it back after the part's kinematic delay, 3 seconds by default. That
  is not only after a drop in EVA construction: at every load, every time the player comes back near the
  part, and every time on-rails time warp stops. 371 stock parts carry `ModuleCargoPart`.
- **A part with a suspension tunes it to that mass, and is thrown up when the mass comes back.**
  `ModuleWheelSuspension` sets the spring from the mass of the craft at every physics step while the wheel
  touches the ground, and the wheel collider takes its sprung mass from the rigidbody: for 3 seconds, the
  suspension of a 0.1 t wheel is set and pressed for 4 t. When the mass drops back, the pressed spring
  throws the part. Among the parts carrying `ModuleCargoPart`, 12 have a suspension: the landing legs LT-05,
  LT-1 and LT-2, the five landing gears, and the rover wheels M1, S2, TR-2L and the Making History one. A
  craft of several parts never goes through this.
- **Why stock does it is not written anywhere.** It only applies on low gravity bodies, the heavier the
  lower the gravity. A part reloaded alone on the ground starts in the ground collider by as much as the
  ground moved since it was saved, since the ground rebuilt at load is not where it was
  ([The culprit](../../the-culprit.md)), and moves of less than 10 cm are not corrected when it is put back
  onto the ground (`Vessel.CheckGroundCollision`). The physics then pushes it out, and on the Mun that push
  is plain to see: batteries, struts and solar panels lying alone pop up at a load. In development tests,
  the extra mass makes those pops smaller on the Mun; with this mod, there were none, with or without it.
- **A kerbal bumping into the part is not a reason to keep it.** The extra mass lasts the 3 seconds after
  the part goes off rails; a kerbal walking into the part later meets its own mass.
- **On a slope, another stock move remains.** Read in the code, not measured: when `CheckGroundCollision`
  puts a craft back onto a slope, it compares the drop to its lowest point with the ground straight under
  its root, and sees a gap that is not there; past the 10 cm it ignores, it sinks the craft into the slope.
  That does not depend on this mod's ground, and a large part on a steep slope could still need the extra
  mass.
- **Breaking Ground's deployed experiments** go through the same wait from their own code, which also
  rivets them: they are left out here, see
  [Breaking Ground's deployed experiments](breaking-grounds-deployed-experiments.md).

## The fix planned

A new setting of this mod, on by default, that gives a part back its own mass as soon as
`ModuleCargoPart.OnPartUnpack` has raised it, so that the part settles with its real mass. Whether it should
apply to every part, or only to the parts with a suspension, is what the tests below have to tell.

## To test

**A wheel dropped in EVA construction.** In a sandbox game, an engineer on EVA next to a rover, a second
kerbal on the ground nearby to lift a wheel. In construction mode, take a wheel off the rover and drop it on
the ground a few metres away; watch it for 10 seconds. On Kerbin, then on the Mun. Without this mod, then
with it and the setting off, then with the setting on.

*What should happen.* The wheel jumps about 3 seconds after the drop without this mod and with the setting
off; with the setting on, it stays where it fell.

**Parts left alone, reloaded.** Drop around the rover a few parts of different shapes: a battery, a solar
panel, a strut, a wheel, a landing leg. Save, then load that save ten times, watching the parts for 10
seconds each time. On the Mun first, then on Kerbin.

*What should happen.* Without this mod, some parts pop up at some loads, and the wheel and the leg jump.
With this mod, no part pops up, setting on or off; the wheel and the leg jump only with the setting off.

**A large part on a steep slope.** On the Mun, a part as wide as a rover wheel or more, dropped on a slope
of 25° or more; save, reload ten times. With the setting off, then on.

*What should happen.* No more sliding or popping with the setting on than with it off.

**On the runway.** Parts dropped alone on the runway and on the launch pad, reloaded ten times, with the
setting off, then on.

*What should happen.* The same with both.
