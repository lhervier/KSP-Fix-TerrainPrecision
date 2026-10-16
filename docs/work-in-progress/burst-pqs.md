# Work in progress: BurstPQS

Part of [Terrain Precision Fix](../../README.md), one mod of [Work in progress](../work-in-progress.md): what is still to check, on BurstPQS.

## The ground it builds

**Planned — read in the source, not measured.** BurstPQS builds the terrain in place of stock, and
since its release 1.0.26 places it in double precision on its own: on a body it builds, the vertex patch
of this fix never runs, and both mods place the same quads, from the same numbers. Open: whether the
ground under a craft comes back to the same place at every load, with BurstPQS alone and with both.

**→ Full chapter: [BurstPQS: the ground it builds](burst-pqs/the-ground-it-builds.md)**
