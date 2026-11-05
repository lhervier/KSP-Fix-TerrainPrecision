# BurstPQS: the campaigns, the statics

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#non-regression-tests): one non-regression test, on BurstPQS.

**Status: checked, nothing worse with this mod.** Every scripted campaign of the statics, played with
BurstPQS 1.0.30 (with Kopernicus 252, KSPTextureLoader and KSPBurst with its compiler), each in two
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
| Loading, the craft on the KSC runway, 6 loads | 130.7 | 0.22 |
| Driving on the runway and the grass, the runway deck at a move of the world | −29.8, +47.5, −7.2 (the grass: 0.00) | −0.05, −0.04, −0.03 |
| Scene changes, the launchpad, 11 arrivals | 182.8 | 0.12 |
| Facility levels, the same surface, 4 arrivals each | 77.6 and 106.4 | 0.120 and 0.071 |
| Kerbal Konstructs runway on the Mun, 6 loads | 38.2 | 21.3 at the first load, then 0.01 (the case of [a section of the runway at the first loading](../../work-in-progress/kerbal-konstructs/a-section-of-the-runway-at-the-first-loading.md)) |
| A Kerbal Konstructs static under a landed capsule, before and after a fly-over | 40.4 | 0.012 |

On Real Solar System 20.1.3, the launchpad of Cape Canaveral over 11 arrivals: 1 166 without this mod, 0.11
with it. The runway without its runway fix, 30 loads: the deck before the step between two of its sections
moves by 683 and the step ranges from +78 to +117 without this mod; with it, 0.35 and a step of −3.1.
Driving on that runway, the deck at each move of the world: +191.7 and −25.1 without this mod, +0.03 and
0.00 with it. The Earth being one of the bodies BurstPQS leaves to stock, the ground next to the runway
holds too with this mod: the grass 0.31 over the 30 loads, −0.06 at a move of the world.

## No regression seen

Destroyed buildings and time warp: the same as without BurstPQS.
