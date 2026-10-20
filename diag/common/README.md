# The runs

Part of [Terrain Precision Fix](../../README.md): the saves, the scripts and the `KSP.log` of every
session, without this mod and with it, one folder per fix, as in `docs`:

- [the ground](../ground/README.md), read in [the ground](../../docs/ground/README.md);
- [the statics](../statics/README.md), read in [the statics](../../docs/statics/README.md);
- [the scatter](../scatter/README.md), read in [the scatter](../../docs/scatter/README.md);
- [the ROCs](../rocs/README.md), read in [the ROCs](../../docs/rocs/README.md);
- [the ground anchor](../ground-anchor/README.md), read in [the ground anchor](../../docs/ground-anchor/README.md);
- and here, what the fixes share: Principia, this mod's safeguard on Real Solar System, and the
  [performance runs](perfs/README.md), read in [what the fixes share](../../docs/common/README.md).

Each page has its folder at the same path as the page under `docs`: the logs, saves and crafts of
[An anchor on a static](../../docs/ground-anchor/non-regression/stock/an-anchor-on-a-static.md) are in
[`diag/ground-anchor/non-regression/stock/an-anchor-on-a-static/`](../ground-anchor/non-regression/stock/an-anchor-on-a-static),
and its screenshots in
[`imgs/ground-anchor/non-regression/stock/an-anchor-on-a-static/`](../../imgs/ground-anchor/non-regression/stock/an-anchor-on-a-static).
A file that several pages use is in the folder of the page that measures with it. The scripts that play
the protocols are in the `automation/` folder of each fix.

## With Principia

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[Principia](https://github.com/mockingbirdnest/Principia) Lévy on the stock system, the instruments of each
protocol, and [KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which plays the protocols; this
mod at `logLevel = Debug`, or not: each session is here twice, `-without-this-mod` and `-fix`. Read in
[Principia: the bodies it moves and turns](../../docs/common/non-regression/principia/the-bodies-it-moves-and-turns.md).

- [`loading-principia-without-this-mod.log`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod.log) and
  [`loading-principia-fix.log`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix.log) — the four saves of
  [the loading protocol](../../docs/ground/checking/loading-protocol.md),
  each loaded six times by `run-loading.py`, both instruments at once; what the script printed in
  [`loading-principia-without-this-mod-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod-script.txt)
  and [`loading-principia-fix-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix-script.txt), every line it recorded,
  with the save it was recorded on, in
  [`loading-principia-without-this-mod-lines.json`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-without-this-mod-lines.json)
  and [`loading-principia-fix-lines.json`](non-regression/principia/the-bodies-it-moves-and-turns/loading-principia-fix-lines.json).
- [`flight-principia-without-this-mod.log`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod.log) and
  [`flight-principia-fix.log`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix.log) — one flight each of
  [the protocol of the quads of the highest level, in flight](../../docs/ground/checking/flight-protocol.md),
  from the launchpad of the Space Center, KSP Diag - Terrain Quads and KSP Diag - Floating Origin; for each,
  as for the flights of [In flight](../ground/README.md#the-protocol-of-the-quads-of-the-highest-level-in-flight), what the
  script printed, the readings, the logs, the quads (49 MB once unzipped) and the analysis:
  - without this mod: [`flight-principia-without-this-mod-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-script.txt), [`flight-principia-without-this-mod-readings.json`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-readings.json), [`flight-principia-without-this-mod-logs.csv`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-logs.csv), [`flight-principia-without-this-mod-quads.zip`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-quads.zip) and [`flight-principia-without-this-mod-analysis.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-without-this-mod-analysis.txt);
  - with this mod: [`flight-principia-fix-script.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-script.txt), [`flight-principia-fix-readings.json`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-readings.json), [`flight-principia-fix-logs.csv`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-logs.csv), [`flight-principia-fix-quads.zip`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-quads.zip) and [`flight-principia-fix-analysis.txt`](non-regression/principia/the-bodies-it-moves-and-turns/flight-principia-fix-analysis.txt).

## On Real Solar System

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, and
[Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 with what it requires (Kopernicus,
Modular Flight Integrator, KSPTextureLoader, the RSS textures), as released. This mod ran at
`logLevel = Debug`, so each log also holds one line per quad placed, with how far it was moved. Read in
[This mod's safeguard](../../docs/common/safeguard.md).

- [`reload-venus-mars-rss-fix.log`](safeguard/reload-venus-mars-rss-fix.log) — no instrument, one
  session: six loads of [`reload-venus-rss.sfs`](safeguard/reload-venus-rss.sfs), then six of
  [`reload-mars-rss.sfs`](safeguard/reload-mars-rss.sfs). The six loads after them, on a second site of Mars,
  are not used.
- [`reload-mercury-rss-fix.log`](safeguard/reload-mercury-rss-fix.log) — no instrument: six loads of
  [`reload-mercury-rss.sfs`](safeguard/reload-mercury-rss.sfs). Each one logs KSP moving the craft down 22.4 m,
  the terrain detail its save describes.
