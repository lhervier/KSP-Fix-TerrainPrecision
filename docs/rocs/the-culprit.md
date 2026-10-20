# The culprit: the ROCs

Part of [Terrain Precision Fix](../../README.md), [the ROCs](README.md#the-culprit): where the rounding strikes Breaking Ground's surface features in the stock code, and why it moves them from load to load.

The rounding itself, shared with the ground, the statics and the scatter, is told once in
[The culprit: a float at planet scale](../common/the-culprit.md). The surface features are placed the way
the scatter is ([The culprit: the scatter](../scatter/the-culprit.md)), with one difference: they carry a
collider.

## How stock places them

- **One holder per quad, under the sphere.** `LandClassROC` creates a `ROC <name>` container as a child
  of the terrain sphere, and hangs each holder (`PQSMod_ROCScatterQuad`) from it.
  `PQSMod_ROCScatterQuad.Setup` then does `localPosition = quad.positionPlanet`, as
  `PQSMod_LandClassScatterQuad.Setup` does for the rocks: a vector as long as the radius of the body, in a
  float.
- **Only on the quads of the highest level.** `LandClassROC.Setup` sets the lowest level a quad needs to
  carry surface features to the highest level of the sphere, as stock scatter does.
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
  holder is a physical one: a kerbal, a wheel or a part resting on the feature is moved with it.
- **The identifier does not depend on the holder.** It is computed from the position within the quad,
  so where the holder hangs does not change which features count as picked up.

## Why it is different at every load

The quad is drawn where its position says, the holder where its matrix says, and the two are rounded
from the same 600 km vector in two different ways
([Why the holder has to move at all](../scatter/the-fix.md#why-the-holder-has-to-move-at-all)). Which way
each one rounds depends on where the floating origin stands when the quad is built, and that changes from
load to load.

## With the terrain fix

On stock, both the ground and the holders move from load to load, and not always by the same amount, as
measured on the scatter ([Checking the scatter: loading the same save](../scatter/checking/loading.md)).
The terrain fix takes the quads out of that rounding, not the holders: the ground then stops moving, and
the features go on moving against it, by centimetres, at every load
([Checking the ROCs: loading the same save](checking/loading.md)).

While you drive, the floating origin moves every 500 m, and with it the sphere, the ground and the holders
alike. On stock they jump together; with the terrain fix alone, the ground holds and the holders jump
against it, as the scatter does
([Checking the scatter: driving on while the world moves](../scatter/checking/driving.md)).
