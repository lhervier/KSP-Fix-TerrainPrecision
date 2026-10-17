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
without BurstPQS. With it off, the same bodies show the stock defects in flight (cousins built in flight:
70.6 / 274.1 / 461.5 mm, median / 90th percentile / largest) and under a rover at a move of the world. With
this mod as it installs: [the flight protocol](../../checking-the-culprit-flight.md), 0.45 / 1.05 / 2.15
(0.38 / 0.83 / 2.14 with this mod on KSP alone, published); on the runway of Cape Canaveral, the grass next to
it moves by +0.14 and +0.24 at a move of the world, against +226 and −52.6 with the terrain fix off. The
steps between subdivision levels, a metre or more on the Earth, are those of
[the seam between subdivision levels](../../limits-and-solutions/stock/the-seam-between-subdivision-levels.md),
with or without this mod. The statics fix holds there all the same (see [the campaigns](the-campaigns.md)).

**What it means for this mod**: turning the terrain fix off everywhere, because BurstPQS is installed, would
leave the Earth and the Moon of Real Solar System uncorrected. It has to be turned off only on the bodies
BurstPQS builds, and kept on the bodies it leaves to stock. **It now does so by itself**: `KSP.log` says
`Earth: terrain given back to stock by BurstPQS`, then `Earth: terrain placed in double precision`, and the
same for the Moon. The loading protocol again, the terrain fix on: Earth 0.27, Moon 0.18.

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

**Outer Planets Mod** 2.2.12 (with Kopernicus 251): `BatchPQS enabled for surface` for every body, the
stock ones and its own (Hale, Ovok, Slate, Tekto, Priax, Polta, Wal, Tal, Thatmo, Nissee, Plock, Karen),
nothing left to stock.

*To check:* other planet packs, by the same lines of `KSP.log`. Until that version of Real Solar System is
released, the terrain fix stays needed on the Earth, the Moon and Mars.
