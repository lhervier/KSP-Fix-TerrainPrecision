# Non-regression tests: Deferred

Part of [Terrain Precision Fix](../../README.md), one mod of [Non-regression tests](../non-regression.md): what works without this mod still works with it, with Deferred.

Unless a page says otherwise, each test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1 and this mod, plus the instrument and the mods it names. Each test has a page of
its own.

[Deferred](https://github.com/LGhassen/Deferred) replaces the way KSP draws everything, the terrain
included, and it is the mod that broke KSP Community Fixes' own `PQSOnlyStartOnce`: anything touching the
terrain spheres gets checked against it.

## Drawing the ground

**Checked, no problem.** Deferred draws the ground wherever it is placed and patches nothing this mod
patches. With it installed, the craft and the ground come back as they do without it, after a load and
after a trip out of range.

**→ Full chapter: [Deferred: drawing the ground](deferred/drawing-the-ground.md)**
