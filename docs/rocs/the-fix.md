# The fix: the ROCs

Part of [Terrain Precision Fix](../../README.md), [the ROCs](README.md#the-fix): what the patches do for Breaking Ground's surface features, where they do it, what they leave alone, and when to turn them off.

The features of a quad hang from a holder that is placed and drawn from a 600 km float, and that does not
share the correction the terrain fix gives the quad ([The culprit: the ROCs](the-culprit.md)). So this mod
hangs each holder from its own quad, as [the scatter fix](../scatter/the-fix.md) does for the rocks.

The fix of the surface features is **on by default**. `fixRocs = false` in the settings turns it off; it is
installed when KSP starts, whether the terrain fix is on or not. It is two Harmony patches, in
[`Src/RocFix.cs`](../../Src/RocFix.cs).

## Hanging each holder from its quad

- **After `PQSMod_ROCScatterQuad.Setup`**, which gives a holder its quad: the holder is re-parented under
  the quad, with zero position, identity rotation and unit scale. The features themselves are built later,
  on the first update of the quad once it is visible, so they are placed under the holder already moved.
  From then on the holder follows the quad through everything stock does to it, with nothing more to do.
- **Before `LandClassROC.DestroyQuad`**, which returns a holder to its pool when its quad is destroyed: the
  holder goes back under the `ROC <name>` container, where stock keeps its free holders, before the quad
  itself goes back to the PQS cache to be reused elsewhere. A prefix, because the stock method clears the
  holder's quad.

The features are placed in the quad's own frame, and their *up* is computed from the rotation of the
holder, which stays the sphere's: nothing about a feature changes but the matrix it is drawn with.

## Only on the quads that allow it

Stock gives surface features to the quads of the highest level only, which are the only ones moved out of
the sphere, into a storage that is not attached to the body. Every other quad hangs from the sphere itself,
with the same kind of 600 km local position as the holder, so hanging the holder from it would gain
nothing: on such a quad, the holder is left where stock places it, and with `logLevel = Debug` the log says
so (`left where stock places it`). On a sphere whose quads are not placed relative to its surface, stock
places the holder at the centre of the body: nothing to fix there.

## Other mods that look for the holders

Who would see the holders move, read in stock's code: nobody. Every lookup starts from a collider and
walks **up** to the feature or to its holder, never down from the sphere:

- `Part`, on a contact, and `KerbalEVA`, to offer the pickup: `GetComponentInParent<ROC>` on the
  collider touched;
- `ModuleRobotArmScanner`, the scanning arm: only colliders tagged `ROC` enter its range, and it looks
  for the `ROC` on them, their parents or their children;
- `ROCManager.GetTerrainTag`: up to the `PQSMod_ROCScatterQuad`, then its `quad` field.

The link from a holder to its features does not change, so these all keep working. The `ROC <name>`
container is read back only by `LandClassROC`, which creates it. Of the other mods whose source was read,
only Kopernicus (it adds the `PQSROCControl` to the bodies of a planet pack, and patches the validation of
`ROCManager`) and KSP Community Fixes (a validation fix) deal with surface features, and neither walks the
terrain's hierarchy. Every other mod is unread, as for the
[scatter holders](../scatter/work-in-progress/other-mods/mods-that-look-for-a-scatter-holder-under-its-sphere.md):
if a mod misbehaves around surface features, `fixRocs = false` turns this fix off
([Settings](../common/settings.md)).

## Safeguards

If either patch cannot be applied, the log says `Could not install the surface features fix` and the
features are left exactly where stock places them. If a holder cannot be moved, the log says so and that
holder is left where stock placed it. A holder goes back to its pool only if this fix moved it: it is
recognised by hanging from its quad.
