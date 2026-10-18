# Work in progress: BurstPQS

Part of [Terrain Precision Fix](../../README.md), one mod of [Work in progress](../work-in-progress.md): what is still to check, on BurstPQS.

[BurstPQS](https://github.com/Phantomical/BurstPQS) builds the terrain in place of stock, in Burst-compiled
jobs, and places it in double precision on its own. It requires Kopernicus. Every campaign of this mod was
played again with it, in two installs: **BurstPQS** (KSP, KSP Community Fixes, BurstPQS and what it requires)
and **BurstPQS with this mod, as it installs** (its terrain fix steps back by itself on the bodies BurstPQS
builds; the statics, scatter and anchor fixes on). The short answer so far: BurstPQS holds the ground still, but not the statics nor the scatter, it
leaves three bodies of Real Solar System to stock, and the Mun shows darker quads in a first flight, from
Kopernicus's BurstPQS plugin for its KSC scatter mask. This mod now supports BurstPQS by itself: its terrain
fix steps back on every body BurstPQS builds and keeps correcting the bodies it leaves to stock, and its
scatter fix hangs every holder there.

## The campaigns played with BurstPQS

**In progress — measured.** On the bodies BurstPQS builds, the ground no longer moves at a load, an approach,
a vessel switch, a move of the world or in a fast flight, and it is the same ground as this mod's terrain fix
builds. The statics still move without this mod, and now against a ground that holds; with it, they hold.
This mod's terrain fix steps back by itself on the bodies BurstPQS builds: nothing placed twice, and the
ground holds as with BurstPQS alone.

**→ Full chapter: [BurstPQS: the campaigns](burst-pqs/the-campaigns.md)**

## The bodies BurstPQS leaves to stock

**In progress — measured.** On Real Solar System, BurstPQS gives the Earth, the Moon and Mars back to stock,
and their ground moves as on stock. With this mod's terrain fix off, nothing corrects it; with it on, it
holds. This mod's terrain fix now goes on correcting them by itself, while it steps back on the bodies
BurstPQS builds. The next Real Solar System, not released yet, lets BurstPQS build them: built from its
development version, their ground holds with BurstPQS alone.

**→ Full chapter: [BurstPQS: the bodies it leaves to stock](burst-pqs/the-bodies-it-leaves-to-stock.md)**

## The scatter

**In progress — fixed, measured.** With BurstPQS, rocks, grass and trees move against the ground from one
load to the next by more than on stock, and jump against it at every move of the world. This mod's scatter
fix first missed every holder built as the scene opens; it now hangs them all: hundredths of a millimetre at a
load, rocks with colliders included, nothing at a move of the world or in flight.

**→ Full chapter: [BurstPQS: the scatter](burst-pqs/the-scatter.md)**

## Darker quads on the Mun

**In progress — cause found, reported to BurstPQS ([issue #15](https://github.com/Phantomical/BurstPQS/issues/15)).** From an orbit 5 km above the Mun, whole quads of the ground
are drawn much darker than their neighbours, the relief running on unbroken from one to the next, for the
first minutes of the first flight after KSP starts. Not on KSP with KSP Community Fixes alone, nor with
Kopernicus alone. The cause is the plugin Kopernicus ships for BurstPQS with its KSC scatter mask: it wipes
the colour of every quad of a sphere's first build; taking the mask off the Mun makes them go. Seen also on
Minmus, on Laythe from the ground and on Mercury of Real Solar System.

**→ Full chapter: [BurstPQS: darker quads on the Mun](burst-pqs/darker-quads-on-the-mun.md)**

## Its memory

**To dig — read in its code, not yet seen in the game.** A pinned handle of two noise mods released twice
at every quad, and the Burst versions of the terrain mods dropped without being freed at each scene change.
Maps loaded on demand might also stay loaded after a body is left, but no case was found yet where it happens.

**→ Full chapter: [BurstPQS: its memory](burst-pqs/its-memory.md)**
