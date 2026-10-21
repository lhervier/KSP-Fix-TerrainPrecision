# Checking the ground: in flight

Part of [Terrain Precision Fix](../../../README.md), [the ground](../README.md#checked): the measurements that check [its culprit](../the-culprit.md), in flight, where the quads of the highest level are built and
dropped all the time as the craft goes, on stock and with this mod, on Kerbin and on Earth in Real Solar
System.

[KSP Diag - Terrain Quads](https://github.com/lhervier/KSP-Diag-TerrainQuads) reads the quads, and
[KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin), which only reads,
says when the world moves. Each has its own page, with its method.

This fix is built on top of [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes),
the base most players run, so every campaign on this page is run in an install that has it: KSP 1.12.5
with Harmony, ModuleManager, KSP Community Fixes 1.41.1, the two instruments and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which flies the craft — and this mod, or not;
on Earth, [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 and what it requires
as well. *On stock*, below, means that install without this mod.

Each quad is rounded once, when it is built, through the frame of the moment
([Why it is different at every load](../the-culprit.md#why-it-is-different-at-every-load)). On the
ground, the quads under a craft are built together. In flight, they are built one after the other as the
craft goes, each through the frame of its own moment, while the floating origin moves every 500 m the
craft travels, and every frame once it goes fast. A rocket, `Quad-Rocket`, is launched from the
launchpad and left to fly until it falls into the sea, about a minute later; about once a second, the
*Log* button of Diag TerrainQuads writes, for every quad of the highest level, the distance from the centre
of the body to each of its vertices. Two quads of the highest level that share an edge should put its
vertices at the same distance; the step between them is how far apart they are. *Siblings* are two
quads split from the same quad, at the same moment; *cousins* any other two. It is
[the protocol of the quads of the highest level, in flight](flight-protocol.md), played by its script,
[`run-flight.py`](../../../diag/ground/automation/run-flight.py), and read by
[`analyse-flight.py`](../../../diag/ground/automation/analyse-flight.py): on each body, one flight without this mod, one with it, the same
craft and the same steps.

**→ Full chapter: [The protocol: the quads of the highest level, in flight](flight-protocol.md)**

## On Kerbin

From the launchpad of the Space Center; the highest subdivision level of Kerbin is 10.

**On stock**, one flight, 72 *Logs* over 71 seconds of game time. The first one on the launchpad, the
engine lit and the clamp still holding; the craft then rose to 957 m and reached 653 m/s, and the last
*Log* was taken 30 m above the sea. The world moved 2,365 times: once as the scene opened, none while
the craft was slower than 100 m/s, then every frame from about 235 m/s on. 356 quads of level 10 were
written, most of them in several *Logs*. The session is logged in [`flight-kerbin-stock.log`](../../../diag/ground/checking/flight/flight-kerbin-stock.log); what the script printed is in
[`flight-kerbin-stock-script.txt`](../../../diag/ground/checking/flight/flight-kerbin-stock-script.txt), what each *Log* answered in
[`flight-kerbin-stock-readings.json`](../../../diag/ground/checking/flight/flight-kerbin-stock-readings.json), the two files of the *Logs* in
[`flight-kerbin-stock-logs.csv`](../../../diag/ground/checking/flight/flight-kerbin-stock-logs.csv) and [`flight-kerbin-stock-quads.zip`](../../../diag/ground/checking/flight/flight-kerbin-stock-quads.zip) (zipped: 42 MB once unzipped), and what
`analyse-flight.py` printed in [`flight-kerbin-stock-analysis.txt`](../../../diag/ground/checking/flight/flight-kerbin-stock-analysis.txt). Of the 9,103 shared edges between cousins, 2,940 have a step of more than 1 mm, 1,882 of more
than 5 mm, and 1,120 of more than 10 mm.

**With this mod**, in that same install, with this mod as the only difference, at `logLevel = Debug`.
The session is logged in [`flight-kerbin-fix.log`](../../../diag/ground/checking/flight/flight-kerbin-fix.log); what
the script printed is in [`flight-kerbin-fix-script.txt`](../../../diag/ground/checking/flight/flight-kerbin-fix-script.txt), what
each *Log* answered in [`flight-kerbin-fix-readings.json`](../../../diag/ground/checking/flight/flight-kerbin-fix-readings.json),
the two files of the *Logs* in [`flight-kerbin-fix-logs.csv`](../../../diag/ground/checking/flight/flight-kerbin-fix-logs.csv) and
[`flight-kerbin-fix-quads.zip`](../../../diag/ground/checking/flight/flight-kerbin-fix-quads.zip), and what `analyse-flight.py`
printed in [`flight-kerbin-fix-analysis.txt`](../../../diag/ground/checking/flight/flight-kerbin-fix-analysis.txt). 73 *Logs*:
the same flight to within a few metres, up to 954 m and 654 m/s, the floating origin moved 2,361 times,
every frame from about 236 m/s on.

For the quads of level 10, in millimetres, the median, the 90th percentile and the largest value:

| | on stock | with this mod |
|---|---|---|
| the same quad, from one *Log* to the next, over 100 m/s | 0.050 / 0.226 / 0.699 | 0.050 / 0.238 / 0.855 |
| the step between siblings | 0.007 / 0.033 / 0.418 | 0.061 / 0.220 / 0.783 |
| the step between cousins both there from the first *Log*, built as the scene opened | 0.006 / 0.027 / 0.403 | 0.062 / 0.231 / 0.774 |
| **the step between cousins, one at least built during the flight** | **4.520 / 16.930 / 22.454** | **0.060 / 0.202 / 0.674** |

Each line compares 4,023 to 11,451 pairs of *Logs* or shared edges, about as many on stock as with this
mod; their counts are in the two `analysis.txt` files. Under 100 m/s, the first eleven *Logs*, nothing
moved either way, to the thousandth of a millimetre: the floating origin did not move in that time.

The log shows this mod placing 1,000 quads in the session, 220 of them during the flight, corrected by
34 mm in the median and by 93.9 mm at most: 1.5 steps of a float at the radius of Kerbin, against the
sixteen past which this mod refuses a correction. It refused none, and the log shows no error this mod
causes.

## On Earth

From the launchpad of Cape Canaveral; the highest subdivision level of Earth is 11. The same craft flies
a lower and shorter curve there than on Kerbin.

**On stock**, one flight, 55 *Logs* over 52 seconds of game time, up to 565 m and 488 m/s, the last
*Log* taken 30 m above the sea. The world moved 1,392 times: once as the scene opened, none while the
craft was slower than 100 m/s, then every frame from about 238 m/s on. 224 quads of level 11 were
written. The session is logged in [`flight-earth-rss-stock.log`](../../../diag/ground/checking/flight/flight-earth-rss-stock.log); what the script printed is in
[`flight-earth-rss-stock-script.txt`](../../../diag/ground/checking/flight/flight-earth-rss-stock-script.txt), what each *Log* answered in
[`flight-earth-rss-stock-readings.json`](../../../diag/ground/checking/flight/flight-earth-rss-stock-readings.json), the two files of the *Logs* in
[`flight-earth-rss-stock-logs.csv`](../../../diag/ground/checking/flight/flight-earth-rss-stock-logs.csv) and [`flight-earth-rss-stock-quads.zip`](../../../diag/ground/checking/flight/flight-earth-rss-stock-quads.zip) (zipped: 40 MB once unzipped), and what
`analyse-flight.py` printed in [`flight-earth-rss-stock-analysis.txt`](../../../diag/ground/checking/flight/flight-earth-rss-stock-analysis.txt).

**With this mod**, in that same install, with this mod as the only difference, at `logLevel = Debug`.
The session is logged in [`flight-earth-rss-fix.log`](../../../diag/ground/checking/flight/flight-earth-rss-fix.log);
what the script printed is in [`flight-earth-rss-fix-script.txt`](../../../diag/ground/checking/flight/flight-earth-rss-fix-script.txt),
what each *Log* answered in [`flight-earth-rss-fix-readings.json`](../../../diag/ground/checking/flight/flight-earth-rss-fix-readings.json),
the two files of the *Logs* in [`flight-earth-rss-fix-logs.csv`](../../../diag/ground/checking/flight/flight-earth-rss-fix-logs.csv)
and [`flight-earth-rss-fix-quads.zip`](../../../diag/ground/checking/flight/flight-earth-rss-fix-quads.zip), and what
`analyse-flight.py` printed in [`flight-earth-rss-fix-analysis.txt`](../../../diag/ground/checking/flight/flight-earth-rss-fix-analysis.txt).
56 *Logs*, up to 613 m and 503 m/s, the floating origin moved 1,492 times, every frame from about
236 m/s on: on Earth, the two flights differ by some fifty metres at the top of their curve.

For the quads of level 11, in millimetres, the median, the 90th percentile and the largest value:

| | on stock | with this mod |
|---|---|---|
| the same quad, from one *Log* to the next, over 100 m/s | 0.160 / 0.740 / 2.172 | 0.145 / 0.755 / 2.218 |
| the step between siblings | 0.137 / 0.286 / 1.376 | 0.312 / 0.884 / 2.458 |
| the step between cousins both there from the first *Log*, built as the scene opened | 0.132 / 0.331 / 1.592 | 0.282 / 0.807 / 2.124 |
| **the step between cousins, one at least built during the flight** | **57.458 / 264.204 / 288.716** | **0.381 / 0.827 / 2.137** |

Each line compares 778 to 10,405 pairs of *Logs* or shared edges, about as many on stock as with this
mod. The quads of Earth are larger than those of Kerbin, and the flight shorter: far fewer quads are
built on the way, some 800 shared edges between cousins built in flight, against 4,000 on Kerbin.
Under 100 m/s, the first eleven *Logs*, nothing moved either way: the floating origin did not move in
that time.

The log shows this mod placing 272 quads in the session, 48 of them during the flight, corrected by
585 mm in the median and by 1,093.7 mm at most: 2.2 steps of a float at the radius of Earth, against the
sixteen past which this mod refuses a correction. It refused none, and the log shows no error this mod
causes.

## What the measurements say

**On stock, in flight, the ground is not one surface.** Two quads of the highest level built at different
moments of the flight step up or down where they meet: by 4.5 mm in the median and up to 22.5 mm on
Kerbin; by 57 mm in the median and up to 289 mm on Earth, where a float's step is eight times larger.
Two quads built at the same moment meet within 0.42 mm on Kerbin and 1.6 mm on Earth. While the craft
flies faster than 100 m/s, each quad keeps the height it was built at — from one *Log* to the next, a
vertex moved by 0.70 mm at most on Kerbin and 2.2 mm on Earth, through thousands of moves of the floating
origin — so the step stays as long as the two quads do.

**With this mod, the steps are gone.** Cousins built during the flight meet within 0.674 mm on Kerbin
and 2.137 mm on Earth, no worse than those built together or than siblings on the same body: when a
quad was built no longer matters. What is left is about the same for every pair, under a millimetre on
Kerbin and a few millimetres on Earth. Siblings meet a little less closely than on stock — in the median,
0.061 mm against 0.007 mm on Kerbin, 0.312 mm against 0.137 mm on Earth: on stock, two siblings carry
the same rounding, and with this mod each is placed on its own. Where those remainders come from has
not been checked on its own.

**These flights do not say what a move of the origin does at low speed.** Stock places the quads again
after a move only when the active craft is landed or slower than 100 m/s (`FloatingOrigin.FixedUpdate`), and
the floating origin did not move while these craft were that slow; a rover driving on the ground covers
that case ([the checks of the ground](../README.md#checked)).
Nor do they say anything of the statics, nor of a gap beside an edge: the *Log* writes distances from
the centre of the body, so a step up or down shows, a gap or an overlap along the ground does not.

**Two bodies are enough.** Kerbin and Earth are the two ends of what a player lands on: a float's step of
62.5 mm and of 500 mm at the radius of the body, a stock body and one made by Kopernicus. The code that
places a quad is the same on every body, and the steps grow with the float's step, so no other body was
flown.
