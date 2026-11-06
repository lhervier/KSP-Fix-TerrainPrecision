# Parallax: what it does with the ground

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#non-regression-tests): one non-regression test, on Parallax.

**Status: read in the source, and checked by the tests of the other pages — Parallax draws the ground this
mod places and sets its objects on it; nothing it does is undone by this mod.**
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) draws the terrain with shaders of
its own and adds a scatter of its own objects, some of which a craft can hit, two things that sit right on
the ground this mod places.

## The texture of the ground slides

**Parallax's own, left as it is: it is only drawn.** The terrain shader of Parallax places the texture of
the ground from the position of each point in the Unity scene, which changes at every load, as KSP turns the
body in the scene again by the time played since the save was made
([Why it is different at every load](../../the-culprit.md#why-it-is-different-at-every-load)): the texture comes back slid along the ground, on every body, even when the same
save is loaded again at once, with this mod as without it. The ground the physics uses does not move with
it, and this mod does not touch it.

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
