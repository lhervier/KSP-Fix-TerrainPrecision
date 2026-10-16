# Work in progress: BurstPQS

Part of [Terrain Precision Fix](../../README.md), one mod of [Work in progress](../work-in-progress.md): what is still to check, on BurstPQS.

[BurstPQS](https://github.com/Phantomical/BurstPQS) builds the terrain in place of stock, in Burst-compiled
jobs, and places it in double precision on its own. It requires Kopernicus. Every campaign of this mod was
played again with it, in two installs: **BurstPQS** (KSP, KSP Community Fixes, BurstPQS and what it
requires) and **BurstPQS with this mod, its terrain fix off** (`fixTerrain = false`, the statics, scatter and
anchor fixes on). The short answer so far: BurstPQS holds the ground still, but not the statics nor the
scatter, it leaves three bodies of Real Solar System to stock, and the Mun shows darker quads in flight.

## The campaigns played with BurstPQS

**In progress — measured.** On the bodies BurstPQS builds, the ground no longer moves at a load, an approach,
a vessel switch, a move of the world or in a fast flight, and it is the same ground as this mod's terrain fix
builds. The statics still move without this mod, and now against a ground that holds; with it, they hold.
This mod's terrain fix, left on, does nothing on top of BurstPQS.

**→ Full chapter: [BurstPQS: the campaigns](burst-pqs/the-campaigns.md)**

## The bodies BurstPQS leaves to stock

**In progress — measured.** On Real Solar System, BurstPQS gives the Earth, the Moon and Mars back to stock,
and their ground moves as on stock. With this mod's terrain fix off, nothing corrects it; with it on, it
holds. The terrain fix would have to be turned off body by body.

**→ Full chapter: [BurstPQS: the bodies it leaves to stock](burst-pqs/the-bodies-it-leaves-to-stock.md)**

## The scatter

**In progress — measured.** With BurstPQS, rocks, grass and trees move against the ground from one load to
the next by more than on stock, and jump against it at every move of the world. This mod's scatter fix, as
it is, misses every holder built as the scene opens: nothing at a load, a catch-up in flight only.

**→ Full chapter: [BurstPQS: the scatter](burst-pqs/the-scatter.md)**

## Darker quads on the Mun

**In progress — seen, not measured.** From an orbit 5 km above the Mun, whole quads of the ground are drawn
much darker than their neighbours, the relief running on unbroken from one to the next, for the first
minutes of the flight, then less and less. Not compared yet with the same flight without BurstPQS.

**→ Full chapter: [BurstPQS: darker quads on the Mun](burst-pqs/darker-quads-on-the-mun.md)**
