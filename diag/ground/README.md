# The runs: the ground

Part of [Terrain Precision Fix](../../README.md), [the ground](../../docs/ground/README.md): the saves, the scripts and the `KSP.log` of every session, without this mod and with it. The scripts are in [`automation/`](automation).

## The loading protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, both instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), without this mod and with it:
[the loading protocol](../../docs/ground/checking/loading-protocol.md), each save loaded six
times by its script, [`run-loading.py`](automation/run-loading.py). On Real Solar System, the same,
plus Real Solar System 20.1.3.0 and what it requires (Kopernicus 248, Modular Flight Integrator,
KSPTextureLoader, the RSS textures). Read in
[Checking the ground: loading the same save](../../docs/ground/checking/loading.md).

The saves, a capsule on a small flat fuel tank, made by
[Making the save](../../docs/ground/checking/making-the-save.md):

- [`reload-kerbin-2parts.sfs`](checking/loading/reload-kerbin-2parts.sfs) — on the
  levelled grass of the KSC, just south-west of the west end of the runway;
- [`reload-mune-2parts.sfs`](checking/loading/reload-mune-2parts.sfs) — on flat ground on
  the Mun;
- [`reload-minmus-2parts.sfs`](checking/loading/reload-minmus-2parts.sfs) — on the frozen
  flats of Minmus;
- [`reload-gilly-2parts.sfs`](checking/loading/reload-gilly-2parts.sfs) — on Gilly;
- [`reload-moon-rss-resave.sfs`](checking/loading/reload-moon-rss-resave.sfs) — on flat
  ground on the Moon, made with this mod; it loads only on Real Solar System;
- [`reload-earth-rss-resave.sfs`](checking/loading/reload-earth-rss-resave.sfs) — on the
  grass about 1.4 km west of the KSC on Earth, made with this mod; it loads only on Real Solar System.

Copy a save into the folder of a sandbox game and load it from that game.

- [`loading-stock.log`](checking/loading/loading-stock.log) and
  [`loading-fix.log`](checking/loading/loading-fix.log) — the `KSP.log` of the session the
  four saves of the stock worlds were played in, one after the other, together with a lone capsule on
  the same spots, a series no longer published; without this mod, then with it.
- [`loading-rss-stock.log`](checking/loading/loading-rss-stock.log) and
  [`loading-rss-fix.log`](checking/loading/loading-rss-fix.log) — the same on Real Solar
  System, the Moon then Earth.
- for each save, without this mod (`-stock`) and with it (`-fix`), what the script printed
  (`-script.txt`), and every line it recorded, in both instruments (`-lines.json`):
  - `kerbin-2parts`: [`reload-kerbin-2parts-stock-script.txt`](checking/loading/reload-kerbin-2parts-stock-script.txt),
    [`reload-kerbin-2parts-stock-lines.json`](checking/loading/reload-kerbin-2parts-stock-lines.json),
    [`reload-kerbin-2parts-fix-script.txt`](checking/loading/reload-kerbin-2parts-fix-script.txt) and
    [`reload-kerbin-2parts-fix-lines.json`](checking/loading/reload-kerbin-2parts-fix-lines.json);
  - `mune-2parts`: [`reload-mune-2parts-stock-script.txt`](checking/loading/reload-mune-2parts-stock-script.txt),
    [`reload-mune-2parts-stock-lines.json`](checking/loading/reload-mune-2parts-stock-lines.json),
    [`reload-mune-2parts-fix-script.txt`](checking/loading/reload-mune-2parts-fix-script.txt) and
    [`reload-mune-2parts-fix-lines.json`](checking/loading/reload-mune-2parts-fix-lines.json);
  - `minmus-2parts`: [`reload-minmus-2parts-stock-script.txt`](checking/loading/reload-minmus-2parts-stock-script.txt),
    [`reload-minmus-2parts-stock-lines.json`](checking/loading/reload-minmus-2parts-stock-lines.json),
    [`reload-minmus-2parts-fix-script.txt`](checking/loading/reload-minmus-2parts-fix-script.txt) and
    [`reload-minmus-2parts-fix-lines.json`](checking/loading/reload-minmus-2parts-fix-lines.json);
  - `gilly-2parts`: [`reload-gilly-2parts-stock-script.txt`](checking/loading/reload-gilly-2parts-stock-script.txt),
    [`reload-gilly-2parts-stock-lines.json`](checking/loading/reload-gilly-2parts-stock-lines.json),
    [`reload-gilly-2parts-fix-script.txt`](checking/loading/reload-gilly-2parts-fix-script.txt) and
    [`reload-gilly-2parts-fix-lines.json`](checking/loading/reload-gilly-2parts-fix-lines.json);
  - `moon-rss-resave`: [`reload-moon-rss-resave-stock-script.txt`](checking/loading/reload-moon-rss-resave-stock-script.txt),
    [`reload-moon-rss-resave-stock-lines.json`](checking/loading/reload-moon-rss-resave-stock-lines.json),
    [`reload-moon-rss-resave-fix-script.txt`](checking/loading/reload-moon-rss-resave-fix-script.txt) and
    [`reload-moon-rss-resave-fix-lines.json`](checking/loading/reload-moon-rss-resave-fix-lines.json);
  - `earth-rss-resave`: [`reload-earth-rss-resave-stock-script.txt`](checking/loading/reload-earth-rss-resave-stock-script.txt),
    [`reload-earth-rss-resave-stock-lines.json`](checking/loading/reload-earth-rss-resave-stock-lines.json),
    [`reload-earth-rss-resave-fix-script.txt`](checking/loading/reload-earth-rss-resave-fix-script.txt) and
    [`reload-earth-rss-resave-fix-lines.json`](checking/loading/reload-earth-rss-resave-fix-lines.json).

