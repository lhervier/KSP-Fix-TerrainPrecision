# Breaking Ground's deployed experiments

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned — read in the code, not measured.**

## Why it is a question

A deployed experiment rests on the ground this mod corrects, and is put back onto it far more often than
a craft. Seen in a play save with this mod, around a base on Minmus: when time warp stops, the deployed
experiments jump, a message says each part cannot be deployed because it is not on the surface, and they
fall back to the ground. If this mod caused that, the player would see it on every warp.

## What is already known

- **Each experiment is a craft of a single part.** Once deployed, an experiment is a vessel of its own,
  whose only part carries a `ModuleGroundPart` (`ModuleGroundExperiment`, `ModuleGroundCommsPart` and
  `ModuleGroundExpControl` derive from it through `ModuleGroundSciencePart`). `Vessel.GoOffRails` does
  not wait for the physics hold to end for such a vessel, as for the ground anchor.
- **It is moved onto the ground every time it goes off rails**, not only at load: every time on-rails time
  warp stops. KSP moves a craft of a single part onto the ground collider at every `GoOffRails`
  (`Vessel.CheckGroundCollision`), and for a root carrying a `ModuleGroundPart` it applies even the
  smallest correction, and logs it:

  ```
  [<experiment>]: ground contact! - error. Moving Vessel  up X.XXXm
  ```

  This is where this mod plays a part: that move puts the lowest point of the part on the ground
  collider, which this mod keeps in the same place at every build. The experiment then comes back to the
  same spot after each warp. On stock, it follows the rounding of the ground, which on Minmus is a few
  millimetres.
- **It is let go when it goes on rails, and riveted again seconds later.** `ModuleGroundPart.OnPartPack`
  frees the part: its rigidbody constraints are removed and the joint that holds it to the world is
  destroyed. When it goes off rails, `ModuleGroundPart.OnPartUnpack` starts `MakePartKinematic`, which
  waits in `ModuleCargoPart.MakePartSettle`, then freezes the part and joins it to the world again. The
  experiments keep the default kinematic delay of 3 seconds, so the part is a free body for at least 3
  seconds, then until it moves at under 3 mm/s, for at most 30 seconds of game time. On a body of low
  gravity the wait also raises its mass, to 20 t below 0.8 g. On Minmus, a push of 0.5 m/s in that window
  sends a part 25 cm up and back in 2 seconds.
- **The message comes from the end of that wait.** If the part touches nothing when the wait ends,
  `MakePartKinematic` gives up without riveting it, shows the message, and logs:

  ```
  [ModuleCargoPart]: Part <experiment> cannot deploy unless on the ground.
  ```

  The part then stays free, falls back by gravity, and is only riveted again when it next goes off rails.
  Read in the code, two ways to get there: the part is in the air at that moment, or time warp was started
  again within those seconds, which packs the part away from the ground. The second would show the
  message for every experiment at once. Neither has been played yet.
- **The science does not depend on it.** A deployed experiment works out its situation once, when it
  starts (`DeployedScienceExperiment.Start`), and never again: a part left unriveted keeps producing
  science.
- **None of this goes through the code this mod changes.** The release and rivet are `ModuleGroundPart`'s
  own. This mod's [rivet fix](../../../ground-anchor/the-fix.md#the-rivet) patches
  `ModuleGroundPart.OnPartUnpack` too, but acts on the stock ground anchor only, and its fix of the
  anchor's collider and of the load clamp touch nothing else either.

## To test

**Warp next to deployed experiments.** On Minmus, a few deployed experiments set on the ground around a
small craft, the craft flown. Warp on rails for a few seconds, stop, and watch for 30 seconds; then warp
again, stop, and start warping again within 3 seconds. Note the messages on screen, and the
`Moving Vessel`, `riveting to the ground` and `cannot deploy unless on the ground` lines of `KSP.log`.
Play it without this mod, then with it.

*What should happen.* The same jumps and messages with and without this mod; with it, every `Moving
Vessel` line of an experiment within a few millimetres of the same value from one warp to the next.
