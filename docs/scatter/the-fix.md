# The fix: the scatter

Part of [Terrain Precision Fix](../../README.md), [the scatter](README.md#the-fix): what the patches do for the terrain scatter, where they do it, what they leave alone, and when to turn them off.

The objects of a quad's scatter hang from a holder that is placed and drawn from a 600 km float, and
that does not share the correction the terrain fix gives the quad
([The culprit: the scatter](the-culprit.md)). So this mod hangs each holder from its own quad.

The scatter fix is **on by default**. `fixScatter = false` in the settings turns it off; it is installed
when KSP starts, whether the terrain fix is on or not. It is two Harmony patches, in
[`Src/ScatterFix.cs`](../../Src/ScatterFix.cs). Why it is on, and when to turn it off, is in [On by default: when to turn it off](#on-by-default-when-to-turn-it-off)

## Hanging each holder from its quad

Each holder hangs from its own quad, at no offset. The objects are then drawn in the frame they were
built in, with the very matrix the ground is drawn with, and no transform in the chain holds a 600 km
vector any more.

- **After `PQSMod_LandClassScatterQuad.Setup`**, which gives a holder its quad: the holder is re-parented
  under the quad, with zero position, identity rotation and unit scale. From then on it follows the quad
  through everything stock does to it, floating origin shifts (`PQ.FastUpdateSubQuadsPosition`) and
  re-placements (`PQ.PreciseUpdateSubQuadsPosition`) included, with nothing more to do
  ([measured while you drive](checking/driving.md) and
  [along a flight](checking/flight.md)).
- **Before `PQSLandControl.LandClassScatter.DestroyQuad`**, which returns a holder to its pool when its
  quad is destroyed: the holder goes back under the pool's container, where stock keeps its free holders,
  before the quad itself goes back to the PQS cache to be reused elsewhere. A prefix, because the stock
  method starts by clearing the holder's quad.

This is not a new way of drawing scatter. It is the stock scatter, drawn from the frame stock built it in.

## Why the holder has to move at all

The fix that would leave every other mod alone is the one that keeps the holder under its `Scatter <name>`
container and merely places it better. Reading the stock code, and the way Unity stores a transform, that
way looks closed. Three reasons, from the plainest to the heaviest:

- **The correction is smaller than the step of the number that would carry it.** Unity keeps a child's
  position in its parent's frame, in single precision, whichever call writes it: `position`,
  `localPosition` and `SetPositionAndRotation` all end in that same float. Under the sphere, that number is
  the 600 km vector, where a float changes in steps of 62.5 mm on Kerbin, while the offsets to be taken out
  are the ones measured in
  [Checking the scatter: loading the same save](checking/loading.md),
  up to 110 mm. No value that can be written puts the holder where it belongs.
- **The frame it hangs in is single precision as well.** Even given a perfect local position, the holder is
  drawn through the sphere's matrix, over that same 600 km. That product is what rounds differently at
  every load: it is the defect itself, not a way around it.
- **Out of the sphere, the holder has to be placed by hand before every frame.** Placing it in double
  precision needs a parent near the world origin, and stock then stops carrying it: the world position of a
  quad of the highest level is rewritten whenever the body moves in the game's local space, which in flight
  is every frame, and its rotation whenever stock places the quad again. The holder would have to follow
  both — its objects are built in the quad's frame, so its rotation counts as much as its position — and a
  frame missed would leave them not centimetres but metres behind the ground.

**This is read, not measured.** No build of the scatter fix has tried that way, and nothing else on this
page rests on it: the measurements stand on their own. It is written down because it is the first question
to ask of a fix that moves stock objects, and a reader who sees a way through should say so.

What is left is to take the holder out of the sphere, as the scatter fix does, or to stop drawing the
scatter from the holder's transform altogether and draw it from somewhere else, which changes far more
than where an object hangs. Of the two, hanging the holder from its quad is the smaller change: the quad
is the one object stock already keeps in step, for nothing, with the ground the scatter is built from.
Parallax reaches the same conclusion for its own scatter: the colliders it creates hang from the quad
they belong to, in the quad's frame, so that the object a craft hits is the object the quad draws.

## Only where scatter grows

Only the holders of quads that hang from `LocalSpacePQStorage` are moved. In stock, scatter only exists
on those quads, and any other quad hangs from the sphere with the same kind of 600 km local position as
the holder, so hanging the holder from it would gain nothing.

Holders on a sphere whose quads are not surface relative are left alone too: there, stock places the
holder at the centre of the body, not at a long vector.

## Why moving the holder is safe for stock

Read in the stock code:

- a destroyed quad calls its `onDestroy` delegates, which release its holder, before it goes to the PQS
  cache, so no holder travels with a recycled quad;
- `PQS.ResetSphere` destroys the quads before the scatter destroys its holders;
- the visibility of a holder is switched with `obj.SetActive` from the quad's `onVisible` and
  `onInvisible` delegates, not through the hierarchy, so hanging it from the quad does not change when it
  is shown.

Checked in game as well, over a whole flight and across scene switches: no holder is lost, and every pool
works as in stock ([Non-regression tests: the scatter holders](non-regression/stock/the-scatter-holders.md)).

## Other mods that look for the holders

Safe for stock is not safe for every mod. A holder in use no longer hangs from the `Scatter <name>`
container under the sphere, but from its quad, under `LocalSpacePQStorage`, outside the body's hierarchy.
Its pool, its quad, its delegates and the way it is shown and hidden stay stock, so only code that walks
the hierarchy to find the holders sees the move: under the sphere it no longer finds those in use, under a
quad it finds children stock never puts there. [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter)
is such code, and has to search both places with the scatter fix on.

None of the mods read so far does: stock ([The scatter holders](non-regression/stock/the-scatter-holders.md)),
KSP Community Fixes, which never names a holder
([its own terrain patches](../ground/non-regression/ksp-community-fixes/its-own-terrain-patches.md)), Kopernicus,
the only one that uses the holders, through the scatter's pool
([Kopernicus: scatter with colliders](non-regression/kopernicus/scatter-with-colliders.md)), Parallax,
which has a scatter of its own
([Parallax: what it does with the ground](../ground/non-regression/parallax/what-it-does-with-the-ground.md#read-in-its-source)), and
TUFX 1.1.1, which works on the camera's image and never looks for a terrain object, and Kerbal Planetary
Base Systems, which adds parts and never looks for one either
([Kerbal Planetary Base Systems: a base on the ground](../ground/non-regression/kerbal-planetary-base-systems/a-base-on-the-ground.md)).
Every other mod is
unread: [Mods that look for a scatter holder under its sphere](work-in-progress/other-mods/mods-that-look-for-a-scatter-holder-under-its-sphere.md).

## On by default: when to turn it off

The terrain fix alone leaves the scatter behind. At loading, the scatter comes back further off the corrected
ground than on stock, on Kerbin
([measured](checking/loading.md#the-objects-over-twelve-loads)); and while you
drive, every 500 m, it jumps against the ground by up to a few centimetres, where on stock it moves with the
ground ([measured](checking/driving.md)). Stock scatter has no collider, so neither
changes anything for the game, and most of the gap stays out of sight, since the scatter is sunk into the
ground on purpose, tens of centimetres on Kerbin and about 2 m on the Mun. But the jump can be seen, at a
walking pace and up close, on a rock or a cactus: a defect this mod would add to stock, which its scatter
fix takes away. So the scatter fix is on by default, with the terrain fix it completes.

Give the scatter colliders — the
[Stock Scatter Collider Enabler Patch](https://github.com/Poodmund/Stock-Scatter-Collider-Enabler-Patch)
does, on top of Kopernicus, and it is on CKAN — and the gap stops being visual: the rock a craft hits
stands up to 71 mm from the rock its pilot sees, and a kerbal left on a boulder sinks into it at one load
and stands clear of it at the next. Only the scatter fix closes that gap; the terrain fix alone narrows it
a little (see
[Kopernicus: scatter with colliders](non-regression/kopernicus/scatter-with-colliders.md)).

What it costs is a change to where stock objects hang, which another mod may rely on: a holder in use hangs
from its quad, no longer under the sphere ([Other mods that look for the holders](#other-mods-that-look-for-the-holders)).
None of the mods read so far does, and nothing in
[Why the holder has to move at all](#why-the-holder-has-to-move-at-all) leaves a fix that keeps the holders
where stock puts them. Its cost in time does not show in the measurement (see
[Performance: the scatter fix](../common/performance.md#the-scatter-fix)).

**Turning it off is one line.** If a mod misbehaves around rocks, grass or trees — scatter missing, drawn
twice, or an error naming a scatter holder — open `GameData/KSPFixTerrainPrecision/PluginData/settings.cfg`,
set `fixScatter = false`, and start KSP again: the holders then stay where stock puts them, and the rest of
this mod works as before. `KSP.log` says it: *Scatter fix turned off in the settings*. The scatter is then
back to what the terrain fix alone leaves, a few centimetres off the ground and jumping as you drive.

It is meant to go with the terrain fix, and has only been measured with it: on its own, it would keep the
scatter on the stock ground, which still comes back at a different height at every load
([The scatter fix without the terrain fix](work-in-progress/stock/the-scatter-fix-without-the-terrain-fix.md)).

## Safeguards

- if either patch fails to install, no holder is ever moved;
- a holder that cannot be hung from its quad stays where stock placed it;
- the release only acts on a holder that hangs from its own quad, so it never moves a holder the fix did
  not move;
- with Rock Precision Fix installed, the mod this fix was first published as, the scatter fix is not
  installed and the log says so: both would hang every holder twice.
