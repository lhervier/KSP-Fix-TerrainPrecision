# Checking the culprit: loading the same save

Part of [Terrain Precision Fix](../README.md): the measurements that check the three culprits on a craft
handed back by a save, on stock and with this mod, one page each:
[the ground](checking-the-culprit-loading/the-ground.md), on bare ground;
[the statics](checking-the-culprit-loading/the-statics.md), on a runway with the ground beside it; and
[the scatter](checking-the-culprit-loading/the-scatter.md), among the rocks, the grass and the trees.

This fix is built on top of [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes),
the base most players run, so every campaign of these pages is run in an install that has it: KSP 1.12.5
with Harmony, ModuleManager, KSP Community Fixes 1.41.1, and — for the ground and the statics —
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel), which measures the craft,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), which measures the
ground, and [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which plays the protocols — and
this mod, or not. *On stock* means that install without this mod. Every series is played by the script
of its protocol, once without this mod and once with it, both instruments recording at the same moments.
The saves, the scripts, and the sessions both ways are in [`diag`](../diag/README.md#the-loading-protocol).
The scatter has an instrument of its own, described in its page.

## The ground

A craft set down on bare ground, saved once, and that same save loaded six times, on the four stock
worlds and on the Moon and Earth of [Real Solar System](https://github.com/KSP-RO/RealSolarSystem)
([the loading protocol](checking-the-culprit-loading/the-protocol.md)). The craft comes to rest over
43.7 mm on Kerbin and 292.4 mm on Earth, and within 0.4 mm with this mod; the ground under it comes back
over 43.6 mm and 292.3 mm, and within 0.3 mm with this mod.

**→ Full page: [Checking the ground: loading the same save](checking-the-culprit-loading/the-ground.md)**

## The statics

Two identical craft, one on a runway and one on the ground beside it, the same save loaded six times,
on Kerbin by the runway of the KSC and on the Mun by a runway placed by Kerbal Konstructs
([the runway protocol](checking-the-culprit-loading/the-runway-protocol.md)). The step between the deck
and the ground beside it changes by up to 38.3 mm on Kerbin and 36.1 mm on the Mun; with this mod, the
deck of the KSC comes back within 0.177 mm, and the step within 0.188 mm.

**→ Full page: [Checking the statics: loading the same save](checking-the-culprit-loading/the-statics.md)**

## The scatter

Twelve loads of a save on Kerbin and of one on the Mun, read by
[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) on stock, with this mod as installed, and with its scatter fix turned off. Against the ground, half of the vertices of the scatter come back
61 mm apart on Kerbin on stock, 178 mm with the scatter fix off, and 0.034 mm with this mod.

**→ Full page: [Checking the scatter: loading the same save](checking-the-culprit-loading/the-scatter.md)**

## What the measurements say

**This is also the last proof that the culprit is the right one.** The fix changes where a subtraction
happens, and nothing else about the values placed; were the cause elsewhere, reordering that
subtraction would have left the spread untouched. The same goes for the scatter: the scatter fix changes
the transform a holder hangs from, and nothing about the objects in it, and it removes the holders'
offset and nothing else about where the objects are drawn.
