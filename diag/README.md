# The runs

Part of [Terrain Precision Fix](../README.md): the saves, the scripts and the `KSP.log` of every
session, without this mod and with it. What their readings say is in
[Checking the culprit: loading the same save](../docs/checking-the-culprit-loading.md),
[Coming back to a craft left parked](../docs/checking-the-culprit-approach.md),
[Switching to a craft far away](../docs/checking-the-culprit-switching.md),
[Driving on while the world moves](../docs/checking-the-culprit-driving.md),
[Launching from a launch pad of Making History](../docs/checking-the-culprit-launch-pad.md),
[In flight](../docs/checking-the-culprit-flight.md),
[Anchoring a base](../docs/checking-the-culprit-anchoring.md),
the pages of [Non-regression tests](../docs/non-regression.md) and of
[Limits and solutions](../docs/limits-and-solutions.md).

Each page has its folder here, at the same path as the page under `docs`: the logs, saves and crafts
of [An anchor on a static](../docs/non-regression/stock/an-anchor-on-a-static.md) are in
[`non-regression/stock/an-anchor-on-a-static/`](non-regression/stock/an-anchor-on-a-static), and its
screenshots in [`imgs/non-regression/stock/an-anchor-on-a-static/`](../imgs/non-regression/stock/an-anchor-on-a-static).
A file that several pages use is in the folder of the page that measures with it. The scripts that play
the protocols are in [`automation/`](automation).

## The loading protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, both instruments and
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), without this mod and with it:
[the loading protocol](../docs/checking-the-culprit-loading/the-protocol.md), each save loaded six
times by its script, [`run-loading.py`](automation/run-loading.py). On Real Solar System, the same,
plus Real Solar System 20.1.3.0 and what it requires (Kopernicus 248, Modular Flight Integrator,
KSPTextureLoader, the RSS textures). Read in
[Checking the ground: loading the same save](../docs/checking-the-culprit-loading/the-ground.md).

The saves, a capsule on a small flat fuel tank, made by
[Making the save](../docs/checking-the-culprit-loading/making-the-save.md):

- [`reload-kerbin-2parts.sfs`](checking-the-culprit-loading/reload-kerbin-2parts.sfs) — on the
  levelled grass of the KSC, just south-west of the west end of the runway;
- [`reload-mune-2parts.sfs`](checking-the-culprit-loading/reload-mune-2parts.sfs) — on flat ground on
  the Mun;
- [`reload-minmus-2parts.sfs`](checking-the-culprit-loading/reload-minmus-2parts.sfs) — on the frozen
  flats of Minmus;
- [`reload-gilly-2parts.sfs`](checking-the-culprit-loading/reload-gilly-2parts.sfs) — on Gilly;
- [`reload-moon-rss-resave.sfs`](checking-the-culprit-loading/reload-moon-rss-resave.sfs) — on flat
  ground on the Moon, made with this mod; it loads only on Real Solar System;
- [`reload-earth-rss-resave.sfs`](checking-the-culprit-loading/reload-earth-rss-resave.sfs) — on the
  grass about 1.4 km west of the KSC on Earth, made with this mod; it loads only on Real Solar System.

Copy a save into the folder of a sandbox game and load it from that game.

- [`loading-stock.log`](checking-the-culprit-loading/loading-stock.log) and
  [`loading-fix.log`](checking-the-culprit-loading/loading-fix.log) — the `KSP.log` of the session the
  four saves of the stock worlds were played in, one after the other, together with a lone capsule on
  the same spots, a series no longer published; without this mod, then with it.
- [`loading-rss-stock.log`](checking-the-culprit-loading/loading-rss-stock.log) and
  [`loading-rss-fix.log`](checking-the-culprit-loading/loading-rss-fix.log) — the same on Real Solar
  System, the Moon then Earth.
- for each save, without this mod (`-stock`) and with it (`-fix`), what the script printed
  (`-script.txt`), and every line it recorded, in both instruments (`-lines.json`):
  - `kerbin-2parts`: [`reload-kerbin-2parts-stock-script.txt`](checking-the-culprit-loading/reload-kerbin-2parts-stock-script.txt),
    [`reload-kerbin-2parts-stock-lines.json`](checking-the-culprit-loading/reload-kerbin-2parts-stock-lines.json),
    [`reload-kerbin-2parts-fix-script.txt`](checking-the-culprit-loading/reload-kerbin-2parts-fix-script.txt) and
    [`reload-kerbin-2parts-fix-lines.json`](checking-the-culprit-loading/reload-kerbin-2parts-fix-lines.json);
  - `mune-2parts`: [`reload-mune-2parts-stock-script.txt`](checking-the-culprit-loading/reload-mune-2parts-stock-script.txt),
    [`reload-mune-2parts-stock-lines.json`](checking-the-culprit-loading/reload-mune-2parts-stock-lines.json),
    [`reload-mune-2parts-fix-script.txt`](checking-the-culprit-loading/reload-mune-2parts-fix-script.txt) and
    [`reload-mune-2parts-fix-lines.json`](checking-the-culprit-loading/reload-mune-2parts-fix-lines.json);
  - `minmus-2parts`: [`reload-minmus-2parts-stock-script.txt`](checking-the-culprit-loading/reload-minmus-2parts-stock-script.txt),
    [`reload-minmus-2parts-stock-lines.json`](checking-the-culprit-loading/reload-minmus-2parts-stock-lines.json),
    [`reload-minmus-2parts-fix-script.txt`](checking-the-culprit-loading/reload-minmus-2parts-fix-script.txt) and
    [`reload-minmus-2parts-fix-lines.json`](checking-the-culprit-loading/reload-minmus-2parts-fix-lines.json);
  - `gilly-2parts`: [`reload-gilly-2parts-stock-script.txt`](checking-the-culprit-loading/reload-gilly-2parts-stock-script.txt),
    [`reload-gilly-2parts-stock-lines.json`](checking-the-culprit-loading/reload-gilly-2parts-stock-lines.json),
    [`reload-gilly-2parts-fix-script.txt`](checking-the-culprit-loading/reload-gilly-2parts-fix-script.txt) and
    [`reload-gilly-2parts-fix-lines.json`](checking-the-culprit-loading/reload-gilly-2parts-fix-lines.json);
  - `moon-rss-resave`: [`reload-moon-rss-resave-stock-script.txt`](checking-the-culprit-loading/reload-moon-rss-resave-stock-script.txt),
    [`reload-moon-rss-resave-stock-lines.json`](checking-the-culprit-loading/reload-moon-rss-resave-stock-lines.json),
    [`reload-moon-rss-resave-fix-script.txt`](checking-the-culprit-loading/reload-moon-rss-resave-fix-script.txt) and
    [`reload-moon-rss-resave-fix-lines.json`](checking-the-culprit-loading/reload-moon-rss-resave-fix-lines.json);
  - `earth-rss-resave`: [`reload-earth-rss-resave-stock-script.txt`](checking-the-culprit-loading/reload-earth-rss-resave-stock-script.txt),
    [`reload-earth-rss-resave-stock-lines.json`](checking-the-culprit-loading/reload-earth-rss-resave-stock-lines.json),
    [`reload-earth-rss-resave-fix-script.txt`](checking-the-culprit-loading/reload-earth-rss-resave-fix-script.txt) and
    [`reload-earth-rss-resave-fix-lines.json`](checking-the-culprit-loading/reload-earth-rss-resave-fix-lines.json).

## The switching protocol

