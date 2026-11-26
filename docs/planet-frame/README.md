# Planet Frame

Part of [Terrain Precision Fix](../../README.md): a service the fixes share, not a fix of its own. It has no switch: it
runs whenever a fix that needs it does. It works out, in double precision, the frame a body's terrain sphere hangs in,
and says when a correction is too large to be a rounding.

## The frame of a body's terrain sphere

The quads of the ground and the statics standing on it are placed by stock in the frame of their body's terrain
sphere: how the body is turned in Unity's world, and where its centre sits. The ground and the statics fixes redo
that placement with the frame in double: a point of the sphere goes to the world at
`body.rotation * position + body.position`, with `QuaternionD` and `Vector3d`, and back by the inverse. Both values
come from `CelestialBody`, which holds them in double; the rotation of the body's `Transform` is the same rotation
held in float, and on a 600 km vector it brings back the very rounding being removed.

**→ Where each fix uses it: [Doing the arithmetic in double](../ground/the-fix.md#doing-the-arithmetic-in-double)
for the ground, [How the fix works](../statics/the-fix.md#how-the-fix-works) for the statics**

## The safeguard

A correction larger than sixteen float steps, taken at the distance of the corrected object from the centre of its
body, is refused: the quad, or the static, is left where stock puts it. The limit grows with the body as the rounding
does, 1 m on Kerbin and 8 m on Earth in Real Solar System, while a wrong frame would miss by kilometres. On the four
stock worlds and five bodies of Real Solar System, it never refused a correction.

**→ Full chapter: [This mod's safeguard](safeguard.md)**

## In the mod's code

The service is `PlanetFrame`, in [Src/PlanetFrame.cs](../../Src/PlanetFrame.cs):

- `BodyOf` gives the body a terrain sphere belongs to, remembered between calls, since the quads of one sphere are
  built in bursts;
- `WorldPosition` and `SpherePosition` take a point from the frame of the sphere to the world and back:

```csharp
return body.rotation * spherePosition + body.position;
```

- `IsRoundingCorrection` holds a correction against `MaxCorrectionInFloatSteps` float steps, the step being
  `FloatStep` at the distance of the object from the centre of the body.

The ground fix (`TerrainFix`) and the statics fix (`StaticsFix`) use all of it; the code that tells the ground and the
scatter fixes which bodies BurstPQS builds the terrain of (`BurstPQSCompat`) uses `BodyOf`.
