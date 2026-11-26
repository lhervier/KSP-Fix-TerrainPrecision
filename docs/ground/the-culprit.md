# The culprit: the ground

Part of [Terrain Precision Fix](../../README.md), [the ground](README.md#the-culprit): the stock code that places the ground, and why it places it somewhere else at every load.

Here it is straight away.

This is how every terrain vertex is placed, in `PQS.BuildVertexSurfaceRelative`, in
KSP 1.12.5 (`vertRel` and `planetRel` are `Vector3d` fields):

```csharp
private void BuildVertexSurfaceRelative(VertexBuildData data)
{
    vertRel = vbData.directionFromCenter * vbData.vertHeight;
    planetRel = base.transform.TransformPoint(vertRel);
    verts[vertexIndex] = vertRel;
    buildQuad.verts[vertexIndex] = buildQuad.transform.InverseTransformPoint(planetRel);
}
```

`vertRel` is the vertex relative to the centre of the body, computed in double: a vector 600 km long
on Kerbin. `TransformPoint` turns it into a world position, which in KSP is close to the craft. To get
there, it adds that 600 km vector to the position of the centre of the body, another vector of about
600 km pointing the other way, and keeps the difference.

`InverseTransformPoint` then expresses that world position relative to `buildQuad.transform`, the
`Transform` of the quad the vertex belongs to. That one holds a 600 km vector of its own, built
exactly like `vertRel` — a direction from the centre of the body, times a height, this time the
height of the centre of the quad:

```csharp
// PQ.PreciseUpdateSubQuadsPosition; the same two values are computed in PQ.Subdivide
// when a quad creates its children, and assigned to the Transform in PQ.SetupQuad
positionPlanetRelative = positionPlanePosition.normalized;              // Vector3d
positionPlanet = positionPlanetRelative * sphereRoot.GetSurfaceHeight(positionPlanetRelative);
quadTransform.localPosition = positionPlanet;
```

The parent of that `Transform` is the sphere's quad storage, which hangs off the body without an
offset of its own. So this is a 600 km double stored in a float `localPosition`, under a parent that
sits at the centre of the body.

**That is the error.** A `Transform` works in `float`, and a float holding 600 km can only change in
steps of 62.5 mm. Every one of those values is rounded to the nearest step on the way, and the
roundings pile up in the few centimetres that are left once the two 600 km vectors cancel out. The
quad origin is rounded, and each vertex inside it is rounded on its own, so the mesh is not only moved
but also slightly bent.

## Why it is different at every load

`vertRel` and `positionPlanet` are exactly the same doubles on every load of a save. What changes is the
frame they are converted into, the world matrix of the terrain sphere: its rotation comes back different
from every load, and its translation moves with the floating origin. How and when is told once, for the
ground and everything it carries, in
[A frame that moves: the floating origin](../how-ksp-builds-the-ground/README.md#a-frame-that-moves-the-floating-origin).

That the frame changes at every load is measured. That this change is what draws a new rounding is
read from the stock code and consistent with every measurement taken since; it has not been tested on
its own. It does not need to be: [the fix](the-fix.md) does not care whether a rounding is still
drawn at every load, since it shrinks that rounding to a size where drawing it again no longer matters.
