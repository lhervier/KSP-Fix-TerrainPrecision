# The culprit: parts lying alone

Part of [Terrain Precision Fix](../../README.md), [parts lying alone](README.md#the-culprit): why a part lying alone on the ground pops out of it, the extra mass stock gives it in answer, and why that mass throws the parts with a suspension.

Stock does not say why it makes a part lying alone heavier. What follows is our reading of it: a story we
cannot prove, but every step of which is in stock's code or in our measurements.

## A part alone on the moving ground

The ground rebuilt at a load is never where it was when the save was made
([The culprit: the ground](../ground/the-culprit.md)), and a craft of a single part is put back on a ground
that is a little lower or a little higher than the one it rested on. When the craft goes off rails,
`Vessel.CheckGroundCollision` puts it back on the ground, but leaves it where it is when the move would be
under 10 cm: a part alone then starts inside the ground collider by as much as the ground rose since it was
saved, up to 10 cm, and the physics pushes it out. A large craft takes that push across many parts and
joints; a battery, a strut or a solar panel lying alone is light and held by nothing, and pops up.

So, in stock, a part left alone on the ground sometimes jumps when you load the save or come back to it:
not every time, only when the ground came back higher.

## Stock's answer: the extra mass

Nothing in stock's code accounts for a ground that moves: everything is written as if it came back at the
same height every time. Seen from there, a part alone that jumps at a load is a part that is too light to
stay put. And that is what stock answered, we believe: it makes such a part much heavier for a few seconds,
the time for it to settle.

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
  Kerbin, two hundred times on the Mun. Above 1.1 g, nothing changes. The lower the gravity, the heavier
  the part: the bodies where a pop goes the highest are the ones where the part is made the heaviest.
- **Every time the part goes off rails**, not only after a drop in EVA construction: at every load, every
  time the player comes back near the part, and every time on-rails time warp stops.
- **371 stock parts carry `ModuleCargoPart`**: every part that fits in an inventory. A craft of several
  parts never goes through this.

**And it works.** On the Mun, on stock's ground, we loaded the same save ten times with the extra mass,
then ten times without it. Without it, the parts pop out higher: the batteries by 60 to 69 mm in the median
instead of 26, the solar panels by 303 mm instead of 105, the strut by 41 mm instead of 19
([Checking parts lying alone: loading the same save](checking/loading.md)). The extra mass does not stop the
pops, the parts still start inside the ground, but it makes them two to three times smaller.

## The price: the parts with a suspension

The answer has a price, on the parts that carry their own suspension. `ModuleWheelSuspension` sets the
spring of a wheel from the mass of its craft, at every physics step while the wheel touches the ground.
KSP 1.12.5, `ModuleWheelSuspension.FixedUpdate`:

```csharp
vesselMass = (float)base.vessel.totalMass;
SuspensionSpringUpdate(vesselMass);
```

For the 3 seconds of the extra mass, the suspension of a 0.1 t wheel is set for 4 t on Kerbin, 20 t on the
Mun, and pressed by them: Unity's wheel collider takes the mass it carries from the part's rigidbody.
Depending on how the part rests on the ground, the spring ends up pressed hard. When the part's own mass
comes back, the spring is still pressed for tons, lets go all at once, and throws the part into the air.
A rover wheel taken off a rover in EVA construction and set down on the ground lies still for about
3 seconds, then flies several metres up and lands tens of metres away
([Checking parts lying alone: a wheel dropped in EVA construction](checking/wheel-drop.md)). Wheels already
lying on the ground do it again at every load.

Here the extra mass works the other way round. In the same ten loads on the Mun, on stock's ground, the
wheels were thrown 1.3 to 13.7 m up with it; without it, they popped out of the ground like the other
parts, by 11 to 57 mm.

Among the parts carrying `ModuleCargoPart`, 12 have a suspension: the landing legs LT-05, LT-1 and LT-2,
the five landing gears, and the rover wheels M1, S2, TR-2L and the Making History one.

## With the ground fixed

On stock's ground, the extra mass is a trade: fewer pops for the parts without a suspension, wheels and
legs thrown into the air. This mod changes the terms of that trade.

- **The parts without a suspension no longer need it.** With the ground fixed, a part alone starts where it
  was, at every load, and nothing pushes it out: it settles the same way with the extra mass and without it.
- **The parts with a suspension are still thrown.** The extra mass has nothing to do with the precision of
  the ground: it presses their spring on any ground, moving or not, and the wheels are thrown as high on
  this mod's ground as on stock's.

The extra mass now only does harm, which is why this mod takes it away: see
[The fix: parts lying alone](the-fix.md). With both, the ground fixed and the extra mass gone, the parts
without a suspension stay where they are, and a wheel or a leg lying alone only presses its spring under its
own mass.

## Breaking Ground's deployed experiments

The deployed experiments go through the same coroutine from their own code, `ModuleGroundPart`, which also
rivets them to the ground once it has run. They are not part of this page: see
[Breaking Ground's deployed experiments](../ground/work-in-progress/stock/breaking-grounds-deployed-experiments.md).
