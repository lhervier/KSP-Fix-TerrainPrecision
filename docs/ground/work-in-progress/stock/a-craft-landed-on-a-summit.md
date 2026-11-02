# A craft landed on a summit

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned — seen in game, read in the code, no fix written.**

*Why.* A rover saved on a summit of Eve appears above the ground at every load, and falls back onto its
wheels once physics starts. A light rover takes it; a heavy base, full tanks or fragile legs may not, and
it happens at every load. This mod does not change it: it comes from stock, with or without it.

*Read in the code.* When it loads a landed craft, `Vessel.Load` raises it to the height the terrain
should have at its latitude and longitude, and never lowers it:

```csharp
double val = body.pqsController.GetSurfaceHeight(relSurfaceNVector, overrideQuadBuildCheck: true) - body.Radius;
return Math.Max(alt, val);
```

(`Vessel.getCorrectedLandedAltitude`.) On flat ground, a craft rests above that height and nothing
happens. But the ground built under a craft is a mesh of flat triangles stretched between points of that
computed surface: on a summit or a ridge, the triangles pass below the relief, by several metres on rough
ground. A craft resting on them is saved below the computed height, and loaded above its own position.

A craft of a single part is then moved down onto the ground (`Vessel.CheckGroundCollision`, which logs
`Moving Vessel`). A craft of several parts is not, as long as the subdivision levels saved with it match
the current ones: it wakes up in the air and falls the whole gap.

Stock already handles one case where the saved position cannot be trusted: when the terrain detail
setting has changed, the subdivision levels saved with each landed craft no longer match, and
`CheckGroundCollision` puts every one of them back onto the ground, whatever its number of parts.

*A fix to weigh.* Leave a landed craft at its saved altitude when its saved subdivision levels match the
current ones, which is exactly when stock already trusts that position. What the raise may still protect:
a terrain changed without the levels changing, such as a planet pack updated between two sessions, which
would leave the craft inside the new ground. Keeping the raise beyond a few metres below the computed
height would cover that, at the price of a threshold to choose. Not written yet: this mod touches the
raise only for a craft holding a ground anchor (see [the ground anchor](../../../ground-anchor/README.md)).

*The test.* Without this mod, then with it: a craft of several parts saved on a summit of Eve, and on a
summit of the Mun, recorded from its first load by
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel): its altitude on rails
against its saved altitude, its fall, and any `Moving Vessel` line of `KSP.log`; then six loads.

*What should happen.* Without the change: on rails at the computed height, a fall of several metres at
every load, the same with this mod. With it: on rails at its saved altitude, no fall.
