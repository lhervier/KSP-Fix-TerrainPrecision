# BurstPQS: its release 1.0.28

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on BurstPQS.

**Status: planned.** Every campaign of [Limits and solutions: BurstPQS](../../limits/burst-pqs/README.md)
ran with BurstPQS 1.0.27. Release 1.0.28
([pull request #16](https://github.com/Phantomical/BurstPQS/pull/16)) changes two things in how BurstPQS
places a quad:

- `PQ.PrecisePosition`, the position of a quad in double, is now set from the position BurstPQS places the
  quad at, and kept up to date at every move of the world;
- a quad that `PQ.Subdivide` reuses from its cache is placed before it is made visible, instead of after.

This mod's terrain fix steps back on the bodies BurstPQS builds, and reads neither. Its scatter fix hangs
each scatter holder from its quad, on those bodies too. If the two disagreed, rocks, grass and trees would
be drawn off the ground on the bodies BurstPQS builds, or jump against it at a move of the world.

*To test:* the campaigns of [BurstPQS: the campaigns](../../limits/burst-pqs/the-campaigns.md)
and [BurstPQS: the scatter](../../../scatter/limits/burst-pqs/the-scatter.md) again with release 1.0.28,
with BurstPQS alone and with this mod.
