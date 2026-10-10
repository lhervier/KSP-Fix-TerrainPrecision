# Checking the culprit: driving on while the world moves

Part of [Terrain Precision Fix](../README.md): the measurements that check two culprits under a rover
that keeps driving while the game moves its whole world, on stock and with this mod, on Kerbin and on
Earth in Real Solar System, one page each: [the ground](checking-the-culprit-driving/the-ground.md), on
the grass, and [the statics](checking-the-culprit-driving/the-statics.md), on the runway of the KSC with
the grass beside it.

[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) measures the
ground, and [KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin),
which only reads, says when the world moves. Each has its own page, with its method.

This fix is built on top of [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes),
the base most players run, so every campaign of these pages is run in an install that has it: KSP 1.12.5
with Harmony, ModuleManager, KSP Community Fixes 1.41.1, the two instruments and
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), which drives the rover — and this mod, or
not; on Earth, [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 and what it
requires as well. *On stock* means that install without this mod.

Every 500 m the craft you fly travels, KSP moves the floating origin back onto it, and with it the
terrain sphere, which carries the ground and the statics alike
([Why it is different at every load](the-culprit-ground.md#why-it-is-different-at-every-load)).

## The ground

A rover drives due south on the grass by the KSC, read just before each move of the origin, just after
it, and the same few metres farther on with no move. On stock, the ground under it jumps by 26.6 and
24.7 mm on Kerbin and by 159 mm on Earth; with this mod, no move stands out from what the few metres do.

**→ Full page: [Checking the ground: driving on while the world moves](checking-the-culprit-driving/the-ground.md)**

## The statics

A rover by the runway of the KSC reads a spot on the grass and one on the deck, before and after each
move of the origin. On stock, the deck moves with the grass, by up to 54.8 mm on Kerbin and 231.8 mm on
Earth. With the terrain fix alone, the grass holds and the deck still moves, by up to 41.6 mm; with this
mod as installed, neither does, within 0.07 mm on Kerbin.

**→ Full page: [Checking the statics: driving on while the world moves](checking-the-culprit-driving/the-statics.md)**
