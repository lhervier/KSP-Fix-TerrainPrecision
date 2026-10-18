# BurstPQS: its memory

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [BurstPQS](../../work-in-progress/burst-pqs.md).

**Status: to dig — read in its code, not yet seen in the game.** Reading the code of BurstPQS 1.0.27 shows
two places where memory is released twice or never, and a third where maps may stay loaded after a body is
left. None has been seen in the game yet. Each is noted below with what it could do in the game and how to
look for it; once seen, each will be reported to BurstPQS on its own.

## A pinned handle released twice

The Burst versions of `PQSMod_VertexSimplexColorRGB` and `PQSMod_VertexSimplexMultiChromatic` pin the noise
tables of the mod for each quad, in a `using` declaration in `OnQuadPreBuild`, and hand the pinned table to
the build job:

```csharp
using var simplex = new BurstSimplex(mod.simplex);

jobSet.Add(new BuildJob { simplex = simplex, /* ... */ });
```

`BurstSimplex.Dispose` releases the handle. It runs once as `OnQuadPreBuild` returns, at the end of the
`using` scope, then again when the build job is disposed, since the job's `Dispose` disposes its copy of the
same `BurstSimplex`. This is not a leak: the same handle is released twice, at every quad built.

*What it could do in the game:* the second release may unpin something else that has been given the same
handle in between, and a later quad would read memory that was freed. Only on bodies whose terrain uses one
of these two mods.

*How to see it:* nothing a player sees by hand; the code above shows it alone.

## The Burst versions of the terrain mods, dropped at each set-up

`BatchPQS.PostSetupMods` runs each time the game sets up the terrain mods of a body (`PQS.SetupMods`). It
builds the Burst version of every terrain mod of that body anew, and drops the previous ones without calling
their `Dispose`. Some of them hold memory allocated once at set-up and freed only by `Dispose`: the land
classes of `PQSLandControl`, `PQSMod_HeightColorMap` and `PQSMod_VertexPlanet`, and the noise tables they and
others pin.

BurstPQS writes a line in `KSP.log` at each of these set-ups:
`[BurstPQS] BatchPQS enabled for surface <body>`. On KSP with KSP Community Fixes, BurstPQS and what it
requires, the line comes once for every body as the game starts (a few times for Kerbin), then twice for Kerbin and once for
`KerbinOcean` at each arrival at the space centre and at each load of a flight around Kerbin, and twice for
the Mun at each load of a flight around the Mun.

*What it could do in the game:* memory that grows a little at each scene change and each load of a flight,
by what the dropped Burst versions held. From the code, a small amount for each set-up; it would show only
over a long session.

*How to see it:* load the same flight many times (quick save, then quick load), with BurstPQS and without,
and compare the memory taken by KSP in the Windows Task Manager after the same number of loads. Not tried
yet; the amount for each set-up may be too small to stand out from what KSP itself takes and gives back at a
load.

## Maps loaded on demand that may stay loaded

Kopernicus loads the maps of a body on demand: its `PQSMod_OnDemandHandler` loads them when the body's terrain
is in use, unloads them a while after it no longer is, and says so in `KSP.log`: `[OD] Loading <body>`,
`[OD] Unloading <body>`, and for each map `[OD] ---> Map <name> enabling self` and
`[OD] <--- Map <name> disabling self`. The handler also learns that a body's map is read when the height of a
vertex is computed (`OnVertexBuildHeight`). The Burst version of the handler does not pass that call on, and
the Burst version of a height or colour map loads its map by itself when the map is not loaded. If that
happened while the handler had unloaded the body's maps, the handler would not know the map was loaded again,
and would not unload it.

Reading further, no case has been found yet where BurstPQS builds a quad of a body whose handler has unloaded
its maps: the handler makes the maps ready as the body's terrain starts and each time it becomes active,
before any quad is built. This one may never happen.

*What it could do in the game:* the maps of a body staying in memory after the body is left, until the next
visit. Not a growth: at most once for each body. On stock KSP, the only map Kopernicus loads on demand is its
KSC mask, shared by every body. On Real Solar System, the height map files of RSS-Textures weigh 2 MB for
most bodies and 8 MB for Venus, with their colour maps besides. The Earth (16 MB), the Moon and Mars (4 MB each)
are not concerned with Real Solar System 20.1.3, where BurstPQS leaves them to stock; they will be with the
next Real Solar System, which reads their height maps through Kopernicus and lets BurstPQS build them (see
[the bodies it leaves to stock](the-bodies-it-leaves-to-stock.md)).

*How to see it:* on Real Solar System, visit a body BurstPQS builds, Venus for instance, leave it, and read
`KSP.log`. After `[OD] Unloading Venus`, every map of Venus that said `enabling self` should say
`disabling self`. A map that says `enabling self` with no `[OD] Loading Venus` before it was loaded by
BurstPQS on its own.

## To do

- Find the stock bodies whose terrain uses `PQSMod_VertexSimplexColorRGB` or
  `PQSMod_VertexSimplexMultiChromatic`.
- Measure what each set-up of a body leaves allocated, then try the Task Manager procedure over many loads.
- Look for a case where a quad is built while the handler has unloaded the body's maps, then play the
  `KSP.log` procedure on Real Solar System.
- Report to BurstPQS what is seen, one point at a time.
