# The scatter

Part of [Terrain Precision Fix](../../README.md): the rocks, and around the KSC the grass and the trees,
that stock grows on the terrain. Where the rounding strikes them in the stock code, how this mod takes it
away, how that is checked, what keeps working, what it makes worse, and what is still to check.

> **Fix the ground, and the rocks, the grass and the trees no longer go up and down with it.** On stock,
> they are never placed quite on the ground, but they move with it: the ground and the scatter are drawn
> through the same rounding. Fix the ground alone, and the scatter keeps moving, at every load and every
> 500 m a craft drives, against a ground that no longer does.

> [!WARNING]
> **This fix is not a harmless one, and it can break other mods.** It moves the holders of the scatter
> away from where stock hangs them, and a mod that looks for them there would miss them. None of the mods
> read so far does; if one misbehaves around rocks, grass or trees, `fixScatter = false` turns this fix off
> ([Settings](../common/settings.md)).

## Why it matters

Mostly, it shows. Stock scatter has no collider, so nothing rests on it; but while a rover drives, every
500 m, the rocks and the grass around it jump against the ground. Not by much, a few centimetres at most,
but it can be seen, on a rock or a cactus close to the rover. Give the scatter colliders, as some mods do,
and a part or a kerbal resting on a rock can be moved too, and thrown — a small matter next to the ground
itself.

## The culprit

The scatter is built from the vertices of its quad, but hangs from a *holder* that stays under the body, at
the same 600 km vector in a float. The quad is drawn where its position says, the holder where its matrix
says, and the two need not round the same way. The terrain fix makes it worse: the ground stops moving, the
holders do not, at every load and at every move of the world while you drive. Stock scatter has no
collider, so this is visual — unless a mod gives it one.

The rounding itself, shared with the ground and the statics, is told once in
[The culprit: a float at planet scale](../common/the-culprit.md).

**→ Full chapter: [The culprit: the scatter](the-culprit.md)**

## The fix

Two Harmony patches hang each holder from its own quad, at no offset, and hang it back in its pool when the
quad goes: the stock scatter is then drawn with the very matrix of the ground it was built on. It is on by
default, with the terrain fix it completes. It moves stock objects other mods may look for: if one of them
misbehaves around rocks, grass or trees, one line of the settings file turns it off, `fixScatter = false`
([Settings](../common/settings.md)).

**→ Full chapter: [The fix: the scatter](the-fix.md)**

## Checked

Each situation is measured three times: on stock, with this mod and its scatter fix turned off, and with
this mod as installed, in an install with
[KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes): KSP 1.12.5 with Harmony,
ModuleManager, KSP Community Fixes 1.41.1, [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter),
which reads the scatter against the ground, and [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer),
which plays the protocols.

- **Loading the same save**, twelve times on Kerbin and on the Mun: half of the points measured on the
  scatter come back more than 61 mm apart against the ground on Kerbin, 178 mm with this mod and its scatter
  fix turned off; with this mod as installed, none more than 0.132 mm.

  **→ Full chapter: [Checking the scatter: loading the same save](checking/loading.md)**

- **Driving on while the world moves**, every 500 m a rover drives on Kerbin: on stock, the grass jumps with
  the ground, within 0.13 mm of it; with this mod and its scatter fix turned off, the ground holds and the
  grass jumps against it, by up to 54 mm; with this mod as installed, nothing jumps, within 0.18 mm. Filmed
  on a cactus, too.

  **→ Full chapter: [Checking the scatter: driving on while the world moves](checking/driving.md)**

- **In flight**, a pod in orbit 5 km over the Mun, read every two minutes until it crashes into the relief:
  on stock, no holder of the scatter is drawn on its quad, by up to 21.9 mm; with this mod, every holder is
  drawn exactly on its quad, along the whole flight.

  **→ Full chapter: [Checking the scatter: in flight](checking/flight.md)**

**This is also a proof that the culprit is the right one.** The scatter fix changes the transform a holder
hangs from, and nothing about the objects in it, and it removes the holders' offset and nothing else about
where the objects are drawn.

The saves, the scripts and the readings of every session are in
[the runs of the scatter](../../diag/scatter/README.md).

## Non-regression tests

