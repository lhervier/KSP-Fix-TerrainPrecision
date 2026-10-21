# The runs: the scatter

Part of [Terrain Precision Fix](../../README.md), [the scatter](../../docs/scatter/README.md): the saves, the scripts and the `KSP.log` of every session, without this mod and with it. The scripts are in [`automation/`](automation).

## The scatter

The readings of [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter), kept as they were
logged, copied out of `KSP.log`, in the folder of the page that reads them. They are read in
[Checking the scatter: loading the same save](../../docs/scatter/checking/loading.md),
[Checking the scatter: driving on while the world moves](../../docs/scatter/checking/driving.md),
[Checking the scatter: in flight](../../docs/scatter/checking/flight.md),
[The scatter holders](../../docs/scatter/non-regression/stock/the-scatter-holders.md) and
[Kopernicus: scatter with colliders](../../docs/scatter/non-regression/kopernicus/scatter-with-colliders.md).
What a record holds, line by line, is in
[the instrument's page](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md#the-log).

*The log lines quoted on this page come from runs of an earlier version of this mod, when its log prefix was `[TerrainPrecisionFix]`; it is now `[KSPFixTerrainPrecision]`.*

**The objects** — after a load, while the world moves, and over a flight — were read with Terrain
Precision Fix 0.3.0 at `logLevel = Debug`, each series played by its script through
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), in three configurations named in the files:
`stock`, without this mod; `fix`, with this mod as installed, its scatter fix on; and `fix-no-scatter`,
with `fixScatter = false`, the terrain fix alone. The records were copied out of `KSP.log` by
[`extract-scatter-records.py`](automation/extract-scatter-records.py), and each series keeps beside them
what its script printed (`-script.txt`) and the number and closing line of every record it took
(`-lines.json`). With the scatter fix on, this mod wrote to `KSP.log` that it had acted on each body before
its first record, as in:

```
[TerrainPrecisionFix] Kerbin: scatter drawn from its terrain quads (first holder was +23.16 mm off)
[TerrainPrecisionFix] Mun: scatter drawn from its terrain quads (first holder was -7.51 mm off)
```

**The holder pools and the colliders** were read earlier, in three configurations: on stock, with Terrain
Precision Fix 0.1.0 alone (`tpf` in the names of the files), and with the scatter fix as well (`both`),
when it was a mod of its own, Rock Precision Fix 0.1.0, installed next to it: the same two patches, whose
lines in these logs are tagged `[RockPrecisionFix]`.

