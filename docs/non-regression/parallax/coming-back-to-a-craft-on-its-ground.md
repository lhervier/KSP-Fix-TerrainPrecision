# Parallax: coming back to a craft on its ground

Part of [Terrain Precision Fix](../../../README.md), one test of [Non-regression tests](../../non-regression.md), on [Parallax](../parallax.md).

**Status: checked on Kerbin — with Parallax installed, a craft left parked comes back as it does without
Parallax.** Over six round trips of a rover in the tundra of Kerbin, the parked capsule came back within
31 mm without this mod, and within 0.12 mm with it.

## Where to drive

The rover drives 2.6 km away in a straight line, and back. On the ground of Parallax, that line has to stay
clear of every object of its scatter with a collider: a rock or a tree on the way stops the rover. On
Kerbin, the oaks of Parallax grow from 52 m up in the grasslands, the highlands, the shores and the
mountains, its pines from 140 m, its palms on the shores and its cacti in the deserts and the badlands
(`Parallax_StockScatterTextures/Configs/Kerbin.cfg`); none of those grows in the tundra. The pines that
stand there are of the stock scatter, which has no collider: a rover driven into one goes through it. The
grass west of the KSC, where [the approach protocol](../../checking-the-culprit-approach/the-protocol.md)
parks its craft, lies at about 65 m, where the oaks of Parallax can grow.

## The test

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) 1.0.5 with its stock textures and what
it requires, Deferred, both instruments,
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) and
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), and
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which plays the protocol; this mod with its
defaults (at `logLevel = Debug`), or not.

**The save**, [`approach-kerbin-tundra.sfs`](../../../diag/non-regression/parallax/coming-back-to-a-craft-on-its-ground/approach-kerbin-tundra.sfs),
made without this mod: the two craft of the approach protocol, in the tundra of Kerbin at 72° north, around
midday. The craft the readings are about, a Mk1 command pod on an FL-T100 tank, is landed at latitude
72.0008°, longitude 29.9958°, and is the target of the rover, landed 26 m to its south-east, facing
south-east, the way it drives off.

![The rover at its starting spot in the tundra of Kerbin, the parked capsule to its left, 26 m away](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/the-save.jpg)

*The save, seen from behind the rover, the way it drives off.*

**The protocol**: [the approach protocol](../../checking-the-culprit-approach/the-protocol.md), played by its
script, [`run-approach.py`](../../../diag/automation/run-approach.py), the rover driving off south-east
(`--heading 135`): six round trips, five records per trip in both instruments, without this mod, then with
it.

## Six round trips

**Without this mod**, the ground under the parked capsule comes back at another height each time the
capsule is loaded again, and the capsule with it, as without Parallax: back beside it, *Moved* from −13.2
to +25.7 mm.

**With this mod**, the ground and the capsule come back to the same place: back beside it, *Moved* from
−0.075 to +0.058 mm.

Read off the screenshots below:

| | without this mod | with this mod |
|---|---|---|
| *Moved* back beside the capsule, trips 1 to 6 (KSP Diag - Landed Vessel) | −9.313, −13.234, +6.669, −12.164, +25.668, +5.405 mm | −0.058, +0.041, +0.041, +0.058, −0.075, −0.041 mm |
| *Settled*, spread over the 30 records (KSP Diag - Landed Vessel) | 31.139 mm | 0.115 mm |
| *Ground under craft*, spread over the 30 records (KSP Diag - Terrain Height) | 31.171 mm | 0.059 mm |

At the first record of all, as the scene opens, the capsule settles once on the ground of the session:
*Moved* +40.867 mm without this mod, +0.911 mm with it.

<details>
<summary>The tables without this mod, trip by trip</summary>

![Without this mod, trip 1, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip1-landed-vessel-without-this-mod.jpg)
![Without this mod, trip 1, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip1-terrain-height-without-this-mod.jpg)
![Without this mod, trip 2, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip2-landed-vessel-without-this-mod.jpg)
![Without this mod, trip 2, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip2-terrain-height-without-this-mod.jpg)
![Without this mod, trip 3, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip3-landed-vessel-without-this-mod.jpg)
![Without this mod, trip 3, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip3-terrain-height-without-this-mod.jpg)
![Without this mod, trip 4, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip4-landed-vessel-without-this-mod.jpg)
![Without this mod, trip 4, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip4-terrain-height-without-this-mod.jpg)
![Without this mod, trip 5, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip5-landed-vessel-without-this-mod.jpg)
![Without this mod, trip 5, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip5-terrain-height-without-this-mod.jpg)
![Without this mod, trip 6, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip6-landed-vessel-without-this-mod.jpg)
![Without this mod, trip 6, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip6-terrain-height-without-this-mod.jpg)

</details>

<details>
<summary>The tables with this mod, trip by trip</summary>

![With this mod, trip 1, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip1-landed-vessel-fix.jpg)
![With this mod, trip 1, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip1-terrain-height-fix.jpg)
![With this mod, trip 2, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip2-landed-vessel-fix.jpg)
![With this mod, trip 2, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip2-terrain-height-fix.jpg)
![With this mod, trip 3, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip3-landed-vessel-fix.jpg)
![With this mod, trip 3, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip3-terrain-height-fix.jpg)
![With this mod, trip 4, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip4-landed-vessel-fix.jpg)
![With this mod, trip 4, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip4-terrain-height-fix.jpg)
![With this mod, trip 5, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip5-landed-vessel-fix.jpg)
![With this mod, trip 5, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip5-terrain-height-fix.jpg)
![With this mod, trip 6, the parked capsule](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip6-landed-vessel-fix.jpg)
![With this mod, trip 6, the ground under it](../../../imgs/non-regression/parallax/coming-back-to-a-craft-on-its-ground/trip6-terrain-height-fix.jpg)

</details>

The logs, what the script printed and every line it recorded are in
[`diag`](../../../diag/README.md#with-parallax).
