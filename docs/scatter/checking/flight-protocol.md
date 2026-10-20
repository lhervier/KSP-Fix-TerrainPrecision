# The protocol: the scatter, along a flight

Part of [Terrain Precision Fix](../../../README.md), [the scatter](../README.md#checked), for [Checking the scatter: in flight](flight.md):
how the scatter is read by [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) along a
flight low over the Mun. What each reading is, and what a record holds, are in
[its page](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md). The protocol
is the same on stock and with this mod.

[The protocol load after load](loading-protocol.md) reads scatter
built right after a load, around a craft that does not move. Over a flight, the world origin follows the
craft, and the terrain keeps building the quads ahead of it and destroying those behind it: reading the
rocks along a flight shows where they are drawn once they have come through that.

## The save

[`ref-mune-5km.sfs`](../../../diag/scatter/checking/flight/ref-mune-5km.sfs), a sandbox game of
KSP 1.12.5: a single Mk1 command pod in a circular equatorial orbit 5 km over the Mun, the same save as
[PQSBench's](https://github.com/lhervier/KSP-PQSBench/blob/main/perfs/README.md). Some of the Mun's
relief rises above that orbit, so the pod crashes into it after a while. Copy it into the folder of a
sandbox game and load it from that game.

## The protocol

1. **Scatter on, and the log written at once**: steps 1 and 2 of
   [the protocol load after load](loading-protocol.md#the-protocol).
2. **Load the save.**
3. **Press *Record the rocks*** 30 s into the flight, then again every two minutes, and once more after
   the crash.
4. **Copy `KSP.log`** before relaunching KSP.

Each record reads on its own: the heights of every quad and of its holders, as after a load. To compare
two installs, fly the same save in each and press at the same moments after the load: the pod then passes
over the same ground, and each record names the same quads as its counterpart, or quads next to them when
the two presses are a second apart.

## Played by a script

[`run-scatter-flight.py`](../../../diag/scatter/automation/run-scatter-flight.py) plays this protocol through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), with nothing but Python 3: start KSP with
KSP-MCPServer and Diag Scatter installed, copy the save into a sandbox game, wait for the main menu, then
run `python run-scatter-flight.py --folder <your sandbox game> --out out`. It presses *Record the rocks* at
30 s and every two minutes after it, counted from the end of the load, five times, then once more after the
crash. The game keeps the wrecked pod as the craft flown, frozen where it hit the relief, and pauses a
minute later: the script takes the crash for one when the pod stops moving while the game runs, and lets
the game run again. It writes the number and the closing line of each record to `lines.json`; the records
stay in `KSP.log`.

The pod flies 5 km above the ground, so every quad, the nearest included, stands 5 km or more from the
world origin: its heights carry the precision of that distance, about a millimetre, where the landed saves
resolve the nearest quad to a few micrometres
([precision](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md#precision)).
