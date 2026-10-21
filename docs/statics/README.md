# The statics

Part of [Terrain Precision Fix](../../README.md): the runway, the launchpad and the buildings of the KSC,
the launch sites of the Making History expansion, and the bases a mod such as Kerbal Konstructs plants
anywhere on a body. Where the rounding strikes them in the stock code, how this mod takes it away, how that
is checked, what keeps working, what it makes worse, and what is still to check.

The rounding itself, shared with the ground and the scatter, is told once in
[The culprit: a float at planet scale](../common/the-culprit.md).

## The culprit

`PQSCity` and `PQSCity2` place the statics the same way as the ground, a 600 km vector in a float
`Transform` hanging from the body, through the same frame. Unlike the quads a craft stands on, stock gives
them no place outside the body where a precise position would be kept.

**→ Full chapter: [The culprit: the statics](the-culprit.md)**

## The fix

A static cannot hold a precise position under its sphere, so it is taken out of it in flight, while a craft
is near it, and placed in double in the same frame. It follows its body, and it goes back exactly where
stock left it before every scene change, and whenever stock code that expects it there runs. A launch pad
of Making History is also taken out for the moment it measures the ground to set itself on it. It is on by
default; `fixStatics = false` turns it off ([Settings](../common/settings.md)).

**The statics fix is the riskiest of the fixes on by default.** It changes the hierarchy of Unity objects,
and any mod that looks for a static where stock puts it — among the children of a body's terrain sphere —
or reads its `localPosition` as a position relative to the centre of the body, finds it missing, or
somewhere else. What limits the exposure: a static is only out of its sphere in flight, while a craft is
near it, and it is put back before every scene change.

**→ Full chapter: [The fix: the statics](the-fix.md)**

## Checked

Each situation is measured twice, without this mod and with it, in an install with
[KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes): KSP 1.12.5 with Harmony,
ModuleManager, KSP Community Fixes 1.41.1, the instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which plays the protocols — and this mod, or
not. In each summary, the first figure is without this mod, the second with it.

- **Loading the same save**, six times, two identical craft, one on a runway and one on the ground beside
  it. On the runway of the KSC, its deck comes back over 116.5 mm, and within 0.177 mm with this mod. The
  step between the deck and the grass beside it changes by up to 38.3 mm: the runway draws a rounding of
  its own, apart from the ground. On the Mun, a runway placed by Kerbal Konstructs does the same, over
  17.7 mm, and holds within 0.015 mm with this mod from the second loading on.

  **→ Full chapter: [Checking the statics: loading the same save](checking/loading.md)**

- **Driving on while the world moves**, by the runway of the KSC: every 500 m, its deck moves with the
  grass, by up to 54.8 mm on Kerbin and 231.8 mm on Earth. With the terrain fix alone, the grass holds and
  the deck still moves, by up to 41.6 mm; with this mod as installed, neither does, within 0.07 mm.

  **→ Full chapter: [Checking the statics: driving on while the world moves](checking/driving.md)**

- **Launching from a launch pad of Making History**, the Desert Launch Site, in six sessions of the game:
  the deck the craft stands on spreads over 592.8 mm, and 0.001 mm with this mod; its feet stand on the
  ground either way.

  **→ Full chapter: [Checking the culprit: launching from a launch pad of Making History](checking/launch-pad.md)**

The statics are not measured in flight. The saves, the scripts and the `KSP.log` of every session, both
ways, are in [the runs of the statics](../../diag/statics/README.md).

## Non-regression tests

