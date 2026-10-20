# This mod's safeguard

Part of [Terrain Precision Fix](../../README.md), [what the fixes share](README.md#non-regression-tests): one non-regression test, on stock and on Real Solar System.

**Status: checked on Kerbin, the Mun, Minmus and Gilly, and on the Moon, Earth, Venus, Mars and Mercury of
Real Solar System — the safeguard never refused a correction. The largest one was 3.9 float steps on stock,
4.4 on Real Solar System, a quarter of the limit.**

*The rule.* This mod refuses any correction larger than sixteen float steps, taken at the distance from
the centre of the body: the quad, or the static, is then left where stock puts it
([Safeguards](../ground/the-fix.md#safeguards)). The limit grows with the body, as the rounding does:
15.6 mm on Gilly, 62.5 mm on Minmus, 250 mm on the Mun, 1 m on Kerbin, 8 m on Earth. It is the same for the
ground and for the statics.

*Why it is a non-regression test.* A correction refused by mistake puts the defect back where it was
refused. The small bodies are where the limit is tightest in millimetres: a limit set too low against the
rounding there would show as quads left as stock builds them. On Earth, ten times the size of Kerbin, a
float step is eight times as large: the bodies of Real Solar System are where a limit that does not grow
would show.

## The margin on stock

The sessions with this mod ran at `logLevel = Debug`, which logs how far each quad was moved. The quads
placed and the largest correction on each body, over every log of the runs taken with this mod:

| body | float step | limit | quads placed | largest correction |
|---|---|---|---|---|
| Kerbin | 62.5 mm | 1 m | 81 980 | 221.1 mm, 3.5 steps |
| the Mun | 15.6 mm | 250 mm | 9 636 | 57.8 mm, 3.7 steps |
| Minmus | 3.9 mm | 62.5 mm | 4 752 | 12.6 mm, 3.2 steps |
| Gilly | 0.98 mm | 15.6 mm | 12 044 | 3.8 mm, 3.9 steps |

The float step is the one at the radius of the body. A quad that stands higher than the next power of two
metres from the centre has a step twice as large, and a correction worth half as many steps: on Gilly,
13 km in radius, that is every quad more than 3.4 km above its datum, so its count is an upper bound.

## The margin on Real Solar System

The same, over every log taken with this mod in Real Solar System, which also logs how far each static was
moved:

| body | float step | limit | quads placed | largest correction |
|---|---|---|---|---|
| Earth | 500 mm | 8 m | 40 183 | 2 182 mm, 4.4 steps |
| Venus | 500 mm | 8 m | 2 112 | 1 792 mm, 3.6 steps |
| the Moon | 125 mm | 2 m | 17 600 | 456 mm, 3.6 steps |
| Mars | 250 mm | 4 m | 5 140 | 308 mm, 1.2 steps |
| Mercury | 250 mm | 4 m | 1 532 | 259 mm, 1.0 step |

The statics of Earth stay further from it: the KSC was corrected by 1 541 mm at most, 3.1 steps, over
72 placements, and the tracking station of Cape Canaveral by 1 317 mm, 2.6 steps, over 12.

Venus, Mars and Mercury are read at loads only; no descent onto them is flown. In flight, where the terrain
is built continuously, this mod is checked on Earth, whose float step is the largest of these bodies
([Checking the ground: in flight](../ground/checking/flight.md#on-earth)): what it
corrects is the rounding of a position at the distance of the body's centre, whatever the subdivision
level of the quad.

## The line to look for

No log of these runs holds the line the safeguard writes when it refuses a correction. This is the line to
look for in a log, given once per body, at the first refusal:

```
[TerrainPrecisionFix] <body>: a correction of … m is more than 16 float steps (… m at that distance), too large to be a rounding error, the quads concerned are left as stock builds them
```

For a static, the line ends with *the statics concerned are left where stock places them*.

## A limit that does not grow: the first version

The first version of the safeguard was a fixed metre, set against roundings of a few centimetres on
Kerbin. On Earth, a correction of two float steps already exceeds it. In the sessions marked *first
safeguard* in [the runs of the ground](../../diag/ground/README.md#on-real-solar-system), played on the
Moon, Earth's terrain was built too, and that version refused corrections of 1.094 m and 1.318 m:

```
[TerrainPrecisionFix] Earth: a correction of 1.094 m is too large to be a rounding error, the quads concerned are left as stock builds them
```

Those quads stayed as stock builds them, with the defect, and nothing else showed in the logs: no error
besides those every session of that install shows.

## The saves

The loads on Venus, Mars and Mercury, taken with this mod alone, have their saves and their logs in
[`diag/common/safeguard`](../../diag/common/safeguard): the same pod on its tank, placed with *Set Position*
in the debug menu (Alt+F12, *Cheats*).

- [`reload-venus-rss.sfs`](../../diag/common/safeguard/reload-venus-rss.sfs) — Venus (latitude −13.05°, longitude
  −49.81°, the plain where Venera 14 landed), the craft *landed*;
- [`reload-mars-rss.sfs`](../../diag/common/safeguard/reload-mars-rss.sfs) — Mars (latitude 47.64°, longitude 134.29°,
  Utopia Planitia, where Viking 2 landed), the craft in *prelaunch*;
- [`reload-mercury-rss.sfs`](../../diag/common/safeguard/reload-mercury-rss.sfs) — Mercury (latitude 73.40°, longitude
  −79.50°, Borealis Planitia), the craft *landed*. Real Solar System roughens Mercury's terrain
  everywhere with two layers of noise, finer than the collision mesh can follow: at each load, KSP
  first lifts the craft to the height it computes for that spot, 22.4 m above the mesh, then its
  ground pass moves it back down, to where it was saved. That gap is terrain detail, far beyond any
  rounding.

Copy a save into the folder of a sandbox game and load it from that game.
