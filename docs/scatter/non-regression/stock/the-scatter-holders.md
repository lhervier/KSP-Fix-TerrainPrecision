# The scatter holders

Part of [Terrain Precision Fix](../../../../README.md), [the scatter](../../README.md#non-regression-tests): one non-regression test, on stock.

**Status: checked with the scatter fix on, no problem — no holder lost, and every pool works as in
stock, over a flight and across scene switches.** The scatter fix, on by default, hangs each holder of
terrain scatter from its own quad, and hangs it back in its pool's container when the quad is destroyed
([The fix: the scatter](../../the-fix.md)). A holder missed on the way would be left on a quad that
stock sends back to its cache of quads, to be reused elsewhere, or on another body: nothing would show on
screen.

Both series are played on stock and with this mod as installed, its scatter fix on, in an install with
[KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes), the base most players run:
KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, the instrument, and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which plays the protocol. *On stock* means that
install without this mod.

## What stock does with the holders

Read in the stock code: stock relies neither on the hierarchy nor on where a holder hangs.

- **The pool** is kept in two lists of the scatter, `cacheAssigned` and `cacheUnassigned`, not in the
  hierarchy; a holder in use is released by the `onDestroy` delegates of its quad, before the quad goes to
  the PQS cache.
- **A holder is shown and hidden** with `obj.SetActive`, a quad with `meshRenderer.enabled`, so the
  holder does not inherit anything from the quad's object.
- **When a collision or a raycast hits the ground**, stock asks the object hit whether it is a quad
  (`GetComponent<PQ>()` in `Part`, `ModuleWheelDamage`, `ModuleDeployableSolarPanel`,
  `ModuleGroundSciencePart`), not its parents: a holder or an object of scatter hanging from a quad is not
  taken for the ground.

## The protocol

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) reads every pool of holders through
stock's own bookkeeping, on its button *Record the holder pools*, in any scene; what it counts, and what a
record holds, are in [its page](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md#6-the-pools-of-holders). Before either
series: terrain scatter on, and the log written at once, steps 1 and 2 of
[the protocol load after load](../../checking/loading-protocol.md#the-protocol).

**Over a flight.** Load [`ref-mune-5km.sfs`](../../../../diag/scatter/checking/flight/ref-mune-5km.sfs), copied into the folder of a sandbox
game: a Mk1 command pod in a circular equatorial orbit 5 km over the Mun. Flying that low, the terrain
keeps building the quads ahead of the pod and destroying those behind it, sending their holders through
the pool all the way, and some of the Mun's relief rises above the orbit, so the pod crashes after a
while. Press *Record the holder pools* 30 s into the flight, then again about every two minutes, and once
more after the crash. The moments do not need to be exact: each record is a check of its own. Copy
`KSP.log` before relaunching KSP. The script
[`run-scatter-holders.py`](../../../../diag/scatter/automation/run-scatter-holders.py) plays it through KSP-Util-MCPServer:
`python run-scatter-holders.py flight --folder <your sandbox game> --out out`. The game keeps the wrecked pod
as the craft flown, frozen where it hit the relief, and pauses a minute later: the script takes the crash
for one when the pod stops moving while the game runs.

**Across scene switches.** Leaving a body switches its terrain off, and stock then destroys that body's
holders. Load [`reference-mune.sfs`](../../../../diag/scatter/checking/loading/reference-mune.sfs) from the Space Center, copied
into the folder of a sandbox game, and press *Record the holder pools* once the terrain has settled; go
back to the Space Center, and press it there; load [`reference-kerbin.sfs`](../../../../diag/scatter/checking/loading/reference-kerbin.sfs),
and press it once the terrain has settled. Copy `KSP.log` before relaunching KSP. Expected: the Mun's pool
in the first record only, Kerbin's from the second on, and `0 broken rules` in all three. The same script
plays it: `python run-scatter-holders.py scenes --folder <your sandbox game> --out out`.

## The holder pools, over a flight

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) keeps a second reading,
[the holder pools](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md#6-the-pools-of-holders).
It reads every pool of holders through stock's own bookkeeping, and counts the holders that break a rule
stock keeps: a holder in use that no longer exists or stands on a quad that is not active, a free holder
that does not hang from its pool's container or still has a quad, a count that disagrees with its list, a
holder in no pool.

It is taken during a flight, where the terrain keeps building quads ahead of the craft and destroying
those behind it: the save [`ref-mune-5km.sfs`](../../../../diag/scatter/checking/flight/ref-mune-5km.sfs),
a Mk1 command pod in a circular equatorial orbit 5 km over the Mun, loaded once, one record 30 s into the
flight, then every two minutes, and one after the pod crashed into the relief, about 617 s into the flight.
Once on stock, once with this mod ([The protocol](#the-protocol)). The records are in
[`mun-5km-stock-holders.log`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/mun-5km-stock-holders.log) and
[`mun-5km-fix-holders.log`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/mun-5km-fix-holders.log), six each,
with what the script printed beside them
([`mun-5km-stock-script.txt`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/mun-5km-stock-script.txt),
[`mun-5km-fix-script.txt`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/mun-5km-fix-script.txt)) and what it
recorded ([`mun-5km-stock-lines.json`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/mun-5km-stock-lines.json),
[`mun-5km-fix-lines.json`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/mun-5km-fix-lines.json)).

| record | in use, on stock | free, on stock | broken rules, on stock | in use, with this mod | free, with this mod | broken rules, with this mod |
|---|---|---|---|---|---|---|
| 1, 30 s | 352 | 32 | 0 | 352 | 32 | 0 |
| 2, 150 s | 176 | 208 | 0 | 168 | 216 | 0 |
| 3, 270 s | 160 | 224 | 0 | 152 | 232 | 0 |
| 4, 390 s | 224 | 160 | 0 | 216 | 168 | 0 |
| 5, 510 s | 152 | 232 | 0 | 152 | 232 | 0 |
| 6, after the crash | 568 | 40 | 0 | 568 | 40 | 0 |

**No holder is lost.** With this mod, every holder handed back hangs in its pool's container, without a
quad, and every holder in use stands on a live quad of the Mun, at every record, the one after the crash
included.

**The pool works as in stock.** It holds as many holders on stock as with this mod, 384 until the crash
and 608 after it, as stock makes new ones when it has none free left, and those go through the fix as
well. Where the counts in use differ by 8, at records 2 to 4, the two pods passed over neighbouring quads,
their clocks a second apart: the two flights do not take their records over the very same ground.

## The holder pools, across scene switches

The quads of the most detailed level are shared by every body, and leaving a body switches its terrain
off. This series checks that its holders go back to their pools before stock destroys them, and that
none travels on a quad to the next body.

The same install, on stock and with this mod, one session each, following [the protocol](#the-protocol):
`reference-mune.sfs` loaded from the Space Center, back to the Space Center, then `reference-kerbin.sfs`,
with a record in each of the three scenes. The records are in
[`scenes-stock-holders.log`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/scenes-stock-holders.log) and
[`scenes-fix-holders.log`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/scenes-fix-holders.log), with what the
script printed ([`scenes-stock-script.txt`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/scenes-stock-script.txt),
[`scenes-fix-script.txt`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/scenes-fix-script.txt)) and what it
recorded ([`scenes-stock-lines.json`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/scenes-stock-lines.json),
[`scenes-fix-lines.json`](../../../../diag/scatter/non-regression/stock/the-scatter-holders/scenes-fix-lines.json)). Every record
ends on `0 in no pool` and `0 broken rules`:

| record | scene | pools | holders in use | free |
|---|---|---|---|---|
| 1 | the Mun | the Mun's `Rock00` | 128 | 32 |
| 2 | the Space Center | Kerbin's `Tree00`, `Grass00`, `boulder`, `Pine00`, `cactus` | 3 | 317 |
| 3 | Kerbin | the same five | 118 | 202 |

Those are, pool for pool, the counts of the session on stock. The Mun's pool is gone from the second record
on, and no holder of the Mun turned up under a quad of Kerbin.
