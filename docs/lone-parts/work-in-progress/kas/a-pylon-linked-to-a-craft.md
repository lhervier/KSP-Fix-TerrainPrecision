# KAS: a pylon linked to a craft

Part of [Terrain Precision Fix](../../../../README.md), [parts lying alone](../../README.md#work-in-progress): one point of the work in progress, on KAS.

**Status: planned — read in the source, not played. Expected: no worse, and likely better, than stock.**

*What a pylon is for.* [Kerbal Attachment System](https://github.com/ihsoft/KAS) links crafts with hoses and
cables. The hose of its RTS-1 resource transfer station is only so long, and its GP-20 and BGP-400 pylons
are made to extend it: a light pylon set on the ground, with a socket a hose plugs into, to chain links
across long distances. The GP-20 weighs 20 kg; the BGP-400, 45 kg, adds batteries and a probe core. Neither
anchors anything: the ground anchors of KSP do not replace them, and they do not replace a ground anchor.

*Why it is a question.* Set down in EVA construction, a pylon is a craft of a single part. Both pylons carry
`ModuleCargoPart`, and stock makes each of them much heavier for 3 seconds every time it goes off rails, as
any part lying alone ([The culprit: parts lying alone](../../the-culprit.md#stocks-answer-the-extra-mass)):
the GP-20 weighs 20 t on the Mun while the craft at the other end of the hose settles. With this mod, it
keeps its own 20 kg.

*Only when the hose does not couple.* The RTS-1 lets the player choose, in its menu, whether the hose
couples the two ends (`coupleMode = SetViaGUI`, and both pylons have `allowCoupling = true`). Coupled, the
pylon becomes a part of the craft at the other end: that craft has more than one part, stock never makes it
heavier, and this mod changes nothing. Only a pylon at the end of a hose that does not couple is a part
lying alone.

*Nothing in KAS holds a pylon to the ground.* The current pylons carry only the socket of the hose
(`KASLinkTargetBase`), `ModuleCargoPart`, and, on the BGP-400, the probe core and its batteries. What holds
a pylon at rest is stock's own anchor, which every landed craft gets once it has stayed still for
1.5 seconds: a fixed joint to the world, which breaks under a force set from the mass of the craft.
KSP 1.12.5, `Vessel.AddRBAnchor`:

```csharp
joint.breakForce = Mathf.Max((float)totalMass, PhysicsGlobals.PartRBMassMin) * (float)graviticAcceleration.magnitude * GameSettings.VESSEL_ANCHOR_BREAK_FORCE_FACTOR;
```

The factor is 1.05, and the force is set again at every physics step: on the Mun, the anchor of a GP-20
breaks at about 34 kN while stock makes it weigh 20 t, and at about 34 N once its own mass is back. Stock
also drops the anchor when the force on it turns by more than 20° in a tenth of a second, or points down.
Once its 3 seconds are over, a pylon of 20 kg is held the same way with this mod and without it: a rover
running into it pushes it away, in stock as with this mod.

*What the hose does.* The hose of the RTS-1 is a rope, not a rod: a joint of KAS (`KASJointCableBase`) that
only limits the distance between its two ends, and leaves them free to turn. Its length is the distance
between the two sockets at the moment the hose is plugged in, and it is saved with the game. Shorter than
that, the hose is slack and pulls on nothing. Past it, it pulls back like a spring of 1 kN per metre, and
it breaks at 1 kN, about a metre past its length (`cableSpringForce = 1`, `linkBreakForce = 1`, in the
units of KSP, where masses are in tonnes and forces in kilonewtons). A hose plugged in has no slack: as soon
as the two sockets come back a little further apart at a load, it pulls. That happens when the craft sinks
onto its suspension as it settles, or when it comes back a little elsewhere because stock built the ground
at another height.

*What should follow, read in the source.* At a load, the two ends of a hose come back a few centimetres
further apart at most, which makes a pull of a few tens of newtons, far under the 1 kN that breaks the hose.

- **In stock**, a pylon weighing 20 t takes that pull without moving: the hose stays a little taut, and does
  not break. It would only break if the craft moved about a metre away, which a load does not do.
- **With this mod**, a pylon of 20 kg slides towards the craft as soon as the pull goes past its anchor,
  about 34 N on the Mun: 3 to 4 cm past the length of the hose. It slides only by that much: once the hose
  is slack again, nothing pulls on it. It moves by a few centimetres and stops; it is not dragged.

Neither breaks the link: at worst, with this mod, a pylon of 20 kg comes a few centimetres closer to the
craft, which is what a player expects of a part that light at the end of a taut hose. And since the ground
of this mod comes back at the same height at every load, the two ends have less to make up for than in
stock.

*The test.* With KAS installed, on the Mun: a rover carrying an RTS-1, a GP-20 pylon set on the ground a
few metres away, linked to the station by its hose, **not coupled**; save, then load the save ten times,
the pylon set as target in [KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel).
Without this mod, with this mod and `fixLonePartMass = false`, then with this mod as installed. Then the
same with a BGP-400 pylon, and on Kerbin.

*What should happen.* With this mod as installed, the pylon moves by a few centimetres at most, towards
the craft, and stays linked at every load; without this mod and with `fixLonePartMass = false`, it does not
move, and stays linked too.
