# Kopernicus: scatter with colliders

Part of [Terrain Precision Fix](../../../README.md), one test of [Non-regression tests](../../non-regression.md), on [Kopernicus](../../non-regression.md#kopernicus).

**Status: checked, no problem — the terrain fix halves a stock gap, and does not close it; the scatter
fix of this mod, off by default, closes it.** Stock scatter has no collider, but Kopernicus can give it one: Kopernicus with the
[Stock Scatter Collider Enabler Patch](https://github.com/Poodmund/Stock-Scatter-Collider-Enabler-Patch),
both on CKAN, do. The offset described in [The culprit: the scatter](../../the-culprit-scatter.md) then
stops being visual: the physics engine is handed the holder's position, while the pilot sees what is
drawn from the holder's matrix, and those are the two numbers that round differently. The rock a craft
hits is not the rock its pilot sees. Kopernicus replaces the stock scatter holder with its own subclass,
`PQSMod_KopernicusLandClassScatterQuad`, which is the one measured here.

## The protocol

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) needs a mod that gives the scatter
colliders: here the [Stock Scatter Collider Enabler Patch](https://github.com/Poodmund/Stock-Scatter-Collider-Enabler-Patch),
a single config file that asks [Kopernicus](https://github.com/Kopernicus/Kopernicus) to give every stock
object of scatter a collision mesh of its own shape, on most stock bodies. It is on CKAN. Its own version
file says KSP 1.8 to 1.11, but it holds no code, and it works on 1.12.5. What the instrument reads, and
what a record holds, are in
[its page](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md#7-the-collider-of-each-object).

The save: [`ref-kerbin-scatter-collider-eva.sfs`](../../../diag/non-regression/kopernicus/scatter-with-colliders/ref-kerbin-scatter-collider-eva.sfs), a Mk1
command pod landed in a desert of Kerbin (latitude −5.6080°, longitude −143.5447°), with Jebediah out on
EVA, standing on a boulder next to it. Copy it into the folder of a sandbox game and load it from that
game.

1. **Scatter on, and the log written at once**: steps 1 and 2 of
   [the protocol load after load](../../checking-the-culprit-loading/the-scatter-protocol.md#the-protocol).
2. **Install Kopernicus, then that patch.** Note the version of each: they belong with the readings.
3. **Load the save and press *Record the rocks*.** The closing line of the record ends on how many
   colliders were measured: 0 means nothing gave the scatter around the craft a collider.
4. **Take a picture of the kerbal's feet**, from as near the same viewpoint as you can. A kerbal always
   sinks a little into whatever it stands on, so one picture proves nothing: what shows is how much it
   changes from one load to the next. The kerbal stands on the collider, so it sinks into the rock one
   sees, or floats above it; the reading itself does not need it.
5. **Load the same save again, press *Record the rocks* and take the picture again.** Six times in all.

To make your own save: land a craft where there are rocks — on Kerbin, boulders stand in the deserts —
walk a kerbal up a rock with the jetpack, and save there.

## The gap between a rock and its collider

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) measures, object by object, where the
physics engine holds the collider of an object of scatter against where the object is drawn, following
[the protocol](#the-protocol),
in KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, Kopernicus 1.12.1.247 and the Stock
Scatter Collider Enabler Patch 1.0.1: one save, a kerbal standing on a boulder in a desert of Kerbin,
loaded six times per configuration, one record and one picture of the kerbal's feet per load. Six objects
carry a collider on the quad read: one `boulder` and five `cactus`.

Three configurations: on stock, with the terrain fix alone — this mod as installed by default — and with
the scatter fix as well, off by default. **The series with the scatter fix was taken when it was a mod of
its own**, Rock Precision Fix 0.1.0, installed next to Terrain Precision Fix 0.1.0: the same two patches,
whose lines in its logs are tagged `[RockPrecisionFix]`. The records and the pictures of the three
series are listed in [`diag`](../../../diag/README.md#the-scatter-the-colliders).

| the collider against the object drawn, over 36 readings | on stock | with the terrain fix alone | with both fixes |
|---|---|---|---|
| *up* | −68.7 to +104.2 mm | −70.2 to +70.3 mm | −0.026 to +0.022 mm |
| *up*, root mean square | 48.1 mm | 31.6 mm | 0.010 mm |
| *across*, at most | 83.3 mm | 44.5 mm | 0.058 mm |

Load by load, on stock, then with the terrain fix alone; *up* is positive when the collider stands above
the object one sees:

| load | *up* of the six colliders, on stock | largest *across* | *up* of their holder's matrix | *up* of the six colliders, the terrain fix alone | largest *across* | *up* of their holder's matrix |
|---|---|---|---|---|---|---|
| 1 | −59.1 to +15.3 mm | 42.6 mm | +51.2 mm | −36.2 to +0.1 mm | 44.5 mm | +119.9 mm |
| 2 | −68.7 to +2.3 mm | 83.3 mm | −9.4 mm | −55.5 to +37.7 mm | 27.7 mm | +1.1 mm |
| 3 | +39.2 to +104.2 mm | 38.7 mm | +10.1 mm | −3.0 to +70.3 mm | 32.8 mm | +55.6 mm |
| 4 | −2.3 to +73.3 mm | 23.4 mm | 0.000 mm | −4.4 to +32.2 mm | 24.5 mm | +10.9 mm |
| 5 | −50.8 to +5.0 mm | 37.8 mm | +11.2 mm | −70.2 to −33.9 mm | 28.7 mm | +151.7 mm |
| 6 | −2.0 to +87.7 mm | 52.5 mm | −69.3 mm | −48.2 to +44.1 mm | 38.7 mm | +75.1 mm |

Each object is drawn afresh at every load: over its six loads, the boulder alone covers 102 mm on stock
and 72 mm with the terrain fix alone, and the widest cactus 163 mm and 114 mm.

The records and the pictures of the kerbal's feet, load by load:

| series | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| on stock | [1](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.png) | [2](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.png) | [3](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.png) | [4](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.png) | [5](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.png) | [6](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.png) |
| the terrain fix alone | [1](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load1.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load1.png) | [2](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load2.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load2.png) | [3](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load3.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load3.png) | [4](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load4.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load4.png) | [5](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load5.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load5.png) | [6](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load6.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-tpf-load6.png) |
| both fixes | [1](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-both-load1.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-both-load1.png) | [2](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-both-load2.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-both-load2.png) | [3](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-both-load3.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-both-load3.png) | [4](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-both-load4.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-both-load4.png) | [5](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-both-load5.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-both-load5.png) | [6](../../../diag/non-regression/kopernicus/scatter-with-colliders/collider-both-load6.log) · [picture](../../../imgs/non-regression/kopernicus/scatter-with-colliders/collider-both-load6.png) |

**With the terrain fix alone, the gap is halved, not closed.** The collider and the object stay
centimetres apart, drawn afresh at every load: the terrain fix leaves the holder hanging from the sphere,
over the 600 km vector the culprit is about.

**The gap does not follow the holder.** In one of the stock loads, the holder of those six objects sits
exactly on its quad, *up* and *across* 0.000 mm, and its colliders still stand up to 73 mm from the
objects they belong to. Whatever separates them happens below the holder, where each object carries its
own position under it — which is why hanging the holder from its quad settles it for the objects as well.

**And it is visible.** On the boulder the kerbal stands on, the gap reads −4.3, −48.1, +48.2, +10.2, −9.1
and +53.7 mm over the stock loads: its boots sink to the ankles at one load and stand clear of the rock at
the next. With both fixes, the six pictures are interchangeable. They are illustrations, not measurements:
the viewpoint is not exactly the same twice, and a kerbal sinks a little into whatever it stands on.

## What Kopernicus does with the holders

Read in its source. Kopernicus is the only mod read that uses the holders, and the scatter fix moves them
([Other mods that look for the holders](../../the-fix-scatter.md#other-mods-that-look-for-the-holders)).
It reaches them through the scatter (`scatterParent`, which the scatter fix reads at every call, and the
pool), not through the hierarchy, and reaches the objects of a holder through the holder's own children,
which follow it. Its lethal and heat emitting scatter computes world positions from the holder's matrix
and positions in the quad's frame, which the scatter fix makes exact. Its optional scatter colliders end
up below the quad: they are the ones measured above, and the fix brings each of them onto the object it
belongs to. Stock's `GetComponent<PQ>()` still finds no quad on them, which is what the instrument relies
on to tell the ground from a rock when it casts a ray at them.

## Solution

The scatter fix of this mod, off by default (`fixScatter = true` turns it on), and only with the terrain
fix as well: the same series reads −0.026 to +0.022 mm with both. The collider and the object are the
same object again, to a hundredth of a millimetre, at every load. Why it is off by default, and when to
turn it on: [Off by default: should you turn it on?](../../the-fix-scatter.md#off-by-default-should-you-turn-it-on)
