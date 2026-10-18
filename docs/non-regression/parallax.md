# Non-regression tests: Parallax

Part of [Terrain Precision Fix](../../README.md), one mod of [Non-regression tests](../non-regression.md): what works without this mod still works with it, with Parallax.

Unless a page says otherwise, each test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1, [Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) 1.0.5 with
its stock textures and what it requires (Kopernicus, ModularFlightIntegrator, KSPTextureLoader and
KSPBurst), Deferred, and this mod, plus the instruments and the mods each page names. Each test has a page
of its own.

Parallax draws the terrain with shaders of its own and adds a scatter of its own objects, rocks and trees
a craft can hit, standing right on the ground this mod places.

## What it does with the ground

**Read in the source.** Parallax draws the ground this mod places, and hangs its objects from the terrain
quads, so they follow it. Up to 1.0.4, its rocks turned under a craft at every load; Parallax Continued
1.0.5 fixes that with a change of ours.

**→ Full chapter: [Parallax: what it does with the ground](parallax/what-it-does-with-the-ground.md)**

## A craft on one of its rocks

**Checked on the Mun.** A capsule resting on one of its rocks stays on it, load after load, an hour of time
warp before each, and after a restart of KSP: within 30 mm without this mod, within 3 mm with it.

**→ Full chapter: [Parallax: a craft on one of its rocks](parallax/a-craft-on-one-of-its-rocks.md)**

## Loading a craft on its ground

**Checked on Kerbin, the Mun and Minmus.** A capsule loaded six times comes back as it does without
Parallax: on Kerbin, within 73 mm without this mod and within 0.010 mm with it.

**→ Full chapter: [Parallax: loading a craft on its ground](parallax/loading-a-craft-on-its-ground.md)**

## Coming back to a craft on its ground

**Checked in the tundra of Kerbin, clear of its objects with a collider.** A capsule left parked while a
rover drives away and back comes back within 31 mm without this mod, and within 0.12 mm with it.

**→ Full chapter: [Parallax: coming back to a craft on its ground](parallax/coming-back-to-a-craft-on-its-ground.md)**

## Its scatter grows the same at every load

**Checked on Eve.** Parallax decides where its objects grow from the mesh of the terrain, which stock
builds a little differently at every load: a plant showed at 3 loads out of 12 without this mod, and at
none with it.

**→ Full chapter: [Parallax: its scatter grows the same at every load](parallax/its-scatter-grows-the-same-at-every-load.md)**