## The switching protocol

The install of [The loading protocol](#the-loading-protocol), on Kerbin: the six rounds of
[the switching protocol](../../docs/ground/checking/switching-protocol.md), played by its script,
[`run-switching.py`](automation/run-switching.py), on
[`switch-kerbin.sfs`](checking/switching/switch-kerbin.sfs), a capsule landed on the grass
west of the KSC and a rover 1.97 km to the south of it. Read in
[Switching to a craft far away](../../docs/ground/checking/switching.md).

- [`switching-stock.log`](checking/switching/switching-stock.log) — the `KSP.log` of the
  session without this mod; what the script printed in
  [`switching-stock-script.txt`](checking/switching/switching-stock-script.txt), and every
  line it recorded, in both instruments, in
  [`switching-stock-lines.json`](checking/switching/switching-stock-lines.json).
- [`switching-fix.log`](checking/switching/switching-fix.log) — the same with this mod; what
  the script printed in [`switching-fix-script.txt`](checking/switching/switching-fix-script.txt),
  and every line it recorded in [`switching-fix-lines.json`](checking/switching/switching-fix-lines.json).

## The approach protocol

The install of [The loading protocol](#the-loading-protocol), on Kerbin: the six round trips of
[the approach protocol](../../docs/ground/checking/approach-protocol.md), in a single flight,
played by its script, [`run-approach.py`](automation/run-approach.py), on
[`approach-kerbin.sfs`](checking/approach/approach-kerbin.sfs), a capsule landed on the
flat grass west of the KSC and a rover 26 m from it. Read in
[Coming back to a craft left parked](../../docs/ground/checking/approach.md).

- [`approach-stock.log`](checking/approach/approach-stock.log) — the `KSP.log` of the
  session without this mod; what the script printed in
  [`approach-stock-script.txt`](checking/approach/approach-stock-script.txt), and every line
  it recorded, in both instruments, in
  [`approach-stock-lines.json`](checking/approach/approach-stock-lines.json).
- [`approach-fix.log`](checking/approach/approach-fix.log) — the same with this mod; what
  the script printed in [`approach-fix-script.txt`](checking/approach/approach-fix-script.txt),
  and every line it recorded in [`approach-fix-lines.json`](checking/approach/approach-fix-lines.json).
- [`approach-diag1-stock.log`](checking/approach/approach-diag1-stock.log) — the `KSP.log`
  of an earlier session without this mod, kept for the record: its round trips stayed within range of
  the parked craft, so the game never unloaded it and there was nothing to read.

## The driving protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag - Terrain Height, KSP Diag
- Floating Origin and KSP-Util-MCPServer, without this mod and with it, at `logLevel = Debug`: one run of
three shifts of [the driving protocol](../../docs/ground/checking/driving-protocol.md), played by
its script, [`run-driving.py`](automation/run-driving.py); on Earth, Real Solar System 20.1.3.0 and what
it requires as well. Each log with this mod holds one line per quad it placed, with how far it was
moved. Read in
[Checking the ground: driving on while the world moves](../../docs/ground/checking/driving.md).

The saves, [`Diag2-Rover`](checking/driving/Diag2-Rover.craft) alone on the grass south of
the runway of the KSC, facing due south:

- [`driving-kerbin.sfs`](checking/driving/driving-kerbin.sfs) — on Kerbin;
- [`driving-earth-rss.sfs`](checking/driving/driving-earth-rss.sfs) — on Earth, by the KSC
  at Cape Canaveral; it loads only on Real Solar System.

The logs:

- [`driving-stock.log`](checking/driving/driving-stock.log) and
  [`driving-diag2-fix.log`](checking/driving/driving-diag2-fix.log) — on Kerbin, without this
  mod and with it; what the script printed in
  [`driving-stock-script.txt`](checking/driving/driving-stock-script.txt) and
  [`driving-diag2-fix-script.txt`](checking/driving/driving-diag2-fix-script.txt), and every
  line it recorded in [`driving-stock-lines.json`](checking/driving/driving-stock-lines.json)
  and [`driving-diag2-fix-lines.json`](checking/driving/driving-diag2-fix-lines.json).
- [`driving-earth-rss-stock.log`](checking/driving/driving-earth-rss-stock.log) and
  [`driving-earth-rss-diag2-fix.log`](checking/driving/driving-earth-rss-diag2-fix.log) — on
  Earth, the same; what the script printed in
  [`driving-earth-rss-stock-script.txt`](checking/driving/driving-earth-rss-stock-script.txt)
  and [`driving-earth-rss-diag2-fix-script.txt`](checking/driving/driving-earth-rss-diag2-fix-script.txt),
  and every line it recorded in
  [`driving-earth-rss-stock-lines.json`](checking/driving/driving-earth-rss-stock-lines.json)
  and [`driving-earth-rss-diag2-fix-lines.json`](checking/driving/driving-earth-rss-diag2-fix-lines.json).
- [`driving-earth-rss-stock-1.log`](checking/driving/driving-earth-rss-stock-1.log) and
  [`driving-earth-rss-stock-2.log`](checking/driving/driving-earth-rss-stock-2.log) — two
  earlier runs on Earth without this mod, played by hand and watched, where the rover was seen to jump.

## The protocol of the quads of the highest level, in flight

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag - Terrain Quads, KSP Diag
- Floating Origin and KSP-Util-MCPServer, without this mod and with it at `logLevel = Debug`: on each body,
one flight of [the protocol of the quads of the highest level, in flight](../../docs/ground/checking/flight-protocol.md),
[`Quad-Rocket`](checking/flight/Quad-Rocket.craft) launched from the launchpad, played by its script,
[`run-flight.py`](automation/run-flight.py), and read by [`analyse-flight.py`](automation/analyse-flight.py).
Read in [Checking the ground: in flight](../../docs/ground/checking/flight.md).

- [`flight-kerbin-stock.log`](checking/flight/flight-kerbin-stock.log) — on Kerbin, from the launchpad of the Space Center, 72 *Logs*, without this mod; what the script printed in
  [`flight-kerbin-stock-script.txt`](checking/flight/flight-kerbin-stock-script.txt), what each *Log* answered in
  [`flight-kerbin-stock-readings.json`](checking/flight/flight-kerbin-stock-readings.json), the two files of the *Logs* in
  [`flight-kerbin-stock-logs.csv`](checking/flight/flight-kerbin-stock-logs.csv) and [`flight-kerbin-stock-quads.zip`](checking/flight/flight-kerbin-stock-quads.zip)
  (zipped: 42 MB once unzipped), and what `analyse-flight.py` printed in
  [`flight-kerbin-stock-analysis.txt`](checking/flight/flight-kerbin-stock-analysis.txt).
- [`flight-earth-rss-stock.log`](checking/flight/flight-earth-rss-stock.log) — on Earth, Real Solar System 20.1.3.0 as released and what it requires added, from the
  launchpad of Cape Canaveral, 55 *Logs*, without this mod; what the script printed in
  [`flight-earth-rss-stock-script.txt`](checking/flight/flight-earth-rss-stock-script.txt), what each *Log* answered in
  [`flight-earth-rss-stock-readings.json`](checking/flight/flight-earth-rss-stock-readings.json), the two files of the *Logs* in
  [`flight-earth-rss-stock-logs.csv`](checking/flight/flight-earth-rss-stock-logs.csv) and [`flight-earth-rss-stock-quads.zip`](checking/flight/flight-earth-rss-stock-quads.zip)
  (zipped: 40 MB once unzipped), and what `analyse-flight.py` printed in
  [`flight-earth-rss-stock-analysis.txt`](checking/flight/flight-earth-rss-stock-analysis.txt).
- [`flight-kerbin-fix.log`](checking/flight/flight-kerbin-fix.log) — on Kerbin, from the launchpad of the
  Space Center, 73 *Logs*; what the script printed in [`flight-kerbin-fix-script.txt`](checking/flight/flight-kerbin-fix-script.txt), what each *Log*
  answered in [`flight-kerbin-fix-readings.json`](checking/flight/flight-kerbin-fix-readings.json), the two
  files of the *Logs* in [`flight-kerbin-fix-logs.csv`](checking/flight/flight-kerbin-fix-logs.csv) and
  [`flight-kerbin-fix-quads.zip`](checking/flight/flight-kerbin-fix-quads.zip) (zipped: 43 MB once unzipped),
  and what `analyse-flight.py` printed in
  [`flight-kerbin-fix-analysis.txt`](checking/flight/flight-kerbin-fix-analysis.txt).
- [`flight-earth-rss-fix.log`](checking/flight/flight-earth-rss-fix.log) — on Earth, Real Solar System
  20.1.3.0 as released and what it requires added, from the launchpad of Cape Canaveral, 56 *Logs*; what
  the script printed in [`flight-earth-rss-fix-script.txt`](checking/flight/flight-earth-rss-fix-script.txt),
  what each *Log* answered in [`flight-earth-rss-fix-readings.json`](checking/flight/flight-earth-rss-fix-readings.json),
  the two files of the *Logs* in [`flight-earth-rss-fix-logs.csv`](checking/flight/flight-earth-rss-fix-logs.csv)
  and [`flight-earth-rss-fix-quads.zip`](checking/flight/flight-earth-rss-fix-quads.zip) (zipped: 41 MB once
  unzipped), and what `analyse-flight.py` printed in
  [`flight-earth-rss-fix-analysis.txt`](checking/flight/flight-earth-rss-fix-analysis.txt).

## The seam between subdivision levels

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Quads](https://github.com/lhervier/KSP-Diag-TerrainQuads) and KSP-Util-MCPServer, without
this mod and with it at `logLevel = Debug`: the craft `Diag3-Rocket` on the launchpad, reverted to
launch by the script of [the protocol of the seam](../../docs/ground/limits/stock/the-seam-between-subdivision-levels/the-protocol.md),
[`run-revert.py`](automation/run-revert.py), until the finer quad is above at the largest gap, on land:
`--min-step 500 --ut 64800` on Earth, `--min-step 50 --ut 3600` on Kerbin. Read in
[Measured without this mod](../../docs/ground/limits/stock/the-seam-between-subdivision-levels.md#measured-without-this-mod) and
[The seam with this mod](../../docs/ground/limits/stock/the-seam-between-subdivision-levels.md#the-seam-with-this-mod).

- [`revert-earth-rss-stock.log`](limits/stock/the-seam-between-subdivision-levels/revert-earth-rss-stock.log) — on Earth, Real Solar System
  20.1.3.0 as released and what it requires added, at Cape Canaveral, without this mod, with
  `--candidates 8 --max-reverts 80`: 79 loads, the screenshots taken at 8 of them; what the script
  printed in [`revert-earth-rss-stock-script.txt`](limits/stock/the-seam-between-subdivision-levels/revert-earth-rss-stock-script.txt),
  and every reading in [`revert-earth-rss-stock-readings.json`](limits/stock/the-seam-between-subdivision-levels/revert-earth-rss-stock-readings.json).
- [`revert-kerbin-stock.log`](limits/stock/the-seam-between-subdivision-levels/revert-kerbin-stock.log) — on Kerbin, at the Space Center,
  without this mod, seven loads; what the script printed in
  [`revert-kerbin-stock-script.txt`](limits/stock/the-seam-between-subdivision-levels/revert-kerbin-stock-script.txt), and every reading in
  [`revert-kerbin-stock-readings.json`](limits/stock/the-seam-between-subdivision-levels/revert-kerbin-stock-readings.json).
- [`revert-earth-rss-fix-diag4.log`](limits/stock/the-seam-between-subdivision-levels/revert-earth-rss-fix-diag4.log) — on Earth, Real Solar
  System 20.1.3.0 as released and what it requires added, at Cape Canaveral, nine loads; what the
  script printed in [`revert-earth-rss-fix-diag4-script.txt`](limits/stock/the-seam-between-subdivision-levels/revert-earth-rss-fix-diag4-script.txt),
  and every reading in [`revert-earth-rss-fix-diag4-readings.json`](limits/stock/the-seam-between-subdivision-levels/revert-earth-rss-fix-diag4-readings.json).
- [`revert-kerbin-fix-diag4.log`](limits/stock/the-seam-between-subdivision-levels/revert-kerbin-fix-diag4.log) — on Kerbin, at the Space
  Center, ten loads; what the script printed in
  [`revert-kerbin-fix-diag4-script.txt`](limits/stock/the-seam-between-subdivision-levels/revert-kerbin-fix-diag4-script.txt), and every
  reading in [`revert-kerbin-fix-diag4-readings.json`](limits/stock/the-seam-between-subdivision-levels/revert-kerbin-fix-diag4-readings.json).

## With Deferred

The install of [On the stock system](../statics/README.md#on-the-stock-system) plus [Deferred](https://github.com/LGhassen/Deferred)
1.3.5 and [Shabby](https://github.com/KSPModdingLibs/Shabby) 0.4.2, both instruments at once, this mod at
`logLevel = Debug`, and [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which plays the
protocols through the scripts of [`automation/`](automation). Read in
[Deferred](../../docs/ground/non-regression/deferred/drawing-the-ground.md).

- [`automation/run-runway.py`](../statics/automation/run-runway.py) — plays
  [the runway protocol](../../docs/statics/checking/loading-protocol.md).
- [`automation/run-approach.py`](automation/run-approach.py) — plays
  [the approach protocol](../../docs/ground/checking/approach-protocol.md).
- [`runway-deferred-fix.log`](non-regression/deferred/drawing-the-ground/runway-deferred-fix.log) — the six loadings of `runway-kerbin.sfs`;
  the lines read are in [`runway-deferred-fix-lines.json`](non-regression/deferred/drawing-the-ground/runway-deferred-fix-lines.json).
- [`runway-without-deferred-fix.log`](non-regression/deferred/drawing-the-ground/runway-without-deferred-fix.log) — the same script on the
  same install, Deferred and Shabby taken out; the lines read are in
  [`runway-without-deferred-fix-lines.json`](non-regression/deferred/drawing-the-ground/runway-without-deferred-fix-lines.json).
- [`approach-deferred-fix.log`](non-regression/deferred/drawing-the-ground/approach-deferred-fix.log) — the six round trips of
  `approach-kerbin.sfs`, in a single flight; the lines read are in
  [`approach-deferred-fix-lines.json`](non-regression/deferred/drawing-the-ground/approach-deferred-fix-lines.json).

## With Kerbal Planetary Base Systems

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Kerbal Planetary Base Systems](https://github.com/n116-software/KerbalPlanetaryBaseSystems) 1.6.16 with
Community Category Kit and Community Resource Pack, both instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer); this mod at `logLevel = Debug`, or not: each
session is here twice, `-without-this-mod` and `-fix`. Read in
[Kerbal Planetary Base Systems: a base on the ground](../../docs/ground/non-regression/kerbal-planetary-base-systems/a-base-on-the-ground.md).

- [`kpbs-kerbin-hull-2.sfs`](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/kpbs-kerbin-hull-2.sfs) — a base of
  28 parts of Kerbal Planetary Base Systems, legs retracted, on a slope of Kerbin.
- [`loading-kpbs-without-this-mod.log`](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/loading-kpbs-without-this-mod.log) and
  [`loading-kpbs-fix.log`](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/loading-kpbs-fix.log) — that save, loaded six
  times by `run-loading.py`, both instruments at once; what the script printed in
  [`loading-kpbs-without-this-mod-script.txt`](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/loading-kpbs-without-this-mod-script.txt)
  and [`loading-kpbs-fix-script.txt`](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/loading-kpbs-fix-script.txt), every
  line it recorded in
  [`loading-kpbs-without-this-mod-lines.json`](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/loading-kpbs-without-this-mod-lines.json)
  and [`loading-kpbs-fix-lines.json`](non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/loading-kpbs-fix-lines.json), and the
  screenshots of the two tables in
  [`imgs/ground/non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/`](../../imgs/ground/non-regression/kerbal-planetary-base-systems/a-base-on-the-ground).

## With Parallax

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) with its stock textures and what it
requires, Deferred, and this mod at `logLevel = Debug`, or not: each session is here twice,
`-without-this-mod` and `-fix`. Read in
[the non-regression tests on Parallax](../../docs/ground/README.md#parallax).

On Parallax Continued 1.0.5, with both instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer):

- The four saves of [the loading protocol](#the-loading-protocol), loaded six times each by
  `run-loading.py`: `loading-<body>-*` in
  [`loading-a-craft-on-its-ground/`](non-regression/parallax/loading-a-craft-on-its-ground/), what the script printed and every
  line it recorded, one `KSP.log` per session (`loading-without-this-mod.log.gz`, `loading-fix.log.gz`);
  the screenshots of the tables in
  [`imgs/ground/non-regression/parallax/loading-a-craft-on-its-ground/`](../../imgs/ground/non-regression/parallax/loading-a-craft-on-its-ground).
- [`approach-kerbin-tundra.sfs`](non-regression/parallax/coming-back-to-a-craft-on-its-ground/approach-kerbin-tundra.sfs) — the
  two craft of [the approach protocol](#the-approach-protocol) in the tundra of Kerbin, at 72° north.
  Six round trips by `run-approach.py --heading 135`: `approach-*` in
  [`coming-back-to-a-craft-on-its-ground/`](non-regression/parallax/coming-back-to-a-craft-on-its-ground/), with the
  `KSP.log`, what the script printed and every line it recorded; the screenshots of the tables, trip by
  trip, in
  [`imgs/ground/non-regression/parallax/coming-back-to-a-craft-on-its-ground/`](../../imgs/ground/non-regression/parallax/coming-back-to-a-craft-on-its-ground).

## On Real Solar System

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, plus [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 and what
it requires (Kopernicus, Modular Flight Integrator, KSPTextureLoader, the RSS textures), as released
unless said otherwise. This mod ran at `logLevel = Debug`, so each log also holds one line per quad
placed, with how far it was moved. The sessions marked *first safeguard* ran with its first version,
a fixed metre, and hold the line where it refused part of Earth's terrain.

Two saves are only used by [The ground workaround](../../docs/ground/non-regression/real-solar-system/the-ground-workaround.md),
next to the two of [The loading protocol](#the-loading-protocol):

- [`reload-moon-rss.sfs`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss.sfs) —
  a capsule on an empty FL-T100, landed on flat ground on the Moon, made without this mod;
  `reload-moon-rss-resave.sfs` is the same craft, saved again at a later load;
- [`reload-earth-rss-landed.sfs`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed.sfs) —
  `reload-earth-rss-resave.sfs` with one line changed in the file: the situation of the craft, from
  `PRELAUNCH` to `LANDED`.

Without this mod, played by hand, watching the craft, Real Solar System as released unless said
otherwise:

- [`reload-moon-rss-stock.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-stock.log) —
  Diag LandedVessel: six loads of `reload-moon-rss.sfs`, then one of a save taken after the sixth.
- [`reload-moon-rss-vgpeoff-stock.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-vgpeoff-stock.log) —
  Diag LandedVessel: the first load of `reload-moon-rss.sfs` with Real Solar System's
  `VesselGroundPositionEnhancer` turned off, by an empty assembly named `WorldStabilizer` in `GameData`.
- [`reload-moon-rss-stock-14loads.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-stock-14loads.log) —
  Diag LandedVessel: fourteen loads of `reload-moon-rss.sfs`.
- [`reload-moon-rss-stock-tipped.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-stock-tipped.log) —
  Diag TerrainHeight: the first load of `reload-moon-rss-resave.sfs`, where the craft tipped over.
- [`reload-earth-rss-stock.log`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-stock.log) —
  Diag LandedVessel alone: six loads of `reload-earth-rss-resave.sfs`.
- [`reload-moon-rss-resave-stock-diag2.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-resave-stock-diag2.log) —
  Diag TerrainHeight: six loads of `reload-moon-rss-resave.sfs`, where the craft jumped once and tipped
  over once.
- [`reload-earth-rss-landed-stock.log`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-stock.log) —
  not by hand: both instruments and KSP-Util-MCPServer, six loads of `reload-earth-rss-landed.sfs` played by
  [`automation/run-loading.py`](automation/run-loading.py); what the script printed in
  [`reload-earth-rss-landed-stock-script.txt`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-stock-script.txt),
  every line of both instruments in
  [`reload-earth-rss-landed-stock-readings.json`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-stock-readings.json).

With this mod:

- [`reload-moon-rss-fix.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-fix.log) — Diag LandedVessel, Real Solar System's
  component turned off by an empty assembly named `WorldStabilizer`: one load of
  `reload-moon-rss.sfs`, the save made without this mod, then that save taken again as
  `reload-moon-rss-resave.sfs` and loaded six times. *First safeguard.*
- [`reload-moon-rss-fix-vgpe-on.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-fix-vgpe-on.log) — Diag LandedVessel, Real Solar
  System as released: the loads of `reload-moon-rss-resave.sfs`, six of them recorded. *First
  safeguard.*
- [`reload-moon-rss-fix-diag2.log`](checking/loading/reload-moon-rss-fix-diag2.log) — Diag TerrainHeight: six loads of
  `reload-moon-rss-resave.sfs`.
- [`reload-moon-rss-fix-24loads.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-fix-24loads.log) — no instrument:
  24 loads of `reload-moon-rss-resave.sfs` in a row. *First safeguard.*
- [`reload-earth-rss-fix.log`](checking/loading/reload-earth-rss-fix.log) — Diag LandedVessel: six loads of
  `reload-earth-rss-resave.sfs`, the craft in *prelaunch*.
- [`reload-earth-rss-fix-diag2.log`](checking/loading/reload-earth-rss-fix-diag2.log) — Diag TerrainHeight: the same six
  loads.
- [`reload-earth-rss-fix-chain.log`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-fix-chain.log) — no instrument, one
  session: 27 loads of `reload-earth-rss-landed.sfs`, the craft *landed*, then, after going back to the
  space centre, 24 of `reload-earth-rss-resave.sfs`, the craft in *prelaunch*.
- [`reload-earth-rss-landed-fix.log`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-fix.log) —
  both instruments and KSP-Util-MCPServer, six loads of `reload-earth-rss-landed.sfs` played by
  [`automation/run-loading.py`](automation/run-loading.py); what the script printed in
  [`reload-earth-rss-landed-fix-script.txt`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-fix-script.txt),
  every line of both instruments in
  [`reload-earth-rss-landed-fix-readings.json`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-fix-readings.json).
- [`reload-rss-without-workaround-fix.log`](non-regression/real-solar-system/the-ground-workaround/reload-rss-without-workaround-fix.log) —
  the same, Real Solar System built from the sources of its release 20.1.3.0 with the change
  [`rss-20.1.3-without-its-ground-workaround.diff`](non-regression/real-solar-system/the-ground-workaround/rss-20.1.3-without-its-ground-workaround.diff),
  which keeps its `VesselGroundPositionEnhancer` from doing anything: one session, six loads of
  `reload-earth-rss-landed.sfs`, then six of `reload-moon-rss-resave.sfs`; what the script printed in
  [`reload-earth-rss-landed-without-workaround-fix-script.txt`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-without-workaround-fix-script.txt)
  and [`reload-moon-rss-resave-without-workaround-fix-script.txt`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-resave-without-workaround-fix-script.txt),
  every line of both instruments in
  [`reload-earth-rss-landed-without-workaround-fix-readings.json`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-landed-without-workaround-fix-readings.json)
  and [`reload-moon-rss-resave-without-workaround-fix-readings.json`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-resave-without-workaround-fix-readings.json).

- [`launch-earth-rss-fix.log`](limits/stock/the-seam-between-subdivision-levels/launch-earth-rss-fix.log) — no instrument, MechJeb2 2.15.0.0
  added to the install: one session, a small rocket launched from the VAB onto the launchpad at Cape
  Canaveral, then flown towards orbit, the flight started over three times. The launch was saved
  afterwards as [`rss-launch-to-earth-orbit.sfs`](limits/stock/the-seam-between-subdivision-levels/rss-launch-to-earth-orbit.sfs), which needs MechJeb2
  to load. Used in [The seam between subdivision levels](../../docs/ground/limits/stock/the-seam-between-subdivision-levels.md).

[The approach protocol](#the-approach-protocol) on the Moon, with both instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer) added, read in
[Coming back to a craft left parked, on the Moon](../../docs/ground/non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon.md):

- [`approach-moon-rss.sfs`](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/approach-moon-rss.sfs) —
  the two craft of the approach protocol in the Sea of Tranquillity, the rover set for the low gravity of
  the Moon. Six round trips by
  `run-approach.py --save approach-moon-rss --speed 10 --slow-from 150 --home-speed 2`, without this
  mod, then with it, each in one flight.
- [`approach-moon-without-this-mod.log`](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/approach-moon-without-this-mod.log) —
  the `KSP.log` of the session without this mod. Before the six round trips, it also holds the making of
  the save (its rover's wheels set, the save written), the rover driven about 1.3 km to try its speeds and
  its braking, and the save loaded again before the script loads it. What the script printed in
  [`approach-moon-without-this-mod-script.txt`](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/approach-moon-without-this-mod-script.txt),
  and every line it recorded in
  [`approach-moon-without-this-mod-lines.json`](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/approach-moon-without-this-mod-lines.json).
- [`approach-moon-fix.log`](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/approach-moon-fix.log) —
  the same with this mod; what the script printed in
  [`approach-moon-fix-script.txt`](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/approach-moon-fix-script.txt),
  and every line it recorded in
  [`approach-moon-fix-lines.json`](non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/approach-moon-fix-lines.json).
- The screenshots of the tables, trip by trip, in
  [`imgs/ground/non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon/`](../../imgs/ground/non-regression/real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon).

[The switching protocol](../../docs/ground/checking/switching-protocol.md) on the Moon, the switch
made as the map view's *Switch To* does, with both instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer) added, read in
[Switching to a craft left parked, on the Moon](../../docs/ground/non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon.md):

- [`switch-moon-rss.sfs`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-rss.sfs) —
  the two craft of `approach-moon-rss.sfs`, the rover driven about 3 km due south, flown, the capsule its
  target. Six switches by
  `run-switching.py --save switch-moon-rss --rounds 6 --scene-shots`, in each of the three sessions below.
- [`switch-moon-without-this-mod.log`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-without-this-mod.log) —
  without this mod; what the script printed in
  [`switch-moon-without-this-mod-script.txt`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-without-this-mod-script.txt),
  and every line it recorded in
  [`switch-moon-without-this-mod-lines.json`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-without-this-mod-lines.json).
- [`switch-moon-fix.log`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-fix.log) —
  the same with this mod; what the script printed in
  [`switch-moon-fix-script.txt`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-fix-script.txt),
  and every line it recorded in
  [`switch-moon-fix-lines.json`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-fix-lines.json).
- [`switch-moon-fix-workaround-built-out.log`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-fix-workaround-built-out.log) —
  the same with this mod, Real Solar System built with the change
  [`rss-20.1.3-without-its-ground-workaround.diff`](non-regression/real-solar-system/the-ground-workaround/rss-20.1.3-without-its-ground-workaround.diff);
  what the script printed in
  [`switch-moon-fix-workaround-built-out-script.txt`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-fix-workaround-built-out-script.txt),
  and every line it recorded in
  [`switch-moon-fix-workaround-built-out-lines.json`](non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/switch-moon-fix-workaround-built-out-lines.json).
- The screenshots of the tables, and of the scene after each switch, in
  [`imgs/ground/non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon/`](../../imgs/ground/non-regression/real-solar-system/switching-to-a-craft-left-parked-on-the-moon).
