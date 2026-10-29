# The ROCs

Part of [Terrain Precision Fix](../../README.md): Breaking Ground's surface features (ROCs), the objects
studied in EVA or with the robotic arms. Where the rounding strikes them in the stock code, how this mod
takes it away, how that is checked, and what is still to check.

> **Fix the ground, and Breaking Ground's surface features no longer come back at the same height as the
> ground.** On stock, they are never placed quite on the ground, but they move with it. Fix the ground
> alone, and they keep moving, at every load and every 500 m a craft drives, against a ground that no longer
> does.

> [!WARNING]
> **This fix is not a harmless one, and it can break other mods.** It moves the holders of the surface
> features away from where stock hangs them, and a mod that looks for them there would miss them. If one
> misbehaves around surface features, `fixRocs = false` turns this fix off
> ([Settings](../common/settings.md)).

## Why it matters

Unlike stock rocks, a surface feature has a collider: a kerbal or a part resting on one is moved with it,
and can be thrown, if not by much. Above all, it shows: while a rover drives by them, every 500 m, the
features jump against the ground. Not by much either, but enough to be seen.

## The culprit

The surface features are placed like the scatter: built from the vertices of their quad, but hung from a
*holder* that stays under the body, at a 600 km vector in a float. Unlike stock rocks, they carry a
collider: a kerbal or a part resting on one moves with it. The terrain fix makes it show: the ground stops
moving, the holders do not.

The rounding itself, shared with the ground, the statics and the scatter, is told once in
[The culprit: a float at planet scale](../common/the-culprit.md).

**→ Full chapter: [The culprit: the ROCs](the-culprit.md)**

## The fix

Two Harmony patches hang each holder from its own quad, at no offset, and hang it back in its pool when
the quad goes, as the scatter fix does for the rocks. It is on by default. It moves stock objects other mods
may look for: if one of them misbehaves around surface features, one line of the settings file turns it
off, `fixRocs = false` ([Settings](../common/settings.md)).

**→ Full chapter: [The fix: the ROCs](the-fix.md)**

## Checked

Measured with this mod and its fix of the surface features turned off, then with this mod as installed,
in an install with [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes): KSP 1.12.5
with the Breaking Ground expansion, Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel), and
[KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer), which plays the protocol.

- **Loading the same save**, six times, Jebediah Kerman standing on a Mun stone: with the fix of the
  surface features off, the kerbal settles over a range of 10.04 mm, the ground under the stone held
  still; with this mod as installed, 0.008 mm.

  **→ Full chapter: [Checking the ROCs: loading the same save](checking/loading.md)**

The saves, the scripts and the readings of every session are in
[the runs of the ROCs](../../diag/rocs/README.md).

## Work in progress

**Driving on while the world moves: planned.** Every 500 m a craft travels, the floating origin moves,
and with it the ground and the holders of the surface features. With the terrain fix alone, the ground
holds and the features would jump against it, as the scatter does; with this mod as installed, they should
not.

**→ Full chapter: [Driving on while the world moves, by a ROC](work-in-progress/driving.md)**

**Scene changes and time warp, with Jeb on a ROC: planned.** Both are checked on the statics of the KSC;
they are still to play with a kerbal standing on a surface feature.

**→ Full chapter: [Scene changes and time warp, with Jeb on a ROC](work-in-progress/scene-changes-and-time-warp.md)**
