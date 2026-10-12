# Non-regression tests: Kopernicus

Part of [Terrain Precision Fix](../../README.md), one mod of [Non-regression tests](../non-regression.md): what works without this mod still works with it, with Kopernicus.

Unless a page says otherwise, each test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1 and this mod, plus the instrument and the mods it names. Each test has a page of
its own.

Most planet packs go through [Kopernicus](https://github.com/Kopernicus/Kopernicus), and it touches
several things this mod deals with. The bodies here are ones Kopernicus reconfigures: Kerbin itself, and
Earth in Real Solar System, which is Kerbin given another radius, another terrain and another place for
the KSC. Its flag fix needs a patch of this mod: it is in
[Limits and solutions](../limits-and-solutions.md#kopernicus).

## The terrain

**Checked, no problem.** Kopernicus changes the terrain of existing bodies, so this mod has to still find
the ground where it expects it. Over six loads on Kerbin, a terrain quad spreads over 116.0 mm (median)
without this mod and 0.079 mm with it.

**→ Full chapter: [Kopernicus: the terrain](kopernicus/the-terrain.md)**

## Scatter with colliders

**Checked — the terrain fix alone narrows a stock gap a little; the scatter fix, on by default, closes it.**
Kopernicus can give rocks a collider, which stock places apart from the rock drawn: over six loads, −71.3 to
+59.9 mm without this mod, −58.6 to +54.5 mm with its scatter fix off, −0.022 to +0.022 mm with this mod.

**→ Full chapter: [Kopernicus: scatter with colliders](kopernicus/scatter-with-colliders.md)**

## The KSC moved to Cape Canaveral

**Checked, no problem.** Kopernicus moves the KSC for Real Solar System, so this mod has to handle it at
its new place. It takes the KSC out of its sphere there and puts it back, and the launchpad comes back
to the same place through every way of leaving a flight, within 0.2 mm.

**→ Full chapter: [Kopernicus: the KSC moved by Real Solar System](kopernicus/the-ksc-moved-by-real-solar-system.md)**