The install of [The loading protocol](#the-loading-protocol), on Kerbin: the six rounds of
[the switching protocol](../docs/checking-the-culprit-switching/the-protocol.md), played by its script,
[`run-switching.py`](automation/run-switching.py), on
[`switch-kerbin.sfs`](checking-the-culprit-switching/switch-kerbin.sfs), a capsule landed on the grass
west of the KSC and a rover 1.97 km to the south of it. Read in
[Switching to a craft far away](../docs/checking-the-culprit-switching.md).

- [`switching-stock.log`](checking-the-culprit-switching/switching-stock.log) — the `KSP.log` of the
  session without this mod; what the script printed in
  [`switching-stock-script.txt`](checking-the-culprit-switching/switching-stock-script.txt), and every
  line it recorded, in both instruments, in
  [`switching-stock-lines.json`](checking-the-culprit-switching/switching-stock-lines.json).
- [`switching-fix.log`](checking-the-culprit-switching/switching-fix.log) — the same with this mod; what
  the script printed in [`switching-fix-script.txt`](checking-the-culprit-switching/switching-fix-script.txt),
  and every line it recorded in [`switching-fix-lines.json`](checking-the-culprit-switching/switching-fix-lines.json).

## The approach protocol

The install of [The loading protocol](#the-loading-protocol), on Kerbin: the six round trips of
[the approach protocol](../docs/checking-the-culprit-approach/the-protocol.md), in a single flight,
played by its script, [`run-approach.py`](automation/run-approach.py), on
[`approach-kerbin.sfs`](checking-the-culprit-approach/approach-kerbin.sfs), a capsule landed on the
flat grass west of the KSC and a rover 26 m from it. Read in
[Coming back to a craft left parked](../docs/checking-the-culprit-approach.md).

- [`approach-stock.log`](checking-the-culprit-approach/approach-stock.log) — the `KSP.log` of the
  session without this mod; what the script printed in
  [`approach-stock-script.txt`](checking-the-culprit-approach/approach-stock-script.txt), and every line
  it recorded, in both instruments, in
  [`approach-stock-lines.json`](checking-the-culprit-approach/approach-stock-lines.json).
- [`approach-fix.log`](checking-the-culprit-approach/approach-fix.log) — the same with this mod; what
  the script printed in [`approach-fix-script.txt`](checking-the-culprit-approach/approach-fix-script.txt),
  and every line it recorded in [`approach-fix-lines.json`](checking-the-culprit-approach/approach-fix-lines.json).
- [`approach-diag1-stock.log`](checking-the-culprit-approach/approach-diag1-stock.log) — the `KSP.log`
  of an earlier session without this mod, kept for the record: its round trips stayed within range of
  the parked craft, so the game never unloaded it and there was nothing to read.

## The runway protocol

The install of [The loading protocol](#the-loading-protocol): the six loadings of
[the runway protocol](../docs/checking-the-culprit-loading/the-runway-protocol.md), played by its script,
[`run-runway.py`](automation/run-runway.py). Read in
[Checking the statics: loading the same save](../docs/checking-the-culprit-loading/the-statics.md).

The saves:

- [`runway-kerbin.sfs`](checking-the-culprit-loading/runway-kerbin.sfs) — two identical craft, one on
  the grass beside the runway of the KSC and one on the runway, 152 m apart;
- [`runway-mun-kk.sfs`](checking-the-culprit-loading/runway-mun-kk.sfs) — the same on the Mun: one craft
  on a runway placed by [Kerbal Konstructs](https://github.com/KSP-RO/Kerbal-Konstructs) 1.12.3 and one
  on the ground 42 m away. The runway itself is in the two files of
  [`runway-mun-kk/GameData/KerbalKonstructs/NewInstances/`](checking-the-culprit-loading/runway-mun-kk/GameData/KerbalKonstructs/NewInstances/):
  copy that `GameData` into the folder of KSP, over its own, before loading the save. Made by
  [Making the save on the Mun](../docs/checking-the-culprit-loading/making-the-mun-save.md).

The logs, without this mod (`-stock`) and with it (`-fix`):

- [`runway-stock.log`](checking-the-culprit-loading/runway-stock.log) and
  [`runway-fix.log`](checking-the-culprit-loading/runway-fix.log) — on Kerbin, `runway-kerbin.sfs`; what
  the script printed in [`runway-stock-script.txt`](checking-the-culprit-loading/runway-stock-script.txt)
  and [`runway-fix-script.txt`](checking-the-culprit-loading/runway-fix-script.txt), and every line it
  recorded, in both instruments, in [`runway-stock-lines.json`](checking-the-culprit-loading/runway-stock-lines.json)
  and [`runway-fix-lines.json`](checking-the-culprit-loading/runway-fix-lines.json).
- [`runway-mun-kk-stock.log`](checking-the-culprit-loading/runway-mun-kk-stock.log) and
  [`runway-mun-kk-fix.log`](checking-the-culprit-loading/runway-mun-kk-fix.log) — on the Mun,
  `runway-mun-kk.sfs`, Kerbal Konstructs 1.12.3 added to the install with CustomPreLaunchChecks 1.8.1;
  what the script printed in [`runway-mun-kk-stock-script.txt`](checking-the-culprit-loading/runway-mun-kk-stock-script.txt)
  and [`runway-mun-kk-fix-script.txt`](checking-the-culprit-loading/runway-mun-kk-fix-script.txt), and
  every line it recorded in [`runway-mun-kk-stock-lines.json`](checking-the-culprit-loading/runway-mun-kk-stock-lines.json)
  and [`runway-mun-kk-fix-lines.json`](checking-the-culprit-loading/runway-mun-kk-fix-lines.json).

## The driving protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag - Terrain Height, KSP Diag
- Floating Origin and KSP-MCPServer, without this mod and with it, at `logLevel = Debug`: one run of
three shifts of [the driving protocol](../docs/checking-the-culprit-driving/the-protocol.md), played by
its script, [`run-driving.py`](automation/run-driving.py); on Earth, Real Solar System 20.1.3.0 and what
it requires as well. Each log with this mod holds one line per quad it placed, with how far it was
moved. Read in
[Checking the ground: driving on while the world moves](../docs/checking-the-culprit-driving/the-ground.md).

The saves, [`Diag2-Rover`](checking-the-culprit-driving/Diag2-Rover.craft) alone on the grass south of
the runway of the KSC, facing due south:

- [`driving-kerbin.sfs`](checking-the-culprit-driving/driving-kerbin.sfs) — on Kerbin;
- [`driving-earth-rss.sfs`](checking-the-culprit-driving/driving-earth-rss.sfs) — on Earth, by the KSC
  at Cape Canaveral; it loads only on Real Solar System.

The logs:

- [`driving-stock.log`](checking-the-culprit-driving/driving-stock.log) and
  [`driving-diag2-fix.log`](checking-the-culprit-driving/driving-diag2-fix.log) — on Kerbin, without this
  mod and with it; what the script printed in
  [`driving-stock-script.txt`](checking-the-culprit-driving/driving-stock-script.txt) and
  [`driving-diag2-fix-script.txt`](checking-the-culprit-driving/driving-diag2-fix-script.txt), and every
  line it recorded in [`driving-stock-lines.json`](checking-the-culprit-driving/driving-stock-lines.json)
  and [`driving-diag2-fix-lines.json`](checking-the-culprit-driving/driving-diag2-fix-lines.json).
- [`driving-earth-rss-stock.log`](checking-the-culprit-driving/driving-earth-rss-stock.log) and
  [`driving-earth-rss-diag2-fix.log`](checking-the-culprit-driving/driving-earth-rss-diag2-fix.log) — on
  Earth, the same; what the script printed in
  [`driving-earth-rss-stock-script.txt`](checking-the-culprit-driving/driving-earth-rss-stock-script.txt)
  and [`driving-earth-rss-diag2-fix-script.txt`](checking-the-culprit-driving/driving-earth-rss-diag2-fix-script.txt),
  and every line it recorded in
  [`driving-earth-rss-stock-lines.json`](checking-the-culprit-driving/driving-earth-rss-stock-lines.json)
  and [`driving-earth-rss-diag2-fix-lines.json`](checking-the-culprit-driving/driving-earth-rss-diag2-fix-lines.json).
- [`driving-earth-rss-stock-1.log`](checking-the-culprit-driving/driving-earth-rss-stock-1.log) and
  [`driving-earth-rss-stock-2.log`](checking-the-culprit-driving/driving-earth-rss-stock-2.log) — two
  earlier runs on Earth without this mod, played by hand and watched, where the rover was seen to jump.

## The protocol of the runway and the grass while the world moves

The install of [The driving protocol](#the-driving-protocol): the moves of the origin of
[the protocol of the runway and the grass while the world moves](../docs/checking-the-culprit-driving/the-runway-protocol.md),
played by its script, [`run-driving-runway.py`](automation/run-driving-runway.py), from
[`driving-runway-kerbin.sfs`](checking-the-culprit-driving/driving-runway-kerbin.sfs), `Diag2-Rover`
alone on the grass by the north edge of the runway of the KSC. Read in
[Checking the statics: driving on while the world moves](../docs/checking-the-culprit-driving/the-statics.md#by-the-runway-of-the-ksc). Earth is under
[On Real Solar System](#on-real-solar-system).

- [`driving-runway-stock.log`](checking-the-culprit-driving/driving-runway-stock.log) — without this mod,
  three moves; what the script printed in
  [`driving-runway-stock-script.txt`](checking-the-culprit-driving/driving-runway-stock-script.txt), and
  every line it recorded in [`driving-runway-stock-lines.json`](checking-the-culprit-driving/driving-runway-stock-lines.json).
- [`driving-runway-diag2-fix.log`](checking-the-culprit-driving/driving-runway-diag2-fix.log) — this mod as it is
  installed; what the script printed in
  [`driving-runway-diag2-fix-script.txt`](checking-the-culprit-driving/driving-runway-diag2-fix-script.txt), and every
  line it recorded in [`driving-runway-diag2-fix-lines.json`](checking-the-culprit-driving/driving-runway-diag2-fix-lines.json).
- [`driving-runway-diag2-fix-terrain-only.log`](checking-the-culprit-driving/driving-runway-diag2-fix-terrain-only.log) —
  an earlier run, with an earlier version of the script, this mod with `fixStatics = false`; what the
  script printed in
  [`driving-runway-diag2-fix-terrain-only-script.txt`](checking-the-culprit-driving/driving-runway-diag2-fix-terrain-only-script.txt),
  and every line it recorded in
  [`driving-runway-diag2-fix-terrain-only-lines.json`](checking-the-culprit-driving/driving-runway-diag2-fix-terrain-only-lines.json).

## The launch pad protocol

KSP 1.12.5 with the Making History expansion, Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) and KSP-MCPServer,
without this mod and with it: six launches of
[`Capsule.craft`](checking-the-culprit-launch-pad/Capsule.craft), a Mk1 command pod on an FL-T100 tank,
from the Desert Launch Site, one session of the game each, by the script of
[the launch pad protocol](../docs/checking-the-culprit-launch-pad/the-protocol.md),
[`run-launch-pad.py`](automation/run-launch-pad.py). Read in
[Launching from a launch pad of Making History](../docs/checking-the-culprit-launch-pad.md).

- [`launch-pad-stock-1.log`](checking-the-culprit-launch-pad/launch-pad-stock-1.log), [`launch-pad-stock-2.log`](checking-the-culprit-launch-pad/launch-pad-stock-2.log), [`launch-pad-stock-3.log`](checking-the-culprit-launch-pad/launch-pad-stock-3.log), [`launch-pad-stock-4.log`](checking-the-culprit-launch-pad/launch-pad-stock-4.log), [`launch-pad-stock-5.log`](checking-the-culprit-launch-pad/launch-pad-stock-5.log) and [`launch-pad-stock-6.log`](checking-the-culprit-launch-pad/launch-pad-stock-6.log) — the `KSP.log`
  of each session without this mod; what the script printed in
  [`launch-pad-stock-script.txt`](checking-the-culprit-launch-pad/launch-pad-stock-script.txt), and every
  line it recorded in [`launch-pad-stock-lines.json`](checking-the-culprit-launch-pad/launch-pad-stock-lines.json).
- [`launch-pad-fix-1.log`](checking-the-culprit-launch-pad/launch-pad-fix-1.log), [`launch-pad-fix-2.log`](checking-the-culprit-launch-pad/launch-pad-fix-2.log), [`launch-pad-fix-3.log`](checking-the-culprit-launch-pad/launch-pad-fix-3.log), [`launch-pad-fix-4.log`](checking-the-culprit-launch-pad/launch-pad-fix-4.log), [`launch-pad-fix-5.log`](checking-the-culprit-launch-pad/launch-pad-fix-5.log) and [`launch-pad-fix-6.log`](checking-the-culprit-launch-pad/launch-pad-fix-6.log) — the same
  with this mod; what the
  script printed in [`launch-pad-fix-script.txt`](checking-the-culprit-launch-pad/launch-pad-fix-script.txt), and every line
  it recorded in [`launch-pad-fix-lines.json`](checking-the-culprit-launch-pad/launch-pad-fix-lines.json).

## The protocol of the quads of the highest level, in flight

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag - Terrain Quads, KSP Diag
- Floating Origin and KSP-MCPServer, without this mod and with it at `logLevel = Debug`: on each body,
one flight of [the protocol of the quads of the highest level, in flight](../docs/checking-the-culprit-flight/the-protocol.md),
[`Quad-Rocket`](checking-the-culprit-flight/Quad-Rocket.craft) launched from the launchpad, played by its script,
[`run-flight.py`](automation/run-flight.py), and read by [`analyse-flight.py`](automation/analyse-flight.py).
Read in [Checking the ground: in flight](../docs/checking-the-culprit-flight/the-ground.md).

- [`flight-kerbin-stock.log`](checking-the-culprit-flight/flight-kerbin-stock.log) — on Kerbin, from the launchpad of the Space Center, 72 *Logs*, without this mod; what the script printed in
  [`flight-kerbin-stock-script.txt`](checking-the-culprit-flight/flight-kerbin-stock-script.txt), what each *Log* answered in
  [`flight-kerbin-stock-readings.json`](checking-the-culprit-flight/flight-kerbin-stock-readings.json), the two files of the *Logs* in
  [`flight-kerbin-stock-logs.csv`](checking-the-culprit-flight/flight-kerbin-stock-logs.csv) and [`flight-kerbin-stock-quads.zip`](checking-the-culprit-flight/flight-kerbin-stock-quads.zip)
  (zipped: 42 MB once unzipped), and what `analyse-flight.py` printed in
  [`flight-kerbin-stock-analysis.txt`](checking-the-culprit-flight/flight-kerbin-stock-analysis.txt).
- [`flight-earth-rss-stock.log`](checking-the-culprit-flight/flight-earth-rss-stock.log) — on Earth, Real Solar System 20.1.3.0 as released and what it requires added, from the
  launchpad of Cape Canaveral, 55 *Logs*, without this mod; what the script printed in
  [`flight-earth-rss-stock-script.txt`](checking-the-culprit-flight/flight-earth-rss-stock-script.txt), what each *Log* answered in
  [`flight-earth-rss-stock-readings.json`](checking-the-culprit-flight/flight-earth-rss-stock-readings.json), the two files of the *Logs* in
  [`flight-earth-rss-stock-logs.csv`](checking-the-culprit-flight/flight-earth-rss-stock-logs.csv) and [`flight-earth-rss-stock-quads.zip`](checking-the-culprit-flight/flight-earth-rss-stock-quads.zip)
  (zipped: 40 MB once unzipped), and what `analyse-flight.py` printed in
  [`flight-earth-rss-stock-analysis.txt`](checking-the-culprit-flight/flight-earth-rss-stock-analysis.txt).
- [`flight-kerbin-fix.log`](checking-the-culprit-flight/flight-kerbin-fix.log) — on Kerbin, from the launchpad of the
  Space Center, 73 *Logs*; what the script printed in [`flight-kerbin-fix-script.txt`](checking-the-culprit-flight/flight-kerbin-fix-script.txt), what each *Log*
  answered in [`flight-kerbin-fix-readings.json`](checking-the-culprit-flight/flight-kerbin-fix-readings.json), the two
  files of the *Logs* in [`flight-kerbin-fix-logs.csv`](checking-the-culprit-flight/flight-kerbin-fix-logs.csv) and
  [`flight-kerbin-fix-quads.zip`](checking-the-culprit-flight/flight-kerbin-fix-quads.zip) (zipped: 43 MB once unzipped),
  and what `analyse-flight.py` printed in
  [`flight-kerbin-fix-analysis.txt`](checking-the-culprit-flight/flight-kerbin-fix-analysis.txt).
- [`flight-earth-rss-fix.log`](checking-the-culprit-flight/flight-earth-rss-fix.log) — on Earth, Real Solar System
  20.1.3.0 as released and what it requires added, from the launchpad of Cape Canaveral, 56 *Logs*; what
  the script printed in [`flight-earth-rss-fix-script.txt`](checking-the-culprit-flight/flight-earth-rss-fix-script.txt),
  what each *Log* answered in [`flight-earth-rss-fix-readings.json`](checking-the-culprit-flight/flight-earth-rss-fix-readings.json),
  the two files of the *Logs* in [`flight-earth-rss-fix-logs.csv`](checking-the-culprit-flight/flight-earth-rss-fix-logs.csv)
  and [`flight-earth-rss-fix-quads.zip`](checking-the-culprit-flight/flight-earth-rss-fix-quads.zip) (zipped: 41 MB once
  unzipped), and what `analyse-flight.py` printed in
  [`flight-earth-rss-fix-analysis.txt`](checking-the-culprit-flight/flight-earth-rss-fix-analysis.txt).

## The ground anchor protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel),
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), and this mod at
`logLevel = Debug`, or not: [`ground-anchor-kerbin.sfs`](checking-the-culprit-anchoring/ground-anchor-kerbin.sfs), Bill Kerman places a
ground anchor on the desert of Kerbin beside the rover of [`Diag3-Rover.craft`](checking-the-culprit-anchoring/Diag3-Rover.craft),
alone, then with one of the rover's batteries attached on top of it; quicksave and quickload twice,
played by hand. Three sessions: without this mod, with this mod and `fixGroundAnchorLoad = false`, and with
this mod as installed. Read in
[Checking the culprit: anchoring a base](../docs/checking-the-culprit-anchoring.md).

- [`ground-anchor-kerbin-without-this-mod.log`](checking-the-culprit-anchoring/ground-anchor-kerbin-without-this-mod.log), which
  holds a first placement, given up, before the two measured;
- [`ground-anchor-kerbin-model-fix.log`](checking-the-culprit-anchoring/ground-anchor-kerbin-model-fix.log), which holds a first
  series of both cases before the measured one, the anchor with a battery read without it set as target;
- [`ground-anchor-kerbin-fix.log`](checking-the-culprit-anchoring/ground-anchor-kerbin-fix.log).

Below 50 frames per second: the same install, *Frame Limit* at 30 and KSP-MCPServer, the base of
[`anchor-base-desert-airfield.sfs`](checking-the-culprit-anchoring/anchor-base-desert-airfield.sfs) loaded, then ten quicksaves and quickloads
played by [`automation/run-anchor-on-a-static.py`](automation/run-anchor-on-a-static.py) with `--from-save`
and `--only base`. Three sessions: without this mod, with this mod and `fixGroundAnchorRivet = false`, and
with this mod as installed. Read in
[Checking the culprit: anchoring a base, below 50 frames per second](../docs/checking-the-culprit-anchoring.md#below-50-frames-per-second).

- without this mod: [`anchor-rivet-30fps-without-this-mod.log`](checking-the-culprit-anchoring/anchor-rivet-30fps-without-this-mod.log), with what the script
  printed in [`anchor-rivet-30fps-without-this-mod-script.txt`](checking-the-culprit-anchoring/anchor-rivet-30fps-without-this-mod-script.txt) and the readings
  of KSP Diag - Landed Vessel in [`anchor-rivet-30fps-without-this-mod-readings.json`](checking-the-culprit-anchoring/anchor-rivet-30fps-without-this-mod-readings.json);
- with `fixGroundAnchorRivet = false`: [`anchor-rivet-30fps-rivet-fix-off.log`](checking-the-culprit-anchoring/anchor-rivet-30fps-rivet-fix-off.log), with what the script
  printed in [`anchor-rivet-30fps-rivet-fix-off-script.txt`](checking-the-culprit-anchoring/anchor-rivet-30fps-rivet-fix-off-script.txt) and the readings
  of KSP Diag - Landed Vessel in [`anchor-rivet-30fps-rivet-fix-off-readings.json`](checking-the-culprit-anchoring/anchor-rivet-30fps-rivet-fix-off-readings.json);
- with this mod as installed: [`anchor-rivet-30fps-rivet-fix-on.log`](checking-the-culprit-anchoring/anchor-rivet-30fps-rivet-fix-on.log), with what the script
  printed in [`anchor-rivet-30fps-rivet-fix-on-script.txt`](checking-the-culprit-anchoring/anchor-rivet-30fps-rivet-fix-on-script.txt) and the readings
  of KSP Diag - Landed Vessel in [`anchor-rivet-30fps-rivet-fix-on-readings.json`](checking-the-culprit-anchoring/anchor-rivet-30fps-rivet-fix-on-readings.json).

## The seam between subdivision levels

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Quads](https://github.com/lhervier/KSP-Diag-TerrainQuads) and KSP-MCPServer, without
this mod and with it at `logLevel = Debug`: the craft `Diag3-Rocket` on the launchpad, reverted to
launch by the script of [the protocol of the seam](../docs/limits-and-solutions/stock/the-seam-between-subdivision-levels/the-protocol.md),
[`run-revert.py`](automation/run-revert.py), until the finer quad is above at the largest gap, on land:
`--min-step 500 --ut 64800` on Earth, `--min-step 50 --ut 3600` on Kerbin. Read in
[Measured without this mod](../docs/limits-and-solutions/stock/the-seam-between-subdivision-levels.md#measured-without-this-mod) and
[The seam with this mod](../docs/limits-and-solutions/stock/the-seam-between-subdivision-levels.md#the-seam-with-this-mod).

- [`revert-earth-rss-stock.log`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-earth-rss-stock.log) — on Earth, Real Solar System
  20.1.3.0 as released and what it requires added, at Cape Canaveral, without this mod, with
  `--candidates 8 --max-reverts 80`: 79 loads, the screenshots taken at 8 of them; what the script
  printed in [`revert-earth-rss-stock-script.txt`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-earth-rss-stock-script.txt),
  and every reading in [`revert-earth-rss-stock-readings.json`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-earth-rss-stock-readings.json).
- [`revert-kerbin-stock.log`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-kerbin-stock.log) — on Kerbin, at the Space Center,
  without this mod, seven loads; what the script printed in
  [`revert-kerbin-stock-script.txt`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-kerbin-stock-script.txt), and every reading in
  [`revert-kerbin-stock-readings.json`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-kerbin-stock-readings.json).
- [`revert-earth-rss-fix-diag4.log`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-earth-rss-fix-diag4.log) — on Earth, Real Solar
  System 20.1.3.0 as released and what it requires added, at Cape Canaveral, nine loads; what the
  script printed in [`revert-earth-rss-fix-diag4-script.txt`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-earth-rss-fix-diag4-script.txt),
  and every reading in [`revert-earth-rss-fix-diag4-readings.json`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-earth-rss-fix-diag4-readings.json).
- [`revert-kerbin-fix-diag4.log`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-kerbin-fix-diag4.log) — on Kerbin, at the Space
  Center, ten loads; what the script printed in
  [`revert-kerbin-fix-diag4-script.txt`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-kerbin-fix-diag4-script.txt), and every
  reading in [`revert-kerbin-fix-diag4-readings.json`](limits-and-solutions/stock/the-seam-between-subdivision-levels/revert-kerbin-fix-diag4-readings.json).

## The altitude where KSP turns the body

Without this mod: KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin) and
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer); on the stock system, then with Real Solar
System 20.1.3.0 and what it requires, then with Outer Planets Mod 2.2.12, Kopernicus 248, Modular Flight
Integrator and KSPTextureLoader as for Real Solar System, and the Community Terrain Texture Pack 1.0.5.

- [`rotation-thresholds.txt`](non-regression/stock/a-static-turning-with-its-body/rotation-thresholds.txt) — what
  [`automation/run-rotation-threshold.py`](automation/run-rotation-threshold.py) printed, body by body:
  a craft moved from orbit to orbit, the altitude above which KSP turns the body rather than the world.
  No log kept: the readings are the script's. Read in
  [A static turning with its body](../docs/non-regression/stock/a-static-turning-with-its-body.md).

## The scene changes protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), this mod at
`logLevel = Debug`,
and KSP-MCPServer, which plays the test through [`automation/run-scene-changes.py`](automation/run-scene-changes.py):
a new career at the Custom difficulty (on Kerbin, the same as [`career-with-the-parts.sfs`](non-regression/stock/destroyed-buildings/career-with-the-parts.sfs)),
`Diag3-Rocket.craft` on the launchpad, eleven arrivals in flight through every way of leaving
it, and `Diag3-Rover.craft` launched from the SPH onto the runway; one script per way in
[`automation/scene-changes/`](automation/scene-changes/). On Earth, Real Solar System 20.1.3.0 and what it
requires (Kopernicus 248, Modular Flight Integrator,
KSPTextureLoader, the RSS textures). Each one played again without this mod. Read in
[Scene changes](../docs/non-regression/stock/scene-changes.md).

- [`scene-changes-kerbin-fix.log`](non-regression/stock/scene-changes/scene-changes-kerbin-fix.log) and
  [`scene-changes-kerbin-without-this-mod.log`](non-regression/stock/scene-changes/scene-changes-kerbin-without-this-mod.log) — on
  Kerbin; what the script printed in
  [`scene-changes-kerbin-fix-script.txt`](non-regression/stock/scene-changes/scene-changes-kerbin-fix-script.txt) and
  [`scene-changes-kerbin-without-this-mod-script.txt`](non-regression/stock/scene-changes/scene-changes-kerbin-without-this-mod-script.txt),
  every line of Diag Terrain Height in
  [`scene-changes-kerbin-fix-readings.json`](non-regression/stock/scene-changes/scene-changes-kerbin-fix-readings.json) and
  [`scene-changes-kerbin-without-this-mod-readings.json`](non-regression/stock/scene-changes/scene-changes-kerbin-without-this-mod-readings.json),
  and a screenshot of its table in
  [`scene-changes-kerbin-fix-table.png`](non-regression/stock/scene-changes/scene-changes-kerbin-fix-table.png) and
  [`scene-changes-kerbin-without-this-mod-table.png`](non-regression/stock/scene-changes/scene-changes-kerbin-without-this-mod-table.png).
- [`scene-changes-earth-rss-fix.log`](non-regression/stock/scene-changes/scene-changes-earth-rss-fix.log) and
  [`scene-changes-earth-rss-without-this-mod.log`](non-regression/stock/scene-changes/scene-changes-earth-rss-without-this-mod.log)
  — on Earth; the same in
  [`scene-changes-earth-rss-fix-script.txt`](non-regression/stock/scene-changes/scene-changes-earth-rss-fix-script.txt),
  [`scene-changes-earth-rss-without-this-mod-script.txt`](non-regression/stock/scene-changes/scene-changes-earth-rss-without-this-mod-script.txt),
  [`scene-changes-earth-rss-fix-readings.json`](non-regression/stock/scene-changes/scene-changes-earth-rss-fix-readings.json) and
  [`scene-changes-earth-rss-without-this-mod-readings.json`](non-regression/stock/scene-changes/scene-changes-earth-rss-without-this-mod-readings.json),
  [`scene-changes-earth-rss-fix-table.png`](non-regression/stock/scene-changes/scene-changes-earth-rss-fix-table.png) and
  [`scene-changes-earth-rss-without-this-mod-table.png`](non-regression/stock/scene-changes/scene-changes-earth-rss-without-this-mod-table.png).
- [`scene-changes-earth-rss-without-this-mod-earlier.log`](non-regression/stock/scene-changes/scene-changes-earth-rss-without-this-mod-earlier.log)
  — an earlier session on Earth without this mod, kept for the error of the Knowledge Base it shows.

## The destroyed buildings protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), this mod at
`logLevel = Debug`,
and KSP-MCPServer, which plays the test through
[`automation/run-destroyed-buildings.py`](automation/run-destroyed-buildings.py): a new career at the Custom
difficulty (the same as [`career-with-the-parts.sfs`](non-regression/stock/destroyed-buildings/career-with-the-parts.sfs), which a player can start
from), [`VAB-Dropper.craft`](non-regression/stock/destroyed-buildings/VAB-Dropper.craft) dropped twice onto the VAB from the
launchpad, `Diag3-Rover.craft` launched from the SPH onto the runway around the VAB in ruins, the VAB
repaired, and `Diag3-Rocket.craft` launched from it; three arrivals on the launchpad, two on the runway.
Played again without this mod. Read in
[Destroyed buildings](../docs/non-regression/stock/destroyed-buildings.md).

- [`destroyed-buildings-kerbin-fix.log`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-fix.log) and
  [`destroyed-buildings-kerbin-without-this-mod.log`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-without-this-mod.log);
  what the script printed in
  [`destroyed-buildings-kerbin-fix-script.txt`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-fix-script.txt) and
  [`destroyed-buildings-kerbin-without-this-mod-script.txt`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-without-this-mod-script.txt),
  every line of Diag Terrain Height in
  [`destroyed-buildings-kerbin-fix-readings.json`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-fix-readings.json) and
  [`destroyed-buildings-kerbin-without-this-mod-readings.json`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-without-this-mod-readings.json),
  and a screenshot of its table in
  [`destroyed-buildings-kerbin-fix-table.png`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-fix-table.png) and
  [`destroyed-buildings-kerbin-without-this-mod-table.png`](non-regression/stock/destroyed-buildings/destroyed-buildings-kerbin-without-this-mod-table.png).

## The facility levels protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), this mod at
`logLevel = Debug`,
and KSP-MCPServer, which plays the test through
[`automation/run-facility-levels.py`](automation/run-facility-levels.py): a new career at the Custom
difficulty (the same as [`career-with-the-parts.sfs`](non-regression/stock/destroyed-buildings/career-with-the-parts.sfs)), `Diag3-Rocket.craft` launched onto the launchpad and `Diag3-Rover.craft` onto the runway, four
arrivals on each at each of their three levels. Played again without this mod. Read in
[Facility levels](../docs/non-regression/stock/facility-levels.md).

- [`facility-levels-kerbin-fix.log`](non-regression/stock/facility-levels/facility-levels-kerbin-fix.log) and
  [`facility-levels-kerbin-without-this-mod.log`](non-regression/stock/facility-levels/facility-levels-kerbin-without-this-mod.log);
  what the script printed in
  [`facility-levels-kerbin-fix-script.txt`](non-regression/stock/facility-levels/facility-levels-kerbin-fix-script.txt) and
  [`facility-levels-kerbin-without-this-mod-script.txt`](non-regression/stock/facility-levels/facility-levels-kerbin-without-this-mod-script.txt),
  every line of Diag Terrain Height in
  [`facility-levels-kerbin-fix-readings.json`](non-regression/stock/facility-levels/facility-levels-kerbin-fix-readings.json) and
  [`facility-levels-kerbin-without-this-mod-readings.json`](non-regression/stock/facility-levels/facility-levels-kerbin-without-this-mod-readings.json),
  and the screenshots of its table, every twelve arrivals, in
  [`facility-levels-kerbin-fix-table-1.png`](non-regression/stock/facility-levels/facility-levels-kerbin-fix-table-1.png),
  [`facility-levels-kerbin-fix-table-2.png`](non-regression/stock/facility-levels/facility-levels-kerbin-fix-table-2.png),
  [`facility-levels-kerbin-without-this-mod-table-1.png`](non-regression/stock/facility-levels/facility-levels-kerbin-without-this-mod-table-1.png) and
  [`facility-levels-kerbin-without-this-mod-table-2.png`](non-regression/stock/facility-levels/facility-levels-kerbin-without-this-mod-table-2.png).

## The time warp protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), this mod at
`logLevel = Debug`, and KSP-MCPServer, which plays the test through
[`automation/run-time-warp.py`](automation/run-time-warp.py): a new sandbox game, `Diag3-Rover.craft`
launched from the SPH onto the runway, three days of time warp at 100 000×, then *Warp To* the night and
the next noon at the KSC; four readings, a screenshot at each. Played again without this mod. Read in
[Time warp](../docs/non-regression/stock/time-warp.md) and
[The lights of the KSC](../docs/non-regression/stock/the-lights-of-the-ksc.md).

- [`time-warp-kerbin-fix.log`](non-regression/stock/time-warp/time-warp-kerbin-fix.log) and
  [`time-warp-kerbin-without-this-mod.log`](non-regression/stock/time-warp/time-warp-kerbin-without-this-mod.log);
  what the script printed in
  [`time-warp-kerbin-fix-script.txt`](non-regression/stock/time-warp/time-warp-kerbin-fix-script.txt) and
  [`time-warp-kerbin-without-this-mod-script.txt`](non-regression/stock/time-warp/time-warp-kerbin-without-this-mod-script.txt),
  every line of Diag Terrain Height in
  [`time-warp-kerbin-fix-readings.json`](non-regression/stock/time-warp/time-warp-kerbin-fix-readings.json) and
  [`time-warp-kerbin-without-this-mod-readings.json`](non-regression/stock/time-warp/time-warp-kerbin-without-this-mod-readings.json),
  and a screenshot of its table in
  [`time-warp-kerbin-fix-table.png`](non-regression/stock/time-warp/time-warp-kerbin-fix-table.png) and
  [`time-warp-kerbin-without-this-mod-table.png`](non-regression/stock/time-warp/time-warp-kerbin-without-this-mod-table.png).

## The time warp flyover protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, Kerbal Konstructs 1.12.3 with the launch
pad of [`non-regression/stock/time-warp/warp-static-mun-kk/`](non-regression/stock/time-warp/warp-static-mun-kk/) and its CustomPreLaunchChecks,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), this mod at
`logLevel = Debug`,
and KSP-MCPServer, which plays the test through
[`automation/run-time-warp-flyover.py`](automation/run-time-warp-flyover.py): the capsule of
[`warp-static-mun-kk.sfs`](non-regression/stock/time-warp/warp-static-mun-kk.sfs) on that launch pad, near the highest point of the Mun's
equator, read before and after `Diag3-Rover.craft`, put on a low orbit of the Mun, passes over it in time
warp at 10×. Played again without this mod. Read in
[Time warp](../docs/non-regression/stock/time-warp.md#in-flight-low-over-a-static).

- [`time-warp-flyover-mun-kk-fix.log`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-fix.log) and
  [`time-warp-flyover-mun-kk-without-this-mod.log`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-without-this-mod.log);
  what the script printed in
  [`time-warp-flyover-mun-kk-fix-script.txt`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-fix-script.txt) and
  [`time-warp-flyover-mun-kk-without-this-mod-script.txt`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-without-this-mod-script.txt),
  every line of Diag Terrain Height in
  [`time-warp-flyover-mun-kk-fix-readings.json`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-fix-readings.json) and
  [`time-warp-flyover-mun-kk-without-this-mod-readings.json`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-without-this-mod-readings.json),
  and a screenshot of its table in
  [`time-warp-flyover-mun-kk-fix-table.png`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-fix-table.png) and
  [`time-warp-flyover-mun-kk-without-this-mod-table.png`](non-regression/stock/time-warp/time-warp-flyover-mun-kk-without-this-mod-table.png).

## The anchor on a static protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, both instruments, this mod at
`logLevel = Debug`, and KSP-MCPServer: in a new sandbox game, [`Diag3-Rover-Two-Anchors.craft`](non-regression/stock/an-anchor-on-a-static/Diag3-Rover-Two-Anchors.craft)
launched from the SPH onto the runway of the KSC, then in another game onto the runway of the Desert
Airfield, Bill Kerman aboard with his inventory emptied; Bill places an anchor alone and an anchor with a
battery on it, by hand; then [`automation/run-anchor-on-a-static.py`](automation/run-anchor-on-a-static.py)
reads both anchors as placed, and after each of five quicksaves and quickloads. Played again without this
mod. Read in [An anchor on a static](../docs/non-regression/stock/an-anchor-on-a-static.md).

- [`anchor-on-a-static-with-this-mod.log`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-with-this-mod.log), one session for
  both runways, the Desert Airfield first, followed by three more quicksaves and quickloads there that are
  not part of the test; [`anchor-on-a-static-runway-without-this-mod.log`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-without-this-mod.log)
  and [`anchor-on-a-static-desert-airfield-without-this-mod.log`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-without-this-mod.log);
- what the script printed, and the readings of both instruments, for each runway with and without this mod:
  - the runway of the KSC, with this mod: [`anchor-on-a-static-runway-with-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-with-this-mod-script.txt) and
    [`anchor-on-a-static-runway-with-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-with-this-mod-readings.json);
  - the runway of the KSC, without it: [`anchor-on-a-static-runway-without-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-without-this-mod-script.txt) and
    [`anchor-on-a-static-runway-without-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-without-this-mod-readings.json);
  - the Desert Airfield, with this mod: [`anchor-on-a-static-desert-airfield-with-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-with-this-mod-script.txt) and
    [`anchor-on-a-static-desert-airfield-with-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-with-this-mod-readings.json);
  - the Desert Airfield, without it: [`anchor-on-a-static-desert-airfield-without-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-without-this-mod-script.txt) and
    [`anchor-on-a-static-desert-airfield-without-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-without-this-mod-readings.json).

## On the stock system

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, this mod and one instrument.

- [`runway-mun-kk-colliders-fix.log`](checking-the-culprit-loading/runway-mun-kk-colliders-fix.log) — four loadings of
  `runway-mun-kk.sfs`, every collider under each craft listed at each loading, with its height above the terrain
  KSP computes there.
- [`flight-basics-fix.log`](non-regression/kerbal-konstructs/a-ground-station-opened-in-flight/flight-basics-fix.log) — no instrument, this mod at
  `logLevel = Debug`: KSP started, then *Training → Flight Basics* from the main menu, straight into
  flight on the launchpad, and back to the main menu. Read in
  [Kerbal Konstructs: a ground station opened in flight](../docs/non-regression/kerbal-konstructs/a-ground-station-opened-in-flight.md#why).

## With Deferred

The install of [On the stock system](#on-the-stock-system) plus [Deferred](https://github.com/LGhassen/Deferred)
1.3.5 and [Shabby](https://github.com/KSPModdingLibs/Shabby) 0.4.2, both instruments at once, this mod at
`logLevel = Debug`, and [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which plays the
protocols through the scripts of [`automation/`](automation). Read in
[Deferred](../docs/non-regression/deferred/drawing-the-ground.md).

- [`automation/run-runway.py`](automation/run-runway.py) — plays
  [the runway protocol](../docs/checking-the-culprit-loading/the-runway-protocol.md).
- [`automation/run-approach.py`](automation/run-approach.py) — plays
  [the approach protocol](../docs/checking-the-culprit-approach/the-protocol.md).
- [`runway-deferred-fix.log`](non-regression/deferred/drawing-the-ground/runway-deferred-fix.log) — the six loadings of `runway-kerbin.sfs`;
  the lines read are in [`runway-deferred-fix-lines.json`](non-regression/deferred/drawing-the-ground/runway-deferred-fix-lines.json).
- [`runway-without-deferred-fix.log`](non-regression/deferred/drawing-the-ground/runway-without-deferred-fix.log) — the same script on the
  same install, Deferred and Shabby taken out; the lines read are in
  [`runway-without-deferred-fix-lines.json`](non-regression/deferred/drawing-the-ground/runway-without-deferred-fix-lines.json).
- [`approach-deferred-fix.log`](non-regression/deferred/drawing-the-ground/approach-deferred-fix.log) — the six round trips of
  `approach-kerbin.sfs`, in a single flight; the lines read are in
  [`approach-deferred-fix-lines.json`](non-regression/deferred/drawing-the-ground/approach-deferred-fix-lines.json).

## With Principia

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Principia](https://github.com/mockingbirdnest/Principia) Lévy on the stock system, the instruments of each
protocol, and [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which plays the protocols; this
mod at `logLevel = Debug`, or not: each session is here twice, `-without-this-mod` and `-fix`. Read in
[Principia: the bodies it moves and turns](../docs/non-regression/principia/the-bodies-it-moves-and-turns.md).

- [`loading-principia-without-this-mod.log`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod.log) and
  [`loading-principia-fix.log`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix.log) — the four saves of
  [the loading protocol](../docs/checking-the-culprit-loading/the-protocol.md),
  each loaded six times by `run-loading.py`, both instruments at once; what the script printed in
  [`loading-principia-without-this-mod-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod-script.txt)
  and [`loading-principia-fix-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix-script.txt), every line it recorded,
  with the save it was recorded on, in
  [`loading-principia-without-this-mod-lines.json`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod-lines.json)
  and [`loading-principia-fix-lines.json`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix-lines.json).
- [`flight-principia-without-this-mod.log`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod.log) and
  [`flight-principia-fix.log`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix.log) — one flight each of
  [the protocol of the quads of the highest level, in flight](../docs/checking-the-culprit-flight/the-protocol.md),
  from the launchpad of the Space Center, KSP Diag - Terrain Quads and KSP Diag - Floating Origin; for each,
  as for the flights of [In flight](#the-protocol-of-the-quads-of-the-highest-level-in-flight), what the
  script printed, the readings, the logs, the quads (49 MB once unzipped) and the analysis:
  - without this mod: [`flight-principia-without-this-mod-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-script.txt), [`flight-principia-without-this-mod-readings.json`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-readings.json), [`flight-principia-without-this-mod-logs.csv`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-logs.csv), [`flight-principia-without-this-mod-quads.zip`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-quads.zip) and [`flight-principia-without-this-mod-analysis.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-analysis.txt);
  - with this mod: [`flight-principia-fix-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-script.txt), [`flight-principia-fix-readings.json`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-readings.json), [`flight-principia-fix-logs.csv`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-logs.csv), [`flight-principia-fix-quads.zip`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-quads.zip) and [`flight-principia-fix-analysis.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-analysis.txt).

## With Kerbal Planetary Base Systems

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Kerbal Planetary Base Systems](https://github.com/n116-software/KerbalPlanetaryBaseSystems) 1.6.16 with
Community Category Kit and Community Resource Pack, both instruments and
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer); this mod at `logLevel = Debug`, or not: each
session is here twice, `-without-this-mod` and `-fix`. Read in
[Kerbal Planetary Base Systems: a base on the ground](../docs/non-regression/kerbal-planetary-base-systems/a-base-on-the-ground.md).

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
  [`imgs/non-regression/kerbal-planetary-base-systems/a-base-on-the-ground/`](../imgs/non-regression/kerbal-planetary-base-systems/a-base-on-the-ground).

## With Parallax

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) 1.0.4 rebuilt with the first commit
of our change, since merged as
[pull request #157](https://github.com/Gameslinx/Parallax-Continued/pull/157) and released in 1.0.5,
with its three packs of stock textures and what it requires,
[KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders),
[KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin), and this mod, or not.
Read in [Parallax: its terrain and its scatter](../docs/work-in-progress/parallax/its-terrain-and-its-scatter.md).

- [`capsule-on-a-rock-mun.sfs`](work-in-progress/parallax/its-terrain-and-its-scatter/capsule-on-a-rock-mun.sfs) —
  a Mk1 capsule on an empty FL-T100 fuel tank, landed on top of a rock of the Mun, saved with Parallax
  rebuilt with the change.
- [`rocks-eve-jeb.sfs`](work-in-progress/parallax/its-terrain-and-its-scatter/rocks-eve-jeb.sfs) —
  Jebediah Kerman on EVA on the ground of Eve, among rocks and plants.
- [`the-same-objects/`](work-in-progress/parallax/its-terrain-and-its-scatter/the-same-objects/) — that
  save loaded again at once, twelve times, without this mod (`without-this-mod/`) and with it
  (`with-this-mod/`): the line of KSP Diag - Floating Origin at each load (`readings.json`), the output
  of the script and the `KSP.log` of the session.

## With Kerbal Konstructs

KSP 1.12.5 with the Making History expansion, Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Kerbal Konstructs](https://github.com/KSP-RO/Kerbal-Konstructs) 1.12.3 and CustomPreLaunchChecks 1.8.1,
which it requires, no instrument, this mod at `logLevel = Debug`.

- [`kk-group-editor-fix.log`](limits-and-solutions/kerbal-konstructs/the-group-editor/kk-group-editor-fix.log) — `non-reg-runway-mune-kk.sfs`, its
  runway in `GameData/KerbalKonstructs/NewInstances`: the group moved with the gizmo of the group editor,
  saved with *Save&Close*, then the save loaded again. Read in
  [Kerbal Konstructs: the group editor](../docs/limits-and-solutions/kerbal-konstructs/the-group-editor.md).
- [`kk-ground-station-fix.log`](non-regression/kerbal-konstructs/a-ground-station-opened-in-flight/kk-ground-station-fix.log) —
  [`kk-ground-station.sfs`](non-regression/kerbal-konstructs/a-ground-station-opened-in-flight/kk-ground-station.sfs), a career game, a pod on the launchpad: a water tower
  of Kerbal Konstructs set up beside it, in flight, as a closed CommNet ground station, then opened from
  the facility manager of Kerbal Konstructs. Read in
  [Kerbal Konstructs: a ground station opened in flight](../docs/non-regression/kerbal-konstructs/a-ground-station-opened-in-flight.md).

## With Kopernicus

KSP 1.12.5 with the Making History expansion, Harmony, ModuleManager, KSP Community Fixes 1.41.1 and
[Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 with what it requires (Kopernicus
248, Modular Flight Integrator, KSPTextureLoader, the RSS textures), no instrument. Each
session plays the mission [`kopernicus-flag-fix/Missions/KSC flag fix`](limits-and-solutions/kopernicus/the-flag-fix/Missions)
once, as described in [Seeing the patch](../docs/limits-and-solutions/kopernicus/the-flag-fix.md#seeing-the-patch).

- [`kopernicus-flag-fix-without-this-mod.log`](limits-and-solutions/kopernicus/the-flag-fix/kopernicus-flag-fix-without-this-mod.log) —
  without this mod.
- [`kopernicus-flag-fix-patch-off.log`](limits-and-solutions/kopernicus/the-flag-fix/kopernicus-flag-fix-patch-off.log) — this mod at
  `logLevel = Debug`, with `patchKopernicus = false`.
- [`kopernicus-flag-fix-patch-on.log`](limits-and-solutions/kopernicus/the-flag-fix/kopernicus-flag-fix-patch-on.log) — this mod at
  `logLevel = Debug`, with its defaults.

## On Real Solar System

The same install plus [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 and what
it requires (Kopernicus, Modular Flight Integrator, KSPTextureLoader, the RSS textures), as released
unless said otherwise. This mod ran at `logLevel = Debug`, so each log also holds one line per quad
placed, with how far it was moved. The sessions marked *first safeguard* ran with its first version,
a fixed metre, and hold the line where it refused part of Earth's terrain.

Two saves are only used by [The ground workaround](../docs/non-regression/real-solar-system/the-ground-workaround.md),
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

With this mod:

- [`reload-moon-rss-fix.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-fix.log) — Diag LandedVessel, Real Solar System's
  component turned off by an empty assembly named `WorldStabilizer`: one load of
  `reload-moon-rss.sfs`, the save made without this mod, then that save taken again as
  `reload-moon-rss-resave.sfs` and loaded six times. *First safeguard.*
- [`reload-moon-rss-fix-vgpe-on.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-fix-vgpe-on.log) — Diag LandedVessel, Real Solar
  System as released: the loads of `reload-moon-rss-resave.sfs`, six of them recorded. *First
  safeguard.*
- [`reload-moon-rss-fix-diag2.log`](checking-the-culprit-loading/reload-moon-rss-fix-diag2.log) — Diag TerrainHeight: six loads of
  `reload-moon-rss-resave.sfs`.
- [`reload-moon-rss-fix-24loads.log`](non-regression/real-solar-system/the-ground-workaround/reload-moon-rss-fix-24loads.log) — no instrument:
  24 loads of `reload-moon-rss-resave.sfs` in a row. *First safeguard.*
- [`reload-earth-rss-fix.log`](checking-the-culprit-loading/reload-earth-rss-fix.log) — Diag LandedVessel: six loads of
  `reload-earth-rss-resave.sfs`, the craft in *prelaunch*.
- [`reload-earth-rss-fix-diag2.log`](checking-the-culprit-loading/reload-earth-rss-fix-diag2.log) — Diag TerrainHeight: the same six
  loads.
- [`reload-earth-rss-fix-chain.log`](non-regression/real-solar-system/the-ground-workaround/reload-earth-rss-fix-chain.log) — no instrument, one
  session: 27 loads of `reload-earth-rss-landed.sfs`, the craft *landed*, then, after going back to the
  space centre, 24 of `reload-earth-rss-resave.sfs`, the craft in *prelaunch*.
- [`kopernicus-flag-glitch-without-this-mod.log`](limits-and-solutions/kopernicus/the-flag-fix/kopernicus-flag-glitch-without-this-mod.log),
  [`kopernicus-flag-glitch-statics-fix.log`](limits-and-solutions/kopernicus/the-flag-fix/kopernicus-flag-glitch-statics-fix.log) and
  [`kopernicus-flag-glitch-statics-fix-off.log`](limits-and-solutions/kopernicus/the-flag-fix/kopernicus-flag-glitch-statics-fix-off.log) —
  MechJeb2 2.15.3 added to the first and the third, and Kopernicus built from the sources of its release
  248 with the change
  [`kopernicus-248-without-its-flag-fix.diff`](limits-and-solutions/kopernicus/the-flag-fix/kopernicus-248-without-its-flag-fix.diff),
  which turns its flag fix off: a craft on the launchpad at Cape Canaveral, without this mod, then with
  it, then with its statics fix turned off. Read in
  [The flag glitch](../docs/limits-and-solutions/kopernicus/the-flag-fix.md#the-flag-glitch).
- [`reload-venus-mars-rss-fix.log`](non-regression/real-solar-system/this-mods-safeguard/reload-venus-mars-rss-fix.log) — no instrument, one
  session: six loads of [`reload-venus-rss.sfs`](non-regression/real-solar-system/this-mods-safeguard/reload-venus-rss.sfs), then six of
  [`reload-mars-rss.sfs`](non-regression/real-solar-system/this-mods-safeguard/reload-mars-rss.sfs). The six loads after them, on a second site of Mars,
  are not used.
- [`reload-mercury-rss-fix.log`](non-regression/real-solar-system/this-mods-safeguard/reload-mercury-rss-fix.log) — no instrument: six loads of
  [`reload-mercury-rss.sfs`](non-regression/real-solar-system/this-mods-safeguard/reload-mercury-rss.sfs). Each one logs KSP moving the craft down 22.4 m,
  the terrain detail its save describes.
- [`launch-earth-rss-fix.log`](limits-and-solutions/stock/the-seam-between-subdivision-levels/launch-earth-rss-fix.log) — no instrument, MechJeb2 2.15.0.0
  added to the install: one session, a small rocket launched from the VAB onto the launchpad at Cape
  Canaveral, then flown towards orbit, the flight started over three times. The launch was saved
  afterwards as [`rss-launch-to-earth-orbit.sfs`](limits-and-solutions/stock/the-seam-between-subdivision-levels/rss-launch-to-earth-orbit.sfs), which needs MechJeb2
  to load. Used in [The seam between subdivision levels](../docs/limits-and-solutions/stock/the-seam-between-subdivision-levels.md).
- [`runway-earth-rss-without-runway-fix.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix.log) —
  without this mod,
  [KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders),
  [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) and
  [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer) added, and Real Solar System built from the
  sources of its release 20.1.3.0 with the change
  [`rss-20.1.3-without-its-runway-fix.diff`](non-regression/real-solar-system/the-runway-fix/rss-20.1.3-without-its-runway-fix.diff),
  which keeps its runway fix from doing anything: the protocol of
  [The test](../docs/non-regression/real-solar-system/the-runway-fix.md#the-test), played by
  [`automation/run-runway-fix.py`](automation/run-runway-fix.py), three launches, thirty loads;
  what the script printed in [`runway-earth-rss-without-runway-fix-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-without-runway-fix-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-readings.json), and the screenshots of its table, every four loads, in
  [`runway-earth-rss-without-runway-fix-tables/`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-tables/).
- [`runway-earth-rss-without-runway-fix-fix.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix.log) —
  the same install, with this mod;
  what the script printed in [`runway-earth-rss-without-runway-fix-fix-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-without-runway-fix-fix-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix-readings.json), and the screenshots of its table in
  [`runway-earth-rss-without-runway-fix-fix-tables/`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix-tables/).
- [`runway-earth-rss-as-released.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released.log) and
  [`runway-earth-rss-as-released-fix.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix.log) —
  the same instruments, Real Solar System as released, without this mod, then with it: one launch of the
  same protocol, the rover read 8 m before the edge;
  what the script printed in [`runway-earth-rss-as-released-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-as-released-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-readings.json), and
  [`runway-earth-rss-as-released-fix-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix-script.txt),
  [`runway-earth-rss-as-released-fix-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix-readings.json);
  the screenshots of the table in
  [`runway-earth-rss-as-released-table.png`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-table.png) and
  [`runway-earth-rss-as-released-fix-table.png`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix-table.png).
- [`driving-runway-earth-rss-stock.log`](checking-the-culprit-driving/driving-runway-earth-rss-stock.log) — without
  this mod,
  [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), Diag FloatingOrigin and
  KSP-MCPServer added, Real Solar System built without its runway fix as above: the protocol of the
  runway and the grass while the world moves, from `driving-runway-earth-rss.sfs`, two moves of the
  origin; what the script printed in
  [`driving-runway-earth-rss-stock-script.txt`](checking-the-culprit-driving/driving-runway-earth-rss-stock-script.txt),
  and every line it recorded in
  [`driving-runway-earth-rss-stock-lines.json`](checking-the-culprit-driving/driving-runway-earth-rss-stock-lines.json).
  Read in [Checking the statics: driving on while the world moves](../docs/checking-the-culprit-driving/the-statics.md#by-the-runway-of-the-ksc-at-cape-canaveral).
- [`driving-runway-earth-rss-diag2-fix.log`](checking-the-culprit-driving/driving-runway-earth-rss-diag2-fix.log) — the same with this mod,
  [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), Diag FloatingOrigin and
  [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer) added, Real Solar System built without its
  runway fix as above: the protocol of the runway and the grass while the world moves, played by its
  script from `driving-runway-earth-rss.sfs`, two moves of the origin; what the script printed in
  [`driving-runway-earth-rss-diag2-fix-script.txt`](checking-the-culprit-driving/driving-runway-earth-rss-diag2-fix-script.txt),
  and every line it recorded in
  [`driving-runway-earth-rss-diag2-fix-lines.json`](checking-the-culprit-driving/driving-runway-earth-rss-diag2-fix-lines.json).
  Read in [Checking the statics: driving on while the world moves](../docs/checking-the-culprit-driving/the-statics.md#by-the-runway-of-the-ksc-at-cape-canaveral).
- [`station-kourou-rss-fix.log`](non-regression/real-solar-system/a-commnet-ground-station/station-kourou-rss-fix.log) —
  [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer) added: one session, a rover driven by its `drive_to` tool
  in 500 m legs toward the CommNet ground station of Kourou, from 28.86 km to 27.30 km, then
  [`station-kourou-rss.sfs`](non-regression/real-solar-system/a-commnet-ground-station/station-kourou-rss.sfs) loaded and driven from 27.83 km to 27.30 km by
  [`automation/run-station-approach.py`](automation/run-station-approach.py). Read in
  [A CommNet ground station from a planet pack](../docs/non-regression/real-solar-system/a-commnet-ground-station.md).

## The scatter

The readings of [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter), kept as they were
logged, copied out of `KSP.log`, in the folder of the page that reads them. They are read in
[Checking the scatter: loading the same save](../docs/checking-the-culprit-loading/the-scatter.md),
[Checking the scatter: driving on while the world moves](../docs/checking-the-culprit-driving/the-scatter.md),
[Checking the scatter: in flight](../docs/checking-the-culprit-flight/the-scatter.md),
[The scatter holders](../docs/non-regression/stock/the-scatter-holders.md) and
[Kopernicus: scatter with colliders](../docs/non-regression/kopernicus/scatter-with-colliders.md).
What a record holds, line by line, is in
[the instrument's page](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md#the-log).

**The objects** — after a load, while the world moves, and over a flight — were read with Terrain
Precision Fix 0.3.0 at `logLevel = Debug`, each series played by its script through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), in three configurations named in the files:
`stock`, without this mod; `fix`, with this mod as installed, its scatter fix on; and `fix-no-scatter`,
with `fixScatter = false`, the terrain fix alone. The records were copied out of `KSP.log` by
[`extract-scatter-records.py`](automation/extract-scatter-records.py), and each series keeps beside them
what its script printed (`-script.txt`) and the number and closing line of every record it took
(`-lines.json`). With the scatter fix on, this mod wrote to `KSP.log` that it had acted on each body before
its first record, as in:

```
[TerrainPrecisionFix] Kerbin: scatter drawn from its terrain quads (first holder was +23.16 mm off)
[TerrainPrecisionFix] Mun: scatter drawn from its terrain quads (first holder was -7.51 mm off)
```

**The holder pools and the colliders** were read earlier, in three configurations: on stock, with Terrain
Precision Fix 0.1.0 alone (`tpf` in the names of the files), and with the scatter fix as well (`both`),
when it was a mod of its own, Rock Precision Fix 0.1.0, installed next to it: the same two patches, whose
lines in these logs are tagged `[RockPrecisionFix]`.

The protocols are [the scatter, load after load](../docs/checking-the-culprit-loading/the-scatter-protocol.md),
[the scatter, while the world moves](../docs/checking-the-culprit-driving/the-scatter-protocol.md)
and [the scatter, along a flight](../docs/checking-the-culprit-flight/the-scatter-protocol.md), and the
chapters *The protocol* of [The scatter
holders](../docs/non-regression/stock/the-scatter-holders.md#the-protocol)
and [Kopernicus: scatter with
colliders](../docs/non-regression/kopernicus/scatter-with-colliders.md#the-protocol).

The saves:

- [`reference-kerbin.sfs`](checking-the-culprit-loading/scatter/reference-kerbin.sfs) and [`reference-mune.sfs`](checking-the-culprit-loading/scatter/reference-mune.sfs)
  — a single Mk1 command pod landed on Kerbin, about 8 km north-west of the KSC, where the scatter is
  grass and trees, and on the Mun, where it is rocks;
- [`driving-kerbin.sfs`](checking-the-culprit-driving/driving-kerbin.sfs) — the rover of
  [the driving protocol](#the-driving-protocol), on the grass south of the runway of the KSC;
- [`cactus-kerbin.sfs`](checking-the-culprit-driving/scatter/cactus-kerbin.sfs) — the same rover in a
  desert of Kerbin, 497 m north of a cactus, facing it: the save of the film;
- [`ref-mune-5km.sfs`](checking-the-culprit-flight/scatter/ref-mune-5km.sfs) — a single Mk1 command pod in a circular equatorial
  orbit 5 km over the Mun, the same save as
  [PQSBench's](https://github.com/lhervier/KSP-PQSBench/blob/main/perfs/README.md);
- [`ref-kerbin-scatter-collider-eva.sfs`](non-regression/kopernicus/scatter-with-colliders/ref-kerbin-scatter-collider-eva.sfs) — a Mk1 command pod
  landed in a desert of Kerbin, with Jebediah out on EVA, standing on a boulder next to it.

### The scatter: the objects, over twelve loads

KSP 1.12.5 on Windows, `GameData` holding Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag -
Scatter and KSP-MCPServer, and this mod for `fix` and `fix-no-scatter`. Terrain scatter on, the log flushed at
once. Each save loaded twelve times per configuration, in a single session of KSP, by
[`run-scatter-loading.py`](automation/run-scatter-loading.py), which pressed *Record the rocks* every 3 s
after each load until every holder was built and the counts were the same twice in a row; one file per
load, holding the last record taken after it.

| load | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kerbin, `stock` | [`1`](checking-the-culprit-loading/scatter/kerbin-stock-load1.log) | [`2`](checking-the-culprit-loading/scatter/kerbin-stock-load2.log) | [`3`](checking-the-culprit-loading/scatter/kerbin-stock-load3.log) | [`4`](checking-the-culprit-loading/scatter/kerbin-stock-load4.log) | [`5`](checking-the-culprit-loading/scatter/kerbin-stock-load5.log) | [`6`](checking-the-culprit-loading/scatter/kerbin-stock-load6.log) | [`7`](checking-the-culprit-loading/scatter/kerbin-stock-load7.log) | [`8`](checking-the-culprit-loading/scatter/kerbin-stock-load8.log) | [`9`](checking-the-culprit-loading/scatter/kerbin-stock-load9.log) | [`10`](checking-the-culprit-loading/scatter/kerbin-stock-load10.log) | [`11`](checking-the-culprit-loading/scatter/kerbin-stock-load11.log) | [`12`](checking-the-culprit-loading/scatter/kerbin-stock-load12.log) |
| Kerbin, `fix-no-scatter` | [`1`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load1.log) | [`2`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load2.log) | [`3`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load3.log) | [`4`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load4.log) | [`5`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load5.log) | [`6`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load6.log) | [`7`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load7.log) | [`8`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load8.log) | [`9`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load9.log) | [`10`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load10.log) | [`11`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load11.log) | [`12`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-load12.log) |
| Kerbin, `fix` | [`1`](checking-the-culprit-loading/scatter/kerbin-fix-load1.log) | [`2`](checking-the-culprit-loading/scatter/kerbin-fix-load2.log) | [`3`](checking-the-culprit-loading/scatter/kerbin-fix-load3.log) | [`4`](checking-the-culprit-loading/scatter/kerbin-fix-load4.log) | [`5`](checking-the-culprit-loading/scatter/kerbin-fix-load5.log) | [`6`](checking-the-culprit-loading/scatter/kerbin-fix-load6.log) | [`7`](checking-the-culprit-loading/scatter/kerbin-fix-load7.log) | [`8`](checking-the-culprit-loading/scatter/kerbin-fix-load8.log) | [`9`](checking-the-culprit-loading/scatter/kerbin-fix-load9.log) | [`10`](checking-the-culprit-loading/scatter/kerbin-fix-load10.log) | [`11`](checking-the-culprit-loading/scatter/kerbin-fix-load11.log) | [`12`](checking-the-culprit-loading/scatter/kerbin-fix-load12.log) |
| the Mun, `stock` | [`1`](checking-the-culprit-loading/scatter/mun-stock-load1.log) | [`2`](checking-the-culprit-loading/scatter/mun-stock-load2.log) | [`3`](checking-the-culprit-loading/scatter/mun-stock-load3.log) | [`4`](checking-the-culprit-loading/scatter/mun-stock-load4.log) | [`5`](checking-the-culprit-loading/scatter/mun-stock-load5.log) | [`6`](checking-the-culprit-loading/scatter/mun-stock-load6.log) | [`7`](checking-the-culprit-loading/scatter/mun-stock-load7.log) | [`8`](checking-the-culprit-loading/scatter/mun-stock-load8.log) | [`9`](checking-the-culprit-loading/scatter/mun-stock-load9.log) | [`10`](checking-the-culprit-loading/scatter/mun-stock-load10.log) | [`11`](checking-the-culprit-loading/scatter/mun-stock-load11.log) | [`12`](checking-the-culprit-loading/scatter/mun-stock-load12.log) |
| the Mun, `fix-no-scatter` | [`1`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load1.log) | [`2`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load2.log) | [`3`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load3.log) | [`4`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load4.log) | [`5`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load5.log) | [`6`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load6.log) | [`7`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load7.log) | [`8`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load8.log) | [`9`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load9.log) | [`10`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load10.log) | [`11`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load11.log) | [`12`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-load12.log) |
| the Mun, `fix` | [`1`](checking-the-culprit-loading/scatter/mun-fix-load1.log) | [`2`](checking-the-culprit-loading/scatter/mun-fix-load2.log) | [`3`](checking-the-culprit-loading/scatter/mun-fix-load3.log) | [`4`](checking-the-culprit-loading/scatter/mun-fix-load4.log) | [`5`](checking-the-culprit-loading/scatter/mun-fix-load5.log) | [`6`](checking-the-culprit-loading/scatter/mun-fix-load6.log) | [`7`](checking-the-culprit-loading/scatter/mun-fix-load7.log) | [`8`](checking-the-culprit-loading/scatter/mun-fix-load8.log) | [`9`](checking-the-culprit-loading/scatter/mun-fix-load9.log) | [`10`](checking-the-culprit-loading/scatter/mun-fix-load10.log) | [`11`](checking-the-culprit-loading/scatter/mun-fix-load11.log) | [`12`](checking-the-culprit-loading/scatter/mun-fix-load12.log) |

What the script printed and what it recorded, per save and configuration:

| series | what the script printed | what it recorded |
|---|---|---|
| Kerbin, `stock` | [`kerbin-stock-script.txt`](checking-the-culprit-loading/scatter/kerbin-stock-script.txt) | [`kerbin-stock-lines.json`](checking-the-culprit-loading/scatter/kerbin-stock-lines.json) |
| Kerbin, `fix-no-scatter` | [`kerbin-fix-no-scatter-script.txt`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-script.txt) | [`kerbin-fix-no-scatter-lines.json`](checking-the-culprit-loading/scatter/kerbin-fix-no-scatter-lines.json) |
| Kerbin, `fix` | [`kerbin-fix-script.txt`](checking-the-culprit-loading/scatter/kerbin-fix-script.txt) | [`kerbin-fix-lines.json`](checking-the-culprit-loading/scatter/kerbin-fix-lines.json) |
| the Mun, `stock` | [`mun-stock-script.txt`](checking-the-culprit-loading/scatter/mun-stock-script.txt) | [`mun-stock-lines.json`](checking-the-culprit-loading/scatter/mun-stock-lines.json) |
| the Mun, `fix-no-scatter` | [`mun-fix-no-scatter-script.txt`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-script.txt) | [`mun-fix-no-scatter-lines.json`](checking-the-culprit-loading/scatter/mun-fix-no-scatter-lines.json) |
| the Mun, `fix` | [`mun-fix-script.txt`](checking-the-culprit-loading/scatter/mun-fix-script.txt) | [`mun-fix-lines.json`](checking-the-culprit-loading/scatter/mun-fix-lines.json) |

Every record of Kerbin, in the three series, ends on the same line, but for its number:

```
End of record 2: 64 quads with rocks, 118 holders (0 not built yet); nearest quad 'Kerbin Zn3010000130': 218 rocks, 1780 vertices measured, 0 without ground under them, 0 colliders measured
```

and every record of the Mun on this one:

```
End of record 26: 128 quads with rocks, 128 holders (0 not built yet); nearest quad 'Mun Zp211333000': 20 rocks, 200 vertices measured, 0 without ground under them, 0 colliders measured
```

So every record was taken once all the holders were built, and all the records of a body name the same
nearest quad: its objects and their measured vertices compare one by one from one load to the next, and
from one series to another.

### The scatter: the objects, across a move of the world

The same install, with `driving-kerbin.sfs`, by
[`run-scatter-driving.py`](automation/run-scatter-driving.py): six loads per configuration, in a single
session of KSP, one move of the origin per load, the rover stopped 498.6 m from the origin, then just after
the move, then 2.6 m farther on with no move. Each record ends on the same counts: 8 quads with rocks, 13
holders, all built, the nearest quad `Kerbin Zn3010001020` with 50 rocks and 400 vertices.

| load | before the move | after it | a few metres farther on |
|---|---|---|---|
| `stock`, 1 | [`before`](checking-the-culprit-driving/scatter/kerbin-stock-load1-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-stock-load1-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-stock-load1-again.log) |
| `stock`, 2 | [`before`](checking-the-culprit-driving/scatter/kerbin-stock-load2-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-stock-load2-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-stock-load2-again.log) |
| `stock`, 3 | [`before`](checking-the-culprit-driving/scatter/kerbin-stock-load3-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-stock-load3-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-stock-load3-again.log) |
| `stock`, 4 | [`before`](checking-the-culprit-driving/scatter/kerbin-stock-load4-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-stock-load4-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-stock-load4-again.log) |
| `stock`, 5 | [`before`](checking-the-culprit-driving/scatter/kerbin-stock-load5-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-stock-load5-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-stock-load5-again.log) |
| `stock`, 6 | [`before`](checking-the-culprit-driving/scatter/kerbin-stock-load6-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-stock-load6-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-stock-load6-again.log) |
| `fix-no-scatter`, 1 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load1-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load1-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load1-again.log) |
| `fix-no-scatter`, 2 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load2-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load2-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load2-again.log) |
| `fix-no-scatter`, 3 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load3-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load3-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load3-again.log) |
| `fix-no-scatter`, 4 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load4-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load4-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load4-again.log) |
| `fix-no-scatter`, 5 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load5-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load5-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load5-again.log) |
| `fix-no-scatter`, 6 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load6-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load6-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-load6-again.log) |
| `fix`, 1 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-load1-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-load1-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-load1-again.log) |
| `fix`, 2 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-load2-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-load2-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-load2-again.log) |
| `fix`, 3 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-load3-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-load3-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-load3-again.log) |
| `fix`, 4 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-load4-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-load4-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-load4-again.log) |
| `fix`, 5 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-load5-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-load5-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-load5-again.log) |
| `fix`, 6 | [`before`](checking-the-culprit-driving/scatter/kerbin-fix-load6-before.log) | [`after`](checking-the-culprit-driving/scatter/kerbin-fix-load6-after.log) | [`again`](checking-the-culprit-driving/scatter/kerbin-fix-load6-again.log) |

What the script printed and what it recorded, per configuration:

| series | what the script printed | what it recorded |
|---|---|---|
| `stock` | [`kerbin-stock-script.txt`](checking-the-culprit-driving/scatter/kerbin-stock-script.txt) | [`kerbin-stock-lines.json`](checking-the-culprit-driving/scatter/kerbin-stock-lines.json) |
| `fix-no-scatter` | [`kerbin-fix-no-scatter-script.txt`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-script.txt) | [`kerbin-fix-no-scatter-lines.json`](checking-the-culprit-driving/scatter/kerbin-fix-no-scatter-lines.json) |
| `fix` | [`kerbin-fix-script.txt`](checking-the-culprit-driving/scatter/kerbin-fix-script.txt) | [`kerbin-fix-lines.json`](checking-the-culprit-driving/scatter/kerbin-fix-lines.json) |

The film, with `fix-no-scatter` and KSP Diag - Floating Origin as well, by
[`film-scatter-driving.py`](automation/film-scatter-driving.py) on `cactus-kerbin.sfs`: the records just
before and just after the move that was kept,
[`cactus-fix-no-scatter-before.log`](checking-the-culprit-driving/scatter/cactus-fix-no-scatter-before.log) and
[`cactus-fix-no-scatter-after.log`](checking-the-culprit-driving/scatter/cactus-fix-no-scatter-after.log): 148 holders, all of
them `cactus`, and on the nearest quad, `Kerbin Zn2101001033`, 5 cactus and 50 vertices.

### The scatter: the objects, over a flight

Where the scatter is drawn once the terrain has kept building and destroying quads under a moving craft,
with the world origin following it. The same install, `stock` and `fix`, by
[`run-scatter-flight.py`](automation/run-scatter-flight.py): `ref-mune-5km.sfs` loaded once, then *Record
the rocks* pressed 30 s into the flight, again every two minutes, and once more after the pod crashed.

| flight | records | what the script printed | what it recorded |
|---|---|---|---|
| `stock` | [`mun-5km-stock-rocks.log`](checking-the-culprit-flight/scatter/mun-5km-stock-rocks.log) | [`mun-5km-stock-script.txt`](checking-the-culprit-flight/scatter/mun-5km-stock-script.txt) | [`mun-5km-stock-lines.json`](checking-the-culprit-flight/scatter/mun-5km-stock-lines.json) |
| `fix` | [`mun-5km-fix-rocks.log`](checking-the-culprit-flight/scatter/mun-5km-fix-rocks.log) | [`mun-5km-fix-script.txt`](checking-the-culprit-flight/scatter/mun-5km-fix-script.txt) | [`mun-5km-fix-lines.json`](checking-the-culprit-flight/scatter/mun-5km-fix-lines.json) |

Each file holds the six records. On stock, the script did not see the crash, the game keeping the wrecked
pod as the craft flown: the sixth record was taken by hand, and its line in `mun-5km-stock-lines.json` says
so. Every record has all its holders built, and 200 vertices measured on its nearest quad, all of them
with ground under them:

| record | quads with rocks, `stock` | nearest quad, `stock` | quads with rocks, `fix` | nearest quad, `fix` |
|---|---|---|---|---|
| 1 | 352 | `Mun Xn233333333` | 352 | `Mun Xn233333333` |
| 2 | 176 | `Mun Xn213333331` | 176 | `Mun Xn213333333` |
| 3 | 160 | `Mun Xn211311131` | 152 | `Mun Xn211311131` |
| 4 | 224 | `Mun Xn122002220` | 216 | `Mun Xn122002222` |
| 5 | 152 | `Mun Xn013313333` | 152 | `Mun Xn013331111` |
| 6, after the crash | 568 | `Mun Zn200000011` | 568 | `Mun Zn200000011` |

### The scatter: the holder pools, over a flight

The install of [the objects](#the-scatter-the-objects-over-twelve-loads), `stock` and `fix`, by
[`run-scatter-holders.py`](automation/run-scatter-holders.py) with `flight`: `ref-mune-5km.sfs` loaded once,
then *Record the holder pools* pressed 30 s into the flight, again every two minutes, and once more after the
pod crashed.

| flight | records | what the script printed | what it recorded |
|---|---|---|---|
| `stock` | [`mun-5km-stock-holders.log`](non-regression/stock/the-scatter-holders/mun-5km-stock-holders.log) | [`mun-5km-stock-script.txt`](non-regression/stock/the-scatter-holders/mun-5km-stock-script.txt) | [`mun-5km-stock-lines.json`](non-regression/stock/the-scatter-holders/mun-5km-stock-lines.json) |
| `fix` | [`mun-5km-fix-holders.log`](non-regression/stock/the-scatter-holders/mun-5km-fix-holders.log) | [`mun-5km-fix-script.txt`](non-regression/stock/the-scatter-holders/mun-5km-fix-script.txt) | [`mun-5km-fix-lines.json`](non-regression/stock/the-scatter-holders/mun-5km-fix-lines.json) |

With this mod, it wrote to `KSP.log` that it had acted on the Mun before the first record:

```
[TerrainPrecisionFix] Mun: terrain placed in double precision (first quad corrected by 3.32 mm)
[TerrainPrecisionFix] Mun: scatter drawn from its terrain quads (first holder was +1.65 mm off)
```

Each file holds the six records. Every record of both flights ends on `0 broken rules`:

| record | in use, `stock` | free, `stock` | in use, `fix` | free, `fix` |
|---|---|---|---|---|
| 1 | 352 | 32 | 352 | 32 |
| 2 | 176 | 208 | 168 | 216 |
| 3 | 160 | 224 | 152 | 232 |
| 4 | 224 | 160 | 216 | 168 |
| 5 | 152 | 232 | 152 | 232 |
| 6, after the crash | 568 | 40 | 568 | 40 |

### The scatter: the holder pools, across scene switches

The same install, `stock` and `fix`, by [`run-scatter-holders.py`](automation/run-scatter-holders.py) with
`scenes`. One session each: `reference-mune.sfs` loaded from the Space Center, back to the Space Center, then
`reference-kerbin.sfs`, with *Record the holder pools* pressed in each of the three scenes.

| session | records | what the script printed | what it recorded |
|---|---|---|---|
| `stock` | [`scenes-stock-holders.log`](non-regression/stock/the-scatter-holders/scenes-stock-holders.log) | [`scenes-stock-script.txt`](non-regression/stock/the-scatter-holders/scenes-stock-script.txt) | [`scenes-stock-lines.json`](non-regression/stock/the-scatter-holders/scenes-stock-lines.json) |
| `fix` | [`scenes-fix-holders.log`](non-regression/stock/the-scatter-holders/scenes-fix-holders.log) | [`scenes-fix-script.txt`](non-regression/stock/the-scatter-holders/scenes-fix-script.txt) | [`scenes-fix-lines.json`](non-regression/stock/the-scatter-holders/scenes-fix-lines.json) |

With this mod, it wrote to `KSP.log` that it had acted on each body before its first record:

```
[TerrainPrecisionFix] Kerbin: terrain placed in double precision (first quad corrected by 11.32 mm)
[TerrainPrecisionFix] Kerbin: scatter drawn from its terrain quads (first holder was +19.08 mm off)
[TerrainPrecisionFix] Mun: terrain placed in double precision (first quad corrected by 8.57 mm)
[TerrainPrecisionFix] Mun: scatter drawn from its terrain quads (first holder was +7.86 mm off)
```

Every record of both sessions ends on `0 in no pool` and `0 broken rules`, with the same counts:

| record | scene | pools | holders in use | free |
|---|---|---|---|---|
| 1 | the Mun | the Mun's `Rock00` | 128 | 32 |
| 2 | the Space Center | Kerbin's `Tree00`, `Grass00`, `boulder`, `Pine00`, `cactus` | 3 | 317 |
| 3 | Kerbin | the same five | 118 | 202 |

### The scatter: the colliders

A different install, because stock scatter has no collider: the one of
[the objects](#the-scatter-the-objects-over-twelve-loads), plus
[Kopernicus](https://github.com/Kopernicus/Kopernicus) 1.12.1-247, ModularFlightIntegrator 1.2.10 and
KSPTextureLoader 1.0.36, which it needs, and the
[Stock Scatter Collider Enabler Patch](https://github.com/Poodmund/Stock-Scatter-Collider-Enabler-Patch)
1.0.1, which gives every stock object of scatter a collision mesh of its own shape. Three series, `stock`,
`fix-no-scatter` and `fix`, by [`run-scatter-loading.py`](automation/run-scatter-loading.py):
`ref-kerbin-scatter-collider-eva.sfs` loaded six times in one session each, each load with a record and a
picture of the kerbal's feet, the camera set to the same viewpoint before each (`--camera 0.75 75.63 -6.42
60`).

| load | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `stock` | [`1`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.log) | [`2`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.log) | [`3`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.log) | [`4`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.log) | [`5`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.log) | [`6`](non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.log) |
| its pictures | [`1`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load1.png) | [`2`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load2.png) | [`3`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load3.png) | [`4`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load4.png) | [`5`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load5.png) | [`6`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-stock-load6.png) |
| `fix-no-scatter` | [`1`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load1.log) | [`2`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load2.log) | [`3`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load3.log) | [`4`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load4.log) | [`5`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load5.log) | [`6`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load6.log) |
| its pictures | [`1`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load1.png) | [`2`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load2.png) | [`3`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load3.png) | [`4`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load4.png) | [`5`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load5.png) | [`6`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-load6.png) |
| `fix` | [`1`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load1.log) | [`2`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load2.log) | [`3`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load3.log) | [`4`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load4.log) | [`5`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load5.log) | [`6`](non-regression/kopernicus/scatter-with-colliders/collider-fix-load6.log) |
| its pictures | [`1`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-load1.png) | [`2`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-load2.png) | [`3`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-load3.png) | [`4`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-load4.png) | [`5`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-load5.png) | [`6`](../imgs/non-regression/kopernicus/scatter-with-colliders/collider-fix-load6.png) |

| series | what the script printed | what it recorded |
|---|---|---|
| `stock` | [`collider-stock-script.txt`](non-regression/kopernicus/scatter-with-colliders/collider-stock-script.txt) | [`collider-stock-lines.json`](non-regression/kopernicus/scatter-with-colliders/collider-stock-lines.json) |
| `fix-no-scatter` | [`collider-fix-no-scatter-script.txt`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-script.txt) | [`collider-fix-no-scatter-lines.json`](non-regression/kopernicus/scatter-with-colliders/collider-fix-no-scatter-lines.json) |
| `fix` | [`collider-fix-script.txt`](non-regression/kopernicus/scatter-with-colliders/collider-fix-script.txt) | [`collider-fix-lines.json`](non-regression/kopernicus/scatter-with-colliders/collider-fix-lines.json) |

Every record of the three series ends on the same line, but for its number:

```
End of record 2: 173 quads with rocks, 306 holders (0 not built yet); nearest quad 'Kerbin Xn0131000203': 6 rocks, 60 vertices measured, 0 without ground under them, 6 colliders measured
```

The same nearest quad throughout, carrying the same six objects with a collider — one `boulder` and five
`cactus` — so they compare one by one from one load to the next, and from one series to another.
