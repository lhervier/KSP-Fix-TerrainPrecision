# Scene changes

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#non-regression-tests): one non-regression test, on stock.

**Status: checked on Kerbin and on Earth in Real Solar System.** With this mod, after every way of
leaving a flight and coming back to the craft on the launchpad, the launchpad is where it was, within
0.14 mm; without it, it moves by up to 121 mm on Kerbin and 599 mm on Earth. A craft launched from the
VAB stands on the launchpad, one launched from the SPH on the runway, and every building of the space
centre opens.

*Why.* This mod takes the KSC out of its terrain sphere in flight, near a craft, and has to put it back
before every scene change: the next scene, and the next flight, look for it under its sphere
([The fix: the statics](../../the-fix.md)): KSP finds the buildings of the KSC by their place
in the hierarchy below it, and places a new craft on a spawn point that hangs from it, on the launchpad or
on the runway. A craft leaving for another body takes the KSC out of
its reach: it goes back under its sphere on the way, and has to come out again when the player switches
back to a craft near it.

## The test

A new career at the Custom difficulty, set up for the two craft below to be built: the largest starting
funds and science (500 000 and 5 000), funds penalties at 10 %, *Bypass Entry Purchase After Research* on;
the Research and Development upgraded twice, to its last level, and the nodes the craft need researched;
every other facility at its first level. On Kerbin, that career is
[`career-with-the-parts.sfs`](../../../../diag/statics/non-regression/stock/destroyed-buildings/career-with-the-parts.sfs): copied as `persistent.sfs` into
a new folder of `saves`, it opens at the space centre. A craft on the launchpad, then, in turn, leaving the
flight and coming back to the craft each time:

1. *Revert to Launch*, twice;
2. a quicksave (F5), then a quickload of it (F9), twice;
3. the space centre: the Astronaut Complex, the Research and Development, Mission Control and the
   Administration, each opened and closed; then the Tracking Station, entered through its building, and
   the craft flown from there;
4. the space centre again, the Vehicle Assembly Building entered through its building, and a launch;
5. *Revert to Vehicle Assembly Building*, and a launch;
6. *Recover*, and a launch from the space centre;
7. *Quit to Main Menu*, and the game loaded back into the flight of the craft;
8. the space centre again, the Space Plane Hangar entered through its building, and a second craft, a
   rover, launched from it onto the runway, its brakes put on at once; the rover then put on a circular
   orbit 100 km above the Mun (`Alt+F12 → Cheats → Set Orbit`; on Earth, the Moon), and the player
   switched back to the craft on the launchpad from the map view (*Switch To*).

That makes eleven arrivals of the craft on the launchpad, with the launch that starts the game, and one of
the rover on the runway. At each one, once the craft has settled,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) records a line (its button
*Record*): the ground under the craft, the launchpad or the runway, and the ground KSP computes for the same
spot. In a sandbox game, three of the buildings of step 3 only show a dialog saying they are closed in that
mode: hence the career.

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag - Terrain Height, and this mod
with its defaults at `logLevel = Debug`; on Earth, Real Solar System 20.1.3.0 and what it requires
(Kopernicus 248, Modular Flight Integrator, KSPTextureLoader, the RSS textures). Then the same without this
mod.

*Played by a script.* [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer) plays the test through
[`diag/statics/automation/run-scene-changes.py`](../../../../diag/statics/automation/run-scene-changes.py), with
[`Diag3-Rocket.craft`](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/craft/Diag3-Rocket.craft)
in the `Ships/VAB` folder of the game and
[`Diag3-Rover.craft`](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/craft/Diag3-Rover.craft)
in its `Ships/SPH` folder: it starts and sets up the career itself from the main menu, and closes the
guide of a new career by its button wherever it shows; it takes a screenshot of the table of Diag Terrain
Height at the end. Each way of leaving the flight is a script of its
own, in [`diag/statics/automation/scene-changes/`](../../../../diag/statics/automation/scene-changes/), that can also be played
alone. Every step is one a player can take: the test
plays just as well by hand, pressing *Record* of Diag Terrain Height at each arrival.

