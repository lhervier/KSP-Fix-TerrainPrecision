# Kopernicus: scatter with colliders

Part of [Terrain Precision Fix](../../../../README.md), [the scatter](../../README.md#non-regression-tests): one non-regression test, on Kopernicus.

**Status: checked, no problem — the terrain fix alone narrows a stock gap a little, and does not close
it; the scatter fix of this mod, on by default, closes it.** Stock scatter has no collider, but Kopernicus can give it one: Kopernicus with the
[Stock Scatter Collider Enabler Patch](https://github.com/Poodmund/Stock-Scatter-Collider-Enabler-Patch),
both on CKAN, do. The offset described in [The culprit: the scatter](../../the-culprit.md) then
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

The save: [`ref-kerbin-scatter-collider-eva.sfs`](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/ref-kerbin-scatter-collider-eva.sfs), a Mk1
command pod landed in a desert of Kerbin (latitude −5.6080°, longitude −143.5447°), with Jebediah out on
EVA, standing on a boulder next to it. Copy it into the folder of a sandbox game and load it from that
game.

1. **Scatter on, and the log written at once**: steps 1 and 2 of
   [the protocol load after load](../../checking/loading-protocol.md#the-protocol).
2. **Install Kopernicus, then that patch.** Note the version of each: they belong with the readings.
   Kopernicus needs ModularFlightIntegrator and KSPTextureLoader: without the second, KSP loads Kopernicus
   without running it (`KSP.log`: *has not met dependency 'KSPTextureLoader'*), and no record measures a
   collider.
3. **Load the save and press *Record the rocks*.** The closing line of the record ends on how many
   colliders were measured: 0 means nothing gave the scatter around the craft a collider.
4. **Take a picture of the kerbal's feet**, from as near the same viewpoint as you can. A kerbal always
   sinks a little into whatever it stands on, so one picture proves nothing: what shows is how much it
   changes from one load to the next. The kerbal stands on the collider, so it sinks into the rock one
   sees, or floats above it; the reading itself does not need it.
5. **Load the same save again, press *Record the rocks* and take the picture again.** Six times in all.

[`run-scatter-loading.py`](../../../../diag/scatter/automation/run-scatter-loading.py), the script of
[the protocol load after load](../../checking/loading-protocol.md#played-by-a-script),
plays it through [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer):
`python run-scatter-loading.py --folder <your sandbox game> --save ref-kerbin-scatter-collider-eva --loads 6
--scene-shots --camera 0.75 75.63 -6.42 60 --out out`. The last option puts the flight camera 0.75 m from the
kerbal, looking at its feet, before each picture, so that the six pictures are taken from the same
viewpoint.

To make your own save: land a craft where there are rocks — on Kerbin, boulders stand in the deserts —
walk a kerbal up a rock with the jetpack, and save there.

## The gap between a rock and its collider

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) measures, object by object, where the
physics engine holds the collider of an object of scatter against where the object is drawn, following
[the protocol](#the-protocol), in KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
Kopernicus 1.12.1-247, ModularFlightIntegrator 1.2.10, KSPTextureLoader 1.0.36, the Stock Scatter Collider
Enabler Patch 1.0.1 and KSP-MCPServer: one save, a kerbal standing on a boulder in a desert of Kerbin,
loaded six times per configuration, one record and one picture of the kerbal's feet per load. Six objects
carry a collider on the quad read, `Kerbin Xn0131000203`: one `boulder` and five `cactus`.

Three configurations: on stock, that install without this mod; *scatter fix off*, this mod with
`fixScatter = false`, its terrain fix alone; and *with this mod*, as installed. The records and the pictures
of the three series are listed below and in [`diag`](../../../../diag/scatter/README.md#the-scatter-the-colliders).

| the collider against the object drawn, over 36 readings | on stock | scatter fix off | with this mod |
|---|---|---|---|
| *up* | −71.3 to +59.9 mm | −58.6 to +54.5 mm | −0.022 to +0.022 mm |
| *up*, root mean square | 36.8 mm | 30.4 mm | 0.012 mm |
| *across*, at most | 63.9 mm | 49.0 mm | 0.065 mm |

Load by load, on stock, then with the scatter fix off; *up* is positive when the collider stands above
the object one sees:

| load | *up* of the six colliders, on stock | largest *across* | *up* of their holder's matrix | *up* of the six colliders, scatter fix off | largest *across* | *up* of their holder's matrix |
|---|---|---|---|---|---|---|
| 1 | −71.3 to +30.3 mm | 57.1 mm | 0.000 mm | −25.9 to +14.3 mm | 49.0 mm | +117.2 mm |
| 2 | −28.1 to +59.9 mm | 39.0 mm | −4.3 mm | −15.5 to +17.5 mm | 23.4 mm | +11.6 mm |
| 3 | −31.9 to +50.8 mm | 24.8 mm | 0.000 mm | −7.2 to +48.4 mm | 35.0 mm | −31.8 mm |
| 4 | −56.4 to +29.6 mm | 62.8 mm | +57.2 mm | −58.6 to +54.5 mm | 22.5 mm | +51.6 mm |
| 5 | −64.1 to +1.7 mm | 49.2 mm | 0.000 mm | −51.6 to +27.8 mm | 31.1 mm | −7.3 mm |
| 6 | +22.8 to +55.3 mm | 63.9 mm | +4.6 mm | −51.9 to +19.0 mm | 34.5 mm | +112.4 mm |

Each object is drawn afresh at every load: over its six loads, each object of the quad covers from 112 to
182 mm on stock, and 149 mm with the scatter fix off, all of them by the same amount; with this mod, none
moves.

The records and the pictures of the kerbal's feet, load by load:

| series | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| on stock | [1](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.png) | [2](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.png) | [3](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.png) | [4](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.png) | [5](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.png) | [6](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.png) |
| scatter fix off | [1](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load1.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load1.png) | [2](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load2.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load2.png) | [3](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load3.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load3.png) | [4](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load4.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load4.png) | [5](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load5.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load5.png) | [6](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load6.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load6.png) |
| with this mod | [1](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load1.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load1.png) | [2](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load2.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load2.png) | [3](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load3.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load3.png) | [4](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load4.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load4.png) | [5](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load5.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load5.png) | [6](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load6.log) · [picture](../../../../imgs/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-load6.png) |

What the script printed, and what it recorded: [`collider-stock-script.txt`](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-script.txt), [`collider-stock-lines.json`](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-stock-lines.json) | [`collider-fix-no-scatter-script.txt`](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-script.txt), [`collider-fix-no-scatter-lines.json`](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-lines.json) | [`collider-fix-script.txt`](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-script.txt), [`collider-fix-lines.json`](../../../../diag/scatter/non-regression/kopernicus/scatter-with-colliders/collider-fix-lines.json).

**With the scatter fix off, the gap is narrowed a little, not closed.** The collider and the object stay
centimetres apart, drawn afresh at every load: the terrain fix leaves the holder hanging from the sphere,
over the 600 km vector the culprit is about.

**The gap does not follow the holder.** In three of the stock loads, the holder of those six objects sits
exactly on its quad, *up* 0.000 mm, and its colliders still stand up to 71 mm from the objects they belong
to. Whatever separates them happens below the holder, where each object carries its own position under it
— which is why hanging the holder from its quad settles it for the objects as well.

**And it is visible.** On the boulder the kerbal stands on, the gap reads +19.2, +59.9, +50.8, −30.8, −47.4
and +55.3 mm over the stock loads: its boots sink into the rock at one load and stand clear of it at the
next. With this mod, the gap stays within 0.022 mm, and the six pictures are interchangeable. They are
illustrations, not measurements: a kerbal sinks a little into whatever it stands on.

## What Kopernicus does with the holders

Read in its source. Kopernicus is the only mod read that uses the holders, and the scatter fix moves them
([Other mods that look for the holders](../../the-fix.md#other-mods-that-look-for-the-holders)).
It reaches them through the scatter (`scatterParent`, which the scatter fix reads at every call, and the
pool), not through the hierarchy, and reaches the objects of a holder through the holder's own children,
which follow it. Its lethal and heat emitting scatter computes world positions from the holder's matrix
and positions in the quad's frame, which the scatter fix makes exact. Its optional scatter colliders end
up below the quad: they are the ones measured above, and the fix brings each of them onto the object it
belongs to. Stock's `GetComponent<PQ>()` still finds no quad on them, which is what the instrument relies
on to tell the ground from a rock when it casts a ray at them.

## Solution

The scatter fix of this mod, on by default (`fixScatter = false` turns it off), and only with the terrain
fix as well: the same series reads −0.022 to +0.022 mm with this mod. The collider and the object are the
same object again, to a hundredth of a millimetre, at every load. Why it is on by default, and when to
turn it off: [On by default: when to turn it off](../../the-fix.md#on-by-default-when-to-turn-it-off)
