# BurstPQS: the scatter

Part of [Terrain Precision Fix](../../../../README.md), [the scatter](../../README.md#limits-and-solutions): one limit, on BurstPQS.

**Status: checked, a problem this mod fixes, the scatter fix on by default.** BurstPQS lets stock spawn the scatter,
and stock still places each scatter holder through the sphere, rounded at planet scale. The ground no longer
moves; the holders do, and the rocks, grass and trees move against the ground. This mod's scatter fix first
missed most of them with BurstPQS; it now hangs them all. Read by KSP Diag - Scatter, in millimetres.

[The scatter, at every load](../../checking/loading-protocol.md), twelve loads: how
much the height of each measured vertex above the ground changes from one load to the next, median over the
vertices:

| | stock (published) | this mod, scatter fix off (published) | this mod (published) | BurstPQS | BurstPQS + this mod, before its BurstPQS support | BurstPQS + this mod |
|---|---|---|---|---|---|---|
| Kerbin | 61 | 178 | 0.034 | 141 | 137 | **0.065** |
| Mun | 31 | 23 | 0.008 | 18 | 20 | **0.013** |
| Kerbin, rocks with colliders (Kopernicus, Stock Scatter Collider Enabler Patch) | 61 | 150 | 0.018 | 111 | 122 | **0.023** |

[The scatter, while the world moves](../../checking/driving-protocol.md), six loads,
one move each: the ground holds, and with BurstPQS alone every holder jumps against it, the measured vertices
by −17.0 to +27.9. With this mod before its BurstPQS support, by −23.3 to +21.9; with it now, by −0.18 to
+0.23, every holder at 0.00 from its quad. [In flight](../../checking/flight-protocol.md),
from a 5 km orbit of the Mun: with BurstPQS alone, the holders are up to 26 mm off their quads all flight
long; with this mod before its BurstPQS support, 204 holders out of 1 152 were off at 30 s, none from 150 s
on; with it now, none at any reading, from 30 s on.

**Why this mod's scatter fix first missed them**: it hung a holder from its quad only when the quad sat in
the storage of the highest subdivision level as the holder was set up. Stock keeps those quads there in any
frame of the world; BurstPQS puts them there only once the world turns with the body. As a scene opens the
world does not turn yet, the quads around the craft are built outside that storage, and their holders were
left where stock puts them. **What it does now**: on a body BurstPQS builds, it hangs a holder from its quad
whatever the quad hangs from. BurstPQS builds the mesh of a quad against the quad's own transform wherever
the quad hangs, so a holder drawn with that transform is drawn with the ground, and follows the quad when
BurstPQS moves it into the storage.

With colliders on the scatter, the rocks around the craft of that save, the boulder the kerbal stands on
among them, come back at the same height against the ground at every load, six of them measured with their
collider at each of the six loads.
