# BurstPQS: the bodies it leaves to stock

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [BurstPQS](../../work-in-progress/burst-pqs.md).

**Status: in progress — measured.** BurstPQS builds a body only if every terrain mod of that body has a
Burst version; otherwise it gives the whole body back to stock, and says so in `KSP.log`:
`[BurstPQS] BatchPQS not supported for surface <body>. Falling back to regular PQS`. On stock KSP, every body
is built by BurstPQS. On Real Solar System, **the Earth, the Moon and Mars are not**: two terrain mods of Real
Solar System, `PQSMod_VertexHeightMapRSS` and `PQSMod_VertexDefineCoastSmooth`, have no Burst version
(`is not supported by BatchPQS`). The Earth keeps its stock name in the log, `Kerbin`.

On those bodies the ground moves as on stock, and with this mod's terrain fix off nothing corrects it.
[The loading protocol](../../checking-the-culprit-loading.md) on Real Solar System, six loads, ground under
the craft, spread in millimetres:

| | BurstPQS | BurstPQS + this mod, terrain fix off | BurstPQS + this mod, terrain fix on | this mod alone (published) |
|---|---|---|---|---|
| Earth | 792 | 1 080 | **0.27** | 0.3 |
| Moon | 334 | 272 | **0.13** | 0.1 |

With the terrain fix on, the log says `Earth: terrain placed in double precision`, and the ground holds as
without BurstPQS. The same bodies show stock steps between subdivision levels (up to 2.6 m on the Earth) and
in flight (cousins built in flight: 70.6 / 274.1 / 461.5 mm, median / 90th percentile / largest), and the
ground still jumps under a rover at a move of the world. The statics fix holds there all the same (see
[the campaigns](the-campaigns.md)).

**What it means for this mod**: turning the terrain fix off everywhere, because BurstPQS is installed, would
leave the Earth and the Moon of Real Solar System uncorrected. It has to be turned off only on the bodies
BurstPQS builds, and kept on the bodies it leaves to stock.

## With the next Real Solar System

The development version of Real Solar System, on its master branch but not released yet, uses Kopernicus's
own `VertexHeightMap` in place of `PQSMod_VertexHeightMapRSS`, and ships a Burst version of
`PQSMod_VertexDefineCoastSmooth` (`RealSolarSystem.BurstPQS.dll`). Built from that branch, in place of Real
Solar System 20.1.3, the rest of the install unchanged: `KSP.log` says `BatchPQS enabled for surface` for
every body, the Earth (`Kerbin`), the Moon and Mars included, and nothing falls back to stock. The same loading
protocol, six loads, ground under the craft, spread in millimetres:

| | without BurstPQS | BurstPQS |
|---|---|---|
| Earth | 846.5 | **0.38** |
| Moon | 210.9 | **0.15** |

With that version, BurstPQS holds the ground of these bodies as this mod's terrain fix does (0.3 and 0.1,
published). The saves were made with Real Solar System 20.1.3, whose height maps are read slightly
differently: the craft settles once at every load (about 3 mm on the Earth, 134 mm on the Moon), always by the
same amount.

*To check:* Outer Planets Mod and other planet packs, by the same lines of `KSP.log`. Until that version of
Real Solar System is released, the terrain fix stays needed on the Earth, the Moon and Mars.
