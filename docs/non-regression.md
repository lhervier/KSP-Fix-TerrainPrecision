# Non-regression tests

Part of [Terrain Precision Fix](../README.md): what works without this mod still works with it.

[The checks of each fix](../README.md#the-culprit-a-float-at-planet-scale-in-a-frame-that-moves) show what this mod fixes. These tests check
the other side, one mod at a time, stock first: what this mod could break, played in game with it, and
compared with the game without it where the two have to be told apart. Only what has been checked is
here; what is still to check is in [Work in progress](work-in-progress.md), and what this mod does make
worse, with its solution, in [Limits and solutions](limits-and-solutions.md).

Unless a page says otherwise, each test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1 and this mod, plus the instrument and the mods it names. Each mod has a page of
its own, and each test a page under it.

## Stock

Existing saves go through one more draw of the ground, always the same one. Over loadings, an orbit and a
return to the space centre, the KSC keeps every building registered, and a craft launched from the VAB or
the SPH stands on the launchpad or the runway. Through every scene change, the KSC comes back to the same
place, and through days of time warp it stays put, its lights following day and night. An anchored base
stays where it was placed on a runway, of the KSC or of a launch site of Making History. Every scatter
holder goes back to its pool.

**→ Full chapter: [Non-regression tests: stock](non-regression/stock.md)**

## KSP Community Fixes

None of its patches places the terrain, and every measurement on these pages was taken with it installed.

**→ Full chapter: [Non-regression tests: KSP Community Fixes](non-regression/ksp-community-fixes.md)**

## Kopernicus

The ground is as stable under Kopernicus as without it, and the KSC it moves to Cape Canaveral for Real
Solar System is placed where it puts it. The rocks it can give a collider are hit where they are drawn.

**→ Full chapter: [Non-regression tests: Kopernicus](non-regression/kopernicus.md)**

## Real Solar System

Its two workarounds for this defect, one for a landed craft and one for the runway, have nothing left to
correct with this mod, and its CommNet ground stations keep relaying.

**→ Full chapter: [Non-regression tests: Real Solar System](non-regression/real-solar-system.md)**

## Kerbal Konstructs

A CommNet ground station it opens in flight, beside a craft, finds its body while its static is out of
its sphere, and relays.

**→ Full chapter: [Non-regression tests: Kerbal Konstructs](non-regression/kerbal-konstructs.md)**

## Deferred

It draws the ground wherever this mod places it, and the craft and the ground come back as they do
without it.

**→ Full chapter: [Non-regression tests: Deferred](non-regression/deferred.md)**

## Principia

It turns and moves the bodies itself, and the craft and the ground come back as they do without it, after
a load and in flight.

**→ Full chapter: [Non-regression tests: Principia](non-regression/principia.md)**

## Kerbal Planetary Base Systems

One of the most popular part mods, built for bases on the ground. Its plugin touches nothing of the
ground, and its parts are held up by stock modules; a base reloaded on a slope jumps without this mod,
and stays within a millimetre with it.

**→ Full chapter: [Non-regression tests: Kerbal Planetary Base Systems](non-regression/kerbal-planetary-base-systems.md)**

## Parallax

It draws the terrain with shaders of its own and sets rocks and trees on the ground this mod places. Its
objects follow the ground, a craft resting on one of its rocks stays on it, and a craft on its ground comes
back as it does without it, after a load and after a trip out of range.

**→ Full chapter: [Non-regression tests: Parallax](non-regression/parallax.md)**
