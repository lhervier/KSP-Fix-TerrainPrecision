# The ground anchor

Part of [Terrain Precision Fix](../../README.md): the stock ground anchor, and the base it holds. Unlike the
ground, the statics and the scatter, its culprit is not a rounding: two stock behaviours raise an anchored
base when it is loaded. How this mod takes them away, how that is checked, and what keeps working.

## The culprit

Two stock behaviours raise an anchored vessel when it is loaded, and the anchor, riveted to the ground,
keeps it there: the anchor's collider stops 2 cm above its bottom, and KSP raises a landed vessel to the
height it computes for the terrain, above the ground it actually rests on. Neither is a rounding.

**→ Full chapter: [The culprit: the ground anchor](the-culprit.md)**

## The fix

The anchor's collider is brought down to the bottom of the anchor, and a vessel holding an anchor is loaded
where it was saved instead of being raised: each by its own setting, `fixGroundAnchorModel` and
`fixGroundAnchorLoad`, both on by default, for the stock anchor only.

**And a third.** KSP rivets an anchor again one frame after it is loaded, and below 50 frames per second the
physics moves it in between, by under a millimetre at each load. A third setting,
`fixGroundAnchorRivet`, on by default, freezes it from the moment it is loaded, so that a base behaves the
same at any frame rate.

Loading a vessel where it was saved is only safe on a ground that comes back where it was: it relies on the
fix of [the ground](../ground/README.md). The settings are in [Settings](../common/settings.md).

**→ Full chapter: [The fix: the ground anchor](the-fix.md)**

## Checked

- **Anchoring a base**, an anchor placed on Kerbin, alone then with a battery on it, saved and loaded
  twice: on stock, the anchor comes back 4.1 cm higher than placed, and the base 26.3 cm above the ground at
  its second load; with this mod, both within 0.08 mm.

  **→ Full chapter: [Checking the culprit: anchoring a base](checking/anchoring.md)**

- **Below 50 frames per second**, at 30: a base held in the air sinks at every load, 7.1 mm over eleven
  loads on stock and 8.5 mm with this mod and its third setting off; with this mod as installed, not at all.

  **→ Full chapter: [Checking the culprit: anchoring a base, below 50 frames per second](checking/anchoring.md#below-50-frames-per-second)**

The saves, the scripts and the `KSP.log` of every session, both ways, are in
[the runs of the ground anchor](../../diag/ground-anchor/README.md).

## Non-regression tests

What works without this mod still works with it. Unless a page says otherwise, each test is played in KSP
1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1 and this mod, plus the instrument and the
mods it names. A base saved without this mod and loaded with it is in
[existing saves](../common/existing-saves.md); and removing this mod raises an anchored base again at its
next load, as stock raises it: [Removing this mod](the-fix.md#removing-this-mod).

### Stock

**An anchor on a static: checked on Kerbin, on a runway of each kind of static.** An anchor stays put only
if what it stands on comes back too. On the runways of the KSC and the Desert Airfield, an anchor and an
anchored base stay within 0.15 mm of the runway, once 1.6 mm; without this mod, up to 116 mm away.

**→ Full chapter: [An anchor on a static](non-regression/stock/an-anchor-on-a-static.md)**
