# BurstPQS: the campaigns, the statics

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#non-regression-tests): one non-regression test, on BurstPQS.

**Status: checked, nothing worse with this mod.** Every scripted campaign of the statics, played with
BurstPQS 1.0.27 (with Kopernicus 251, KSPTextureLoader and KSPBurst with its compiler), each in two
installs: **BurstPQS** (KSP, KSP Community Fixes, BurstPQS and what it requires) and **BurstPQS with this
mod, as it installs**. The saves are the published ones. In each table, the spread over the repetitions of
the protocol, in millimetres. The ground campaigns, and what BurstPQS does, are in
[BurstPQS: the campaigns](../../../ground/limits/burst-pqs/the-campaigns.md).

## The statics

BurstPQS places the ground in double on the bodies it builds, but has no code for `PQSCity` or `PQSCity2`.
Without this mod the statics keep the stock rounding, and since the ground no longer moves, they now move
**against** it:

| Protocol | BurstPQS | BurstPQS + this mod |
|---|---|---|
| Loading, the craft on the KSC runway, 6 loads | 193.1 | 0.32 |
| Driving on the runway and the grass, the runway deck at a move of the world | +28.3, +11.6, −21.0 (the grass: 0.00) | −0.03, +0.02, −0.7 |
| Scene changes, the launchpad, 11 arrivals | 108.0 | 0.16 |
| Facility levels, the same surface, 4 arrivals each | 152.4 and 116.3 | 0.062 and 0.066 |
| Kerbal Konstructs runway on the Mun, 6 loads | 31.9 | 21.3 at the first load, then 0.03 (the case of [a section of the runway at the first loading](../../work-in-progress/kerbal-konstructs/a-section-of-the-runway-at-the-first-loading.md)) |
| A Kerbal Konstructs static under a landed capsule, before and after a fly-over | 8.6 | 0.014 |

On Real Solar System, the launchpad of Cape Canaveral over 11 arrivals: 594 without this mod, 0.14 with
it; the runway without its runway fix: 576 from one load to the next and a step of +116.5 between two of its
sections, 0.29 and −3.1 with this mod. Driving on that runway without this mod, the rover turned over just
after a move of the world; with it, it drove on, the deck moving by −0.05 and +0.01 at each move. The Earth
being one of the bodies BurstPQS leaves to stock, the ground next to the runway holds too with this mod: the
grass 0.24 from one load to the next, +0.14 and +0.24 at a move of the world.

## No regression seen

Destroyed buildings and time warp: the same as without BurstPQS.
