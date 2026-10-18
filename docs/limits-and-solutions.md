# Limits and solutions

Part of [Terrain Precision Fix](../README.md): what this mod makes worse, or would break without a patch
of its own, and the solution to each.

[Non-regression tests](non-regression.md) list what keeps working with this mod. This page lists the
rest: what has been checked and found worse, in stock or in another mod, one mod at a time. Each limit
says how much worse, and its solution: a patch this mod applies to another mod, a fix of its own, or none
yet. What is still to check is in [Work in progress](work-in-progress.md).

Unless a page says otherwise, each limit is measured in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1 and this mod, plus the instrument and the mods it names.

**The statics fix is the riskiest of the fixes on by default.** To place a static in double, this mod takes
it out
of its terrain sphere ([The fix: the statics](the-fix-statics.md)). That changes the hierarchy of Unity
objects, and any mod that looks for a static where stock puts it — among the children of a body's
terrain sphere — or reads its `localPosition` as a position relative to the centre of the body, finds it
missing, or somewhere else. What limits the exposure: a static is only out of its sphere in flight, while
a craft is near it, and it is put back before every scene change. Kopernicus and Kerbal Konstructs each
look for a static under its sphere once in flight, and this mod patches both, below. Each patch stands
for a small change in that mod, given as a diff to apply to its source: with it, the patch has nothing
left to do.

## Stock

The terrain fix widens two stock defects, both visual. The scatter is drawn further off the ground, and
jumps against it while you drive: the scatter fix, on by default, closes both. The crack between
subdivision levels widens, with no solution yet.

**→ Full chapter: [Limits and solutions: stock](limits-and-solutions/stock.md)**

## Kopernicus

Its flag fix looks the KSC up under its sphere, and would throw in flight near it: a patch of this mod,
on by default, keeps it from running there.

**→ Full chapter: [Limits and solutions: Kopernicus](limits-and-solutions/kopernicus.md)**

## Kerbal Konstructs

Its group editor, in flight, would send a group moved with its gizmo elsewhere on its body, and save it
there: a patch of this mod, on by default, prevents it.

**→ Full chapter: [Limits and solutions: Kerbal Konstructs](limits-and-solutions/kerbal-konstructs.md)**

## BurstPQS

It holds the ground still on the bodies it builds, but not the statics nor the scatter, which this mod still
corrects. This mod supports it by itself: its terrain fix steps back on the bodies BurstPQS builds, and takes
over on the Earth, the Moon and Mars, which the latest Real Solar System (20.1.3) leaves to stock; its
scatter fix hangs every holder there.

**→ Full chapter: [Limits and solutions: BurstPQS](limits-and-solutions/burst-pqs.md)**
