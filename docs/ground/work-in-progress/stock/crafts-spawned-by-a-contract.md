# Crafts spawned by a contract

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned — read in the code, not measured.**

*Why.* Two kinds of contracts put a craft on the ground of a body, far from any craft of the player: a
craft to repair, often a rover, and a kerbal to rescue from a wreck. Several of them have been seen to
jump when the player reaches them.

*Read in the code.* Neither is placed on the ground the way a launch is, and neither starts in `PRELAUNCH`:

- **A craft to repair** (`VesselRepairContract`) is built by `ContractSystem.ConstructShip`, at the height
  the terrain should have at its latitude and longitude, not at the height of the ground actually built:

  ```csharp
  alt = targetBody.pqsController.GetSurfaceHeight(surfaceNVector, overrideQuadBuildCheck: true) - targetBody.Radius;
  ```

  `MissionSystem.putShiptoGround` then casts a ray down onto the ground collider, which exists only where
  the terrain is built at that moment. The craft is saved `LANDED`, with its subdivision levels at 0, so
  stock moves it onto the ground again (`Vessel.CheckGroundCollision`) the first time it is loaded.
- **A wreck holding a kerbal to rescue** (`RecoverAsset`) is a single part written straight into the save,
  50 m above that same computed height:

  ```csharp
  node.SetValue("sit", "LANDED");
  node.SetValue("landed", "True");
  node.SetValue("alt", (CelestialUtilities.TerrainAltitude(targetBody, latitude, longitude) + 50.0).ToString(CultureInfo.InvariantCulture));
  node.SetValue("hgt", "0");
  ```

  A craft of a single part is moved onto the ground at every load.

The computed height and the ground built from it only meet at the vertices of the terrain mesh: between
them, the gap reaches several metres on rough ground. The jumps seen would then be stock's own, and
nothing this mod removes, nor makes worse: what it corrects is the rounding of the ground, a few
centimetres on Kerbin. This is still to be shown in game.

*The test.* In a career save, take each contract with its craft on the ground of the Mun and of Kerbin,
and save before going near. Reach the craft, with
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) recording it from its first
load, and note every `Moving Vessel` line of `KSP.log`; then save and load six times. Play it without this
mod and with it.

*What should happen.* The craft should come to rest the same way with and without this mod at its first
load, and, with it, stay within a millimetre over the next loads.
