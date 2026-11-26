# Terrain Precision Fix

**⚠️ Work in progress.** This is an active investigation, not a finished mod. The figures, the code and the conclusions on these pages can still change, and several questions are still open — each page has its own *Work in progress*.

A mod for stock KSP 1.12: several fixes for the ground and for what stands on it, the runways, launchpads and
buildings, the rocks and the surface features, plus an anchored base and a part lying alone. Each is kept as small
as possible, a handful of Harmony patches, and has its own folder below: what goes wrong in game, why, how it was
checked, and what the mod does about it. It is a mod of its own, built and measured on top of
[KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes), the base most players run.

The ground moving is one cause among several of a craft that moves when a scene opens, and this mod removes only
that one: a lander that hops because its legs are still unfolding will go on hopping. Two other causes have their own
fixes: [Suspension Bounce Fix](https://github.com/lhervier/KSP-Fix-SuspensionBounce) for landing legs and wheels,
and [Landed Shape Fix](https://github.com/lhervier/KSP-Fix-LandedShape) for a craft that physics had bent to fit the
ground, and that a load brings back unbent.

**How this was made.** The investigation and the code were written with Claude, Anthropic's AI
assistant. Everything here was reviewed and validated by a human — me — who very much enjoyed
learning along the way how KSP builds the ground you land on. I am saying so up front, because
contributions made with an AI deserve a closer look than others, and because some people would
rather stop reading here. That look is what these pages are built for: every figure on them comes from an
in-game measurement, the instrument behind the headline figures is public and runs on a stock
install, the stock code quoted here is a handful of lines anyone can check, and the fix is a few short
files you can read in one sitting.

## How KSP builds the ground

The ground KSP builds under you is never built at the same height twice, nor are the runways and buildings on it:
at every load, every 500 m driven, every return to a parked craft. When it comes back higher, the craft is launched.

**→ Full chapter: [How KSP builds the ground](docs/how-ksp-builds-the-ground/README.md)**

## Planet Frame

Not a fix: the frame a body's terrain sphere hangs in, worked out in double precision, which the ground and the
statics fixes share. It also refuses any correction too large to be a rounding, and leaves the object where stock
puts it.

**→ Full chapter: [Planet Frame](docs/planet-frame/README.md)**

## The ground

The terrain a craft stands on comes back higher or lower each time it is rebuilt. The mod places its quads in double
precision: at a load, it moves 0.3 mm instead of 43.6 on Kerbin, 292.3 on Earth in Real Solar System. Setting:
`fixTerrain`.

**→ Full chapter: [The ground](docs/ground/README.md)**

## The statics

The KSC's runway, launchpad and buildings, and the launch sites of Making History and Kerbal Konstructs, come back at
a height of their own. The mod places them in double precision: the KSC runway moves 0.177 mm at a load instead of
116.5. Setting: `fixStatics`.

**→ Full chapter: [The statics](docs/statics/README.md)**

## The scatter

Fix the ground, and the rocks, grass and trees, which stock moves with it, keep moving against it. The mod draws
them from the quads they grow on: against the ground at a load, 0.132 mm instead of 61 on stock. Setting:
`fixScatter`.

**→ Full chapter: [The scatter](docs/scatter/README.md)**

## The ROCs

Breaking Ground's surface features are placed like the scatter, with a collider a kerbal can stand on. The mod
draws them from their quads too: a kerbal on one moves 0.008 mm at a load instead of 10.04 with the ground fixed
alone. Setting: `fixRocs`.

**→ Full chapter: [The ROCs](docs/rocs/README.md)**

## The ground anchor

Not a rounding: two stock behaviours raise an anchored base, and its riveted anchor keeps it in the
air. The mod lowers the anchor's collider and loads the base where it was saved: 0.08 mm at its second load instead
of 26.3 cm. Settings: `fixGroundAnchor…`.

**→ Full chapter: [The ground anchor](docs/ground-anchor/README.md)**

## Parts lying alone

Not a rounding: for 3 seconds, stock makes a part lying alone far heavier, which throws a wheel up. The mod removes
that weight: a wheel alone on the Mun rises 13 to 15 mm at a load, not 1.3 to 13.7 m. Setting: `fixLonePartMass`.

**→ Full chapter: [Parts lying alone](docs/lone-parts/README.md)**

## Checked

Each fix's checked cases have their pages in its folder: the save each starts from, how to play it by hand, the
script that plays it, and what it shows without and with this mod. Each situation where a craft meets the ground is
measured twice, without this mod and with it: one instrument reads the landed craft, another the ground itself, and
in flight a third reads the quads the ground is made of; a fourth reads the scatter. In each summary, the first figure
is without this mod, the second with it.

Every campaign is run in KSP 1.12.5 with Harmony, ModuleManager and KSP Community Fixes 1.41.1; *on stock* means that
install without this mod. Each run keeps its save, zipped, and its `KSP.log`, compressed, without the loading of the
game's assets. The scripts drive KSP through
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), and need nothing but Python 3.

## What every fix shares

**It does not slow the game down**: timed frame by frame, it came out no dearer than stock. Saves made without this
mod load with it, Principia works with it, and Tilt'Em and KAS are still to check.

**→ Full chapter: [What the fixes share](docs/common/README.md)**

## Installing

Requires KSP 1.12 and [HarmonyKSP](https://github.com/KSPModdingLibs/HarmonyKSP) (the usual
`GameData/000_Harmony`, also installed by KSP Community Fixes).

Copy `GameData/KSPFixTerrainPrecision` into the `GameData` folder of KSP. Every fix is on by default, and each can be
turned off in [the settings](docs/common/settings.md). Nothing is written to your saves: removing the folder gives
you the stock terrain, statics, scatter and ground anchors back. An anchored base is then raised again at its next
load, as stock raises it: [Removing this mod](docs/ground-anchor/the-fix.md#removing-this-mod).

## Building

Set `KSPDIR` to your KSP install folder, which must contain `GameData/000_Harmony`, and run `build.bat`. It needs the
.NET SDK, and compiles `GameData/KSPFixTerrainPrecision/KSPFixTerrainPrecision.dll`.

## License

MIT, see [LICENSE](LICENSE).
