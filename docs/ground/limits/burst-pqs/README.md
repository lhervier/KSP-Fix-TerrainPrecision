# BurstPQS

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#limits-and-solutions): what this mod makes worse with BurstPQS, or would break without a support of its own, and the solution to each.

[BurstPQS](https://github.com/Phantomical/BurstPQS) builds the terrain in place of stock, in Burst-compiled
jobs, and places it in double precision on its own. It requires Kopernicus. Every campaign of this mod was
played again with it, in two installs: **BurstPQS** (KSP, KSP Community Fixes, BurstPQS and what it requires)
and **BurstPQS with this mod, as it installs**. BurstPQS holds the ground still on the bodies it builds, but
not the statics nor the scatter, which this mod still corrects. Without a support of its own, this mod would
get two things wrong with BurstPQS: its terrain fix would place the same quads as BurstPQS, or, turned off,
would leave uncorrected the bodies BurstPQS gives back to stock; and its scatter fix would miss the holders
built as a scene opens. **This mod supports BurstPQS by itself**, with nothing to set: its terrain fix steps
back on every body BurstPQS builds and keeps correcting the bodies it leaves to stock, and its scatter fix
hangs every holder there.

Unless a page says otherwise, each limit is measured in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1, BurstPQS 1.0.27 and what it requires (Kopernicus 251, Modular Flight Integrator,
KSPTextureLoader, KSPBurst), and this mod, plus the instrument and the mods it names. Release 1.0.28 is not
checked yet: [BurstPQS: its release 1.0.28](../../work-in-progress/burst-pqs/its-release-1-0-28.md).

## The campaigns played with BurstPQS

**Checked, nothing worse with this mod.** On the bodies BurstPQS builds, the ground no longer moves at a load,
an approach, a vessel switch, a move of the world or in a fast flight, and it is the same ground as this mod's
terrain fix builds. The statics still move without this mod, and now against a ground that holds; with it,
they hold. This mod's terrain fix steps back by itself on the bodies BurstPQS builds: nothing placed twice,
and the ground holds as with BurstPQS alone. The scatter moves against the ground without this mod, and holds
with it (see [The scatter](#the-scatter) below). The anchor has nothing to play: BurstPQS never touches it.

**→ Full chapter: [BurstPQS: the campaigns](the-campaigns.md)**, and for the statics,
[BurstPQS: the campaigns, the statics](../../../statics/non-regression/burst-pqs/the-campaigns.md)

## The bodies BurstPQS leaves to stock

**A limit this mod handles by itself, until the next Real Solar System.** With Real Solar System 20.1.3, its
latest release, BurstPQS gives the Earth, the Moon and Mars back to stock, and their ground moves as on
stock. With this mod's terrain fix off, nothing corrects it; with it on, it holds. This mod's terrain fix
takes over on them by itself, while it steps back on the bodies BurstPQS builds: until the next Real Solar
System is out, it stays needed there. That version, on its master branch but not released yet, lets
BurstPQS build them, and the case goes away: built from it, their ground holds with BurstPQS alone.

**→ Full chapter: [BurstPQS: the bodies it leaves to stock](the-bodies-it-leaves-to-stock.md)**

## The scatter

**A problem this mod fixes, the scatter fix on by default.** With BurstPQS, rocks, grass and trees move
against the ground from one load to the next by more than on stock, and jump against it at every move of the
world. This mod's scatter fix first missed every holder built as the scene opens; it now hangs them all:
hundredths of a millimetre at a load, rocks with colliders included, nothing at a move of the world or in
flight.

**→ Full chapter: [BurstPQS: the scatter](../../../scatter/limits/burst-pqs/the-scatter.md)**

## Darker quads: not from this mod

Seen during these campaigns, with or without this mod: in the first flight after KSP starts, whole quads of
the ground of the Mun are drawn much darker than their neighbours for a minute or two, the relief running on
unbroken from one to the next; also on Minmus, Laythe and Mercury of Real Solar System. Not on KSP with KSP
Community Fixes alone, nor with Kopernicus alone. The cause is in Kopernicus: the plugin it ships for
BurstPQS with its KSC scatter mask wipes the colour of every quad of a body's first build. Already reported to
BurstPQS as [issue #14](https://github.com/Phantomical/BurstPQS/issues/14), traced there to Kopernicus by
BurstPQS's author, and to be fixed in the next release of Kopernicus. Our report, with the protocol and the
screenshots, was closed as its duplicate: [issue #15](https://github.com/Phantomical/BurstPQS/issues/15).
