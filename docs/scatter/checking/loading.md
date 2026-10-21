# Checking the scatter: loading the same save

Part of [Terrain Precision Fix](../../../README.md), [the scatter](../README.md#checked): the measurements that check [its culprit](../the-culprit.md), around a craft handed back by a save, on stock,
with this mod as installed, and with its scatter fix turned off.

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) measures the terrain scatter against
the ground. Its page carries its method; the protocol is
[The protocol: the scatter, load after load](loading-protocol.md).
For every quad carrying scatter around a landed craft, it reads the height of the quad, of each of its
holders, and of the matrices they are drawn with; for every object of the quad nearest to the craft, the
height above the ground right under them of up to 10 of its vertices, spread over the whole object.
Scatter is sunk into the ground on purpose, so that last height says little by itself: what matters is
whether it comes back the same at every load.

**→ Full chapter: [The protocol: the scatter, load after load](loading-protocol.md)**

This fix is built on top of [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes),
the base most players run, so every campaign on this page is run in an install that has it: KSP 1.12.5
with Harmony, ModuleManager, KSP Community Fixes 1.41.1, the instrument, and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which plays the protocol. Three configurations:
*on stock*, that install without this mod; *scatter fix off*, with this mod and `fixScatter = false`, its
terrain fix alone; *with this mod*, as installed, its scatter fix on ([The fix: the
scatter](../the-fix.md)).

