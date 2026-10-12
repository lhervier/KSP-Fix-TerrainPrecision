# Non-regression tests: stock

Part of [Terrain Precision Fix](../../README.md), one mod of [Non-regression tests](../non-regression.md): what works without this mod still works with it, on stock.

Unless a page says otherwise, each test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1 and this mod, plus the instrument and the mods it names. Each test has a page of
its own.

This mod places the terrain quads a craft stands on in double, and takes the statics out of their
terrain sphere in flight, near a craft ([The fix: the ground](../the-fix-ground.md),
[The fix: the statics](../the-fix-statics.md)); with its scatter fix, on by default, it hangs each
holder of terrain scatter from its quad ([The fix: the scatter](../the-fix-scatter.md)). What stock places
on the ground, or finds the statics and the holders by, has to keep working.

## Existing saves

**Checked, no problem — a landed craft goes through one more draw, always the same one.** A craft saved
without this mod comes back once on the corrected ground; saved again with it, on the Moon in Real Solar
System, the workaround that moves a landed craft back onto the ground never had to move it, in 36 loads.

**→ Full chapter: [Existing saves](stock/existing-saves.md)**

## Colliders below the highest subdivision level

**Not a regression, not corrected either; on stock, no such collider exists.** This mod corrects the
quads of the highest level only: a lower-level quad with a collider would jump at every load as in
stock. The collider offset that would allow one is 0 on every stock body, read in game, and Kopernicus
cannot change it. A craft flying very fast over a landed one may leave it on terrain without any
collider: a stock case, read in the code, outside what this mod fixes.

**→ Full chapter: [Colliders below the highest subdivision level](stock/colliders-below-the-highest-subdivision-level.md)**

## Scene changes

**Checked on Kerbin and on Earth in Real Solar System.** This mod has to put the KSC back before every
scene change. Through every way of leaving a flight and coming back, a trip to another body included,
the launchpad stays within 0.14 mm, against up to 599 mm without this mod. A craft launched from the
VAB stands on the launchpad, one from the SPH on the runway, and every building opens.

**→ Full chapter: [Scene changes](stock/scene-changes.md)**

## Destroyed buildings

**Checked on Kerbin.** KSP finds a destructible building by its path below the KSC, which this mod moves in
flight. The VAB, brought down by a heavy craft dropped onto it while the KSC is out of its sphere,
collapses, shows as destroyed at the space centre, stays in ruins through the next flights, and stands again
once repaired, as without this mod; the launchpad and the runway stay within 0.22 mm, against 71 and
87 mm without it.

**→ Full chapter: [Destroyed buildings](stock/destroyed-buildings.md)**

## Facility levels

**Checked on Kerbin.** Each level of a facility is a model of its own, built below the KSC. At each of
their three levels, a craft stands on the launchpad and on the runway of that level, as without this mod,
and stays within 0.24 mm through its arrivals, against up to 174 mm without it.

**→ Full chapter: [Facility levels](stock/facility-levels.md)**

## An anchor on a static

**Checked on Kerbin, on a runway of each kind of static.** An anchor stays put only if what it stands on
comes back too. On the runways of the KSC and the Desert Airfield, an anchor and an anchored base stay
within 0.15 mm of the runway, once 1.6 mm; without this mod, up to 116 mm away.

**→ Full chapter: [An anchor on a static](stock/an-anchor-on-a-static.md)**

## Time warp

**Checked on Kerbin and on the Mun.** A craft on the runway through three days at 100 000×: the runway
stays within 0.12 mm under it. A craft passing 3 km over a static of the Mun in time warp on rails: a
capsule standing on the static reads it within 0.008 mm, against 10.7 mm without this mod.

**→ Full chapter: [Time warp](stock/time-warp.md)**

## The lights of the KSC

**Checked on Kerbin.** A component switches the lights of the KSC with day and night, after finding its
body among its parents, which this mod lends back to it. In flight, the KSC out of its sphere, the
runway lights and the windows come on at night and go off by day, as without this mod.

**→ Full chapter: [The lights of the KSC](stock/the-lights-of-the-ksc.md)**

## A launch pad placed by a mission

**Impossible to reproduce.** A mission of Making History can place a launch pad of its own, which stock
looks for under its sphere once. Read in the code, that never happens in flight, where this mod moves
statics; no way was found to launch from such a pad on stock.

**→ Full chapter: [A launch pad placed by a mission](stock/a-launch-pad-placed-by-a-mission.md)**

## A static turning with its body

**Cannot happen on stock, in Real Solar System or with Outer Planets Mod.** This mod has to turn a static
out of its sphere when KSP turns the body. Measured body by body, no body turns lower than 100 km, far
above any craft near a static this mod has moved.

**→ Full chapter: [A static turning with its body](stock/a-static-turning-with-its-body.md)**

## The map view

**Nothing to test, read in the code.** The map draws the bodies from scaled space, which this mod does
not touch. While it is open, the terrain keeps being built around the active craft exactly as in
flight, and the markers of the launch sites follow their statics wherever this mod places them.

**→ Full chapter: [The map view](stock/the-map-view.md)**

## The scatter holders

**Checked with the scatter fix on, no problem — no holder lost.** The scatter fix takes each holder out
of its pool's container while its quad is in use. Over a flight over the Mun and across scene switches,
every holder went back to its pool, none was left on a quad, and the pools counted as in stock.

**→ Full chapter: [The scatter holders](stock/the-scatter-holders.md)**
