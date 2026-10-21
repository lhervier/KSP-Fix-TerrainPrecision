# The runs: the ground anchor

Part of [Terrain Precision Fix](../../README.md), [the ground anchor](../../docs/ground-anchor/README.md): the saves, the scripts and the `KSP.log` of every session, without this mod and with it. The scripts are in [`automation/`](automation).

## The ground anchor protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel),
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight), and this mod at
`logLevel = Debug`, or not: [`ground-anchor-kerbin.sfs`](checking/anchoring/ground-anchor-kerbin.sfs), Bill Kerman places a
ground anchor on the desert of Kerbin beside the rover of [`Diag3-Rover.craft`](checking/anchoring/Diag3-Rover.craft),
alone, then with one of the rover's batteries attached on top of it; quicksave and quickload twice,
played by hand. Three sessions: without this mod, with this mod and `fixGroundAnchorLoad = false`, and with
this mod as installed. Read in
[Checking the culprit: anchoring a base](../../docs/ground-anchor/checking/anchoring.md).

- [`ground-anchor-kerbin-without-this-mod.log`](checking/anchoring/ground-anchor-kerbin-without-this-mod.log), which
  holds a first placement, given up, before the two measured;
- [`ground-anchor-kerbin-model-fix.log`](checking/anchoring/ground-anchor-kerbin-model-fix.log), which holds a first
  series of both cases before the measured one, the anchor with a battery read without it set as target;
- [`ground-anchor-kerbin-fix.log`](checking/anchoring/ground-anchor-kerbin-fix.log).

Below 50 frames per second: the same install, *Frame Limit* at 30 and KSP-Util-MCPServer, the base of
[`anchor-base-desert-airfield.sfs`](checking/anchoring/anchor-base-desert-airfield.sfs) loaded, then ten quicksaves and quickloads
played by [`automation/run-anchor-on-a-static.py`](automation/run-anchor-on-a-static.py) with `--from-save`
and `--only base`. Three sessions: without this mod, with this mod and `fixGroundAnchorRivet = false`, and
with this mod as installed. Read in
[Checking the culprit: anchoring a base, below 50 frames per second](../../docs/ground-anchor/checking/anchoring.md#below-50-frames-per-second).

- without this mod: [`anchor-rivet-30fps-without-this-mod.log`](checking/anchoring/anchor-rivet-30fps-without-this-mod.log), with what the script
  printed in [`anchor-rivet-30fps-without-this-mod-script.txt`](checking/anchoring/anchor-rivet-30fps-without-this-mod-script.txt) and the readings
  of KSP Diag - Landed Vessel in [`anchor-rivet-30fps-without-this-mod-readings.json`](checking/anchoring/anchor-rivet-30fps-without-this-mod-readings.json);
- with `fixGroundAnchorRivet = false`: [`anchor-rivet-30fps-rivet-fix-off.log`](checking/anchoring/anchor-rivet-30fps-rivet-fix-off.log), with what the script
  printed in [`anchor-rivet-30fps-rivet-fix-off-script.txt`](checking/anchoring/anchor-rivet-30fps-rivet-fix-off-script.txt) and the readings
  of KSP Diag - Landed Vessel in [`anchor-rivet-30fps-rivet-fix-off-readings.json`](checking/anchoring/anchor-rivet-30fps-rivet-fix-off-readings.json);
- with this mod as installed: [`anchor-rivet-30fps-rivet-fix-on.log`](checking/anchoring/anchor-rivet-30fps-rivet-fix-on.log), with what the script
  printed in [`anchor-rivet-30fps-rivet-fix-on-script.txt`](checking/anchoring/anchor-rivet-30fps-rivet-fix-on-script.txt) and the readings
  of KSP Diag - Landed Vessel in [`anchor-rivet-30fps-rivet-fix-on-readings.json`](checking/anchoring/anchor-rivet-30fps-rivet-fix-on-readings.json).

## The anchor on a static protocol

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, both instruments, this mod at
`logLevel = Debug`, and KSP-Util-MCPServer: in a new sandbox game, [`Diag3-Rover-Two-Anchors.craft`](non-regression/stock/an-anchor-on-a-static/Diag3-Rover-Two-Anchors.craft)
launched from the SPH onto the runway of the KSC, then in another game onto the runway of the Desert
Airfield, Bill Kerman aboard with his inventory emptied; Bill places an anchor alone and an anchor with a
battery on it, by hand; then [`automation/run-anchor-on-a-static.py`](automation/run-anchor-on-a-static.py)
reads both anchors as placed, and after each of five quicksaves and quickloads. Played again without this
mod. Read in [An anchor on a static](../../docs/ground-anchor/non-regression/stock/an-anchor-on-a-static.md).

- [`anchor-on-a-static-with-this-mod.log`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-with-this-mod.log), one session for
  both runways, the Desert Airfield first, followed by three more quicksaves and quickloads there that are
  not part of the test; [`anchor-on-a-static-runway-without-this-mod.log`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-without-this-mod.log)
  and [`anchor-on-a-static-desert-airfield-without-this-mod.log`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-without-this-mod.log);
- what the script printed, and the readings of both instruments, for each runway with and without this mod:
  - the runway of the KSC, with this mod: [`anchor-on-a-static-runway-with-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-with-this-mod-script.txt) and
    [`anchor-on-a-static-runway-with-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-with-this-mod-readings.json);
  - the runway of the KSC, without it: [`anchor-on-a-static-runway-without-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-without-this-mod-script.txt) and
    [`anchor-on-a-static-runway-without-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-runway-without-this-mod-readings.json);
  - the Desert Airfield, with this mod: [`anchor-on-a-static-desert-airfield-with-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-with-this-mod-script.txt) and
    [`anchor-on-a-static-desert-airfield-with-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-with-this-mod-readings.json);
  - the Desert Airfield, without it: [`anchor-on-a-static-desert-airfield-without-this-mod-script.txt`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-without-this-mod-script.txt) and
    [`anchor-on-a-static-desert-airfield-without-this-mod-readings.json`](non-regression/stock/an-anchor-on-a-static/anchor-on-a-static-desert-airfield-without-this-mod-readings.json).
