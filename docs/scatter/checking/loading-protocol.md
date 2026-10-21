# The protocol: the scatter, load after load

Part of [Terrain Precision Fix](../../../README.md), [the scatter](../README.md#checked), for [Checking the scatter: loading the same save](loading.md): how the scatter around a landed craft is
read by [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter), load after load. What each
reading is, and what a record holds line by line, are in
[its page](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md). The
protocol is the same on stock, with this mod, and with its scatter fix turned off.

## The saves

Two saves of a sandbox game of KSP 1.12.5. Copy one into the folder of a sandbox game and load it from
that game.

- [`reference-kerbin.sfs`](../../../diag/scatter/checking/loading/reference-kerbin.sfs): a
  single Mk1 command pod landed on Kerbin, about 8 km north-west of the KSC (latitude 0.2696°, longitude
  −75.2783°), where the scatter is grass and trees.
- [`reference-mune.sfs`](../../../diag/scatter/checking/loading/reference-mune.sfs): a single
  Mk1 command pod landed on the Mun (latitude −12.4124°, longitude 91.7314°), where the scatter is rocks.

To make your own: launch any craft, move it with `Alt+F12 → Cheats → Set Position` onto ground with
scatter around it — scatter only exists on the most detailed terrain — and save.

## The protocol

1. **Terrain scatter must be on**: *Settings → Graphics → Terrain Scatters*.
2. **Have KSP write its log at once**: in the debug menu (`Alt+F12 → Debugging`), tick the option that
   flushes the log instantly (`LOG_INSTANT_FLUSH` in `settings.cfg`). Otherwise KSP writes `KSP.log` in
   batches, and a record can wait there until more lines come. Follow the file as it grows, for
   instance with `tail -f KSP.log`.
3. **Load the save and press *Record the rocks*** in the window of Diag Scatter (`Alt+F6` shows or hides
   it). The reading is written to `KSP.log`, and its last line tells what it holds: how many quads carry
   scatter, how many holders are not built yet, and how many objects and vertices were measured on the
   nearest quad. Quads and their scatter are built over several frames after loading: if holders are not
   built yet, or the counts still grow from one press to the next, wait a few seconds and press again.
   Only the last record of each load is kept.
4. **Load the same save again, and press *Record the rocks* again.** Twelve times: how far things move
   changes from one load to the next, and a handful of loads can come out small or large by chance.

KSP overwrites `KSP.log` each time it starts: copy it before relaunching. Reloading the save from within
the game does not overwrite it, and the record numbers keep counting from one load to the next.

## Played by a script

[`run-scatter-loading.py`](../../../diag/scatter/automation/run-scatter-loading.py) plays this protocol through
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), with nothing but Python 3: start KSP with
KSP-Util-MCPServer and Diag Scatter installed, copy a save into a sandbox game, wait for the main menu, then run
`python run-scatter-loading.py --folder <your sandbox game> --save reference-kerbin --loads 12 --out out`.
After each load, it presses *Record the rocks* every 3 s until every holder is built and the counts are the
same twice in a row, writes the number and the closing line of the last record to `lines.json`, and never
saves the game. The records stay in `KSP.log`;
[`extract-scatter-records.py`](../../../diag/scatter/automation/extract-scatter-records.py) copies the last record of
each load out of it, one file per load.

## Reading the records

Compare the records of the successive loads on the nearest quad. Its name has to be the same in every
record for them to compare anything. Vertex by vertex, the same kind of scatter, the same object and the
same vertex, the height above the ground answers the question on its own: constant over the loads for all
the vertices of an object, that object is drawn at the same place against the ground every time;
changing, it is not. The heights above it tell where a change comes from: a vertex's height above the
ground minus its holder's *up* stays constant when the change is the holder's matrix, and the holder's
height minus its quad's height tells whether its centre left its quad's too. The quad's own *up* and
*across* tell whether the ground is drawn away from the quad. The height of the quad itself may change
from one load to the next as well: comparing everything to it keeps that from blurring the rest.
