# The protocol: driving on while the world moves

Part of [Terrain Precision Fix](../../README.md), for
[Checking the ground: driving on while the world moves](the-ground.md): how the ground under a rover that
keeps driving is read by [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight),
just before and just after the game moves its whole world. Nothing is loaded here — from the first line
to the last, it is one single flight. The columns it fills are in
[its window](https://github.com/lhervier/KSP-Diag-TerrainHeight/blob/main/docs/the-window.md). The
protocol is the same without this mod and with it.

KSP keeps the craft you fly near the centre of Unity's world. Every 500 m it drives, the game moves the
whole world back under it, the ground included: this is called the *floating origin*, and
[KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin) explains it
and counts those moves
([What it measures](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/docs/what-it-measures.md)).
This protocol reads the ground on either side of one such move, a few metres apart, then the same few
metres farther on, with no move in between, to tell what the move does from what the few metres do.

## Two instruments

This protocol needs Diag FloatingOrigin in the same install as Diag TerrainHeight. Diag FloatingOrigin
only reads; it is there to tell you when the world moves, through two of its columns:

- **Origin distance (m)**, how far the rover is from the origin of the world. It grows as you drive,
  and drops back near zero when the world moves;
- **Shifts**, how many times the world moved since its previous line. The game moves it once as the
  scene opens, so the first line of the series reads 1 although the rover has not driven 500 m yet.

Every record below is taken in both windows: press *Record* in Diag TerrainHeight's window, then in Diag
FloatingOrigin's, without moving in between. The two tables then have the same number of lines, and
each line of Diag FloatingOrigin says whether the world moved since the line before.

## The save

[`driving-kerbin.sfs`](../../diag/checking-the-culprit-driving/driving-kerbin.sfs), a sandbox game of
KSP 1.12.5. Copy it into the folder of a sandbox game and load it from that game. It holds a single
craft, [`Diag2-Rover`](../../diag/checking-the-culprit-driving/Diag2-Rover.craft), a crewed rover on
four wheels, with batteries and solar panels to recharge them, landed on the flat grass south of the
runway of the KSC, at latitude −0.0581°, longitude −74.7241°, facing due south. No target is set.

**The rover is alone, and has to be.** While another landed craft is loaded nearby, the game does not
move the world at all, however far the rover drives; it only catches up when that craft is unloaded,
2500 m away ([Diag FloatingOrigin, a rover near a parked craft](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/docs/the-measurements-parked-craft.md)).
With a second craft parked nearby, nothing on this page would happen.

You can make your own: copy [`Diag2-Rover.craft`](../../diag/checking-the-culprit-driving/Diag2-Rover.craft)
into the `Ships/SPH` folder of a sandbox game, launch it from the Spaceplane Hangar onto the runway, and
drive due south until it is off the runway and on the grass. Stop, put the brakes on, and save once.

### The same on Earth, in Real Solar System

[`driving-earth-rss.sfs`](../../diag/checking-the-culprit-driving/driving-earth-rss.sfs) holds the same
rover on Earth, on the grass south of the runway of the KSC at Cape Canaveral, at latitude 28.6119°,
longitude −80.6176°. It only loads in an install with
[Real Solar System](https://github.com/KSP-RO/RealSolarSystem) and what it requires. It was made the same
way, from the Spaceplane Hangar of that install.

Real Solar System keeps the origin of the world from moving while a craft rolls on the runway of the KSC:
the whole series is driven on the grass.

## The protocol

Load the save and **do not change scene again** — no save, no load, no trip back to the space centre.
Diag FloatingOrigin reads an **Origin distance** near zero: the origin of the world is on the rover.

![The save just loaded: Origin distance near zero](../../imgs/checking-the-culprit-driving/the-protocol/00-load.png)

Drive due south across the flat grass, away from the runway and the buildings. Then, for each
move of the world, three records.

**1. Just before.** Stop when **Origin distance** reads about 490 m — between 498 and 500 m on Earth.
Wait for the digits of Diag TerrainHeight to stop moving, then record.

![Stopped at 490.6 m from the origin, in Diag FloatingOrigin's window](../../imgs/checking-the-culprit-driving/the-protocol/10-before-fo.png)

![The same stop, in Diag TerrainHeight's window, the digits settled](../../imgs/checking-the-culprit-driving/the-protocol/11-before-th.png)

**2. Just after.** Creep forward until **Origin distance** drops back near zero: the world has moved.
Stop a few metres on — within 2 m on Earth — wait, and record. Diag FloatingOrigin's line reads 1 in **Shifts**.

![Just after the move: Origin distance back near zero, Shifts 1](../../imgs/checking-the-culprit-driving/the-protocol/20-after-fo.png)

**3. The same distance again.** Creep forward about as far as from 1 to 2 — another 2 m on Earth — stop,
wait, and record. Diag FloatingOrigin's line reads 0 in **Shifts**.

![The same distance again: Shifts 0](../../imgs/checking-the-culprit-driving/the-protocol/30-again-fo.png)

![The three lines of one move, in Diag TerrainHeight's window](../../imgs/checking-the-culprit-driving/the-protocol/40-three-lines-th.png)

Then drive on to the next move, 500 m farther, and do it again, three moves in all.

**Three moves, and no more**, because on Kerbin the grass south of the runway is flat for about a
kilometre and a half only. Beyond, the ground slopes down, and on a slope a few metres change **Difference** far more
than a move does: the third line, with no move, shows it. A fourth move, about two kilometres south of
the runway, gave a computed height dropping by 15 to 29 cm from one line to the next, and a
**Difference** changing by 176 mm with no move at all.

## What the three lines are worth

| line | between it and the line before | what the line is worth |
|---|---|---|
| 1 | the rover drove about 490 m | the ground just before the move |
| 2 | a few metres, and one move of the world | the ground just after it |
| 3 | the same few metres, and no move | the same step, without the move |

**Read the change from line 1 to line 2 against the change from line 2 to line 3.** Lines 1 and 2 are
not read at the same spot, so **Difference** can change between them even if the move did nothing:
the ground is built out of flat triangles that do not follow its curve exactly
([Diag TerrainHeight, why a correct reading is not zero](https://github.com/lhervier/KSP-Diag-TerrainHeight/blob/main/docs/this-mods-demonstration.md#why-a-correct-reading-is-not-zero)),
and now and then a few metres cross from one piece of the ground to the next. Line 3 measures what the
few metres do on their own, with no move in between.

⚠️ **Keep a move only when its second line changes at least three times as much as its third.** Below
that, a few metres change the reading nearly as much as the move does, and the move cannot be told
apart.

**Ground KSP computes** says how much the ground's own shape changes between the lines. On the grass of
Kerbin, it reads the same digits to a few thousandths of a millimetre. On Earth, around the KSC, it
changes by about a centimetre per metre: hence the closer stops there, which keep the third line small.

⚠️ **Compare only lines a few metres apart.** Between line 3 of one move and line 1 of the next, the
rover drives about 480 m: **Difference** can change by several centimetres over that distance, with no
move at all.

⚠️ **Stay on the grass.** The ray stops at the first surface it meets: on the runway or a building, it
reads a structure, not the ground.

⚠️ **Do not save while the series is running.** The readings are only comparable if they are all taken
in the one flight the save opened.

**One move says nothing on its own.** It is the series that is worth reading, not a line.

## Played by a script

[`diag/automation/run-driving.py`](../../diag/automation/run-driving.py) plays the protocol above, step
for step, and takes the screenshots. It drives KSP through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), a mod that answers requests sent to it over
HTTP, from the computer KSP runs on only; and it needs nothing but Python 3 — no AI, no package to
install. Anyone can read it top to bottom: it follows the three records above in the same order.

1. Install KSP-MCPServer next to Diag TerrainHeight and Diag FloatingOrigin — and this mod, for the
   series with it — copy [the save](../../diag/checking-the-culprit-driving/driving-kerbin.sfs) into a
   sandbox game, start KSP and wait for the main menu.
2. Run `python run-driving.py --folder <your sandbox game> --moves 3 --out screenshots`. On Earth, add
   `--save driving-earth-rss --before 499 --radius 6371000`: the rover stops 499 m from the origin
   instead of 490 m, and the radius of the body turns metres into degrees.

It loads the save once and never changes scene, then drives due south. For each move of the world, it
stops when the rover is `--before` metres from the origin, waits for the digits to stop moving, and
records in both windows; creeps on until the origin moves, stops and records; creeps on as far again,
with no move, and records. It covers the last 20 m before each first stop at a walking pace: on Earth,
from full speed, the rover would roll past the 500 m. After the last move it takes a screenshot of each table,
prints every line it recorded, writes them to `lines.json` next to the screenshots, and quits KSP —
give it `--keep-running` to leave KSP open. Save `KSP.log` before starting KSP again: KSP writes it anew
at every start.
