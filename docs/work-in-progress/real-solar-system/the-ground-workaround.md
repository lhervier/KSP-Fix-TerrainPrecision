# Real Solar System: the ground workaround

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [Real Solar System](../../work-in-progress/real-solar-system.md).

**Status: in progress.** With this mod, Real Solar System's ground workaround has nothing left to
correct for this defect when a save is loaded, on the Moon and on Earth, and this mod keeps a craft in
place without it ([The ground workaround](../../non-regression/real-solar-system/the-ground-workaround.md)).
Still open, on the Moon, the other moment the workaround runs: switching to a craft left parked. Coming
back to one is played: over six round trips, the workaround ran each time the capsule was handed back to
physics and never moved it, with this mod or without
([Coming back to a craft left parked, on the Moon](../../non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon.md)).

If this mod and the workaround got in each other's way, a craft would be moved by the workaround
(`Moving Vessel` in `KSP.log`), or jump, at a switch where it does not without it.
