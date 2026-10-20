# Parallax: what it does with the ground

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#non-regression-tests): one non-regression test, on Parallax.

**Status: read in the source, and checked by the tests of the other pages — Parallax draws the ground this
mod places and sets its objects on it; nothing it does is undone by this mod.**
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) draws the terrain with shaders of
its own and adds a scatter of its own objects, some of which a craft can hit, two things that sit right on
the ground this mod places. Up to 1.0.4, Parallax had bugs of its own that moved its rocks under a craft at
every load, whatever the ground did; they are fixed in 1.0.5, by a change of ours, and the tests of these
pages are played on 1.0.5.

## Its rocks no longer turn at every load

**Fixed in Parallax Continued 1.0.5, by our change.** Up to 1.0.4, Parallax oriented each object of its
scatter, the rock it draws and the collider it gives it, from the vertical axis of the Unity scene, and KSP
turns the body in the scene again at every load, by the time played since the save was made — the same
turn that makes the ground of stock come back at another place
([Why it is different at every load](../../the-culprit.md#why-it-is-different-at-every-load)).
Every rock came back turned on itself, and a craft resting on one, or right next to one, could start
inside it and be thrown off: the behaviour reported to Parallax in
[issue #125](https://github.com/Gameslinx/Parallax-Continued/issues/125).

Our change, merged into Parallax Continued as
[pull request #157](https://github.com/Gameslinx/Parallax-Continued/pull/157) and released in
[1.0.5](https://github.com/Gameslinx/Parallax-Continued/releases/tag/1.0.5), builds the orientation of each
object in the frame of its terrain quad, the same way in the compute shader that draws the scatter and in
the code that gives the colliders: the rocks hold still.

**→ Seeing it: [The rocks turn at every load](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/reproducing-the-bug.md#the-rocks-turn-at-every-load);
the change: [The change](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/the-change.md)**

## Near the south pole, every collider is on its object

**Fixed in Parallax Continued 1.0.5, by the second commit of our change.** Near the south pole, for the
objects that stand along the radius of the body, such as the trees of Laythe, the code that oriented the
colliders up to 1.0.4 (`Quaternion.FromToRotation`) no longer turned around the same axis as the compute
shader that draws the objects: the collider was turned around the trunk from the tree drawn, by another
angle at every load. The second commit computes the same rotation on both sides: every collider is on its
object.

**→ Seeing it: [Near the south pole, the colliders part from the objects drawn](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/reproducing-the-bug.md#near-the-south-pole-the-colliders-part-from-the-objects-drawn);
the change: [The second commit: near the south pole](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/the-change.md#the-second-commit-near-the-south-pole)**

## The texture of the ground slides

**Parallax's own, left as it is: it is only drawn.** The terrain shader of Parallax places the texture of
the ground from the position of each point in the Unity scene, which changes at every load for the same
reason as the rocks turned: the texture comes back slid along the ground, on every body, even when the same
save is loaded again at once, with this mod as without it. The ground the physics uses does not move with
it, and neither this mod nor our change touches it.

**→ Seeing it: [What changes at every load all the same](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/reproducing-the-bug.md#what-changes-at-every-load-all-the-same)**

## Read in its source

- **the terrain** — Parallax draws it on the meshes stock builds, and gives the physics no ground of its
  own (Eeloo aside, where it replaces the height map). Its tessellation and its displacement should neither
  create nor hide the crack stock already has where two subdivision levels meet, and that this mod widens
  ([The seam between subdivision levels](../../limits/stock/the-seam-between-subdivision-levels.md#parallax));
- **where its scatter stands** — an object of its scatter is placed on its quad, in the quad's frame, and
  its collider is a child of the quad: it follows the ground wherever this mod places it. Neither the gap of
  the stock scatter nor the scatter fix reaches it, and Parallax never names a stock holder
  ([Other mods that look for the holders](../../../scatter/the-fix.md#other-mods-that-look-for-the-holders));
- **the stock scatter** — Parallax leaves the stock `LandControl` in place on every body but Eeloo, so on a
  body it does not strip, the stock scatter is still there, hanging from the same holders, with the gap this
  mod widens on Kerbin ([The scatter](../../../scatter/limits/stock/the-scatter.md)), and the scatter
  fix acts on it as without Parallax. Its pines of Kerbin are of that stock scatter, and have no collider:
  a rover driven into one goes through it;
- **where its scatter grows** — Parallax draws each object on a triangle of the quad's mesh, and checks the
  slope and a noise there against thresholds: an object right at one of them follows the mesh stock builds
  a little differently at every load, and this mod builds the same
  ([Parallax: its scatter grows the same at every load](../../../scatter/non-regression/parallax/its-scatter-grows-the-same-at-every-load.md)).
