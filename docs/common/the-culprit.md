# The culprit: a float at planet scale, in a frame that moves

Part of [Terrain Precision Fix](../../README.md), [what the fixes share](README.md).

Four of the things this mod fixes share one culprit. Stock places the ground, the statics standing on it,
the scatter growing on it and Breaking Ground's surface features through Unity `Transform`s, whose positions are floats, holding vectors as
long as the radius of the body: 600 km on Kerbin. At that length a float moves in steps of 62.5 mm, so each
value is rounded to the nearest step, up or down.

A rounding on its own would land the same way every time. What draws a new one is the frame these vectors
go through — how the body is turned in Unity's world, and where its terrain sphere sits in it — and that
frame does not stay put. [KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin)
shows the values of KSP's floating origin, on a stock install. Its measurements show that a save does not
give that frame back, and that it changes during a flight with nothing loaded.

**→ On the pages of Diag FloatingOrigin: [loading the same save](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/docs/what-the-measurements-show-loading.md),
[leaving the rotating frame](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/docs/what-the-measurements-show-rotating-frame.md),
[a rover driven 2 km and back](https://github.com/lhervier/KSP-Diag-FloatingOrigin/blob/main/docs/what-the-measurements-show-driving.md)**

Each of the four has a page of its own: where the rounding strikes it in the stock code, how this mod takes
it away, and how that is checked.

- **[The ground](../ground/README.md)**, the quads a craft stands on, and every vertex inside them.
- **[The statics](../statics/README.md)**: the runway, the launchpad and the buildings of the KSC, the
  launch sites of the Making History expansion, and the bases a mod such as Kerbal Konstructs plants on a
  body.
- **[The scatter](../scatter/README.md)**: the rocks, and around the KSC the grass and the trees.
- **[The ROCs](../rocs/README.md)**: Breaking Ground's surface features, placed like the scatter, but
  with a collider.

**[The ground anchor](../ground-anchor/README.md)** is another matter: two stock
behaviours raise an anchored base when it is loaded, and neither is a rounding. So are
**[parts lying alone](../lone-parts/README.md)**: stock makes a part alone on the ground much heavier for a
few seconds after a load, which softened its pops on the moving ground, and throws the parts with a
suspension.

**How each fix is checked.** Each situation where a craft meets the ground is measured twice, without this
mod and with it: one instrument reads the landed craft, another the ground itself, and in flight a third
reads the quads the ground is made of; a fourth reads the scatter. In each summary, the first figure is
without this mod, the second with it. Each measurement has its protocol, its saves and the readings both
ways.
