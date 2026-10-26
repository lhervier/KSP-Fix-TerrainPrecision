# The ground

Part of [Terrain Precision Fix](../../README.md): the terrain quads a craft stands on, and every vertex
inside them. Where the rounding strikes them in the stock code, how this mod takes it away, how that is
checked, what keeps working, what it makes worse, and what is still to check.

The rounding itself, shared with the statics and the scatter, is told once in
[The culprit: a float at planet scale](../common/the-culprit.md).

## The culprit

Stock places a terrain quad, and every vertex inside it, through a Unity `Transform`: a vector 600 km long
stored in a float. Each value is rounded on its own, through the frame of the moment.

**→ Full chapter: [The culprit: the ground](the-culprit.md)**

## The fix

Two Harmony patches redo in double the two placements that go through a float at planet scale: the origin
of each quad, and each vertex inside it. The two 600 km vectors cancel before anything reaches a float,
which is then only asked to hold a distance within the quad. Only the quads a craft can stand on are
touched. It is on by default; `fixTerrain = false` turns it off ([Settings](../common/settings.md)).

**→ Full chapter: [The fix: the ground](the-fix.md)**

## Checked

Each situation where a craft meets the ground is measured twice, without this mod and with it, in an
install with [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes), the base most
players run: KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, the instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which plays the protocols — and this mod, or
not. [KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) reads the craft,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) the ground under it, and
in flight [KSP Diag - Terrain Quads](https://github.com/lhervier/KSP-Diag-TerrainQuads) the quads it is
made of. In each summary, the first figure is without this mod, the second with it.

- **Loading the same save**, six times, on the four stock worlds and the Moon and Earth of
  [Real Solar System](https://github.com/KSP-RO/RealSolarSystem): the ground comes back over 43.6 mm on
  Kerbin and 292.3 mm on Earth, within 0.3 mm with this mod; the craft comes to rest over 43.7 mm and
  292.4 mm, within 0.4 mm.

  **→ Full chapter: [Checking the ground: loading the same save](checking/loading.md)**

- **Coming back to a craft left parked**, driving away until it unloads, then back, six times in one
  flight: its ground comes back over 49.3 mm, and over 0.010 mm with this mod.

  **→ Full chapter: [Checking the culprit: coming back to a craft left parked](checking/approach.md)**

- **Switching to a craft far away**, six loadings: its ground spreads over 112.1 mm, and 0.002 mm with
  this mod; the switch itself moves nothing.

  **→ Full chapter: [Checking the culprit: switching to a craft far away](checking/switching.md)**

- **Driving on while the world moves**: every 500 m a rover drives, KSP moves the floating origin back onto
  it, and the ground with it. On stock, the ground under the rover jumps by 26.6 and 24.7 mm on Kerbin and
  by up to 243 mm on Earth; with this mod, no move stands out from what the few metres driven do.

  **→ Full chapter: [Checking the ground: driving on while the world moves](checking/driving.md)**

- **In flight**, a rocket from the launchpad to the sea, its quads of the highest level written about once
  a second: two quads built at different moments step by up to 22.5 mm where they meet on Kerbin and
  289 mm on Earth, and by 0.67 mm and 2.1 mm at most with this mod.

  **→ Full chapter: [Checking the ground: in flight](checking/flight.md)**

**This is also the last proof that the culprit is the right one.** The fix changes where a subtraction
happens, and nothing else about the values placed; were the cause elsewhere, reordering that subtraction
would have left the spread untouched.

The saves, the scripts and the `KSP.log` of every session, both ways, are in
[the runs of the ground](../../diag/ground/README.md).

## Non-regression tests

What works without this mod still works with it, one mod at a time: played in game with this mod, and
compared with the game without it where the two have to be told apart. Unless a page says otherwise, each
test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1 and this mod, plus
the instrument and the mods it names. Two tests cover every fix at once, and are told in
[what the fixes share](../common/README.md): [existing saves](../common/existing-saves.md) and
[this mod's safeguard](../common/safeguard.md).

### Stock

**The map view: nothing to test, read in the code.** The map draws the bodies from scaled space, which this
mod does not touch. While it is open, the terrain keeps being built around the active craft exactly as in
flight.

**→ Full chapter: [The map view](non-regression/stock/the-map-view.md)**

**Colliders below the highest subdivision level: not a regression, not corrected either; on stock, no
such collider exists.** This mod corrects the quads of the highest level only: a lower-level quad with a
collider would jump at every load as in stock. The collider offset that would allow one is 0 on every
stock body, read in game, and Kopernicus cannot change it.

**→ Full chapter: [Colliders below the highest subdivision level](non-regression/stock/colliders-below-the-highest-subdivision-level.md)**

### KSP Community Fixes

**Its own terrain patches: checked, in the source and in every campaign.** None of its patches places a
terrain quad or a terrain vertex, or names a scatter holder, and every measurement of this mod was taken
with KSP Community Fixes 1.41.1 installed.

**→ Full chapter: [KSP Community Fixes: its own terrain patches](non-regression/ksp-community-fixes/its-own-terrain-patches.md)**

### Kopernicus

**The terrain: checked, no problem.** Most planet packs go through
[Kopernicus](https://github.com/Kopernicus/Kopernicus), which changes the terrain of existing bodies, so
this mod has to still find the ground where it expects it. Over six loads on Kerbin, a terrain quad spreads
over 116.0 mm (median) without this mod and 0.079 mm with it.

**→ Full chapter: [Kopernicus: the terrain](non-regression/kopernicus/the-terrain.md)**

### Real Solar System

The defect grows with the body: a float's step is 62.5 mm at the radius of Kerbin, 125 mm on the Moon,
500 mm on Earth.

**The ground workaround: checked on the Moon and on Earth — with this mod, it has nothing left to correct
for this defect.** Real Solar System moves a landed craft back onto the ground when it is more than 10 cm
off. Over 75 loads in a row with this mod, the craft never moved, and the workaround never had anything to
correct; with Real Solar System built without it, this mod keeps the craft in place on its own.

**→ Full chapter: [Real Solar System: the ground workaround](non-regression/real-solar-system/the-ground-workaround.md)**

**Coming back to a craft left parked, on the Moon: checked, no problem.** Over six round trips of a rover,
the ground under the parked capsule came back within 0.042 mm with this mod, against 31.9 mm without it.

**→ Full chapter: [Real Solar System: coming back to a craft left parked, on the Moon](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon.md)**

**Switching to a craft left parked, on the Moon: checked, no problem.** Switched to from 3 km away, a craft
left parked is loaded again and handed back to physics, where Real Solar System's ground workaround runs.
Over six switches, the capsule came to rest within 0.380 mm with this mod, 0.494 mm with the workaround
built out, against 132.0 mm without this mod; the workaround never moved it.

**→ Full chapter: [Real Solar System: switching to a craft left parked, on the Moon](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon.md)**

### Deferred

**Drawing the ground: checked, no problem.** [Deferred](https://github.com/LGhassen/Deferred) replaces the
way KSP draws everything, the terrain included, and it is the mod that broke KSP Community Fixes' own
`PQSOnlyStartOnce`. It draws the ground wherever it is placed and patches nothing this mod patches. With it
installed, the craft and the ground come back as they do without it, after a load and after a trip out of
range.

**→ Full chapter: [Deferred: drawing the ground](non-regression/deferred/drawing-the-ground.md)**

### Kerbal Planetary Base Systems

**A base on the ground: checked on Kerbin, and read in the source.** One of the most popular part mods,
built for bases on the ground. Its plugin touches nothing of the ground, and its parts are held up by stock
modules; a base reloaded on a slope jumps without this mod, and stays within a millimetre with it.

**→ Full chapter: [Kerbal Planetary Base Systems: a base on the ground](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground.md)**

### Parallax

[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) draws the terrain with shaders of its
own and sets rocks and trees on the ground this mod places. Its scatter is in [the scatter](../scatter/README.md#parallax).

**What it does with the ground: read in the source.** Parallax draws the ground this mod places, and hangs
its objects from the terrain quads, so they follow it.

**→ Full chapter: [Parallax: what it does with the ground](non-regression/parallax/what-it-does-with-the-ground.md)**

**Loading a craft on its ground: checked on Kerbin and Minmus.** A capsule loaded six times comes
back as it does without Parallax: on Kerbin, within 73 mm without this mod and within 0.010 mm with it.

**→ Full chapter: [Parallax: loading a craft on its ground](non-regression/parallax/loading-a-craft-on-its-ground.md)**

**Coming back to a craft on its ground: checked in the tundra of Kerbin, clear of its objects with a
collider.** A capsule left parked while a rover drives away and back comes back within 31 mm without this
mod, and within 0.12 mm with it.

**→ Full chapter: [Parallax: coming back to a craft on its ground](non-regression/parallax/coming-back-to-a-craft-on-its-ground.md)**

## Limits and solutions

What this mod makes worse, or would break without a patch of its own, with the solution to each. Unless a
page says otherwise, each limit is measured in KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes
1.41.1 and this mod, plus the instrument and the mods it names.

### Stock

**The seam between subdivision levels: a stock crack this mod widens, visual only; no solution yet.** Where
the quads this mod corrects meet coarser ones, stock already leaves a crack, and this mod widens it: the
median of the largest gap of a load goes from 157 mm to 225 mm on Kerbin, and from about 1.3 m to 1.9 m on
Earth. The scatter, too, would be drawn further off the corrected ground, but for this mod's scatter fix,
on by default: see [the scatter](../scatter/README.md#limits-and-solutions).

**→ Full chapter: [The seam between subdivision levels](limits/stock/the-seam-between-subdivision-levels.md)**

### BurstPQS

[BurstPQS](https://github.com/Phantomical/BurstPQS) builds the terrain in place of stock and places it in
double on its own. It holds the ground still on the bodies it builds, but not the statics nor the scatter,
which this mod still corrects. **This mod supports it by itself**: its terrain fix steps back on the bodies
BurstPQS builds, and takes over on the Earth, the Moon and Mars, which the latest Real Solar System (20.1.3)
leaves to stock.

**→ Full chapter: [Limits and solutions: BurstPQS](limits/burst-pqs/README.md)**, with
[the bodies it leaves to stock](limits/burst-pqs/the-bodies-it-leaves-to-stock.md) and
[the campaigns played with it](limits/burst-pqs/the-campaigns.md)

## Work in progress

What is still to check: why it is a question, what is already known, and the test planned to answer it.
Once played, a point moves to [Non-regression tests](#non-regression-tests) if nothing is worse, or to
[Limits and solutions](#limits-and-solutions) if something is.

### Stock

**Asteroids and comets held by a claw: planned.** At the first load with this mod, the ground under an
asteroid or a comet resting on it moves once, with a mass on the other end of a joint. A landed comet
also keeps the floating origin from moving within 150 km of it.

**→ Full chapter: [Asteroids and comets held by a claw](work-in-progress/stock/asteroids-and-comets-held-by-a-claw.md)**

**Breaking Ground's deployed experiments: planned.** Each one is put back on the ground, then let go
for a few seconds, every time time warp stops. Seen jumping in a play save; read in the code, that
comes from stock, not from this mod.

**→ Full chapter: [Breaking Ground's deployed experiments](work-in-progress/stock/breaking-grounds-deployed-experiments.md)**

**The ocean: planned.** Read in the logs, this mod corrected terrain quads only, never the ocean; how the
ocean sphere is flagged has not been read, and a craft floating near a coast has not been watched.

**→ Full chapter: [The ocean](work-in-progress/stock/the-ocean.md)**

**Crafts spawned by a contract: planned — read in the code, not measured.** A craft to repair and a wreck
holding a kerbal to rescue are placed at the height the ground should have, not on the ground built, and
not in `PRELAUNCH`; some have been seen to jump when reached. Read in the code, that jump is stock's own.

**→ Full chapter: [Crafts spawned by a contract](work-in-progress/stock/crafts-spawned-by-a-contract.md)**

### KSP Community Fixes

**Its own ground fix: planned — announced, not released.** One of its maintainers plans a ground fix for
it, which this mod's terrain fix would have to step back from.

**→ Full chapter: [KSP Community Fixes: its own ground fix](work-in-progress/ksp-community-fixes/its-own-ground-fix.md)**

### Kopernicus

**A body from a planet pack: planned — nothing has been measured on one.** The campaign is prepared on
Outer Planets Mod.

**→ Full chapter: [Kopernicus: a body from a planet pack](work-in-progress/kopernicus/a-body-from-a-planet-pack.md)**

**Its next release: planned — waits for that release.** It moves the floating origin when a landed craft
is reloaded in flight, which stock and its current release leave alone; read in its source, not measured.

**→ Full chapter: [Kopernicus: its next release](work-in-progress/kopernicus/its-next-release.md)**

### BurstPQS

**Its release 1.0.28: planned.** It changes how BurstPQS places the quads this mod's scatter fix hangs the
scatter from; every campaign ran with 1.0.27.

**→ Full chapter: [BurstPQS: its release 1.0.28](work-in-progress/burst-pqs/its-release-1-0-28.md)**

### Kerbal Konstructs

**The ground it flattens: planned — read in the source, not measured.** Kerbal Konstructs flattens the
ground with stock decals, which edit the height before this fix places it, so the flattening should be
kept.

**→ Full chapter: [Kerbal Konstructs: the ground it flattens](work-in-progress/kerbal-konstructs/the-ground-it-flattens.md)**

### Promised Worlds

**Its bodies: planned — read in the source, not played.** Promised Worlds shapes its bodies with terrain
mods of its own and puts its star systems far from the Sun; read in the code, neither should reach the
ground this mod places.

**→ Full chapter: [Promised Worlds: its bodies](work-in-progress/promised-worlds/its-bodies.md)**

### Parallax

**Loading a craft on the Mun: planned — the save has to be made again with Parallax.** The save of the
Mun was made without Parallax, and the spread it reads with Parallax comes from a Parallax collider at
that spot: with Parallax's colliders off, the capsule comes back as without Parallax.

**→ Full chapter: [Parallax: loading a craft on the Mun](work-in-progress/parallax/loading-a-craft-on-the-mun.md)**
