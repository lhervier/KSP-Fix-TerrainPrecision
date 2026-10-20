# The ROCs

Part of [Terrain Precision Fix](../../README.md): Breaking Ground's surface features (ROCs), the objects
studied in EVA or with the robotic arms. Everything about them is still work in progress: read in stock's
code, with no fix of their own yet.

The rounding they may share with the ground, the statics and the scatter is told once in
[The culprit: a float at planet scale](../common/the-culprit.md).

## Status

**Planned — read in stock's code; no fix of their own yet.** The surface features studied in EVA
or with the robotic arms are placed like the rocks, from a holder that hangs under the terrain sphere,
and unlike stock rocks they carry a collider. If they share the rocks' fault, a player would see:

- a surface feature that comes back a few centimetres higher or lower, or slightly aside, at each load;
- a kerbal, a rover wheel or a part resting on one nudged as the flight starts, since what moves is the
  collider it rests on;
- with this mod, the feature off the corrected ground by a gap that changes at each load, as the scatter
  is without the [scatter fix](../scatter/the-fix.md), which does not cover surface features.

## How stock places them

- **One holder per quad, under the sphere.** `LandClassROC` creates a `ROC <name>` container as a child
  of the terrain sphere, and hangs each holder (`PQSMod_ROCScatterQuad`) from it.
  `PQSMod_ROCScatterQuad.Setup` then does `localPosition = quad.positionPlanet`, as
  `PQSMod_LandClassScatterQuad.Setup` does for the rocks
  ([Why the holder has to move at all](../scatter/the-fix.md#why-the-holder-has-to-move-at-all)).
- **Each feature on a vertex of its quad.** `LandClassROC.CreateScatterMesh` takes the position of a
  feature from `quad.verts`, raises it by half the height of its model, sinks it by its depth, and sets
  it as the feature's `localPosition` under the holder. Seen in game: with the colliders shown, the
  features of a quad sit exactly on vertices of its mesh.
- **The same draw at every load.** The vertex, the rotation and the depth come from
  `Random.InitState(quad.quadSeed)`: within its quad, a feature is placed the same way at every load.
  Whatever moves comes from the holder, not from the draw.
- **The collider follows the holder.** It belongs to the feature's model, a child of the holder, so the
  physics takes its pose from the same chain of transforms as what is drawn, as for
  [scatter with colliders](../scatter/non-regression/kopernicus/scatter-with-colliders.md). An offset of the
  holder is a physical one.
- **The identifier does not depend on the holder.** It is computed from the position within the quad,
  so moving the holder would not change which features count as picked up.

## A fix of their own

The cure would be the scatter fix's: hang each holder in use from its quad instead of the container under
the sphere, behind a setting of its own. Nothing is written yet.

Who would see the holders move, read in stock's code: nobody. Every lookup starts from a collider and
walks **up** to the feature or to its holder, never down from the sphere:

- `Part`, on a contact, and `KerbalEVA`, to offer the pickup: `GetComponentInParent<ROC>` on the
  collider touched;
- `ModuleRobotArmScanner`, the scanning arm: only colliders tagged `ROC` enter its range, and it looks
  for the `ROC` on them, their parents or their children;
- `ROCManager.GetTerrainTag`: up to the `PQSMod_ROCScatterQuad`, then its `quad` field.

The link from a holder to its features would not change, so these all keep working. The `ROC <name>`
container is read back only by `LandClassROC`, which creates it. Of the other mods whose source was read,
only Kopernicus (it adds the `PQSROCControl` to the bodies of a planet pack, and patches the validation of
`ROCManager`) and KSP Community Fixes (a validation fix) deal with surface features, and neither walks the
terrain's hierarchy. Every other mod is unread, as for the
[scatter holders](../scatter/work-in-progress/other-mods/mods-that-look-for-a-scatter-holder-under-its-sphere.md).

## Work in progress

**Loading the same save: planned.** Stand a kerbal on a surface feature with a collider (a small one, on
the Mun), save, then [KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) on the
kerbal over six loads, on stock and with this mod. A kerbal that moves at load while the ground under it
does not shows the feature moving. Then the same with a fix of their own, once written.

**Scene changes and time warp, with Jeb on a ROC: planned.** Both are checked on the statics of the KSC;
they are still to play with a kerbal standing on a surface feature.

**→ Full chapter: [Scene changes and time warp, with Jeb on a ROC](work-in-progress/scene-changes-and-time-warp.md)**
