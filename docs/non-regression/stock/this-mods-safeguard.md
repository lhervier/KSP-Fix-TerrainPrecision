# Stock: this mod's safeguard

Part of [Terrain Precision Fix](../../../README.md), one test of [Non-regression tests](../../non-regression.md), on [stock](../stock.md).

**Status: checked on Kerbin, the Mun, Minmus and Gilly — the safeguard never refused a correction. The
largest one was 3.9 float steps, a quarter of the limit.**

*The rule.* This mod refuses any correction larger than sixteen float steps, taken at the distance from
the centre of the body: the quad, or the static, is then left where stock puts it
([Safeguards](../../the-fix-ground.md#safeguards)). The limit grows with the body, as the rounding does:
1 m on Kerbin, 250 mm on the Mun, 62.5 mm on Minmus, 15.6 mm on Gilly.

*Why it is a non-regression test.* A correction refused by mistake puts the defect back where it was
refused. The small bodies are where the limit is tightest in millimetres: a limit set too low against the
rounding there would show as quads left as stock builds them.

## The margin

The sessions with this mod ran at `logLevel = Debug`, which logs how far each quad was moved. The quads
placed and the largest correction on each body, over every log of the [runs](../../../diag/README.md)
taken with this mod:

| body | float step | limit | quads placed | largest correction |
|---|---|---|---|---|
| Kerbin | 62.5 mm | 1 m | 81 980 | 221.1 mm, 3.5 steps |
| the Mun | 15.6 mm | 250 mm | 9 636 | 57.8 mm, 3.7 steps |
| Minmus | 3.9 mm | 62.5 mm | 4 752 | 12.6 mm, 3.2 steps |
| Gilly | 0.98 mm | 15.6 mm | 12 044 | 3.8 mm, 3.9 steps |

The float step is the one at the radius of the body. A quad that stands higher than the next power of two
metres from the centre has a step twice as large, and a correction worth half as many steps: on Gilly,
13 km in radius, that is every quad more than 3.4 km above its datum, so its count is an upper bound.

No log of these runs holds the line the safeguard writes when it refuses a correction:

```
[TerrainPrecisionFix] <body>: a correction of … m is more than 16 float steps (… m at that distance), too large to be a rounding error, the quads concerned are left as stock builds them
```

The bodies of Real Solar System, ten times the size of Kerbin, have their own margin, of the same order:
[Real Solar System: this mod's safeguard](../real-solar-system/this-mods-safeguard.md).
