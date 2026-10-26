# Parallax: loading a craft on the Mun

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on Parallax.

**Status: planned — the save of the Mun has to be made again with Parallax installed.** The Mun was
played with the other worlds of
[Parallax: loading a craft on its ground](../../non-regression/parallax/loading-a-craft-on-its-ground.md),
and left out of that test: its save was made without Parallax, and the spread it reads with this mod
comes from a Parallax collider at that spot, not from the ground.

If this mod held the ground less well under Parallax on the Mun, a craft landed there would settle
somewhere else at every load, as it does without this mod.

**What is known.** KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) 1.0.5 with its stock textures and what
it requires, [KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel),
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) and this mod with its
defaults. [The loading protocol](../../checking/loading-protocol.md), played by its script,
[`run-loading.py`](../../../../diag/ground/automation/run-loading.py), on
[`reload-mune-2parts.sfs`](../../../../diag/ground/checking/loading/reload-mune-2parts.sfs), six loads:

- with Parallax's rock colliders on (its default), *Ground under craft* spreads over about 0.9 mm, and
  *Moved* stays between −1 and −2 mm at every load;
- with Parallax's rock colliders off (`collisionLevel = -1` in
  `ParallaxContinued/Config/ParallaxGlobalSettings.cfg`), within 0.009 mm, *Moved* under 0.05 mm;
- without Parallax, on the same install, within 0.007 mm.

With the colliders off, the capsule comes back as it does without Parallax, on the same ground. So the
spread comes from a collider of Parallax at that spot, and the test, played on that
save, reads that collider, not the ground this mod places.

*To test:* make the save of the Mun again with Parallax installed, as in
[Making the save](../../checking/making-the-save.md), on a spot where
[KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders) shows no collider of Parallax near the
tank, then play the loading protocol on it, with Parallax's colliders on: six loads without this mod, then
six with it. By hand: load that save, watch the capsule as it goes off rails (it should not move), and
reload it a few times while reading *Settled* in KSP Diag - Landed Vessel. With this mod, it should come
back within a few hundredths of a millimetre, as without Parallax.
