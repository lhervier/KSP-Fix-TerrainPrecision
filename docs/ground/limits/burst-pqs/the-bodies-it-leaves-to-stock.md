# BurstPQS: the bodies it leaves to stock

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#limits-and-solutions): one limit, on BurstPQS.

**Status: checked, a limit this mod handles by itself, until the next Real Solar System.** BurstPQS builds a body only if every terrain mod of that body has a
Burst version; otherwise it gives the whole body back to stock, and says so in `KSP.log`:
`[BurstPQS] BatchPQS not supported for surface <body>. Falling back to regular PQS`. On stock KSP, every body
is built by BurstPQS. On Real Solar System, **the Earth, the Moon and Mars are not**: two terrain mods of Real
Solar System, `PQSMod_VertexHeightMapRSS` and `PQSMod_VertexDefineCoastSmooth`, have no Burst version
(`is not supported by BatchPQS`). The Earth keeps its stock name in the log, `Kerbin`.

**This happens only with Real Solar System 20.1.3, its latest release.** Its master branch, not released yet,
lets BurstPQS build every body, and the case goes away (see [With the next Real Solar System](#with-the-next-real-solar-system)).
Until that version is out, this mod's terrain fix stays needed on these three bodies: it takes over where
BurstPQS gives the body back to stock, and their ground is built and placed without the stock defects.

On those bodies the ground moves as on stock, and with this mod's terrain fix off nothing corrects it.
[The loading protocol](../../README.md#checked) on Real Solar System 20.1.3, six loads, ground under
the craft, spread in millimetres, with BurstPQS 1.0.30 and Kopernicus 252, two series of six loads; on Mars,
the save of [This mod's safeguard](../../../common/safeguard.md), in Utopia Planitia, and the terrain fix off,
played with BurstPQS 1.0.27 and Kopernicus 248:

| | BurstPQS | BurstPQS + this mod, terrain fix off (1.0.27) | BurstPQS + this mod | this mod alone |
|---|---|---|---|---|
| Earth | 438 and 546 | 1 080 | **0.40 and 0.46** | 0.3 (published) |
| Moon | 126 and 194 | 272 | **0.24 and 0.19** | 0.1 (published) |
| Mars (1.0.27) | 40.8 | 24.9 | **0.13** | 0.12 |

With the terrain fix on, the log says `Earth: terrain placed in double precision`, and the same for the Moon
and Mars: the ground holds as without BurstPQS. With it off, the same bodies show the stock defects in flight (cousins built in flight:
70.6 / 274.1 / 461.5 mm, median / 90th percentile / largest, BurstPQS 1.0.27) and under a rover at a move of
the world. With this mod as it installs: [the flight protocol](../../README.md#checked), 0.45 / 1.05 / 2.15
(BurstPQS 1.0.27; 0.38 / 0.83 / 2.14 with this mod on KSP alone, published); on the runway of Cape Canaveral,
the grass next to it moves by −0.06 at a move of the world (BurstPQS 1.0.30), against +191.9 with BurstPQS
alone and +226 with the terrain fix off (1.0.27). The
steps between subdivision levels, a metre or more on the Earth, are those of
[the seam between subdivision levels](../stock/the-seam-between-subdivision-levels.md),
with or without this mod. The statics fix holds there all the same (see [the campaigns](the-campaigns.md)).

**What it means for this mod**: turning the terrain fix off everywhere, because BurstPQS is installed, would
leave the Earth and the Moon of Real Solar System uncorrected. It has to be turned off only on the bodies
BurstPQS builds, and kept on the bodies it leaves to stock. **It now does so by itself**: `KSP.log` says
`Earth: terrain given back to stock by BurstPQS`, then `Earth: terrain placed in double precision`, and the
same for the Moon and Mars, with BurstPQS 1.0.30 and Kopernicus 252 as with 1.0.27.

## With the next Real Solar System

The development version of Real Solar System, on its master branch but not released yet, uses Kopernicus's
own `VertexHeightMap` in place of `PQSMod_VertexHeightMapRSS`, and ships a Burst version of
`PQSMod_VertexDefineCoastSmooth` (`RealSolarSystem.BurstPQS.dll`). Built from that branch, in place of Real
Solar System 20.1.3, the rest of the install unchanged (BurstPQS 1.0.27, Kopernicus 248): `KSP.log` says `BatchPQS enabled for surface` for
every body, the Earth (`Kerbin`), the Moon and Mars included, and nothing falls back to stock. The same loading
protocol, six loads, ground under the craft, spread in millimetres:

| | without BurstPQS | BurstPQS |
|---|---|---|
| Earth | 846.5 | **0.38** |
| Moon | 210.9 | **0.15** |
| Mars | 29.3 | **0.17** |

With that version, BurstPQS holds the ground of these bodies as this mod's terrain fix does (0.3, 0.1 and
0.12). The saves were made with Real Solar System 20.1.3, whose height maps are read slightly
differently: the craft settles once at every load (about 3 mm on the Earth, 134 mm on the Moon, 52 mm on
Mars), always by the same amount.

**Outer Planets Mod** 2.2.12 (with Kopernicus 251): `BatchPQS enabled for surface` for every body, the
stock ones and its own (Hale, Ovok, Slate, Tekto, Priax, Polta, Wal, Tal, Thatmo, Nissee, Plock, Karen),
nothing left to stock.

## To do

- **Wait for the next release of Real Solar System.** Until then, this mod's terrain fix stays needed on the
  Earth, the Moon and Mars. Once it is out, BurstPQS builds every body of the planet packs checked here. Its
  master branch still caps Kopernicus at 251, while BurstPQS 1.0.30 requires 252 or later: the two install
  together only once Real Solar System accepts Kopernicus 252.
- **Look at the darker quads with Kopernicus 252**, which no longer ships the mask that caused them (see
  [Darker quads: not from this mod](README.md#darker-quads-not-from-this-mod),
  [BurstPQS issue #14](https://github.com/Phantomical/BurstPQS/issues/14)). With both, dropping this mod's
  terrain fix, to depend on BurstPQS for the ground, can be considered.