Each save is loaded twelve times per configuration, in a single session of KSP, by the script of the
protocol, [`run-scatter-loading.py`](../../../diag/scatter/automation/run-scatter-loading.py), which records once all
the holders are built and the counts have settled. The records, one file per load, are listed in
[`diag`](../../../diag/scatter/README.md#the-scatter-the-objects-over-twelve-loads), with what the script printed:

- a Mk1 command pod landed on Kerbin, about 8 km north-west of the KSC, where the scatter is grass and
  trees: every record holds the same 64 quads and 118 holders, all of them built, and names the same
  nearest quad, `Kerbin Zn3010000130`, with the same 218 objects, 200 `Grass00` and 18 `Tree00`, and 1,780
  measured vertices;
- a Mk1 command pod landed on the Mun, where the scatter is rocks: 128 quads and 128 holders, and the same
  nearest quad, `Mun Zp211333000`, with 20 `Rock00` and 200 measured vertices.

The *range* of a reading is its largest value minus its smallest over the twelve loads. The *shape* of an
object is the height of each of its vertices minus the height of its first vertex in the log, the lowest of
its model.

## The objects, over twelve loads

**Kerbin**

| | on stock | scatter fix off | with this mod |
|---|---|---|---|
| centre of the nearest quad, range | 133.7 mm | 0.001 mm | 0.002 mm |
| matrix of each quad against its centre | *up* and *across* 0.000 mm everywhere | the same | the same |
| centre of each holder against its quad's | the same height, to the micrometre | range 168 mm (median over the holders), from 129 to 231 mm | the same height, to the micrometre |
| *up* of the holders' matrices | −60 to +61 mm, 0.000 mm 39% of the time | −80 to +148 mm, never 0 | 0.000 mm everywhere, and *across* as well |
| each vertex above the ground, range | **61 mm** (median over the vertices), from 48 to 122 mm | **178 mm** (median), from 176 to 182 mm | **0.034 mm** (median), 0.132 mm at most |
| the same minus its holder's *up*, range | 4.8 mm (median), but over 10 mm for 77 objects, up to 92 mm | 2.1 mm (median), 8.0 mm at most | 0.034 mm (median), 0.132 mm at most |
| shape of each object, range | 0.014 mm (median over the vertices), 0.064 mm at most | 0.013 mm (median), 0.064 mm at most | 0.014 mm (median), 0.065 mm at most |

**The Mun**

| | on stock | scatter fix off | with this mod |
|---|---|---|---|
| centre of the nearest quad, range | 29.3 mm | 0.002 mm | 0.002 mm |
| matrix of each quad against its centre | *up* and *across* 0.000 mm everywhere | the same | the same |
| centre of each holder against its quad's | the same height, to the micrometre | range 25 mm (median over the holders), from 14 to 39 mm | the same height, to the micrometre |
| *up* of the holders' matrices | within 0.1 mm of 0 three times out of four, otherwise ±15.3 mm | −27 to +32 mm, never 0 | 0.000 mm everywhere, and *across* as well |
| each vertex above the ground, range | **31 mm** (median over the vertices), from 21 to 39 mm | **23 mm** (median), from 22 to 23 mm | **0.008 mm** (median), 0.039 mm at most |
| the same minus its holder's *up*, range | 2.3 mm (median), but over 10 mm for 3 rocks out of 20, up to 19.2 mm | 0.15 mm (median), 0.53 mm at most | 0.008 mm (median), 0.039 mm at most |
| shape of each object, range | 0.003 mm (median over the vertices), 0.013 mm at most | 0.003 mm (median), 0.012 mm at most | 0.002 mm (median), 0.013 mm at most |

**No object changes shape from one load to the next**, in any configuration. Within an object, the
heights of its vertices against each other come back the same at every load to within 0.065 mm, trees 20 m
tall included, while the whole object moves by centimetres: none of them comes back leaning another way,
sunk deeper at one end or stretched.

**On stock**, the holders stand where their quads are, but are not drawn there, and most of what moves
the objects against the ground is that gap. Not all of it: once their holder's offset is taken off, 77
objects out of 218 keep more than 10 mm on Kerbin, up to 92 mm, and 3 rocks out of 20 on the Mun, up to
19.2 mm. In stock the ground itself moves against the centre of its quad from one load to the next, by
77 mm under half of the vertices on Kerbin and 27 mm on the Mun: that is the first culprit, which the
terrain fix corrects.

**With the scatter fix off**, the quads stop moving, and the ground under each vertex moves by 8.0 mm at
most against
its quad on Kerbin, 0.5 mm on the Mun. The holders do not follow the quads: their centres no longer stand
on their quads', the offset of their matrices is never 0, and once it is taken off, no vertex moves by more
than 8.0 mm on Kerbin, 0.53 mm on the Mun. The ground is fixed, the holders are not, and now all of what
moves the objects is the holders.

**With this mod**, on all 118 holders of Kerbin and 128 of the Mun, at every one of the twelve
loads, the centre of the holder and the matrix it is drawn with stand at the height of its quad's centre,
to the micrometre, and neither is shifted from it, up or across. Every measured vertex of the nearest quad
comes back at the same height against the ground at every load: within 0.034 mm for half of them on Kerbin,
0.132 mm at most, and within 0.008 mm on the Mun. A vertex's height above the ground with the scatter fix
off, minus its
holder's *up*, is where that vertex would stand without the holder's offset: averaged over the twelve
loads, vertex by vertex, it agrees with the height measured with this mod to 0.53 mm (median),
1.9 mm at most, on Kerbin, and to 0.06 mm (median), 0.21 mm at most, on the Mun.

**How much the objects move is a draw.** The *up* of a holder changes at every load, and the range of a
dozen draws can come out small or large: split in two halves of six loads, the Kerbin series with the
scatter fix off gives 106 mm for one half and 171 mm for the other. Over all the holders and all the loads,
the *up* of
their matrices is 19 mm on average (root mean square) on stock and 61 mm with the scatter fix off on Kerbin,
5.7 mm and
9.7 mm on the Mun.

**How deep the scatter is sunk.** Stock scatter is sunk into the ground on purpose: on the nearest quad,
the lowest vertex of each object's model sits between 20 and 38 cm below the ground on average on Kerbin,
and about 2 m on the Mun, depending on the load; 316.8 mm and 1,979.8 mm at every load with this mod. What a
shift of a few centimetres changes in play, with and without a mod that gives the scatter
colliders, is in [On by default: when to turn it off](../the-fix.md#on-by-default-when-to-turn-it-off)

## What the measurements say

**The scatter is drawn off its quad; the terrain fix alone widens that on Kerbin, and this mod closes it.** On
stock, the holders of the scatter stand on their quads but are not drawn there, and the objects come back
61 mm apart against the ground for half of their vertices on Kerbin; with the scatter fix off, the ground no
longer moves
but the holders do, and that range grows to 178 mm — a limit of the terrain fix,
[The scatter](../limits/stock/the-scatter.md). With this mod as installed, every holder is drawn exactly on its quad, and no vertex moves by more than 0.132 mm: reload the same save as many times as you
like, and the scatter comes back at the same place, on ground that is in the same place.
