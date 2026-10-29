# The fix: parts lying alone

Part of [Terrain Precision Fix](../../README.md), [parts lying alone](README.md#the-fix): what this mod does to the extra mass of a part lying alone, why for every part, and what it leaves alone.

Stock makes a part lying alone much heavier for 3 seconds every time it goes off rails, which made its pops
smaller on the moving ground, and throws the parts with a suspension
([The culprit: parts lying alone](the-culprit.md)). With the ground fixed, no part starts inside it any
more: for a part without a suspension, the extra mass has nothing left to soften, and for a part with one,
it still throws it. This mod turns it off.

## The extra mass given back

A Harmony postfix on `ModuleCargoPart.OnPartUnpack`: when the coroutine `MakePartSettle` has raised the
part's mass, it gives the part its own mass back, the one `MakePartSettle` kept before raising it. The
coroutine raises the mass before it first waits, so the part never goes through a physics step with the
extra mass. Three seconds later, the coroutine gives back the same mass, and nothing changes. It has a
setting of its own, `fixLonePartMass`, on by default, and lives in
[`Src/LonePartMassFix.cs`](../../Src/LonePartMassFix.cs).

At `logLevel = Debug`, the log says it for each part given its mass back:

```
[KSPFixTerrainPrecision] [DEBUG] Lone part mass fix: 'Pile rechargeable Z-400' given back its own mass, 0.020 t, instead of 20 t
```

## For every part

Not only the parts with a suspension. With the ground fixed, the extra mass changes nothing for the others:
it only stays useful where a part alone still starts inside the ground, and it no longer does
([Checking parts lying alone: loading the same save](checking/loading.md)). Turning it off for every
part keeps one rule, the same on every body, and leaves nothing to look after that no longer does anything.

**Why not keep it for a kerbal bumping into the part?** The extra mass lasts the 3 seconds after the part
goes off rails; a kerbal walking into the part later meets its own mass, on stock as with this mod.

**Why not keep it on a slope?** When `CheckGroundCollision` puts a craft back onto a slope, it compares the
drop to its lowest point with the ground straight under its root, and sees a gap that is not there; past
the 10 cm it ignores, it sinks the craft into the slope. Read in the code, not measured. That does not
depend on the ground this mod fixes, and a tall part on a steep slope could still need the extra mass:
[A tall part on a steep slope](work-in-progress/a-large-part-on-a-steep-slope.md) is to check that it
does not.

## Independent of the fix of the ground

The setting acts whether `fixTerrain` is on or off. With `fixTerrain = false` and `fixLonePartMass = true`,
the ground moves as on stock and the parts lie alone without the extra mass: the install that shows what the
extra mass did on stock's ground
([Checking parts lying alone: loading the same save](checking/loading.md)). On a body above 1.1 g, where
stock adds nothing, it does nothing.

## What it leaves alone

- **Breaking Ground's deployed experiments**, which go through the same coroutine from `ModuleGroundPart`,
  and are riveted to the ground once it has run: see
  [Breaking Ground's deployed experiments](../ground/work-in-progress/stock/breaking-grounds-deployed-experiments.md).
- **A craft of several parts**, which stock never makes heavier.

## Safeguards

- the setting turns the fix off, or on, on its own;
- if the patch cannot be installed, parts are made heavier as on stock, and the log says so;
- the patch only acts when the coroutine has raised the mass, and gives back the mass the coroutine kept.
