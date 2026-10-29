# KAS: a pylon linked to a craft

Part of [Terrain Precision Fix](../../../../README.md), [parts lying alone](../../README.md#work-in-progress): one point of the work in progress, on KAS.

**Status: planned — read in the source, not played.**

*Why.* [Kerbal Attachment System](https://github.com/ihsoft/KAS) links crafts with pipes and cables, and its
GP-20 and BGP-400 pylons are made to stand on the ground at the far end of a link: set down in EVA
construction, a pylon is a craft of a single part, linked to another craft by a joint of KAS. Both pylons
carry `ModuleCargoPart`, and stock makes each of them much heavier for 3 seconds every time it goes off
rails, as any part lying alone ([The culprit: parts lying alone](../../the-culprit.md#the-extra-mass)): the
GP-20, 20 kg, weighs 20 t on the Mun while the craft at the other end of the link settles. With this mod,
the pylon keeps its own mass, and whatever pulls on the link at a load pulls on 20 kg. A pylon dragged or
lifted by its link at a load would be something this mod made worse.

*The test.* With KAS installed, on the Mun: a rover carrying an RTS-1 resource transfer station, a GP-20
pylon set on the ground a few metres away, linked to the station by its pipe; save, then load
the save ten times, the pylon set as target in
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel). Without this mod, with this
mod and `fixLonePartMass = false`, then with this mod as installed. Then the same with a BGP-400 pylon, and
on Kerbin.

*What should happen.* The pylon reads the same *Moved* and *Highest* with this mod as installed as with
`fixLonePartMass = false`, a few millimetres at most, and stays linked at every load.
