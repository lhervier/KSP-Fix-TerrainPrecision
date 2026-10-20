# What the fixes share

Part of [Terrain Precision Fix](../../README.md): what holds for every fix of this mod at once — the
culprit they share, what they cost, how to install, set and build the mod, and the tests that cover them
all.

## The culprit

Stock places the ground, the statics, the scatter and the surface features through Unity `Transform`s whose positions are floats,
holding vectors as long as the radius of the body: at 600 km a float moves in steps of 62.5 mm, and the frame
these vectors go through does not stay put, so each placement draws a new rounding.

**→ Full chapter: [The culprit: a float at planet scale, in a frame that moves](the-culprit.md)**

## Performance

**The fix does not slow the game down.** Timed frame by frame with
[KSPProfiler](https://github.com/KSPModdingLibs/KSPProfiler), on the same flight, every run of the fix came
out a little cheaper than every run of stock on the coroutines the terrain is updated in — by more than the
fix's own saving can explain, so not a gain to claim, but no cost. Measured vertex by vertex with
[PQS Bench](https://github.com/lhervier/KSP-PQSBench), the fix even places a vertex faster than stock, but
that saving is about 0.04 % of the time played, too small for a frame to show. Turned on, the scatter fix
shows no cost these runs can resolve. What the statics fix costs with statics near a craft is not measured
yet.

**→ Full chapter: [Performance](performance.md)**, and the runs in [`diag/common/perfs`](../../diag/common/perfs/README.md)

## Install, settings, build, license

- **[Install](install.md)**: KSP 1.12 and HarmonyKSP; copy `GameData/TerrainPrecisionFixMod`. Nothing is
  written to your saves.
- **[Settings](settings.md)**: the nine values of `settings.cfg`, one per fix and per patch, and `logLevel`.
- **[Build](build.md)**: `KSPDIR`, `build.bat` and the .NET SDK.
- **[License](license.md)**: MIT.

## Checked

This fix is built on top of [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes), the
base most players run: every campaign of these pages is run in an install that has it, KSP 1.12.5 with
Harmony, ModuleManager and KSP Community Fixes 1.41.1. *On stock* means that install without this mod. The
runs shared by every fix are in [the runs of what the fixes share](../../diag/common/README.md).

## Non-regression tests

What works without this mod still works with it, for every fix at once. Unless a page says otherwise, each
test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1 and this mod, plus the
instrument and the mods it names.

**Existing saves: checked, no problem — a landed craft goes through one more draw, always the same one.** A
craft saved without this mod comes back once on the corrected ground; saved again with it, on the Moon in
Real Solar System, the workaround that moves a landed craft back onto the ground never had to move it, in
36 loads.

**→ Full chapter: [Existing saves](existing-saves.md)**

**This mod's safeguard: checked on the four stock worlds and five bodies of Real Solar System — it never
refused a correction.** This mod refuses any correction larger than sixteen float steps, a limit that grows
with the body. The largest correction was 3.9 steps on Gilly, 4.4 on Earth: a quarter of the limit.

**→ Full chapter: [This mod's safeguard](safeguard.md)**

**Principia, the bodies it moves and turns: checked, no problem.**
[Principia](https://github.com/mockingbirdnest/Principia) replaces KSP's orbital mechanics, and takes over
the rotation and the position of every body: the two values this mod places the terrain from. With it
installed, a landed craft comes back from a load, and the ground is built under a rocket in flight, as
without it.

**→ Full chapter: [Principia: the bodies it moves and turns](non-regression/principia/the-bodies-it-moves-and-turns.md)**

## Work in progress

What is still to check, for mods nothing has been checked with yet: why it is a question, what is already
known, and the test planned to answer it.

**Tilt'Em: planned, read in the source.** [Tilt'Em Continued](https://github.com/ballisticfox/TiltEm-Continued)
gives the planets an axial tilt by rewriting the rotation of every body: the ground of a tilted body, when a
craft comes down to where the world turns with it.

**→ Full chapter: [Tilt'Em: a tilted body](work-in-progress/tilt-em/a-tilted-body.md)**

**KAS: planned, read in the source.** Kerbal Attachment System holds parts to the ground and docks crafts
with joints of its own; read in its code, its harpoon is pinned to the world, not to the terrain, and none
of its links should reach what this mod corrects.

**→ Full chapter: [KAS: a part attached to the ground](work-in-progress/kas/a-part-attached-to-the-ground.md)**
