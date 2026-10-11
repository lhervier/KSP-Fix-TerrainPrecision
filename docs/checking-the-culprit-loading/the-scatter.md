# Checking the scatter: loading the same save

Part of [Terrain Precision Fix](../../README.md), one page of
[Checking the culprit: loading the same save](../checking-the-culprit-loading.md): the measurements that check
the third culprit, [the scatter](../the-culprit-scatter.md), around a craft handed back by a save, on stock,
with the terrain fix alone and with the scatter fix as well.

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) measures the terrain scatter against
the ground. Its page carries its method; the protocol is
[The protocol: the scatter, load after load](the-scatter-protocol.md).
For every quad carrying scatter around a landed craft, it reads the height of the quad, of each of its
holders, and of the matrices they are drawn with; for every object of the quad nearest to the craft, the
height above the ground right under them of up to 10 of its vertices, spread over the whole object.
Scatter is sunk into the ground on purpose, so that last height says little by itself: what matters is
whether it comes back the same at every load.

The scatter is measured in three configurations, not two: on stock, with the terrain fix alone — this
mod as installed by default — and with the scatter fix as well, which is off by default
([The fix: the scatter](../the-fix-scatter.md)). **The series with the scatter fix were taken when it was a
mod of its own**, Rock Precision Fix 0.1.0, installed next to Terrain Precision Fix 0.1.0: the same two
patches as this mod's scatter fix, which writes the same messages to `KSP.log`. In the logs of these
series, they are tagged `[RockPrecisionFix]` instead of `[TerrainPrecisionFix]`.