What works without this mod still works with it, one mod at a time: played in game with this mod, and
compared with the game without it where the two have to be told apart. Unless a page says otherwise, each
test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1 and this mod, plus
the instrument and the mods it names. Two tests cover every fix at once, and are told in
[what the fixes share](../common/README.md): [existing saves](../common/existing-saves.md) and
[this mod's safeguard](../common/safeguard.md).

### Stock

**Scene changes: checked on Kerbin and on Earth in Real Solar System.** This mod has to put the KSC back
before every scene change. Through every way of leaving a flight and coming back, a trip to another body
included, the launchpad stays within 0.14 mm, against up to 599 mm without this mod. A craft launched from
the VAB stands on the launchpad, one from the SPH on the runway, and every building opens.

**→ Full chapter: [Scene changes](non-regression/stock/scene-changes.md)**

**Time warp: checked on Kerbin and on the Mun.** A craft on the runway through three days at 100 000×: the
runway stays within 0.12 mm under it. A craft passing 3 km over a static of the Mun in time warp on rails:
a capsule standing on the static reads it within 0.008 mm, against 10.7 mm without this mod.

**→ Full chapter: [Time warp](non-regression/stock/time-warp.md)**

**Destroyed buildings: checked on Kerbin.** KSP finds a destructible building by its path below the KSC,
which this mod moves in flight. The VAB, brought down by a heavy craft dropped onto it while the KSC is out
of its sphere, collapses, shows as destroyed at the space centre, stays in ruins through the next flights,
and stands again once repaired, as without this mod; the launchpad and the runway stay within 0.22 mm,
against 71 and 87 mm without it.

**→ Full chapter: [Destroyed buildings](non-regression/stock/destroyed-buildings.md)**

**Facility levels: checked on Kerbin.** Each level of a facility is a model of its own, built below the
KSC. At each of their three levels, a craft stands on the launchpad and on the runway of that level, as
without this mod, and stays within 0.24 mm through its arrivals, against up to 174 mm without it.

**→ Full chapter: [Facility levels](non-regression/stock/facility-levels.md)**

**The lights of the KSC: checked on Kerbin.** A component switches the lights of the KSC with day and night,
after finding its body among its parents, which this mod lends back to it. In flight, the KSC out of its
sphere, the runway lights and the windows come on at night and go off by day, as without this mod.

**→ Full chapter: [The lights of the KSC](non-regression/stock/the-lights-of-the-ksc.md)**

**The map view: nothing to test, read in the code.** While the map is open, the markers of the launch sites
follow their statics wherever this mod places them.

**→ Full chapter: [The map view](non-regression/stock/the-map-view.md)**

**A launch pad placed by a mission: impossible to reproduce.** A mission of Making History can place a
launch pad of its own, which stock looks for under its sphere once. Read in the code, that never happens in
flight, where this mod moves statics; no way was found to launch from such a pad on stock.

**→ Full chapter: [A launch pad placed by a mission](non-regression/stock/a-launch-pad-placed-by-a-mission.md)**

**A static turning with its body: cannot happen on stock, in Real Solar System or with Outer Planets Mod.**
This mod has to turn a static out of its sphere when KSP turns the body. Measured body by body, no body
turns lower than 100 km, far above any craft near a static this mod has moved.

**→ Full chapter: [A static turning with its body](non-regression/stock/a-static-turning-with-its-body.md)**

### Kopernicus

**The KSC moved to Cape Canaveral: checked, no problem.** Kopernicus moves the KSC for Real Solar System, so
this mod has to handle it at its new place. It takes the KSC out of its sphere there and puts it back, and
the launchpad comes back to the same place through every way of leaving a flight, within 0.2 mm.

**→ Full chapter: [Kopernicus: the KSC moved by Real Solar System](non-regression/kopernicus/the-ksc-moved-by-real-solar-system.md)**

### Real Solar System

**The runway fix: checked on Earth — with this mod, the runway is where it is drawn, with no step.** Real
Solar System turns off the colliders of the runway's sections and holds the floating origin on it. Built
without that fix, with this mod, the runway stood within 0.3 mm over thirty loads, and a move of the origin
moved nothing. As released, the runway fix leaves the runway at another height at each load, 381 mm over
six, and the step still drawn between its sections: with this mod, 0.3 mm, and the sections drawn flush.

**→ Full chapter: [Real Solar System: the runway fix](non-regression/real-solar-system/the-runway-fix.md)**

**A CommNet ground station: checked on Earth, no problem.** Real Solar System adds 63 CommNet ground
stations, statics this mod takes out of their sphere. Driven toward the one of Kourou, a rover sees it
taken out on the way, and CommNet keeps linking the rover to it.

**→ Full chapter: [Real Solar System: a CommNet ground station](non-regression/real-solar-system/a-commnet-ground-station.md)**

### Kerbal Konstructs

**A ground station opened in flight: checked, no problem.** A CommNet ground station Kerbal Konstructs opens
in flight, beside a craft, finds its body while its static is out of its sphere, and relays.

**→ Full chapter: [Kerbal Konstructs: a ground station opened in flight](non-regression/kerbal-konstructs/a-ground-station-opened-in-flight.md)**

### BurstPQS

**The campaigns: checked, nothing worse with this mod.** [BurstPQS](https://github.com/Phantomical/BurstPQS)
places the ground in double on the bodies it builds, and has no code for `PQSCity` or `PQSCity2`: the statics
still move without this mod, and now against a ground that holds; with it, they hold.

**→ Full chapter: [BurstPQS: the campaigns, the statics](non-regression/burst-pqs/the-campaigns.md)**

## Limits and solutions

What this mod makes worse, or would break without a patch of its own, with the solution to each. Kopernicus
and Kerbal Konstructs each look for a static under its sphere once in flight, where the statics fix no
longer leaves it. Each patch, on by default, stands for a small change these mods could make themselves,
given as a diff to apply to their source: with it, the patch has nothing left to do.

### Kopernicus

**The flag fix: a problem this mod patches, the patch on by default.** Kopernicus' fix for the flags of the
KSC looks the KSC up under its sphere. In flight near it, where this mod moves the KSC and keeps the flags
steady itself, that fix would throw; the patch keeps it from running there. Without the patch, nothing goes
wrong in the game: it only spares an error in the log whose stack trace names Kopernicus, where this mod is
the cause — a bug its maintainers would be asked about for nothing.

**→ Full chapter: [Kopernicus: the flag fix](limits/kopernicus/the-flag-fix.md)**

### Kerbal Konstructs

**The group editor: a problem this mod patches, the patch on by default.** This patch is indispensable, and
the most serious problem this mod has met so far. Moving a group with the gizmo of its group editor, in
flight, Kerbal Konstructs reads the group's position from where stock hangs it: without the patch, the group
would be sent elsewhere on its body, and saved there.

**→ Full chapter: [Kerbal Konstructs: the group editor](limits/kerbal-konstructs/the-group-editor.md)**

## Work in progress

What is still to check: why it is a question, what is already known, and the test planned to answer it.
Once played, a point moves to [Non-regression tests](#non-regression-tests) if nothing is worse, or to
[Limits and solutions](#limits-and-solutions) if something is.

### Stock

**Scene changes, with a capsule on the runway: planned.** Every way of leaving a flight and coming back is
checked on the launchpad; it is still to play with a capsule on the runway.

**→ Full chapter: [Scene changes, with a capsule on the runway](work-in-progress/stock/scene-changes.md)**

**A mission spawning a craft: planned.** A mission of Making History spawns a craft on a spawn point of the
KSC, as a launch does.

**→ Full chapter: [A mission spawning a craft](work-in-progress/stock/a-mission-spawning-a-craft.md)**

**The other stock statics: planned.** The KSC 2, the Island Airfield, the pyramids, the monoliths and the
easter eggs are placed like the KSC, and taken out of their sphere the same way; some monoliths are placed
at random, from the seed of the game.

**→ Full chapter: [The other stock statics](work-in-progress/stock/the-other-stock-statics.md)**

### Kerbal Konstructs

Its statics carry the same defect as the KSC's, and this mod corrects them: measured on a runway it placed
on the Mun, in [Checking the statics: loading the same save](checking/loading.md).

**A section of the runway at the first loading: planned — seen, not explained.** At the first loading of a
session, a section of the runway 21.3 mm above the deck is still active under the craft; not a rounding,
and this mod does not touch it.

**→ Full chapter: [Kerbal Konstructs: a section of the runway at the first loading](work-in-progress/kerbal-konstructs/a-section-of-the-runway-at-the-first-loading.md)**

**The rest of the group editor: planned.** Turning, creating, copying and deleting a group in flight, near a
craft, then loading the save again.

**→ Full chapter: [Kerbal Konstructs: the rest of the group editor](work-in-progress/kerbal-konstructs/the-rest-of-the-group-editor.md)**

**A launch from its launch sites: planned.** A craft launched from a launch site of Kerbal Konstructs is
placed on a static this mod moves in flight.

**→ Full chapter: [Kerbal Konstructs: a launch from its launch sites](work-in-progress/kerbal-konstructs/a-launch-from-its-launch-sites.md)**

### Promised Worlds

**Its monuments and its frozen lake: planned — read in its configs, not played.** Promised Worlds places
them through Kopernicus as `PQSCity2`, like the launch sites of Making History, so this mod takes them out
of their sphere in flight.

**→ Full chapter: [Promised Worlds: its monuments and its frozen lake](work-in-progress/promised-worlds/its-monuments-and-its-frozen-lake.md)**

### Other mods

**Mods that look for a static under its sphere: planned.** Any mod that looks for a static where stock puts
it would miss it in flight, near a craft. Kopernicus and Kerbal Konstructs are read and patched, Kerbal
Planetary Base Systems read with nothing to patch; the others are not read.

**→ Full chapter: [Mods that look for a static under its sphere](work-in-progress/other-mods/mods-that-look-for-a-static-under-its-sphere.md)**
