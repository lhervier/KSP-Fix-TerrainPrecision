# Checking the scatter: in flight

Part of [Terrain Precision Fix](../../README.md), one page of
[Checking the culprit: in flight](../checking-the-culprit-flight.md): the measurements that check the third
culprit, [the scatter](../the-culprit-scatter.md), along a flight over the Mun, on stock and with this mod.

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) measures the terrain scatter against
the ground: for every quad carrying scatter, the height of its holders and of the matrices they are drawn
with, and for the objects of the quad nearest to the craft, the height of their vertices above the ground.
After a load, it is read in
[Checking the scatter: loading the same save](../checking-the-culprit-loading/the-scatter.md).
In flight, the world origin follows the craft, and the terrain keeps building quads ahead of it and
destroying those behind it: [the scatter fix](../the-fix-scatter.md) leaves each holder to follow its quad
through all of that, without doing anything more.

This fix is built on top of [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes),
the base most players run, so every campaign on this page is run in an install that has it: KSP 1.12.5
with Harmony, ModuleManager, KSP Community Fixes 1.41.1, the instrument, and
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which plays the protocol. Two configurations: *on stock*, that install without this mod, and *with this mod*, as installed, its
scatter fix on.

The instrument reads the scatter along a flight, following
[The protocol: the scatter, along a flight](the-scatter-protocol.md), played by its script,
[`run-scatter-flight.py`](../../diag/automation/run-scatter-flight.py):
the save [`ref-mune-5km.sfs`](../../diag/checking-the-culprit-flight/scatter/ref-mune-5km.sfs),
a Mk1 command pod in a circular equatorial orbit 5 km over the Mun, loaded once, one record 30 s into the
flight, then every two minutes, and one after the pod crashed into the relief, about 620 s into the flight.
The records are in
[`mun-5km-stock-rocks.log`](../../diag/checking-the-culprit-flight/scatter/mun-5km-stock-rocks.log) and
[`mun-5km-fix-rocks.log`](../../diag/checking-the-culprit-flight/scatter/mun-5km-fix-rocks.log),
six each, with what the script printed beside them
([`diag`](../../diag/README.md#the-scatter-the-objects-over-a-flight)). On stock, the record after the
crash was taken by hand: the script did not see the crash, the game keeping the wrecked pod as the craft
flown.

## The readings

Flown the same way, both flights passed over the same ground, and their records name the same quads, or
quads next to each other where the two clocks were a second apart. The pod is 5 km up, so every quad is at
least that far from the world origin, where single precision coordinates step by about half a millimetre.

| record | quads with scatter, on stock | *up* of the holders' matrices, on stock | largest *across*, on stock | largest gap between a holder's centre and its quad's, on stock | *up*, *across* and gap, with this mod |
|---|---|---|---|---|---|
| 1, 30 s | 352 | −8.0 to +20.3 mm | 21.5 mm | 9.7 mm | 0.000 mm, 352 holders |
| 2, 150 s | 176 | −6.9 to +21.9 mm | 11.0 mm | 9.7 mm | 0.000 mm, 176 holders |
| 3, 270 s | 160 | −13.3 to +1.0 mm | 3.3 mm | 13.3 mm | 0.000 mm, 152 holders |
| 4, 390 s | 224 | −2.4 to +11.7 mm | 4.1 mm | 11.7 mm | 0.000 mm, 216 holders |
| 5, 510 s | 152 | −15.0 to +1.9 mm | 13.8 mm | 11.3 mm | 0.000 mm, 152 holders |
| 6, after the crash | 568 | −14.1 to +13.4 mm | 24.7 mm | 14.1 mm | 0.000 mm, 568 holders |

The matrices of the quads stand on their centres, *up* and *across* 0.000 mm, in every record of both
flights.

**On stock**, the holders are not drawn on their quads, at any record: over the 1,632 holders of the
flight, the *up* of their matrices runs from −15.0 to +21.9 mm, 7.3 mm on average (root mean square), and
only 5 of them stand at 0. Unlike after a load, where each holder's centre stands on its quad's centre to
the micrometre, here the centres themselves stand apart by up to 14 mm: as the pod flies, stock places the
quads again, and leaves their holders where they were first placed.

**With this mod**, at every record, every holder, 1,616 in all, stands at the height of its
quad's centre, to the micrometre, and its matrix too, neither shifted from it, up or across: 0.000 mm.
Those built minutes into the flight and those still there after the crash alike.

## What the measurements say

**Along a flight, stock draws the scatter off its quads, and this mod draws it on them.** On stock,
no holder is drawn on its quad, by up to 21.9 mm over the Mun, and the gap is there from the first record
to the last. With this mod, every holder of the flight is drawn exactly on its quad, those built
minutes into the flight and those left after the crash alike: along a flight, the scatter is drawn on its
quads just as after a load.
