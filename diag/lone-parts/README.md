# The runs: parts lying alone

Part of [Terrain Precision Fix](../../README.md), [parts lying alone](../../docs/lone-parts/README.md): the saves, the scripts and the `KSP.log` of every session, on stock, with this mod and one of its settings turned off, and with this mod as installed. The scripts are in [`automation/`](automation).

KSP 1.12.5 on Windows, played in French, `GameData` holding Harmony, ModuleManager, KSP Community Fixes
1.41.1, KSP Diag - Landed Vessel, KSP-Util-MCPServer, and this mod or not. Each configuration is a single
session of KSP. Copy a save into the folder of a sandbox game and load it from that game.

## Loading the same save

[`lone-parts-mun.sfs`](checking/loading/lone-parts-mun.sfs), loaded ten times per configuration by
[`run-lone-parts.py`](automation/run-lone-parts.py). Read in
[Checking parts lying alone: loading the same save](../../docs/lone-parts/checking/loading.md).

- on stock: [`loading-stock.log`](checking/loading/loading-stock.log),
  [`loading-stock-script.txt`](checking/loading/loading-stock-script.txt),
  [`loading-stock-lines.json`](checking/loading/loading-stock-lines.json);
- with `fixTerrain = false`: [`loading-no-terrain.log`](checking/loading/loading-no-terrain.log),
  [`loading-no-terrain-script.txt`](checking/loading/loading-no-terrain-script.txt),
  [`loading-no-terrain-lines.json`](checking/loading/loading-no-terrain-lines.json);
- with `fixLonePartMass = false`: [`loading-no-lone-part-mass.log`](checking/loading/loading-no-lone-part-mass.log),
  [`loading-no-lone-part-mass-script.txt`](checking/loading/loading-no-lone-part-mass-script.txt),
  [`loading-no-lone-part-mass-lines.json`](checking/loading/loading-no-lone-part-mass-lines.json);
- as installed: [`loading-fix.log`](checking/loading/loading-fix.log),
  [`loading-fix-script.txt`](checking/loading/loading-fix-script.txt),
  [`loading-fix-lines.json`](checking/loading/loading-fix-lines.json).

## A wheel dropped in EVA construction

[`wheel-drop-kerbin.sfs`](checking/wheel-drop/wheel-drop-kerbin.sfs) and
[`wheel-drop-mun.sfs`](checking/wheel-drop/wheel-drop-mun.sfs), five drops per configuration by
[`run-wheel-drop.py`](automation/run-wheel-drop.py). Read in
[Checking parts lying alone: a wheel dropped in EVA construction](../../docs/lone-parts/checking/wheel-drop.md).
In [`checking/wheel-drop/`](checking/wheel-drop/), for each body (`kerbin`, `mun`) and each configuration
(`stock`, `no-lone-part-mass`, `fix`): `wheel-drop-<body>-<configuration>.log`, `-script.txt` and
`-lines.json`.

## On the runway

[`lone-parts-runway.sfs`](checking/runway/lone-parts-runway.sfs), made around the rover of
[`Diag2-Rover.craft`](checking/runway/Diag2-Rover.craft), loaded ten times per configuration by
[`run-lone-parts.py`](automation/run-lone-parts.py). Read in
[Checking parts lying alone: on the runway](../../docs/lone-parts/checking/runway.md). In
[`checking/runway/`](checking/runway/), for each configuration (`stock`, `no-lone-part-mass`, `fix`):
`runway-<configuration>.log`, `-script.txt` and `-lines.json`.
