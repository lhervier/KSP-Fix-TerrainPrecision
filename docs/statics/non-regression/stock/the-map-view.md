# The map view

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#non-regression-tests): one non-regression test, on stock.

**Status: nothing to test, read in the code — the markers of the launch sites follow their statics
wherever this mod places them.** The map draws the bodies from scaled space, which this mod does not touch.
What it does to the terrain while the map is open is in
[the map view of the ground](../../../ground/non-regression/stock/the-map-view.md).

## The launch sites on the map

The map marks each launch site with a node, placed from the site's `Transform`
(`SiteNode`, through `LaunchSite.GetWorldPos`). That `Transform` belongs to a static, which this mod
takes out of its sphere in flight, near a craft (see [The fix: the statics](../../the-fix.md)).
`LaunchSite.GetWorldPos` would look for it by its path under the sphere, and not find it there; but it
only does so when nothing is cached, and `LaunchSite.Setup` caches it when the game loads the planetary
system, long before any flight. The node then follows the `Transform` itself, wherever this mod
places it, and this mod keeps the static at its place on the ground.
