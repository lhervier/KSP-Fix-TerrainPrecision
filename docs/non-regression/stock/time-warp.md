# Time warp

Part of [Terrain Precision Fix](../../../README.md), one test of [Non-regression tests](../../non-regression.md), on [stock](../stock.md).

**Status: checked on Kerbin and on the Mun.** On the ground, a craft on the runway through three days of time
warp at the highest rate, then a night and a day: the KSC stays out of its sphere throughout, and the runway
stays within 0.12 mm under the craft, as without this mod. In flight, a craft passing 3 km over a static of
the Mun in time warp on rails: the static follows it out of its sphere and back, and a capsule standing on it
reads it within 0.008 mm before and after the pass, against 10.7 mm without this mod.

*Why.* Time warp does not turn the body under a static this mod has taken out of its sphere. Whether KSP
turns the body or the world around the craft depends on the craft's altitude alone, not on the time warp
(`OrbitPhysicsManager.checkReferenceFrame`), and no body turns while a craft is near enough for a static to
be out of its sphere ([A static turning with its body](a-static-turning-with-its-body.md)). What time warp
does change depends on where the craft is:

- **on the ground**, the floating origin does not move: KSP moves it at every frame at the highest rates,
  but not for a craft landed or splashed (`FloatingOrigin.FixedUpdate`), so time warp gives this mod nothing
  to do. The craft goes on rails, then off rails onto the ground; and days and nights go by, which switch
  lights of the KSC on and off ([The lights of the KSC](the-lights-of-the-ksc.md)). The test checks that
  nothing in them moves the KSC, or puts it back under its sphere;
