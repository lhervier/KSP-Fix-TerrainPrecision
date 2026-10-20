# Work in progress: stock

Part of [Terrain Precision Fix](../../README.md), one mod of [Work in progress](../work-in-progress.md): what is still to check, on stock.

## Asteroids held by a claw

**Planned.** At the first load with this mod, the ground under an asteroid resting on it moves once, with
a mass on the other end of a joint.

**→ Full chapter: [Asteroids held by a claw](stock/asteroids-held-by-a-claw.md)**

## Breaking Ground's surface features

**Planned.** They are placed like the rocks, and carry a collider: a feature could come back aside at
each load, nudging what rests on it, and the scatter fix does not cover them. The cure would be the
scatter fix's; read in stock's code, nothing looks for them under the sphere.

**→ Full chapter: [Breaking Ground's surface features](stock/breaking-grounds-surface-features.md)**

## Breaking Ground's deployed experiments

**Planned.** They are vessels and should sit on the corrected ground like a craft, but skip the physics
hold, like the ground anchor.

**→ Full chapter: [Breaking Ground's deployed experiments](stock/breaking-grounds-deployed-experiments.md)**

## The ocean

**Planned.** Read in the logs, this mod corrected terrain quads only, never the ocean; how the ocean
sphere is flagged has not been read, and a craft floating near a coast has not been watched.

**→ Full chapter: [The ocean](stock/the-ocean.md)**

## A mission spawning a craft

**Planned.** A mission of Making History spawns a craft on a spawn point of the KSC, as a launch does.

**→ Full chapter: [A mission spawning a craft](stock/a-mission-spawning-a-craft.md)**

## The other stock statics

**Planned.** The KSC 2, the Island Airfield, the pyramids, the monoliths and the easter eggs are placed
like the KSC, and taken out of their sphere the same way; some monoliths are placed at random, from the
seed of the game.

**→ Full chapter: [The other stock statics](stock/the-other-stock-statics.md)**

## The scatter fix without the terrain fix

**Planned.** The scatter fix, on by default, stays on with the terrain fix turned off, but has only
been measured with it.

**→ Full chapter: [The scatter fix without the terrain fix](stock/the-scatter-fix-without-the-terrain-fix.md)**