The protocols are [the scatter, load after load](../../docs/scatter/checking/loading-protocol.md),
[the scatter, while the world moves](../../docs/scatter/checking/driving-protocol.md)
and [the scatter, along a flight](../../docs/scatter/checking/flight-protocol.md), and the
chapters *The protocol* of [The scatter
holders](../../docs/scatter/non-regression/stock/the-scatter-holders.md#the-protocol)
and [Kopernicus: scatter with
colliders](../../docs/scatter/non-regression/kopernicus/scatter-with-colliders.md#the-protocol).

The saves:

- [`reference-kerbin.sfs`](checking/loading/reference-kerbin.sfs) and [`reference-mune.sfs`](checking/loading/reference-mune.sfs)
  — a single Mk1 command pod landed on Kerbin, about 8 km north-west of the KSC, where the scatter is
  grass and trees, and on the Mun, where it is rocks;
- [`driving-kerbin.sfs`](../ground/checking/driving/driving-kerbin.sfs) — the rover of
  [the driving protocol](../ground/README.md#the-driving-protocol), on the grass south of the runway of the KSC;
- [`cactus-kerbin.sfs`](checking/driving/cactus-kerbin.sfs) — the same rover in a
  desert of Kerbin, 497 m north of a cactus, facing it: the save of the film;
- [`ref-mune-5km.sfs`](checking/flight/ref-mune-5km.sfs) — a single Mk1 command pod in a circular equatorial
  orbit 5 km over the Mun, the same save as
  [PQSBench's](https://github.com/lhervier/KSP-Util-PQSBench/blob/main/perfs/README.md);
- [`ref-kerbin-scatter-collider-eva.sfs`](non-regression/kopernicus/scatter-with-colliders/ref-kerbin-scatter-collider-eva.sfs) — a Mk1 command pod
  landed in a desert of Kerbin, with Jebediah out on EVA, standing on a boulder next to it.

### The scatter: the objects, over twelve loads

KSP 1.12.5 on Windows, `GameData` holding Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag -
Scatter and KSP-Util-MCPServer, and this mod for `fix` and `fix-no-scatter`. Terrain scatter on, the log flushed at
once. Each save loaded twelve times per configuration, in a single session of KSP, by
[`run-scatter-loading.py`](automation/run-scatter-loading.py), which pressed *Record the rocks* every 3 s
after each load until every holder was built and the counts were the same twice in a row; one file per
load, holding the last record taken after it.

| load | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kerbin, `stock` | [`1`](checking/loading/kerbin-stock-load1.log) | [`2`](checking/loading/kerbin-stock-load2.log) | [`3`](checking/loading/kerbin-stock-load3.log) | [`4`](checking/loading/kerbin-stock-load4.log) | [`5`](checking/loading/kerbin-stock-load5.log) | [`6`](checking/loading/kerbin-stock-load6.log) | [`7`](checking/loading/kerbin-stock-load7.log) | [`8`](checking/loading/kerbin-stock-load8.log) | [`9`](checking/loading/kerbin-stock-load9.log) | [`10`](checking/loading/kerbin-stock-load10.log) | [`11`](checking/loading/kerbin-stock-load11.log) | [`12`](checking/loading/kerbin-stock-load12.log) |
| Kerbin, `fix-no-scatter` | [`1`](checking/loading/kerbin-fix-no-scatter-load1.log) | [`2`](checking/loading/kerbin-fix-no-scatter-load2.log) | [`3`](checking/loading/kerbin-fix-no-scatter-load3.log) | [`4`](checking/loading/kerbin-fix-no-scatter-load4.log) | [`5`](checking/loading/kerbin-fix-no-scatter-load5.log) | [`6`](checking/loading/kerbin-fix-no-scatter-load6.log) | [`7`](checking/loading/kerbin-fix-no-scatter-load7.log) | [`8`](checking/loading/kerbin-fix-no-scatter-load8.log) | [`9`](checking/loading/kerbin-fix-no-scatter-load9.log) | [`10`](checking/loading/kerbin-fix-no-scatter-load10.log) | [`11`](checking/loading/kerbin-fix-no-scatter-load11.log) | [`12`](checking/loading/kerbin-fix-no-scatter-load12.log) |
| Kerbin, `fix` | [`1`](checking/loading/kerbin-fix-load1.log) | [`2`](checking/loading/kerbin-fix-load2.log) | [`3`](checking/loading/kerbin-fix-load3.log) | [`4`](checking/loading/kerbin-fix-load4.log) | [`5`](checking/loading/kerbin-fix-load5.log) | [`6`](checking/loading/kerbin-fix-load6.log) | [`7`](checking/loading/kerbin-fix-load7.log) | [`8`](checking/loading/kerbin-fix-load8.log) | [`9`](checking/loading/kerbin-fix-load9.log) | [`10`](checking/loading/kerbin-fix-load10.log) | [`11`](checking/loading/kerbin-fix-load11.log) | [`12`](checking/loading/kerbin-fix-load12.log) |
| the Mun, `stock` | [`1`](checking/loading/mun-stock-load1.log) | [`2`](checking/loading/mun-stock-load2.log) | [`3`](checking/loading/mun-stock-load3.log) | [`4`](checking/loading/mun-stock-load4.log) | [`5`](checking/loading/mun-stock-load5.log) | [`6`](checking/loading/mun-stock-load6.log) | [`7`](checking/loading/mun-stock-load7.log) | [`8`](checking/loading/mun-stock-load8.log) | [`9`](checking/loading/mun-stock-load9.log) | [`10`](checking/loading/mun-stock-load10.log) | [`11`](checking/loading/mun-stock-load11.log) | [`12`](checking/loading/mun-stock-load12.log) |
| the Mun, `fix-no-scatter` | [`1`](checking/loading/mun-fix-no-scatter-load1.log) | [`2`](checking/loading/mun-fix-no-scatter-load2.log) | [`3`](checking/loading/mun-fix-no-scatter-load3.log) | [`4`](checking/loading/mun-fix-no-scatter-load4.log) | [`5`](checking/loading/mun-fix-no-scatter-load5.log) | [`6`](checking/loading/mun-fix-no-scatter-load6.log) | [`7`](checking/loading/mun-fix-no-scatter-load7.log) | [`8`](checking/loading/mun-fix-no-scatter-load8.log) | [`9`](checking/loading/mun-fix-no-scatter-load9.log) | [`10`](checking/loading/mun-fix-no-scatter-load10.log) | [`11`](checking/loading/mun-fix-no-scatter-load11.log) | [`12`](checking/loading/mun-fix-no-scatter-load12.log) |
| the Mun, `fix` | [`1`](checking/loading/mun-fix-load1.log) | [`2`](checking/loading/mun-fix-load2.log) | [`3`](checking/loading/mun-fix-load3.log) | [`4`](checking/loading/mun-fix-load4.log) | [`5`](checking/loading/mun-fix-load5.log) | [`6`](checking/loading/mun-fix-load6.log) | [`7`](checking/loading/mun-fix-load7.log) | [`8`](checking/loading/mun-fix-load8.log) | [`9`](checking/loading/mun-fix-load9.log) | [`10`](checking/loading/mun-fix-load10.log) | [`11`](checking/loading/mun-fix-load11.log) | [`12`](checking/loading/mun-fix-load12.log) |

What the script printed and what it recorded, per save and configuration:

| series | what the script printed | what it recorded |
|---|---|---|
| Kerbin, `stock` | [`kerbin-stock-script.txt`](checking/loading/kerbin-stock-script.txt) | [`kerbin-stock-lines.json`](checking/loading/kerbin-stock-lines.json) |
| Kerbin, `fix-no-scatter` | [`kerbin-fix-no-scatter-script.txt`](checking/loading/kerbin-fix-no-scatter-script.txt) | [`kerbin-fix-no-scatter-lines.json`](checking/loading/kerbin-fix-no-scatter-lines.json) |
| Kerbin, `fix` | [`kerbin-fix-script.txt`](checking/loading/kerbin-fix-script.txt) | [`kerbin-fix-lines.json`](checking/loading/kerbin-fix-lines.json) |
| the Mun, `stock` | [`mun-stock-script.txt`](checking/loading/mun-stock-script.txt) | [`mun-stock-lines.json`](checking/loading/mun-stock-lines.json) |
| the Mun, `fix-no-scatter` | [`mun-fix-no-scatter-script.txt`](checking/loading/mun-fix-no-scatter-script.txt) | [`mun-fix-no-scatter-lines.json`](checking/loading/mun-fix-no-scatter-lines.json) |
| the Mun, `fix` | [`mun-fix-script.txt`](checking/loading/mun-fix-script.txt) | [`mun-fix-lines.json`](checking/loading/mun-fix-lines.json) |

Every record of Kerbin, in the three series, ends on the same line, but for its number:

```
End of record 2: 64 quads with rocks, 118 holders (0 not built yet); nearest quad 'Kerbin Zn3010000130': 218 rocks, 1780 vertices measured, 0 without ground under them, 0 colliders measured
```

and every record of the Mun on this one:

```
End of record 26: 128 quads with rocks, 128 holders (0 not built yet); nearest quad 'Mun Zp211333000': 20 rocks, 200 vertices measured, 0 without ground under them, 0 colliders measured
```

So every record was taken once all the holders were built, and all the records of a body name the same
nearest quad: its objects and their measured vertices compare one by one from one load to the next, and
from one series to another.

### The scatter: the objects, across a move of the world

The same install, with `driving-kerbin.sfs`, by
[`run-scatter-driving.py`](automation/run-scatter-driving.py): six loads per configuration, in a single
session of KSP, one move of the origin per load, the rover stopped 498.6 m from the origin, then just after
the move, then 2.6 m farther on with no move. Each record ends on the same counts: 8 quads with rocks, 13
holders, all built, the nearest quad `Kerbin Zn3010001020` with 50 rocks and 400 vertices.

| load | before the move | after it | a few metres farther on |
|---|---|---|---|
| `stock`, 1 | [`before`](checking/driving/kerbin-stock-load1-before.log) | [`after`](checking/driving/kerbin-stock-load1-after.log) | [`again`](checking/driving/kerbin-stock-load1-again.log) |
| `stock`, 2 | [`before`](checking/driving/kerbin-stock-load2-before.log) | [`after`](checking/driving/kerbin-stock-load2-after.log) | [`again`](checking/driving/kerbin-stock-load2-again.log) |
| `stock`, 3 | [`before`](checking/driving/kerbin-stock-load3-before.log) | [`after`](checking/driving/kerbin-stock-load3-after.log) | [`again`](checking/driving/kerbin-stock-load3-again.log) |
| `stock`, 4 | [`before`](checking/driving/kerbin-stock-load4-before.log) | [`after`](checking/driving/kerbin-stock-load4-after.log) | [`again`](checking/driving/kerbin-stock-load4-again.log) |
| `stock`, 5 | [`before`](checking/driving/kerbin-stock-load5-before.log) | [`after`](checking/driving/kerbin-stock-load5-after.log) | [`again`](checking/driving/kerbin-stock-load5-again.log) |
| `stock`, 6 | [`before`](checking/driving/kerbin-stock-load6-before.log) | [`after`](checking/driving/kerbin-stock-load6-after.log) | [`again`](checking/driving/kerbin-stock-load6-again.log) |
| `fix-no-scatter`, 1 | [`before`](checking/driving/kerbin-fix-no-scatter-load1-before.log) | [`after`](checking/driving/kerbin-fix-no-scatter-load1-after.log) | [`again`](checking/driving/kerbin-fix-no-scatter-load1-again.log) |
| `fix-no-scatter`, 2 | [`before`](checking/driving/kerbin-fix-no-scatter-load2-before.log) | [`after`](checking/driving/kerbin-fix-no-scatter-load2-after.log) | [`again`](checking/driving/kerbin-fix-no-scatter-load2-again.log) |
| `fix-no-scatter`, 3 | [`before`](checking/driving/kerbin-fix-no-scatter-load3-before.log) | [`after`](checking/driving/kerbin-fix-no-scatter-load3-after.log) | [`again`](checking/driving/kerbin-fix-no-scatter-load3-again.log) |
| `fix-no-scatter`, 4 | [`before`](checking/driving/kerbin-fix-no-scatter-load4-before.log) | [`after`](checking/driving/kerbin-fix-no-scatter-load4-after.log) | [`again`](checking/driving/kerbin-fix-no-scatter-load4-again.log) |
| `fix-no-scatter`, 5 | [`before`](checking/driving/kerbin-fix-no-scatter-load5-before.log) | [`after`](checking/driving/kerbin-fix-no-scatter-load5-after.log) | [`again`](checking/driving/kerbin-fix-no-scatter-load5-again.log) |
| `fix-no-scatter`, 6 | [`before`](checking/driving/kerbin-fix-no-scatter-load6-before.log) | [`after`](checking/driving/kerbin-fix-no-scatter-load6-after.log) | [`again`](checking/driving/kerbin-fix-no-scatter-load6-again.log) |
| `fix`, 1 | [`before`](checking/driving/kerbin-fix-load1-before.log) | [`after`](checking/driving/kerbin-fix-load1-after.log) | [`again`](checking/driving/kerbin-fix-load1-again.log) |
| `fix`, 2 | [`before`](checking/driving/kerbin-fix-load2-before.log) | [`after`](checking/driving/kerbin-fix-load2-after.log) | [`again`](checking/driving/kerbin-fix-load2-again.log) |
| `fix`, 3 | [`before`](checking/driving/kerbin-fix-load3-before.log) | [`after`](checking/driving/kerbin-fix-load3-after.log) | [`again`](checking/driving/kerbin-fix-load3-again.log) |
| `fix`, 4 | [`before`](checking/driving/kerbin-fix-load4-before.log) | [`after`](checking/driving/kerbin-fix-load4-after.log) | [`again`](checking/driving/kerbin-fix-load4-again.log) |
| `fix`, 5 | [`before`](checking/driving/kerbin-fix-load5-before.log) | [`after`](checking/driving/kerbin-fix-load5-after.log) | [`again`](checking/driving/kerbin-fix-load5-again.log) |
| `fix`, 6 | [`before`](checking/driving/kerbin-fix-load6-before.log) | [`after`](checking/driving/kerbin-fix-load6-after.log) | [`again`](checking/driving/kerbin-fix-load6-again.log) |

What the script printed and what it recorded, per configuration:

| series | what the script printed | what it recorded |
|---|---|---|
| `stock` | [`kerbin-stock-script.txt`](checking/driving/kerbin-stock-script.txt) | [`kerbin-stock-lines.json`](checking/driving/kerbin-stock-lines.json) |
| `fix-no-scatter` | [`kerbin-fix-no-scatter-script.txt`](checking/driving/kerbin-fix-no-scatter-script.txt) | [`kerbin-fix-no-scatter-lines.json`](checking/driving/kerbin-fix-no-scatter-lines.json) |
| `fix` | [`kerbin-fix-script.txt`](checking/driving/kerbin-fix-script.txt) | [`kerbin-fix-lines.json`](checking/driving/kerbin-fix-lines.json) |

The film, with `fix-no-scatter` and KSP Diag - Floating Origin as well, by
[`film-scatter-driving.py`](automation/film-scatter-driving.py) on `cactus-kerbin.sfs`: the records just
before and just after the move that was kept,
[`cactus-fix-no-scatter-before.log`](checking/driving/cactus-fix-no-scatter-before.log) and
[`cactus-fix-no-scatter-after.log`](checking/driving/cactus-fix-no-scatter-after.log): 148 holders, all of
them `cactus`, and on the nearest quad, `Kerbin Zn2101001033`, 5 cactus and 50 vertices.

### The scatter: the objects, over a flight

Where the scatter is drawn once the terrain has kept building and destroying quads under a moving craft,
with the world origin following it. The same install, `stock` and `fix`, by
[`run-scatter-flight.py`](automation/run-scatter-flight.py): `ref-mune-5km.sfs` loaded once, then *Record
the rocks* pressed 30 s into the flight, again every two minutes, and once more after the pod crashed.

| flight | records | what the script printed | what it recorded |
|---|---|---|---|
| `stock` | [`mun-5km-stock-rocks.log`](checking/flight/mun-5km-stock-rocks.log) | [`mun-5km-stock-script.txt`](checking/flight/mun-5km-stock-script.txt) | [`mun-5km-stock-lines.json`](checking/flight/mun-5km-stock-lines.json) |
| `fix` | [`mun-5km-fix-rocks.log`](checking/flight/mun-5km-fix-rocks.log) | [`mun-5km-fix-script.txt`](checking/flight/mun-5km-fix-script.txt) | [`mun-5km-fix-lines.json`](checking/flight/mun-5km-fix-lines.json) |

Each file holds the six records. On stock, the script did not see the crash, the game keeping the wrecked
pod as the craft flown: the sixth record was taken by hand, and its line in `mun-5km-stock-lines.json` says
so. Every record has all its holders built, and 200 vertices measured on its nearest quad, all of them
with ground under them:

| record | quads with rocks, `stock` | nearest quad, `stock` | quads with rocks, `fix` | nearest quad, `fix` |
|---|---|---|---|---|
| 1 | 352 | `Mun Xn233333333` | 352 | `Mun Xn233333333` |
| 2 | 176 | `Mun Xn213333331` | 176 | `Mun Xn213333333` |
| 3 | 160 | `Mun Xn211311131` | 152 | `Mun Xn211311131` |
| 4 | 224 | `Mun Xn122002220` | 216 | `Mun Xn122002222` |
| 5 | 152 | `Mun Xn013313333` | 152 | `Mun Xn013331111` |
| 6, after the crash | 568 | `Mun Zn200000011` | 568 | `Mun Zn200000011` |

### The scatter: the holder pools, over a flight

The install of [the objects](#the-scatter-the-objects-over-twelve-loads), `stock` and `fix`, by
[`run-scatter-holders.py`](automation/run-scatter-holders.py) with `flight`: `ref-mune-5km.sfs` loaded once,
then *Record the holder pools* pressed 30 s into the flight, again every two minutes, and once more after the
pod crashed.

| flight | records | what the script printed | what it recorded |
|---|---|---|---|
| `stock` | [`mun-5km-stock-holders.log`](non-regression/stock/the-scatter-holders/mun-5km-stock-holders.log) | [`mun-5km-stock-script.txt`](non-regression/stock/the-scatter-holders/mun-5km-stock-script.txt) | [`mun-5km-stock-lines.json`](non-regression/stock/the-scatter-holders/mun-5km-stock-lines.json) |
| `fix` | [`mun-5km-fix-holders.log`](non-regression/stock/the-scatter-holders/mun-5km-fix-holders.log) | [`mun-5km-fix-script.txt`](non-regression/stock/the-scatter-holders/mun-5km-fix-script.txt) | [`mun-5km-fix-lines.json`](non-regression/stock/the-scatter-holders/mun-5km-fix-lines.json) |

With this mod, it wrote to `KSP.log` that it had acted on the Mun before the first record:

```
[TerrainPrecisionFix] Mun: terrain placed in double precision (first quad corrected by 3.32 mm)
[TerrainPrecisionFix] Mun: scatter drawn from its terrain quads (first holder was +1.65 mm off)
```

Each file holds the six records. Every record of both flights ends on `0 broken rules`:

| record | in use, `stock` | free, `stock` | in use, `fix` | free, `fix` |
|---|---|---|---|---|
| 1 | 352 | 32 | 352 | 32 |
| 2 | 176 | 208 | 168 | 216 |
| 3 | 160 | 224 | 152 | 232 |
| 4 | 224 | 160 | 216 | 168 |
| 5 | 152 | 232 | 152 | 232 |
| 6, after the crash | 568 | 40 | 568 | 40 |

### The scatter: the holder pools, across scene switches

The same install, `stock` and `fix`, by [`run-scatter-holders.py`](automation/run-scatter-holders.py) with
`scenes`. One session each: `reference-mune.sfs` loaded from the Space Center, back to the Space Center, then
`reference-kerbin.sfs`, with *Record the holder pools* pressed in each of the three scenes.

| session | records | what the script printed | what it recorded |
|---|---|---|---|
| `stock` | [`scenes-stock-holders.log`](non-regression/stock/the-scatter-holders/scenes-stock-holders.log) | [`scenes-stock-script.txt`](non-regression/stock/the-scatter-holders/scenes-stock-script.txt) | [`scenes-stock-lines.json`](non-regression/stock/the-scatter-holders/scenes-stock-lines.json) |
| `fix` | [`scenes-fix-holders.log`](non-regression/stock/the-scatter-holders/scenes-fix-holders.log) | [`scenes-fix-script.txt`](non-regression/stock/the-scatter-holders/scenes-fix-script.txt) | [`scenes-fix-lines.json`](non-regression/stock/the-scatter-holders/scenes-fix-lines.json) |

With this mod, it wrote to `KSP.log` that it had acted on each body before its first record:

```
[TerrainPrecisionFix] Kerbin: terrain placed in double precision (first quad corrected by 11.32 mm)
[TerrainPrecisionFix] Kerbin: scatter drawn from its terrain quads (first holder was +19.08 mm off)
[TerrainPrecisionFix] Mun: terrain placed in double precision (first quad corrected by 8.57 mm)
[TerrainPrecisionFix] Mun: scatter drawn from its terrain quads (first holder was +7.86 mm off)
```

Every record of both sessions ends on `0 in no pool` and `0 broken rules`, with the same counts:

| record | scene | pools | holders in use | free |
|---|---|---|---|---|
| 1 | the Mun | the Mun's `Rock00` | 128 | 32 |
| 2 | the Space Center | Kerbin's `Tree00`, `Grass00`, `boulder`, `Pine00`, `cactus` | 3 | 317 |
| 3 | Kerbin | the same five | 118 | 202 |

### The scatter: the colliders

A different install, because stock scatter has no collider: the one of
[the objects](#the-scatter-the-objects-over-twelve-loads), plus
[Kopernicus](https://github.com/Kopernicus/Kopernicus) 1.12.1-247, ModularFlightIntegrator 1.2.10 and
KSPTextureLoader 1.0.36, which it needs, and the
[Stock Scatter Collider Enabler Patch](https://github.com/Poodmund/Stock-Scatter-Collider-Enabler-Patch)
1.0.1, which gives every stock object of scatter a collision mesh of its own shape. Three series, `stock`,
`fix-no-scatter` and `fix`, by [`run-scatter-loading.py`](automation/run-scatter-loading.py):
`ref-kerbin-scatter-collider-eva.sfs` loaded six times in one session each, each load with a record and a
picture of the kerbal's feet, the camera set to the same viewpoint before each (`--camera 0.75 75.63 -6.42
60`).

| load | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `stock` | [`1`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.log) | [`2`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.log) | [`3`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.log) | [`4`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.log) | [`5`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.log) | [`6`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.log) |
| its pictures | [`1`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.png) | [`2`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.png) | [`3`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.png) | [`4`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.png) | [`5`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.png) | [`6`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.png) |
| `fix-no-scatter` | [`1`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load1.log) | [`2`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load2.log) | [`3`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load3.log) | [`4`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load4.log) | [`5`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load5.log) | [`6`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load6.log) |
| its pictures | [`1`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load1.png) | [`2`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load2.png) | [`3`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load3.png) | [`4`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load4.png) | [`5`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load5.png) | [`6`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load6.png) |
| `fix` | [`1`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load1.log) | [`2`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load2.log) | [`3`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load3.log) | [`4`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load4.log) | [`5`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load5.log) | [`6`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load6.log) |
| its pictures | [`1`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load1.png) | [`2`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load2.png) | [`3`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load3.png) | [`4`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load4.png) | [`5`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load5.png) | [`6`](../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load6.png) |

| series | what the script printed | what it recorded |
|---|---|---|
| `stock` | [`collider-stock-script.txt`](non-regression/kopernicus/scatter-with-colliders/collider-stock-script.txt) | [`collider-stock-lines.json`](non-regression/kopernicus/scatter-with-colliders/collider-stock-lines.json) |
| `fix-no-scatter` | [`collider-fix-no-scatter-script.txt`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-script.txt) | [`collider-fix-no-scatter-lines.json`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-lines.json) |
| `fix` | [`collider-fix-script.txt`](non-regression/kopernicus/scatter-with-colliders/collider-fix-script.txt) | [`collider-fix-lines.json`](non-regression/kopernicus/scatter-with-colliders/collider-fix-lines.json) |

Every record of the three series ends on the same line, but for its number:

```
End of record 2: 173 quads with rocks, 306 holders (0 not built yet); nearest quad 'Kerbin Xn0131000203': 6 rocks, 60 vertices measured, 0 without ground under them, 6 colliders measured
```

The same nearest quad throughout, carrying the same six objects with a collider — one `boulder` and five
`cactus` — so they compare one by one from one load to the next, and from one series to another.

## With Parallax

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) with its stock textures and what it
requires, Deferred, and this mod at `logLevel = Debug`, or not: each session is here twice,
`-without-this-mod` and `-fix`. Read in
[the non-regression tests on Parallax](../../docs/scatter/README.md#parallax).

On Parallax Continued 1.0.5, with both instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer):

- [`capsule-on-a-rock-mun.sfs`](non-regression/parallax/a-craft-on-one-of-its-rocks/capsule-on-a-rock-mun.sfs) — a Mk1
  capsule on an empty FL-T100 fuel tank, landed on top of a rock of the Mun. Loaded twelve times by
  `run-loading.py` with an hour of time warp before each load, then the same in a KSP started again:
  `rock-session1-*` and `rock-session2-*` in
  [`a-craft-on-one-of-its-rocks/`](non-regression/parallax/a-craft-on-one-of-its-rocks/), each with its `KSP.log`
  (`.log.gz`), what the script printed (`-script.txt`) and every line it recorded (`-lines.json`); the
  screenshots of the tables in
  [`imgs/scatter/non-regression/parallax/a-craft-on-one-of-its-rocks/`](../../imgs/scatter/non-regression/parallax/a-craft-on-one-of-its-rocks).

On Parallax Continued 1.0.4 rebuilt with the first commit of our change, since merged as
[pull request #157](https://github.com/Gameslinx/Parallax-Continued/pull/157) and released in 1.0.5, with
[KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders) and
[KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin):

- [`rocks-eve-jeb.sfs`](non-regression/parallax/its-scatter-grows-the-same-at-every-load/rocks-eve-jeb.sfs) —
  Jebediah Kerman on EVA on the ground of Eve, among rocks and plants.
- [`the-same-objects/`](non-regression/parallax/its-scatter-grows-the-same-at-every-load/the-same-objects/) — that
  save loaded again at once, twelve times, without this mod (`without-this-mod/`) and with it
  (`with-this-mod/`): the line of KSP Diag - Floating Origin at each load (`readings.json`), the output
  of the script and the `KSP.log` of the session.
