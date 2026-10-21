# The runs: the statics

Part of [Terrain Precision Fix](../../README.md), [the statics](../../docs/statics/README.md): the saves, the scripts and the `KSP.log` of every session, without this mod and with it. The scripts are in [`automation/`](automation).

## The runway protocol

The install of [The loading protocol](../ground/README.md#the-loading-protocol): the six loadings of
[the runway protocol](../../docs/statics/checking/loading-protocol.md), played by its script,
[`run-runway.py`](automation/run-runway.py). Read in
[Checking the statics: loading the same save](../../docs/statics/checking/loading.md).

The saves:

- [`runway-kerbin.sfs`](checking/loading/runway-kerbin.sfs) — two identical craft, one on
  the grass beside the runway of the KSC and one on the runway, 152 m apart;
- [`runway-mun-kk.sfs`](checking/loading/runway-mun-kk.sfs) — the same on the Mun: one craft
  on a runway placed by [Kerbal Konstructs](https://github.com/KSP-RO/Kerbal-Konstructs) 1.12.3 and one
  on the ground 42 m away. The runway itself is in the two files of
  [`runway-mun-kk/GameData/KerbalKonstructs/NewInstances/`](checking/loading/runway-mun-kk/GameData/KerbalKonstructs/NewInstances/):
  copy that `GameData` into the folder of KSP, over its own, before loading the save. Made by
  [Making the save on the Mun](../../docs/statics/checking/making-the-mun-save.md).

The logs, without this mod (`-stock`) and with it (`-fix`):

- [`runway-stock.log`](checking/loading/runway-stock.log) and
  [`runway-fix.log`](checking/loading/runway-fix.log) — on Kerbin, `runway-kerbin.sfs`; what
  the script printed in [`runway-stock-script.txt`](checking/loading/runway-stock-script.txt)
  and [`runway-fix-script.txt`](checking/loading/runway-fix-script.txt), and every line it
  recorded, in both instruments, in [`runway-stock-lines.json`](checking/loading/runway-stock-lines.json)
  and [`runway-fix-lines.json`](checking/loading/runway-fix-lines.json).
- [`runway-mun-kk-stock.log`](checking/loading/runway-mun-kk-stock.log) and
  [`runway-mun-kk-fix.log`](checking/loading/runway-mun-kk-fix.log) — on the Mun,
  `runway-mun-kk.sfs`, Kerbal Konstructs 1.12.3 added to the install with CustomPreLaunchChecks 1.8.1;
  what the script printed in [`runway-mun-kk-stock-script.txt`](checking/loading/runway-mun-kk-stock-script.txt)
  and [`runway-mun-kk-fix-script.txt`](checking/loading/runway-mun-kk-fix-script.txt), and
  every line it recorded in [`runway-mun-kk-stock-lines.json`](checking/loading/runway-mun-kk-stock-lines.json)
  and [`runway-mun-kk-fix-lines.json`](checking/loading/runway-mun-kk-fix-lines.json).

## The protocol of the runway and the grass while the world moves

The install of [The driving protocol](../ground/README.md#the-driving-protocol): the moves of the origin of
[the protocol of the runway and the grass while the world moves](../../docs/statics/checking/driving-protocol.md),
played by its script, [`run-driving-runway.py`](automation/run-driving-runway.py), from
[`driving-runway-kerbin.sfs`](checking/driving/driving-runway-kerbin.sfs), `Diag2-Rover`
alone on the grass by the north edge of the runway of the KSC. Read in
[Checking the statics: driving on while the world moves](../../docs/statics/checking/driving.md#by-the-runway-of-the-ksc). Earth is under
[On Real Solar System](#on-real-solar-system).

- [`driving-runway-stock.log`](checking/driving/driving-runway-stock.log) — without this mod,
  three moves; what the script printed in
  [`driving-runway-stock-script.txt`](checking/driving/driving-runway-stock-script.txt), and
  every line it recorded in [`driving-runway-stock-lines.json`](checking/driving/driving-runway-stock-lines.json).
- [`driving-runway-diag2-fix.log`](checking/driving/driving-runway-diag2-fix.log) — this mod as it is
  installed; what the script printed in
  [`driving-runway-diag2-fix-script.txt`](checking/driving/driving-runway-diag2-fix-script.txt), and every
  line it recorded in [`driving-runway-diag2-fix-lines.json`](checking/driving/driving-runway-diag2-fix-lines.json).
- [`driving-runway-diag2-fix-terrain-only.log`](checking/driving/driving-runway-diag2-fix-terrain-only.log) —
  an earlier run, with an earlier version of the script, this mod with `fixStatics = false`; what the
  script printed in
  [`driving-runway-diag2-fix-terrain-only-script.txt`](checking/driving/driving-runway-diag2-fix-terrain-only-script.txt),
  and every line it recorded in
  [`driving-runway-diag2-fix-terrain-only-lines.json`](checking/driving/driving-runway-diag2-fix-terrain-only-lines.json).

## The launch pad protocol

KSP 1.12.5 with the Making History expansion, Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) and KSP-Util-MCPServer,
without this mod and with it: six launches of
[`Capsule.craft`](checking/launch-pad/Capsule.craft), a Mk1 command pod on an FL-T100 tank,
from the Desert Launch Site, one session of the game each, by the script of
[the launch pad protocol](../../docs/statics/checking/launch-pad-protocol.md),
[`run-launch-pad.py`](automation/run-launch-pad.py). Read in
[Launching from a launch pad of Making History](../../docs/statics/checking/launch-pad.md).

- [`launch-pad-stock-1.log`](checking/launch-pad/launch-pad-stock-1.log), [`launch-pad-stock-2.log`](checking/launch-pad/launch-pad-stock-2.log), [`launch-pad-stock-3.log`](checking/launch-pad/launch-pad-stock-3.log), [`launch-pad-stock-4.log`](checking/launch-pad/launch-pad-stock-4.log), [`launch-pad-stock-5.log`](checking/launch-pad/launch-pad-stock-5.log) and [`launch-pad-stock-6.log`](checking/launch-pad/launch-pad-stock-6.log) — the `KSP.log`
  of each session without this mod; what the script printed in
  [`launch-pad-stock-script.txt`](checking/launch-pad/launch-pad-stock-script.txt), and every
  line it recorded in [`launch-pad-stock-lines.json`](checking/launch-pad/launch-pad-stock-lines.json).
- [`launch-pad-fix-1.log`](checking/launch-pad/launch-pad-fix-1.log), [`launch-pad-fix-2.log`](checking/launch-pad/launch-pad-fix-2.log), [`launch-pad-fix-3.log`](checking/launch-pad/launch-pad-fix-3.log), [`launch-pad-fix-4.log`](checking/launch-pad/launch-pad-fix-4.log), [`launch-pad-fix-5.log`](checking/launch-pad/launch-pad-fix-5.log) and [`launch-pad-fix-6.log`](checking/launch-pad/launch-pad-fix-6.log) — the same
  with this mod; what the
  script printed in [`launch-pad-fix-script.txt`](checking/launch-pad/launch-pad-fix-script.txt), and every line
  it recorded in [`launch-pad-fix-lines.json`](checking/launch-pad/launch-pad-fix-lines.json).

## The altitude where KSP turns the body

Without this mod: KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin) and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer); on the stock system, then with Real Solar
System 20.1.3.0 and what it requires, then with Outer Planets Mod 2.2.12, Kopernicus 248, Modular Flight
Integrator and KSPTextureLoader as for Real Solar System, and the Community Terrain Texture Pack 1.0.5.

- [`rotation-thresholds.txt`](non-regression/stock/a-static-turning-with-its-body/rotation-thresholds.txt) — what
  [`automation/run-rotation-threshold.py`](automation/run-rotation-threshold.py) printed, body by body:
  a craft moved from orbit to orbit, the altitude above which KSP turns the body rather than the world.
  No log kept: the readings are the script's. Read in
  [A static turning with its body](../../docs/statics/non-regression/stock/a-static-turning-with-its-body.md).

## The scene changes protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), this mod at
`logLevel = Debug`,
and KSP-Util-MCPServer, which plays the test through [`automation/run-scene-changes.py`](automation/run-scene-changes.py):
a new career at the Custom difficulty (on Kerbin, the same as [`career-with-the-parts.sfs`](non-regression/stock/destroyed-buildings/career-with-the-parts.sfs)),
`Diag3-Rocket.craft` on the launchpad, eleven arrivals in flight through every way of leaving
it, and `Diag3-Rover.craft` launched from the SPH onto the runway; one script per way in
[`automation/scene-changes/`](automation/scene-changes/). On Earth, Real Solar System 20.1.3.0 and what it
requires (Kopernicus 248, Modular Flight Integrator,
KSPTextureLoader, the RSS textures). Each one played again without this mod. Read in
[Scene changes](../../docs/statics/non-regression/stock/scene-changes.md).

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
and KSP-Util-MCPServer, which plays the test through
[`automation/run-destroyed-buildings.py`](automation/run-destroyed-buildings.py): a new career at the Custom
difficulty (the same as [`career-with-the-parts.sfs`](non-regression/stock/destroyed-buildings/career-with-the-parts.sfs), which a player can start
from), [`VAB-Dropper.craft`](non-regression/stock/destroyed-buildings/VAB-Dropper.craft) dropped twice onto the VAB from the
launchpad, `Diag3-Rover.craft` launched from the SPH onto the runway around the VAB in ruins, the VAB
repaired, and `Diag3-Rocket.craft` launched from it; three arrivals on the launchpad, two on the runway.
Played again without this mod. Read in
[Destroyed buildings](../../docs/statics/non-regression/stock/destroyed-buildings.md).

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
and KSP-Util-MCPServer, which plays the test through
[`automation/run-facility-levels.py`](automation/run-facility-levels.py): a new career at the Custom
difficulty (the same as [`career-with-the-parts.sfs`](non-regression/stock/destroyed-buildings/career-with-the-parts.sfs)), `Diag3-Rocket.craft` launched onto the launchpad and `Diag3-Rover.craft` onto the runway, four
arrivals on each at each of their three levels. Played again without this mod. Read in
[Facility levels](../../docs/statics/non-regression/stock/facility-levels.md).

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
`logLevel = Debug`, and KSP-Util-MCPServer, which plays the test through
[`automation/run-time-warp.py`](automation/run-time-warp.py): a new sandbox game, `Diag3-Rover.craft`
launched from the SPH onto the runway, three days of time warp at 100 000×, then *Warp To* the night and
the next noon at the KSC; four readings, a screenshot at each. Played again without this mod. Read in
[Time warp](../../docs/statics/non-regression/stock/time-warp.md) and
[The lights of the KSC](../../docs/statics/non-regression/stock/the-lights-of-the-ksc.md).

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
and KSP-Util-MCPServer, which plays the test through
[`automation/run-time-warp-flyover.py`](automation/run-time-warp-flyover.py): the capsule of
[`warp-static-mun-kk.sfs`](non-regression/stock/time-warp/warp-static-mun-kk.sfs) on that launch pad, near the highest point of the Mun's
equator, read before and after `Diag3-Rover.craft`, put on a low orbit of the Mun, passes over it in time
warp at 10×. Played again without this mod. Read in
[Time warp](../../docs/statics/non-regression/stock/time-warp.md#in-flight-low-over-a-static).

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

## On the stock system

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, this mod and one instrument.

- [`runway-mun-kk-colliders-fix.log`](checking/loading/runway-mun-kk-colliders-fix.log) — four loadings of
  `runway-mun-kk.sfs`, every collider under each craft listed at each loading, with its height above the terrain
  KSP computes there.
- [`flight-basics-fix.log`](non-regression/kerbal-konstructs/a-ground-station-opened-in-flight/flight-basics-fix.log) — no instrument, this mod at
  `logLevel = Debug`: KSP started, then *Training → Flight Basics* from the main menu, straight into
  flight on the launchpad, and back to the main menu. Read in
  [Kerbal Konstructs: a ground station opened in flight](../../docs/statics/non-regression/kerbal-konstructs/a-ground-station-opened-in-flight.md#why).

## With Kerbal Konstructs

KSP 1.12.5 with the Making History expansion, Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Kerbal Konstructs](https://github.com/KSP-RO/Kerbal-Konstructs) 1.12.3 and CustomPreLaunchChecks 1.8.1,
which it requires, no instrument, this mod at `logLevel = Debug`.

- [`kk-group-editor-fix.log`](limits/kerbal-konstructs/the-group-editor/kk-group-editor-fix.log) — `non-reg-runway-mune-kk.sfs`, its
  runway in `GameData/KerbalKonstructs/NewInstances`: the group moved with the gizmo of the group editor,
  saved with *Save&Close*, then the save loaded again. Read in
  [Kerbal Konstructs: the group editor](../../docs/statics/limits/kerbal-konstructs/the-group-editor.md).
- [`kk-ground-station-fix.log`](non-regression/kerbal-konstructs/a-ground-station-opened-in-flight/kk-ground-station-fix.log) —
  [`kk-ground-station.sfs`](non-regression/kerbal-konstructs/a-ground-station-opened-in-flight/kk-ground-station.sfs), a career game, a pod on the launchpad: a water tower
  of Kerbal Konstructs set up beside it, in flight, as a closed CommNet ground station, then opened from
  the facility manager of Kerbal Konstructs. Read in
  [Kerbal Konstructs: a ground station opened in flight](../../docs/statics/non-regression/kerbal-konstructs/a-ground-station-opened-in-flight.md).

## With Kopernicus

KSP 1.12.5 with the Making History expansion, Harmony, ModuleManager, KSP Community Fixes 1.41.1 and
[Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 with what it requires (Kopernicus
248, Modular Flight Integrator, KSPTextureLoader, the RSS textures), no instrument. Each
session plays the mission [`kopernicus-flag-fix/Missions/KSC flag fix`](limits/kopernicus/the-flag-fix/Missions)
once, as described in [Seeing the patch](../../docs/statics/limits/kopernicus/the-flag-fix.md#seeing-the-patch).

- [`kopernicus-flag-fix-without-this-mod.log`](limits/kopernicus/the-flag-fix/kopernicus-flag-fix-without-this-mod.log) —
  without this mod.
- [`kopernicus-flag-fix-patch-off.log`](limits/kopernicus/the-flag-fix/kopernicus-flag-fix-patch-off.log) — this mod at
  `logLevel = Debug`, with `patchKopernicus = false`.
- [`kopernicus-flag-fix-patch-on.log`](limits/kopernicus/the-flag-fix/kopernicus-flag-fix-patch-on.log) — this mod at
  `logLevel = Debug`, with its defaults.

## On Real Solar System

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, plus [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 and what
it requires (Kopernicus, Modular Flight Integrator, KSPTextureLoader, the RSS textures), as released
unless said otherwise. This mod ran at `logLevel = Debug`, so each log also holds one line per quad
placed, with how far it was moved. The sessions marked *first safeguard* ran with its first version,
a fixed metre, and hold the line where it refused part of Earth's terrain.

- [`kopernicus-flag-glitch-without-this-mod.log`](limits/kopernicus/the-flag-fix/kopernicus-flag-glitch-without-this-mod.log),
  [`kopernicus-flag-glitch-statics-fix.log`](limits/kopernicus/the-flag-fix/kopernicus-flag-glitch-statics-fix.log) and
  [`kopernicus-flag-glitch-statics-fix-off.log`](limits/kopernicus/the-flag-fix/kopernicus-flag-glitch-statics-fix-off.log) —
  MechJeb2 2.15.3 added to the first and the third, and Kopernicus built from the sources of its release
  248 with the change
  [`kopernicus-248-without-its-flag-fix.diff`](limits/kopernicus/the-flag-fix/kopernicus-248-without-its-flag-fix.diff),
  which turns its flag fix off: a craft on the launchpad at Cape Canaveral, without this mod, then with
  it, then with its statics fix turned off. Read in
  [The flag glitch](../../docs/statics/limits/kopernicus/the-flag-fix.md#the-flag-glitch).

- [`runway-earth-rss-without-runway-fix.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix.log) —
  without this mod,
  [KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders),
  [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) and
  [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer) added, and Real Solar System built from the
  sources of its release 20.1.3.0 with the change
  [`rss-20.1.3-without-its-runway-fix.diff`](non-regression/real-solar-system/the-runway-fix/rss-20.1.3-without-its-runway-fix.diff),
  which keeps its runway fix from doing anything: the protocol of
  [The test](../../docs/statics/non-regression/real-solar-system/the-runway-fix.md#the-test), played by
  [`automation/run-runway-fix.py`](automation/run-runway-fix.py), three launches, thirty loads;
  what the script printed in [`runway-earth-rss-without-runway-fix-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-without-runway-fix-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-readings.json), and the screenshots of its table, every four loads, in
  [`runway-earth-rss-without-runway-fix-tables/`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-tables/).
- [`runway-earth-rss-without-runway-fix-fix.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix.log) —
  the same install, with this mod;
  what the script printed in [`runway-earth-rss-without-runway-fix-fix-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-without-runway-fix-fix-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix-readings.json), and the screenshots of its table in
  [`runway-earth-rss-without-runway-fix-fix-tables/`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-without-runway-fix-fix-tables/).
- [`runway-earth-rss-as-released.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released.log) —
  the same instruments, Real Solar System as released, without this mod: one launch of the same protocol,
  six loads (`--launches 1 --reloads 6`); its last two readings, a taxi played with the witness still
  parked, which keeps the floating origin from moving, are not used;
  what the script printed in [`runway-earth-rss-as-released-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-as-released-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-readings.json), and the screenshots of its table in
  [`runway-earth-rss-as-released-tables/`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-tables/).
- [`runway-earth-rss-as-released-taxi.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-taxi.log) —
  the same install: the taxi alone, before any witness is parked (`--launches 0 --taxi 1500`);
  what the script printed in [`runway-earth-rss-as-released-taxi-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-taxi-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-as-released-taxi-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-taxi-readings.json), and the screenshot of its table in
  [`runway-earth-rss-as-released-taxi-tables/`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-taxi-tables/).
- [`runway-earth-rss-as-released-fix.log`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix.log) —
  the same install, with this mod: the taxi first, then the six loads
  (`--launches 1 --reloads 6 --taxi 1500`);
  what the script printed in [`runway-earth-rss-as-released-fix-script.txt`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix-script.txt), every line of Diag Terrain Height in
  [`runway-earth-rss-as-released-fix-readings.json`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix-readings.json), and the screenshots of its table in
  [`runway-earth-rss-as-released-fix-tables/`](non-regression/real-solar-system/the-runway-fix/runway-earth-rss-as-released-fix-tables/).
- [`driving-runway-earth-rss-stock.log`](checking/driving/driving-runway-earth-rss-stock.log) — without
  this mod,
  [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), Diag FloatingOrigin and
  KSP-Util-MCPServer added, Real Solar System built without its runway fix as above: the protocol of the
  runway and the grass while the world moves, from `driving-runway-earth-rss.sfs`, two moves of the
  origin; what the script printed in
  [`driving-runway-earth-rss-stock-script.txt`](checking/driving/driving-runway-earth-rss-stock-script.txt),
  and every line it recorded in
  [`driving-runway-earth-rss-stock-lines.json`](checking/driving/driving-runway-earth-rss-stock-lines.json).
  Read in [Checking the statics: driving on while the world moves](../../docs/statics/checking/driving.md#by-the-runway-of-the-ksc-at-cape-canaveral).
- [`driving-runway-earth-rss-diag2-fix.log`](checking/driving/driving-runway-earth-rss-diag2-fix.log) — the same with this mod,
  [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), Diag FloatingOrigin and
  [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer) added, Real Solar System built without its
  runway fix as above: the protocol of the runway and the grass while the world moves, played by its
  script from `driving-runway-earth-rss.sfs`, two moves of the origin; what the script printed in
  [`driving-runway-earth-rss-diag2-fix-script.txt`](checking/driving/driving-runway-earth-rss-diag2-fix-script.txt),
  and every line it recorded in
  [`driving-runway-earth-rss-diag2-fix-lines.json`](checking/driving/driving-runway-earth-rss-diag2-fix-lines.json).
  Read in [Checking the statics: driving on while the world moves](../../docs/statics/checking/driving.md#by-the-runway-of-the-ksc-at-cape-canaveral).
- [`station-kourou-rss-fix.log`](non-regression/real-solar-system/a-commnet-ground-station/station-kourou-rss-fix.log) —
  [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer) added: one session, a rover driven by its `drive_to` tool
  in 500 m legs toward the CommNet ground station of Kourou, from 28.86 km to 27.30 km, then
  [`station-kourou-rss.sfs`](non-regression/real-solar-system/a-commnet-ground-station/station-kourou-rss.sfs) loaded and driven from 27.83 km to 27.30 km by
  [`automation/run-station-approach.py`](automation/run-station-approach.py). Read in
  [A CommNet ground station from a planet pack](../../docs/statics/non-regression/real-solar-system/a-commnet-ground-station.md).
