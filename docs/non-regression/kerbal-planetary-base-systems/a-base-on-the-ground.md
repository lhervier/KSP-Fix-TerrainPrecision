# Kerbal Planetary Base Systems: a base on the ground

Part of [Terrain Precision Fix](../../../README.md), one test of [Non-regression tests](../../non-regression.md), on [Kerbal Planetary Base Systems](../../non-regression.md#kerbal-planetary-base-systems).

**Status: nothing to test, read in the source — a base stands on the ground as a stock craft does.**
[Kerbal Planetary Base Systems](https://github.com/n116-software/KerbalPlanetaryBaseSystems), one of the
most popular part mods, adds parts to build bases on the ground, the very thing this mod places: checking
it is only logical. Its plugin never reads or moves the ground, a static or a scatter holder, and its parts
reach the ground through stock modules only: its legs, its landing gear and its drills work on the ground
this mod places as stock parts do.

## What its plugin does

Read in the source of Kerbal Planetary Base Systems 1.6.16 (`Sources/PlanetarySurfaceStructures`).

Its plugin has no Harmony patch, casts no ray, and reads or writes no position. Its part modules:

- **switch parts of a model on and off**: `PlanetaryModule` (a module deployed or packed),
  `ModuleKPBSModelSwitch` (a variant), `ModuleKPBSMeshToggle` (a mesh shown or hidden),
  `ModuleKPBSCorridorNodes` (a corridor where another part is attached). The colliders of a switched
  model go with it, inside the part, which this mod does not touch;
- **run the game logic** of a base: converters, greenhouse, nuclear storage, lights, the editor filter,
  the upgrade of old saves.

It never looks up a terrain sphere, a `PQSCity`, a `PQSCity2` or a scatter holder: neither the statics fix
nor the scatter fix moves anything it looks for.

It also ships two small plugins whose source is not in its repository: Community Category Kit, which adds
its category to the editor's part list, and KSPModFileLocalizer, which translates its files. Neither names
anything of the terrain, of physics or of a craft.

## Its parts on the ground

What touches the ground is configured in its part files, with stock modules:

- **its legs**, the K&K "Bigfoot" and K&K "Little Bigfoot" landing legs, are stock wheels of type `LEG`
  (`ModuleWheelBase`, `ModuleWheelSuspension`), and **its K&K Attachable Landing Gear** a stock motorized
  wheel;
- **its drills**, the K&K Inline Drill and, with a life support mod, the K&K Inline Water Drill, are stock
  harvesters (`ModuleResourceHarvester`, `ModuleAsteroidDrill`). A stock harvester checks that it touches
  the ground with a ray from its impact transform, 5 m long on these drills (KSP 1.12.5):

```csharp
// ModuleResourceHarvester.CheckForImpact
Ray ray = new Ray(position, impactTransformCache.forward);
return Physics.Raycast(ray, out impactHitInfo, ImpactRange, layerMask);
```

That ray hits the collider of the terrain quad, the one this mod places, as it does for a stock drill. A
base of Kerbal Planetary Base Systems stands, rolls and drills on the ground as any stock craft does, and
what this mod changes for it is what it changes for any craft: see the checks of
[the ground](../../../README.md#the-ground).
