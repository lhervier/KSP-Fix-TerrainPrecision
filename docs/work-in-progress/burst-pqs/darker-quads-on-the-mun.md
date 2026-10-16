# BurstPQS: darker quads on the Mun

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [BurstPQS](../../work-in-progress/burst-pqs.md).

**Status: in progress — seen, not measured, not compared.** Seen in the flight of the scatter protocols
([in flight](../../checking-the-culprit-flight/the-scatter-protocol.md), on `ref-mune-5km`: a capsule in a
circular orbit 5 km above the Mun), with BurstPQS, with and without this mod. Whole quads of the ground are
drawn much darker than their neighbours, with stepped edges that follow the quads, while the craters run on
unbroken from one quad to the next: the relief is right, the shading of whole quads is not. It shows from the
start of the flight, moves (some quads turn normal again while others darken), and fades after four minutes
or so. Not compared yet with the same flight without BurstPQS.

Twelve seconds into the flight, the default camera: most of the Mun in view is dark, with a band of light and
dark blocks along its edge.

![The Mun 12 s into the flight from a 5 km orbit, BurstPQS and this mod](../../../imgs/work-in-progress/burst-pqs/mun-5km-t0m12s.png)

The camera pulled back to about 80 km, at 1 min 51 s, 3 min 08 s and 4 min 30 s:

![The Mun at 1 min 51 s, camera pulled back: whole quads darker, stepped edges](../../../imgs/work-in-progress/burst-pqs/mun-5km-t1m51s-zoomed-out.png)

![The Mun at 3 min 08 s: some quads normal again, others dark](../../../imgs/work-in-progress/burst-pqs/mun-5km-t3m08s-zoomed-out.png)

![The Mun at 4 min 30 s: almost every quad normal](../../../imgs/work-in-progress/burst-pqs/mun-5km-t4m30s-zoomed-out.png)

What it could be, read in BurstPQS's code and not checked: the normals of a quad's edges, worked out again
by BurstPQS; tangents approximated; the renderers switched on and off in batches, two levels drawn over each
other for a frame or two. One more lead, from the timing: the darkest quads are those of the first minute,
built as the scene opens, before the world turns with the body, the same quads whose scatter this mod's scatter
fix misses ([the scatter](the-scatter.md)). A quad whose normals were worked out where it was built, and that
is then moved into the storage of the highest level without them being worked out again, would be lit
wrongly until it is built again.

Seen at the same time, in the same flight with the camera pulled back: the camera could be turned to look at
the south pole of the Mun, but not to look at the north pole, held a few degrees short. Not compared yet
without BurstPQS either; it may be the stock camera.

*To test:* the same flight, `ref-mune-5km`, on KSP with KSP Community Fixes alone, then with BurstPQS, then
with BurstPQS and Kopernicus without BurstPQS's terrain (to tell BurstPQS from Kopernicus), two passes each,
from a fresh KSP: the camera left as it opens, then the camera pulled back to about 80 km as the flight
opens; a screenshot every 5 seconds for 5 minutes in each pass, the same instants in every install. Then,
camera pulled back, turn it towards the north pole and towards the south pole, in each install. Darker quads
only with BurstPQS would make it BurstPQS's; then, which quads (built when, at which level), to show to its
author.