## The result

The height of the launchpad under the craft, lowest and highest over its eleven arrivals:

| | without this mod | with this mod |
|---|---|---|
| Kerbin | 2 660.817 to 2 781.323 mm (120.506 mm) | 2 747.132 to 2 747.237 mm (0.105 mm) |
| Earth | 3 302.721 to 3 901.777 mm (599.056 mm) | 3 581.686 to 3 581.821 mm (0.135 mm) |

Back from the other body, the launchpad reads 2 693.563 mm on Kerbin and 3 465.798 mm on Earth without
this mod, 2 747.222 mm and 3 581.782 mm with it: within 0.009 mm of the arrival before it on Kerbin, and
0.030 mm on Earth.

The rover, launched from the SPH, stands on the runway: the runway is under it, 4 031.609 mm above the
terrain on Kerbin and 3 905.569 mm on Earth without this mod, 4 064.285 mm and 3 861.164 mm with it. One
launch from the SPH per session gives one reading, not a spread.

Without this mod, KSP places the KSC again at every arrival, rounded each time in a different way
([The culprits: the statics](../../the-culprit.md)). With it, the KSC comes back to the same place,
whichever way the flight was left.

*The log lines quoted on this page come from runs of an earlier version of this mod, when its log prefix was `[TerrainPrecisionFix]`; it is now `[KSPFixTerrainPrecision]`.*

Only the statics within reach of the craft are taken out: on Kerbin, the KSC alone, the Island Airfield,
33 km away, staying under its sphere; on Earth, the KSC and the tracking station of Cape Canaveral.
Before ten of the eleven exits from the flight, the log shows the KSC put back, just before the scene
change; after each arrival, taken out again:

```
[TerrainPrecisionFix] [DEBUG] Kerbin static 'KSC': back under its sphere
[HighLogic]: =========================== Scene Change : From FLIGHT to SPACECENTER =====================
```

Before the last one, the switch back from the other body, the KSC is already under its sphere: it went
back as soon as the second craft reached the Mun, out of its reach. It comes out again once the flight
is open on the craft on the launchpad. Stripped of the rest:

```
setting new dominant body: Mun
[TerrainPrecisionFix] [DEBUG] Kerbin static 'KSC': back under its sphere
[HighLogic]: =========================== Scene Change : From FLIGHT to FLIGHT =====================
[TerrainPrecisionFix] [DEBUG] Kerbin static 'KSC': out of its sphere, corrected by 121.10 mm
```

At the space centre, every building opens and closes as without this mod, and the recovery report places
the craft on the launchpad.

The logs with this mod show errors that the logs without it do not show this time, all of the interface of
the game, and none of them about the statics:

- on Kerbin and on Earth, a `NullReferenceException` of the Knowledge Base when the map view changes its
  focus (`KnowledgeBase.OnMapFocusChange`), which an earlier session on Earth without this mod shows too
  ([`scene-changes-earth-rss-without-this-mod-earlier.log`](../../../../diag/statics/non-regression/stock/scene-changes/scene-changes-earth-rss-without-this-mod-earlier.log)),
  and so does the session of [Destroyed buildings](destroyed-buildings.md) without this mod;
- on Earth, as KSP quits at the end of the session, a `NullReferenceException` of the tooltip of a crew
  hatch (`CrewHatchController.HideTooltip`);
- on Kerbin, more of the `NullReferenceException` of KSP Community Fixes as the pointer passes over a part
  in the map view (`BlockMapViewPartClick`), which every log shows, with this mod and without it: 18
  against 9 on Kerbin, 18 each on Earth.

Leaving the space centre within its first frames loses the anchor of its camera for the rest of the
session, a bug of the game without this mod, which a script going straight on would trigger:
KSP-Util-MCPServer hands the script back at the space centre only once its camera has taken its place.

The logs, what the script printed, every line of Diag Terrain Height and a screenshot of its table are in
[`diag/statics/non-regression/stock/scene-changes/`](../../../../diag/statics/README.md#the-scene-changes-protocol).
