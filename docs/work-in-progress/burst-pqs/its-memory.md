# BurstPQS: its memory

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [BurstPQS](../../work-in-progress/burst-pqs.md).

**Status: to dig — read in its code, not yet seen in the game.** Reading the code of BurstPQS 1.0.27 shows
three places where memory is released twice or never. None has been seen in the game yet; they are noted
here to be looked at more closely, then reported to BurstPQS.

- **A pinned handle released twice.** The Burst versions of `PQSMod_VertexSimplexColorRGB` and
  `PQSMod_VertexSimplexMultiChromatic` pin the noise tables of the mod for each quad, in a `using`
  declaration in `OnQuadPreBuild`: the handle is released as `OnQuadPreBuild` returns, then again when the
  build job is disposed. *What it could do in the game:* the second release may unpin something else that
  BurstPQS holds pinned, and a later quad would read memory that was freed. Only on bodies whose terrain
  uses one of these two mods.
- **Burst versions of the terrain mods never released.** `BatchPQS.PostSetupMods` builds the Burst version of
  every terrain mod each time the game sets up a body's terrain mods again, and drops the previous ones
  without disposing of them: what they allocated stays allocated. *What it could do in the game:* memory that
  grows a little at each new set-up of a body's terrain.
- **Height maps loaded on demand that are never unloaded.** The Burst version of Kopernicus's
  `PQSMod_OnDemandHandler` does not pass on the call that marks the body's maps as in use. When BurstPQS
  loads a map of a body whose handler has unloaded its maps, nothing unloads it again. *What it could do in
  the game:* the memory taken by the height and colour maps of every body visited, which can be tens of
  megabytes each on Real Solar System.

*To do:* for each, find a way to see it in the game (memory growing across scene changes and body visits,
the bodies that use the two noise mods), then report it to BurstPQS.
