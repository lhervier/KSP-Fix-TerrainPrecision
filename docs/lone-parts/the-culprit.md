# The culprit: parts lying alone

Part of [Terrain Precision Fix](../../README.md), [parts lying alone](README.md#the-culprit): the extra mass stock gives a part lying alone on the ground, what it does on the moving ground, and why it throws the parts with a suspension.

It has nothing to do with the precision of the ground: it is there on any ground, moving or not. But it
only makes sense on the moving one.

## The moving ground, under a part alone

The ground rebuilt at a load is never where it was when the save was made
([The culprit: the ground](../ground/the-culprit.md)), and a craft of a single part is put back on a ground
that is a little lower or a little higher than the one it rested on. When the craft goes off rails,
`Vessel.CheckGroundCollision` puts it back on the ground, but leaves it where it is when the move would be
under 10 cm: a part alone then starts inside the ground collider by as much as the ground rose since it was
saved, and the physics pushes it out. A large craft takes that push across many parts and joints; a
battery, a strut or a solar panel lying alone is light and held by nothing, and pops up. In development
tests on the Mun, such parts popped up at a load; with the fix of the ground, none did.

## The extra mass

When a part goes off rails, `ModuleCargoPart.OnPartUnpack` starts a coroutine, `MakePartSettle`, if the
part is alone in its craft and the craft is landed or on the launch pad. KSP 1.12.5:

```csharp
if (base.vessel.parts.Count != 1)
{
    return;
}
if (base.vessel.situation != Vessel.Situations.LANDED && base.vessel.situation != Vessel.Situations.PRELAUNCH)
{
    return;
}
StartCoroutine(MakePartSettle(waitForMotionStop: false));
```

`MakePartSettle` keeps the part's mass, raises it, waits for the part's kinematic delay, 3 seconds by
default, and gives it back:

```csharp
preSettlingPrefabMass = base.part.prefabMass;
if (base.vessel.mainBody.GeeASL < 0.800000011920929)
{
    base.part.prefabMass = 20f;
}
else if (base.vessel.mainBody.GeeASL < 1.100000023841858)
{
    base.part.prefabMass = 4f;
}
yield return new WaitForSeconds(kinematicDelay);
base.part.prefabMass = preSettlingPrefabMass;
```

- **4 t on Kerbin, 20 t on the Mun**, whatever the part weighs: a 0.1 t wheel weighs forty times its mass on
  Kerbin, two hundred on the Mun. Above 1.1 g, nothing changes.
- **Every time the part goes off rails**, not only after a drop in EVA construction: at every load, every
  time the player comes back near the part, and every time on-rails time warp stops.
- **371 stock parts carry `ModuleCargoPart`**: every part that fits in an inventory. A craft of several
  parts never goes through this.

Why stock does it is not written anywhere. It applies on the bodies where a pop is the most visible, and
the lower the gravity, the heavier the part: read with the moving ground in mind, it looks like an answer
to those pops. A heavier part is pushed out of the ground less visibly: on the Mun, on stock's ground, parts
without a suspension pop up two to three times higher without the extra mass than with it
([Checking parts lying alone: loading the same save](checking/loading.md)).

## The suspension

`ModuleWheelSuspension` sets the spring of a wheel from the mass of its craft, at every physics step while
the wheel touches the ground. KSP 1.12.5, `ModuleWheelSuspension.FixedUpdate`:

```csharp
vesselMass = (float)base.vessel.totalMass;
SuspensionSpringUpdate(vesselMass);
```

For the 3 seconds of the extra mass, the suspension of a 0.1 t wheel is set for 4 t, and pressed by them:
Unity's wheel collider takes the mass it carries from the part's rigidbody. When the part's own mass comes
back, the spring is still pressed for tons, and it throws the part. Seen in a sandbox game, next to the
runway: a rover wheel taken off a rover in EVA construction and dropped on the grass lies still for about
3 seconds, then flies several metres up and lands tens of metres away. Wheels already lying on the ground
do it again at every load. It happens with and without the fix of the ground.

Among the parts carrying `ModuleCargoPart`, 12 have a suspension: the landing legs LT-05, LT-1 and LT-2,
the five landing gears, and the rover wheels M1, S2, TR-2L and the Making History one.

## Breaking Ground's deployed experiments

The deployed experiments go through the same coroutine from their own code, `ModuleGroundPart`, which also
rivets them to the ground once it has run. They are not part of this page: see
[Breaking Ground's deployed experiments](../ground/work-in-progress/stock/breaking-grounds-deployed-experiments.md).