Every series uses [the two saves of the protocol](the-scatter-protocol.md#the-saves),
each loaded twelve times, in KSP 1.12.5 with Harmony, ModuleManager and KSP Community Fixes 1.41.1:

- a Mk1 command pod landed on Kerbin, about 8 km north-west of the KSC, where the scatter is grass and
  trees: every record holds the same 64 quads and 118 holders, all of them built, and names the same
  nearest quad, `Kerbin Zn3010000130`, with the same 218 objects, 200 `Grass00` and 18 `Tree00`, and 1,780
  measured vertices;
- a Mk1 command pod landed on the Mun, where the scatter is rocks: 128 quads and 128 holders, and the same
  nearest quad, `Mun Zp211333000`, with 20 `Rock00` and 200 measured vertices.

The *range* of a reading is its largest value minus its smallest over the twelve loads.

## On stock and with the terrain fix alone

Each series is one save loaded twelve times, on stock, then with the terrain fix alone. The records, one
file per load, each holding the last record taken after that load, are in
[`diag`](../../diag/README.md#the-scatter-the-rocks-over-twelve-loads). Below, the *shape* of an object is
the height of each of its vertices minus the height of its first vertex in the log, the lowest of its
model.

**Kerbin**

| | stock | with the terrain fix alone |
|---|---|---|
| centre of the nearest quad, range | 131 mm | 0.002 mm |
| matrix of each quad against its centre | *up* and *across* 0.000 mm everywhere | the same |
| centre of each holder against its quad's | the same height, to the micrometre | range 148 mm (median over the holders), from 88 to 227 mm |
| *up* of the holders' matrices | −92 to +92 mm, 0.000 mm 28% of the time | −107 to +110 mm, never 0 |
| each vertex above the ground, range | 94 mm (median over the vertices), from 66 to 167 mm | 130 mm (median), from 127 to 134 mm |
| the same minus its holder's *up*, range | 5.3 mm (median), but over 10 mm for 80 objects, up to 119 mm | 1.7 mm (median), 6.6 mm at most |
| shape of each object, range | 0.015 mm (median over the vertices), 0.066 mm at most | 0.015 mm (median), 0.063 mm at most |

**The Mun**

| | stock | with the terrain fix alone |
|---|---|---|
| centre of the nearest quad, range | 33 mm | 0.005 mm |
| matrix of each quad against its centre | *up* and *across* 0.000 mm everywhere | the same |
| centre of each holder against its quad's | the same height, to the micrometre | range 25 mm (median over the holders), from 15 to 42 mm |
| *up* of the holders' matrices | within 0.1 mm of 0 three times out of four, otherwise ±15.2 to ±15.4 mm, nothing in between | −27 to +29 mm, never 0 |
| each vertex above the ground, range | 31 mm (median over the vertices), from 12 to 37 mm | 31 mm (median), from 30 to 32 mm |
| the same minus its holder's *up*, range | 2.2 mm (median), but over 10 mm for 3 rocks out of 20, up to 18.5 mm | 0.55 mm (median), 1.9 mm at most |
| shape of each object, range | 0.002 mm (median over the vertices), 0.011 mm at most | 0.006 mm (median), 0.024 mm at most |

**No object changes shape from one load to the next**, in either series. Within an object, the heights of
its vertices against each other come back the same at every load to within 0.07 mm, trees 20 m tall
included, while the whole object moves by centimetres: none of them comes back leaning another way, sunk
deeper at one end or stretched.

**On stock**, the holders stand where their quads are, but are not drawn there, and most of what moves
the objects against the ground is that gap. Not all of it: once their holder's offset is taken off, 80
objects out of 218 keep more than 10 mm on Kerbin, up to 119 mm, and 3 rocks out of 20 on the Mun, up to
18.5 mm. In stock the ground itself moves against the centre of its quad from one load to the next, by
104 mm under half of the vertices on Kerbin and 27 mm on the Mun: that is the first culprit, which the
terrain fix corrects, and it is why the scatter fix is measured with it.

**With the terrain fix alone**, the quads stop moving, and the ground under each vertex moves by 6.7 mm at
most against its quad on Kerbin, 1.8 mm on the Mun. The holders do not follow the quads: their centres no
longer stand on their quads', the offset of their matrices is never 0, and once it is taken off, no vertex
moves by more than 6.6 mm on Kerbin, 1.9 mm on the Mun. The ground is fixed, the holders are not, and now
all of what moves the objects is the holders.

**How much the objects move is a draw.** The *up* of a holder changes at every load, and the range of a
dozen draws can come out small or large: split in two halves of six loads, the Kerbin series with the
terrain fix alone gives 43 mm for one half and 130 mm for the other. Over all the holders and all the
loads, the *up* of their matrices is 31 mm on average (root mean square) on stock and 40 mm with the
terrain fix alone on Kerbin, 7.5 mm and 9.6 mm on the Mun: the same order of size.

**In play, neither changes much.** Stock scatter has no collider: no craft rests on it and nothing hits
it. And it is sunk into the ground on purpose: on the nearest quad, the lowest vertex of each object's
model sits between 27 and 40 cm below the ground on average on Kerbin, and about 2 m on the Mun, depending
on the load, so a shift of a few centimetres mostly moves the objects within the ground. With colliders on
the scatter, it does matter:
[Kopernicus: scatter with colliders](../non-regression/kopernicus/scatter-with-colliders.md).

## With the scatter fix as well

The same install and the same two saves, with the scatter fix added to
the terrain fix, each save loaded twelve times in a single session of KSP, one record taken after each
load. The install and the 24 records are in
[`diag/runs`](../../diag/README.md#the-scatter-the-rocks-over-twelve-loads).

On Kerbin:

| | with the terrain fix alone | with both fixes |
|---|---|---|
| centre of the nearest quad, range | 0.002 mm | 0.002 mm |
| matrix of each quad against its centre | *up* and *across* 0.000 mm everywhere | the same |
| centre of each holder against its quad's | range 148 mm (median over the holders), up to 227 mm | the same height, to the micrometre |
| *up* of the holders' matrices | −107 to +110 mm, never 0 | 0.000 mm everywhere, and *across* as well |
| each vertex above the ground, range | 130 mm (median over the vertices), from 127 to 134 mm | 0.035 mm (median), 0.125 mm at most |

On the Mun:

| | with the terrain fix alone | with both fixes |
|---|---|---|
| centre of the nearest quad, range | 0.005 mm | 0.004 mm |
| matrix of each quad against its centre | *up* and *across* 0.000 mm everywhere | the same |
| centre of each holder against its quad's | range 25 mm (median over the holders), up to 42 mm | the same height, to the micrometre |
| *up* of the holders' matrices | −27 to +29 mm, never 0 | 0.000 mm everywhere, and *across* as well |
| each vertex above the ground, range | 31 mm (median over the vertices), from 30 to 32 mm | 0.012 mm (median), 0.042 mm at most |

On all 118 holders of Kerbin and 128 of the Mun, at every one of the twelve loads, the centre of the
holder and the matrix it is drawn with stand at the height of its quad's centre, to the micrometre, and
neither is shifted from it, up or across. Every measured vertex of the nearest quad comes back at the same
height against the ground at every load: within 0.035 mm for half of them on Kerbin, 0.125 mm at most, and
within 0.042 mm on the Mun. On average, the lowest vertex of each object's model stands 316.8 mm below the
ground on Kerbin and 1,979.8 mm on the Mun, the same at each of the twelve loads.

In the records taken with the terrain fix alone, a vertex's height above the ground minus its holder's
*up* is where that vertex would stand without the holder's offset. Averaged over the twelve loads of each
series, vertex by vertex, that height and the one measured with both fixes agree to 0.018 mm (median),
1.2 mm at most, on Kerbin, and to 0.080 mm (median), 0.30 mm at most, on the Mun.

## What the measurements say

**The scatter is drawn off its quad, and the terrain fix alone widens that on Kerbin.** On stock, the
holders of the scatter stand on their quads but are not drawn there, and the objects come back 94 mm
apart against the ground for half of their vertices on Kerbin; with the terrain fix alone, the ground no
longer moves but the holders do, and that range grows to 130 mm — the limit
[Rocks, grass and trees](../limits-and-solutions/stock/rocks-grass-and-trees.md). With the scatter fix as
well, every holder is drawn exactly on its quad, and no vertex moves by more than 0.125 mm: reload the same
save as many times as you like, and the scatter comes back at the same place, on ground that is in the
same place.
