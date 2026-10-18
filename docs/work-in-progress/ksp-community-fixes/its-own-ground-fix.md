# KSP Community Fixes: its own ground fix

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [KSP Community Fixes](../../work-in-progress/ksp-community-fixes.md).

**Status: planned — announced, not released.** The author of BurstPQS, also a maintainer of KSP Community
Fixes, placed the terrain in double precision in BurstPQS to try out a fix for the moving ground, and plans
to fix it in KSP Community Fixes as well
([BurstPQS issue #15](https://github.com/Phantomical/BurstPQS/issues/15)).

With such a release, this mod's terrain fix and KSP Community Fixes would each place the same quads, in an
order nothing fixes. This mod handles that case with BurstPQS already: its terrain fix steps back on the
bodies BurstPQS builds ([Limits and solutions: BurstPQS](../../limits-and-solutions/burst-pqs.md)).

*To do:* once a release of KSP Community Fixes places the terrain, read its patch, make this mod's terrain
fix step back where it applies, and play [the loading campaign](../../checking-the-culprit-loading.md) with
both.
