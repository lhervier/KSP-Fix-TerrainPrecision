# BurstPQS: the campaigns

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#limits-and-solutions): one limit, on BurstPQS.

**Status: checked, nothing worse with this mod.** Every scripted campaign of this mod,
played with BurstPQS 1.0.27 (with Kopernicus 251, KSPTextureLoader and KSPBurst with its compiler), each in
two installs: **BurstPQS** (KSP, KSP Community Fixes, BurstPQS and what it requires) and **BurstPQS with this
mod, as it installs**. This mod's terrain fix steps back by itself on the bodies BurstPQS builds: there, the
campaigns were played with it turned off (`fixTerrain = false`), which comes to the same. On Real Solar
System, where BurstPQS leaves the Earth and the Moon to stock and the terrain fix corrects them, they were
played again as this mod installs. The ground campaigns were also played on KSP with KSP Community Fixes
alone. The saves are the published
ones; a save made on stock ground is set down once onto BurstPQS's ground at its first load (the cases of
[Existing saves](../../../common/existing-saves.md)). In each table, the spread over the
repetitions of the protocol, in millimetres.

## What BurstPQS does

BurstPQS replaces `PQS.BuildQuad`: on a body it builds, the vertex placement this mod patches is never
called. It works out the vertices in double precision, and while the world turns with the body, places the
quads in double from the body's own position and rotation, again at every update of their positions. On a
body it cannot build, because one of its terrain mods has no Burst version, it gives the whole body back to
stock (see [the bodies it leaves to stock](the-bodies-it-leaves-to-stock.md)). It has no code for `PQSCity`
or `PQSCity2`, and lets stock spawn the scatter.

## The ground

[The loading protocol](../../checking/loading-protocol.md), six loads, ground under the craft read by
KSP Diag - Terrain Height:

| | KSP + KSPCF | BurstPQS | BurstPQS + this mod |
|---|---|---|---|
| Kerbin | 75.2 | 0.006 | 0.009 |
| Mun | 34.4 | 0.008 | 0.010 |
| Minmus | 6.6 | 0.008 | 0.030 |
| Gilly | 1.5 | 0.010 | 0.007 |

On these four saves, the ground BurstPQS builds lies within 0.04 mm of the ground this mod's terrain fix
builds on KSP alone (the published series): two codes, written apart, place the same ground. The same holds
under the grass craft of the runway save on Kerbin, and on the regolith of the Kerbal Konstructs runway on the
Mun: each is set down by the same amount at every load as in the published series with this mod.

[The approach protocol](../../checking/approach.md), six trips: ground under the craft 21.6 to
25.0 on KSP + KSPCF, 0.012 at most with BurstPQS, with or without this mod.
[The switching protocol](../../checking/switching.md), six rounds: 143.2, then 0.005.
[The driving protocol](../../checking/driving-protocol.md), on the grass: at a move of the world,
*Difference* changes by +51.4 and −48.8 on KSP + KSPCF, by +0.25 and +0.48 with BurstPQS (+0.24, +0.50
with this mod). [The flight protocol](../../checking/flight-protocol.md), the step between cousins
one at least built in flight, median / 90th percentile / largest: 0.071 / 0.228 / 1.000 with BurstPQS,
against 4.520 / 16.930 / 22.454 on stock in the published series. The seams protocol found no step of
50 mm or more between two subdivision levels in 150 reverts, the largest 0.9 mm.

**This mod's terrain fix steps back by itself on the bodies BurstPQS builds**, so that the two never place
the same quads; `KSP.log` says `<body>: terrain placed by BurstPQS` for each. The loading protocol with the
terrain fix on, six loads, ground under the craft: Kerbin 0.005, Mun 0.008, Minmus 0.013, Gilly 0.012.

## The statics

BurstPQS does not touch them. Without this mod they keep the stock rounding, and since the ground no
longer moves, they now move **against** it; with this mod, they hold.

**→ Full chapter: [BurstPQS: the campaigns, the statics](../../../statics/non-regression/burst-pqs/the-campaigns.md)**

## The scatter

BurstPQS lets stock spawn the scatter, and stock still places each holder through the sphere, rounded at
planet scale: the ground holds, the rocks, grass and trees move against it, from one load to the next (141 on
Kerbin, 18 on the Mun, median over the measured vertices) and at every move of the world. This mod's scatter
fix first missed most of the holders with BurstPQS, those built as the scene opens; it now hangs them all:
0.065 on Kerbin and 0.013 on the Mun at a load, rocks with colliders included, nothing at a move of the world
or in flight.

**→ Full chapter: [BurstPQS: the scatter](../../../scatter/limits/burst-pqs/the-scatter.md)**

## The anchor

Nothing to play. The three stock behaviours this mod's anchor fix corrects, the anchor's collider stopping
above its bottom, the vessel raised at its load, the anchor riveted one frame late, are in the anchor's part
and in the loading of a vessel: BurstPQS has no code for either, it only builds and places the terrain.

## No regression seen

The holder pools in flight and across scene changes: no broken rule. The floating origin: the same as
without BurstPQS. Destroyed buildings and time warp: in
[the statics](../../../statics/non-regression/burst-pqs/the-campaigns.md#no-regression-seen).
