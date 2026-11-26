# The runs

Part of [Terrain Precision Fix](../../../README.md): the saves, the scripts and the `KSP.log` of every
session, without this mod and with it, in a `diag` folder in the folder of each fix:

- [the ground](../../ground/diag/README.md), read in [the ground](../../ground/README.md);
- [the statics](../../statics/diag/README.md), read in [the statics](../../statics/README.md);
- [the scatter](../../scatter/diag/README.md), read in [the scatter](../../scatter/README.md);
- [the ROCs](../../rocs/diag/README.md), read in [the ROCs](../../rocs/README.md);
- [the ground anchor](../../ground-anchor/diag/README.md), read in [the ground anchor](../../ground-anchor/README.md);
- [parts lying alone](../../lone-parts/diag/README.md), read in [parts lying alone](../../lone-parts/README.md);
- [this mod's safeguard](../../planet-frame/diag/README.md), read in [Planet Frame](../../planet-frame/README.md);
- and here, what the fixes share: Principia and the [performance runs](perfs/README.md), read in
  [what the fixes share](../README.md).

Each page has its folder at the same path as the page under `docs`: the logs, saves and crafts of
[An anchor on a static](../../ground-anchor/non-regression/stock/an-anchor-on-a-static.md) are in
[`docs/ground-anchor/diag/non-regression/stock/an-anchor-on-a-static/`](../../ground-anchor/diag/non-regression/stock/an-anchor-on-a-static),
and its screenshots in
[`docs/ground-anchor/imgs/non-regression/stock/an-anchor-on-a-static/`](../../ground-anchor/imgs/non-regression/stock/an-anchor-on-a-static).
A file that several pages use is in the folder of the page that measures with it. The scripts that play
the protocols are in the `automation/` folder of each fix.

Each `KSP.log` is kept compressed, as `.log.gz`, without the lines of the game loading its parts, textures,
models and user interface. Every other line is as KSP wrote it, the plugins it loaded among them, and the first
line of each log says it was filtered.

## With Principia

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Principia](https://github.com/mockingbirdnest/Principia) Lévy on the stock system, the instruments of each
protocol, and [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which plays the protocols; this
mod at `logLevel = Debug`, or not: each session is here twice, `-without-this-mod` and `-fix`. Read in
[Principia: the bodies it moves and turns](../non-regression/principia/the-bodies-it-moves-and-turns.md).

- [`loading-principia-without-this-mod.log.gz`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod.log.gz) and
  [`loading-principia-fix.log.gz`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix.log.gz) — the four saves of
  [the loading protocol](../../ground/checking/loading-protocol.md),
  each loaded six times by `run-loading.py`, both instruments at once; what the script printed in
  [`loading-principia-without-this-mod-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod-script.txt)
  and [`loading-principia-fix-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix-script.txt), every line it recorded,
  with the save it was recorded on, in
  [`loading-principia-without-this-mod-lines.json`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod-lines.json)
  and [`loading-principia-fix-lines.json`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix-lines.json).
- [`flight-principia-without-this-mod.log.gz`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod.log.gz) and
  [`flight-principia-fix.log.gz`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix.log.gz) — one flight each of
  [the protocol of the quads of the highest level, in flight](../../ground/checking/flight-protocol.md),
  from the launchpad of the Space Center, KSP Diag - Terrain Quads and KSP Diag - Floating Origin; for each,
  as for the flights of [In flight](../../ground/diag/README.md#the-protocol-of-the-quads-of-the-highest-level-in-flight), what the
  script printed, the readings, the index of the *Logs* and the analysis (the quads they wrote, some 50 MB, are not
  kept: replaying the protocol writes them again):
  - without this mod: [`flight-principia-without-this-mod-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-script.txt), [`flight-principia-without-this-mod-readings.json`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-readings.json), [`flight-principia-without-this-mod-logs.csv`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-logs.csv) and [`flight-principia-without-this-mod-analysis.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-analysis.txt);
  - with this mod: [`flight-principia-fix-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-script.txt), [`flight-principia-fix-readings.json`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-readings.json), [`flight-principia-fix-logs.csv`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-logs.csv) and [`flight-principia-fix-analysis.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-analysis.txt).
