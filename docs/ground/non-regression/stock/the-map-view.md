# The map view

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#non-regression-tests): one non-regression test, on stock.

**Status: nothing to test, read in the code — the map view changes nothing in the ground this mod
places.** The map draws the bodies from scaled space, which this mod does not touch. While the map is
open, the terrain around the active craft is hidden and frozen: no quad is built or dropped, and the quads
already there keep their place and their colliders. The markers of the launch
sites are in [the map view of the statics](../../../statics/non-regression/stock/the-map-view.md).

## The map does not draw the terrain

The map view draws every body as a scaled-down model of its own, in scaled space. The terrain quads,
which this mod places, belong to the terrain sphere of the body, which is not what the map shows. This
mod patches nothing in scaled space.

## The terrain is frozen while the map is open

The terrain sphere of each body is switched on and off by `PQSMod_CelestialBodyTransform.OnPreUpdate`.
While the map is open, an active sphere is switched off, whatever the altitude, and an inactive one is not
switched on. Stripped of the rest:

```csharp
// PQSMod_CelestialBodyTransform.OnPreUpdate
if (sphere.isActive)
{
    if (MapView.MapIsEnabled || sphere.visibleAltitude > deactivateAltitude)
        sphere.DeactivateSphere();
}
else if (!MapView.MapIsEnabled && sphere.visibleAltitude < deactivateAltitude)
    sphere.ActivateSphere();
```

Switching a sphere off only hides it: `PQS.DeactivateSphere` turns off the renderers of its quads and stops
`PQS.UpdateQuads`, which builds and drops quads. The quads stay where they are, colliders included: a craft
landed on the Mun stays on the ground with the map open, at the same altitude. Closing the map switches the
sphere back on (`PQS.ActivateSphere`), which shows the same quads again and lets the subdivision go on from
where it stopped. So the map builds, moves and drops no quad that this mod places: there is nothing to
check that [the ground](../../README.md) does not already measure.
