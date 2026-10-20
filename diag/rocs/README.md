# The runs: the ROCs

Part of [Terrain Precision Fix](../../README.md), [the ROCs](../../docs/rocs/README.md): the saves and the `KSP.log` of every session, with this mod and its fix of the surface features turned off, and with this mod as installed. The script is the ground's, in [`../ground/automation/`](../ground/automation).

## Loading the same save

KSP 1.12.5 on Windows, with the Breaking Ground expansion, `GameData` holding Harmony, ModuleManager, KSP
Community Fixes 1.41.1, KSP Diag - Landed Vessel, KSP-MCPServer and this mod, with `fixRocs = false` for
`rocs-fix-off`. The save loaded six times per configuration, in a single session of KSP each, by
[`run-loading.py`](../ground/automation/run-loading.py), which recorded once the live line had stopped
moving. Read in
[Checking the ROCs: loading the same save](../../docs/rocs/checking/loading.md).

The save, [`roc-mune-jeb.sfs`](checking/loading/roc-mune-jeb.sfs): Jebediah Kerman standing on a small Mun
stone, the pod Jebediah stepped out of standing 6 m away. Copy it into the folder of a sandbox game and load
it from that game.

- [`loading-rocs-fix-off.log`](checking/loading/loading-rocs-fix-off.log) — the `KSP.log` of the session
  with the fix of the surface features off; what the script printed in
  [`roc-mune-jeb-rocs-fix-off-script.txt`](checking/loading/roc-mune-jeb-rocs-fix-off-script.txt), and
  every line it recorded in
  [`roc-mune-jeb-rocs-fix-off-lines.json`](checking/loading/roc-mune-jeb-rocs-fix-off-lines.json).
- [`loading-fix.log`](checking/loading/loading-fix.log) — the same with this mod as installed; what the
  script printed in [`roc-mune-jeb-fix-script.txt`](checking/loading/roc-mune-jeb-fix-script.txt), and every
  line it recorded in [`roc-mune-jeb-fix-lines.json`](checking/loading/roc-mune-jeb-fix-lines.json).