- **in flight**, from the lowest rate on rails, 5×, KSP moves the floating origin at every frame, and a
  craft covers kilometres in a second. Every move of the origin moves the terrain sphere, and this mod moves
  each static out of it along
  ([Keeping a static out of its sphere in place](../../the-fix-statics.md#keeping-a-static-out-of-its-sphere-in-place)):
  if it missed one, the static would be left behind, and this mod would take where it was left as its new
  place. On Kerbin, KSP does not allow time warp on rails in the atmosphere, so no craft flies in time warp
  near the KSC: the test is played on the Mun, which has no atmosphere.

## On the ground

### The test

A new sandbox game, its universal time set to 3 600 s, in daylight at the KSC. Then:

1. [`Diag3-Rover.craft`](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/craft/Diag3-Rover.craft)
   launched from the SPH onto the runway, its brakes put on at once;
2. time warp on rails at the highest rate, 100 000×, with the `.` key, for three days of Kerbin, then back
   to normal time with the `,` key;
3. *Warp To* the night at the KSC, nine tenths into its day (noon being half);
4. *Warp To* the next noon at the KSC.

At the launch and at the end of each warp, once the craft has settled,
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) records a line (its button
*Record*): the ground under the craft, the runway, and the ground KSP computes for the same spot.

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, KSP Diag - Terrain Height, and this mod
with its defaults at `logLevel = Debug`. Then the same without this mod.

*Played by a script.* [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer) plays the test through
[`diag/automation/run-time-warp.py`](../../../diag/automation/run-time-warp.py), the rover in the
`Ships/SPH` folder of the game: it starts the game itself from the main menu, and takes a screenshot of the
table of Diag Terrain Height at the end. *Warp To* is the one of the
map view, or of an alarm. Every step is one a player can take: the test plays just as well by hand.

### The result

In the log with this mod, the KSC is taken out of its sphere once, as the rover arrives on the runway, and
goes back under it only when the game leaves the flight for the space centre, after the test. Nothing in
between, through the three days at 100 000× and the two *Warp To*:

```
[TerrainPrecisionFix] [DEBUG] Kerbin static 'KSC': out of its sphere, corrected by 3.17 mm
Warping to UT:137318.0. Max Rate Allowed: 5.0x.
Real-time resumed. Current UT is: 137318.0. TgtUT Error is -0.0137s. (Undershot)
Warping to UT:150278.0. Max Rate Allowed: 5.0x.
Real-time resumed. Current UT is: 150278.0. TgtUT Error is -0.0115s. (Undershot)
[TerrainPrecisionFix] [DEBUG] Kerbin static 'KSC': back under its sphere
```

The height of the runway under the rover above the ground KSP computes, lowest and highest over its four
readings:

| | without this mod | with this mod |
|---|---|---|
| runway | 4 248.879 to 4 248.999 mm (0.120 mm) | 4 301.261 to 4 301.372 mm (0.111 mm) |

The logs with this mod and without it show no error.

The logs, what the script printed, every line of Diag Terrain Height and a screenshot of its table, for
both sessions, are in
[`diag/non-regression/stock/time-warp/`](../../../diag/README.md#the-time-warp-protocol).

## In flight, low over a static

### The test

The static is a launch pad placed with [Kerbal Konstructs](https://github.com/KSP-RO/Kerbal-Konstructs)
1.12.3 (*KSC LaunchPad lv 1*, of its *Squad KSC* statics): stock has no static on the Mun a craft can stand
on. It stands near the highest point of the Mun's equator, at latitude −0.2773°, longitude −132.9521°, with a
capsule landed on it. The save is [`warp-static-mun-kk.sfs`](../../../diag/non-regression/stock/time-warp/warp-static-mun-kk.sfs), and
the launch pad is in [`diag/non-regression/stock/time-warp/warp-static-mun-kk/`](../../../diag/non-regression/stock/time-warp/warp-static-mun-kk/), to copy into the
`GameData` of KSP with Kerbal Konstructs installed. Then:

1. the save loaded;
2. the space centre, and
   [`Diag3-Rover.craft`](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/craft/Diag3-Rover.craft)
   launched from the SPH onto the runway: not from the launchpad, which KSP clears before a launch,
   recovering whatever stands on a launch pad, this one included;
3. the rover put on a circular orbit of the Mun 9 000 m up (`Alt+F12 → Cheats → Set Orbit`), inclined by the
   capsule's latitude, its southernmost point over the capsule, 60 km before it. With the maximum rate of
   time warp set by the periapsis (`ORBIT_WARP_MAXRATE_MODE = PeAltitude` in `settings.cfg`), KSP allows
   every rate on rails once the periapsis is 250 m above the Mun's highest relief, 8 300 m; set by the
   altitude, it allows 10× from 5 000 m up;
4. time warp on rails at 10×, with the `.` key, until the rover is past the capsule and 40 km from it, then
   back to normal time;
5. *Switch To* the capsule, from the map view.

At the first loading and after the pass, once the capsule has settled, KSP Diag - Terrain Height records a
line: the ground under the capsule, the launch pad, and the ground KSP computes for the same spot, 27.6 m
below the deck on this slope.

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, Kerbal Konstructs 1.12.3 and its
CustomPreLaunchChecks, KSP Diag - Terrain Height, and this mod with its defaults at `logLevel = Debug`. Then
the same without this mod.

*Played by a script*,
[`diag/automation/run-time-warp-flyover.py`](../../../diag/automation/run-time-warp-flyover.py), the save and
the rover in the game, and a screenshot of the table of Diag Terrain Height at the end. The same holds:
every step is one a player can take.

### The result

The rover passed 3 km from the capsule, the static 2.6 km below it, at ten times its 549 m/s over the
ground. In the log with this mod, the launch pad goes out of its sphere as the rover comes within reach, and
back under it as it leaves, ten seconds later, all of it in time warp. Stripped of the rest:

```
[TerrainPrecisionFix] [DEBUG] Mun static 'NewGroup': out of its sphere, corrected by 31.15 mm
[TerrainPrecisionFix] [DEBUG] Mun static 'NewGroup': back under its sphere
[FLIGHT GLOBALS]: Switching To Vessel Capsule ----------------------
[TerrainPrecisionFix] [DEBUG] Mun static 'NewGroup': out of its sphere, corrected by 24.20 mm
```

The height of the launch pad under the capsule above the ground KSP computes, before and after the pass:

| | without this mod | with this mod |
|---|---|---|
| launch pad | 27 608.905, then 27 598.229 mm (10.676 mm) | 27 575.044, then 27 575.036 mm (0.008 mm) |

Without this mod, the launch pad comes back 10.7 mm lower after the *Switch To*: the draw of every loading
([Checking the statics: loading the same save](../../checking-the-culprit-loading/the-statics.md)). With it, it comes
back where it was: had it been left behind during the pass, it would have come back by as much. Both logs
show the same four errors, as the save is first loaded, before this mod takes anything out of its sphere:
`CompileID failed because it reached the scene root without finding a 'SpaceCenter' game object`,
`Triggers on concave MeshColliders are not supported` twice, and `Material doesn't have a texture property
'_MainTex'`, the first time Kerbal Konstructs shows the launch pad.

The logs, what the script printed, every line of Diag Terrain Height and a screenshot of its table, for both
sessions, are in
[`diag/non-regression/stock/time-warp/`](../../../diag/README.md#the-time-warp-flyover-protocol).