What works without this mod still works with it, one mod at a time: played in game with this mod, and
compared with the game without it where the two have to be told apart. Unless a page says otherwise, each
test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1 and this mod, plus
the instrument and the mods it names. Two tests cover every fix at once, and are told in
[what the fixes share](../common/README.md): [existing saves](../common/existing-saves.md) and
[this mod's safeguard](../common/safeguard.md).

### Stock

**The scatter holders: checked with the scatter fix on, no problem — no holder lost.** The scatter fix takes
each holder out of its pool's container while its quad is in use. Over a flight over the Mun and across
scene switches, every holder went back to its pool, none was left on a quad, and the pools counted as in
stock.

**→ Full chapter: [The scatter holders](non-regression/stock/the-scatter-holders.md)**

### Kopernicus

**Scatter with colliders: checked — the terrain fix alone narrows a stock gap a little; the scatter fix, on
by default, closes it.** Kopernicus can give rocks a collider, which stock places apart from the rock drawn:
over six loads, −71.3 to +59.9 mm without this mod, −58.6 to +54.5 mm with its scatter fix off, −0.022 to
+0.022 mm with this mod.

**→ Full chapter: [Kopernicus: scatter with colliders](non-regression/kopernicus/scatter-with-colliders.md)**

### Parallax

[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) adds a scatter of its own objects,
rocks and trees a craft can hit, standing right on the ground this mod places, and hangs them from the
terrain quads. What it does with the ground is in [the ground](../ground/README.md#parallax).

**A craft on one of its rocks: checked on the Mun.** A capsule resting on one of its rocks stays on it, load
after load, an hour of time warp before each, and after a restart of KSP: within 30 mm without this mod,
within 3 mm with it.

**→ Full chapter: [Parallax: a craft on one of its rocks](non-regression/parallax/a-craft-on-one-of-its-rocks.md)**

**Its scatter grows the same at every load: checked on Eve.** Parallax decides where its objects grow from
the mesh of the terrain, which stock builds a little differently at every load: a plant showed at 3 loads
out of 12 without this mod, and at none with it.

**→ Full chapter: [Parallax: its scatter grows the same at every load](non-regression/parallax/its-scatter-grows-the-same-at-every-load.md)**

## Limits and solutions

What this mod makes worse, or would break without a patch of its own, with the solution to each.

### Stock

**The scatter: a stock defect the terrain fix widens on Kerbin, and a jump it adds while you drive, visual
only; the scatter fix closes both, on by default.** Stock draws terrain scatter a few centimetres off the
ground, differently at every load: 61 mm apart on Kerbin on stock, 178 mm with the terrain fix alone. And
while you drive, the scatter now jumps against the ground every 500 m, by up to 54 mm, where on stock it
moves with the ground.

**→ Full chapter: [The scatter](limits/stock/the-scatter.md)**

### BurstPQS

**The scatter: a problem this mod fixes, the scatter fix on by default.**
[BurstPQS](https://github.com/Phantomical/BurstPQS) places the ground in double, but lets stock spawn the
scatter, and stock still places each scatter holder through the sphere, rounded at planet scale. Without a
support of its own, the scatter fix would miss the holders built as a scene opens: it hangs every holder
there.

**→ Full chapter: [BurstPQS: the scatter](limits/burst-pqs/the-scatter.md)**

## Work in progress

What is still to check: why it is a question, what is already known, and the test planned to answer it.
Once played, a point moves to [Non-regression tests](#non-regression-tests) if nothing is worse, or to
[Limits and solutions](#limits-and-solutions) if something is.

### Stock

**Scene changes and time warp, with Jeb on the scatter: planned.** Both are checked on the statics of the
KSC; they are still to play with a kerbal standing on a rock.

**→ Full chapter: [Scene changes and time warp, with Jeb on the scatter](work-in-progress/stock/scene-changes-and-time-warp.md)**

**The scatter fix without the terrain fix: planned.** The scatter fix, on by default, stays on with the
terrain fix turned off, but has only been measured with it.

**→ Full chapter: [The scatter fix without the terrain fix](work-in-progress/stock/the-scatter-fix-without-the-terrain-fix.md)**

### Other mods

**Mods that look for a scatter holder under its sphere: planned.** With the scatter fix on, as by default,
any mod that looks for a scatter holder where stock puts it would miss it. Stock, KSP Community Fixes,
Kopernicus, Parallax, TUFX and Kerbal Planetary Base Systems are read; the others are not.

**→ Full chapter: [Mods that look for a scatter holder under its sphere](work-in-progress/other-mods/mods-that-look-for-a-scatter-holder-under-its-sphere.md)**
