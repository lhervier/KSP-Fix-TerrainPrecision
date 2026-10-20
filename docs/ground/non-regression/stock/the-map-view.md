# The map view

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#non-regression-tests): one non-regression test, on stock.

**Status: nothing to test, read in the code — the map view changes nothing in the ground this mod
places.** The map draws the bodies from scaled space, which this mod does not touch. The terrain keeps
being built around the active craft while the map is open, exactly as in flight. The markers of the launch
sites are in [the map view of the statics](../../../statics/non-regression/stock/the-map-view.md).

## The map does not draw the terrain

The map view draws every body as a scaled-down model of its own, in scaled space. The terrain quads,
which this mod places, belong to the terrain sphere of the body, which is not what the map shows. This
mod patches nothing in scaled space.

## The terrain keeps going as in flight

The terrain sphere of each body is switched on and off by `PQSMod_CelestialBodyTransform.OnPreUpdate`,
by the altitude of the camera. While the map is open, that switch is held: an active sphere is not
switched off, an inactive one is not switched on, whatever the altitude. Stripped of the rest:

```csharp
// PQSMod_CelestialBodyTransform.OnPreUpdate
if (sphere.isActive)
{
    if (!MapView.MapIsEnabled && sphere.visibleAltitude > deactivateAltitude)
        sphere.DeactivateSphere();
}
else if (!MapView.MapIsEnabled && sphere.visibleAltitude < deactivateAltitude)
    sphere.ActivateSphere();
```

The same method keeps the target of the sphere on the active craft, map or not
(`sphere.SetTarget(FlightGlobals.fetch.activeVessel.transform)`). So an active sphere goes on
subdividing around the craft, as it does in flight: the map builds and drops no quad that flight would
not, and the quads of the highest subdivision level, those this mod corrects, are the ones around the
craft, as in flight. What this mod does there is what the checks of [the ground](../../README.md)
measure.
