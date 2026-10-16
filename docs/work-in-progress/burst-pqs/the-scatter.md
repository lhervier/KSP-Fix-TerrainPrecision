# BurstPQS: the scatter

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [BurstPQS](../../work-in-progress/burst-pqs.md).

**Status: in progress — measured.** BurstPQS lets stock spawn the scatter, and stock still places each scatter
holder through the sphere, rounded at planet scale. The ground no longer moves; the holders do, and the rocks,
grass and trees move against the ground. Read by KSP Diag - Scatter, in millimetres.

[The scatter, at every load](../../checking-the-culprit-loading/the-scatter-protocol.md), twelve loads: how
much the height of each measured vertex above the ground changes from one load to the next, median over the
vertices:

| | stock (published) | this mod, scatter fix off (published) | this mod (published) | BurstPQS | BurstPQS + this mod |
|---|---|---|---|---|---|
| Kerbin | 61 | 178 | 0.034 | **141** | **137** |
| Mun | 31 | 23 | 0.008 | **18** | **20** |
| Kerbin, rocks with colliders (Kopernicus, Stock Scatter Collider Enabler Patch) | 61 | 150 | 0.018 | **111** | **122** |

[The scatter, while the world moves](../../checking-the-culprit-driving/the-scatter-protocol.md), six loads,
one move each: the ground holds (the nearest quad within 0.15), and every holder jumps against it, by −8.9 to
+26.1 with BurstPQS, by −22.4 to +19.9 with this mod. [In flight](../../checking-the-culprit-flight/the-scatter-protocol.md),
from a 5 km orbit of the Mun, the holders are up to 26 mm off their quads all flight long with BurstPQS; with
this mod, 204 holders out of 1 152 are off at 30 s, none from 150 s on.

**This mod's scatter fix misses them**: it hangs a holder from its quad only when the quad sits in the
storage of the highest subdivision level as the holder is set up. Stock keeps those quads there in any frame
of the world; BurstPQS puts them there only once the world turns with the body. As a scene opens the world
does not turn yet, the quads around the craft are built outside that storage, and their holders are left
where stock puts them. In flight those quads are soon built again, and their holders hung; on the ground
they are not, hence nothing at a load. With colliders on the scatter, a craft against a rock finds that rock
at a different height at every load.

*To do:* hang the holders of the quads built before the world turns with the body, when BurstPQS moves those
quads into the storage; then play these three protocols again.
