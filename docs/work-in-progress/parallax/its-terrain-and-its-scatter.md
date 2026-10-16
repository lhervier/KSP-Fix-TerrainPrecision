# Parallax: its terrain and its scatter

Part of [Terrain Precision Fix](../../../README.md), one point of [Work in progress](../../work-in-progress.md), on [Parallax](../../work-in-progress/parallax.md).

**Status: in progress — what is to check is that the ground of Parallax comes back where the save left
it, with this mod as without it: a craft resting on one of its rocks, loaded again and again, should stay
on it. Parallax as released has bugs of its own in the way of that test. A change to Parallax on our
fork corrects the two that move its rocks and their colliders; one is only drawn and is left as it is;
and this mod corrects the last without touching Parallax.**
[Parallax Continued](https://github.com/Gameslinx/Parallax-Continued) draws the terrain with shaders of
its own and adds a scatter of its own objects, some of which a craft can hit, two things that sit right
on the ground this fix places.

## The bugs of Parallax in the way

The first three are Parallax's own, shown and explained in the pages of our fork of Parallax Continued,
[Scatter rotation](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/README.md),
with their protocols, their saves and the runs of each build. The fourth comes from the ground of stock
KSP.

### Its rocks turn at every load

**Corrected by a change to Parallax, on our fork.** Parallax orients each object of its scatter, the
rock it draws and the collider it gives it, from the vertical axis of the Unity scene, and KSP turns the
body in the scene again at every load, by the time played since the save was made — the same turn that
makes the ground of stock come back at another place
([Why it is different at every load](../../the-culprit-ground.md#why-it-is-different-at-every-load)).
Every rock comes back turned on itself, and a craft resting on one, or right next to one, can start
inside it and be thrown off: the behaviour reported to Parallax in
[issue #125](https://github.com/Gameslinx/Parallax-Continued/issues/125). As long as the rocks turn, a
craft on a rock is thrown off whatever the ground does, and the test has nothing to read.

The change, on the branch
[`fix/scatter-rotation`](https://github.com/Gameslinx/Parallax-Continued/compare/1.0.4...lhervier:KSP-ExtMod-ParallaxContinued:fix/scatter-rotation)
of our fork, builds the orientation of each object in the frame of its terrain quad, the same way in the
compute shader that draws the scatter and in the code that gives the colliders: the rocks hold still.

**→ Seeing it: [The rocks turn at every load](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/reproducing-the-bug.md#the-rocks-turn-at-every-load);
the change: [The change](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/the-change.md)**

### Near the south pole, a collider apart from its object

**Already in the release; made worse by the first commit of our change, corrected by its second.** Near
the south pole, for the objects that stand along the radius of the body, such as the trees of Laythe,
the code that orients the colliders (`Quaternion.FromToRotation`) no longer turns around the same axis as
the compute shader that draws the objects: on the release, the collider is turned around the trunk from
the tree drawn, by another angle at every load. The first commit of our change kept that gap and added
its own defect, the tree drawn stretched and, now and then for one frame, an object drawn across the
screen. The second commit computes the same rotation on both sides, without the rounding that stretched
the tree: every collider is on its object. A craft against such a tree would otherwise hit a collider
that is not where the tree is drawn.

**→ Seeing it: [Near the south pole, the colliders part from the objects drawn](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/reproducing-the-bug.md#near-the-south-pole-the-colliders-part-from-the-objects-drawn);
the change: [The second commit: near the south pole](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/the-change.md#the-second-commit-near-the-south-pole)**

### The texture of the ground slides

**Left as it is: it is only drawn.** The terrain shader of Parallax places the texture of the ground from
the position of each point in the Unity scene, which changes at every load for the same reason as the
rocks turn: the texture comes back slid along the ground, on every body, even when the same save is
loaded again at once. The ground the physics uses does not move with it, so it is not in the way of the
test, and neither this mod nor our change touches it.

**→ Seeing it: [What changes at every load all the same](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/reproducing-the-bug.md#what-changes-at-every-load-all-the-same)**

### An object of its scatter here and there comes and goes

**Corrected by this mod, without touching Parallax.** Parallax decides where each object of its scatter
grows from the mesh of the terrain quad, which stock KSP builds a little differently at every load: an
object here and there grows at one load and not at the next. With this mod, the same objects grow at
every load.

**→ Full chapter: [With this mod, its scatter grows the same at every load](#with-this-mod-its-scatter-grows-the-same-at-every-load)**

## The test: a craft on a rock

**Still to play**: a craft of several parts resting on a rock of Parallax, the same save loaded again and
again, after time played and after a restart of KSP, without this mod and with it, read by
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) and
[KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight); then the loading and
approach campaigns of those two instruments on the ground of Parallax. A craft of several parts, because
KSP puts a craft of a single part back down on whatever is under it at every load
(`Vessel.CheckGroundCollision`), and so hides where the rock came back. It is to play on Parallax rebuilt
with our change, once that change is checked: on the release, the rock turns under the craft
([Its rocks turn at every load](#its-rocks-turn-at-every-load)). What is still to check of the change
itself is in the
[Work in progress](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/work-in-progress.md)
of our fork.

**Already seen, with this mod only**: a capsule on a fuel tank, resting on a rock of the Mun, stays on
it. Without this mod, it is still to play.

![A capsule standing on a rock of the Mun after the last of the loads below, with KSP Diag - Colliders outlining the collider of the rock](../../../imgs/work-in-progress/parallax/its-terrain-and-its-scatter/capsule-on-a-rock.jpg)

*Parallax Continued 1.0.4 rebuilt with the first commit of our change, the only one that changes
anything away from the south pole, and this mod, the Mun,
[`capsule-on-a-rock-mun.sfs`](../../../diag/work-in-progress/parallax/its-terrain-and-its-scatter/capsule-on-a-rock-mun.sfs):
a Mk1 capsule on an empty FL-T100 fuel tank, landed on top of a rock. Loaded twelve times, an hour of game time of time warp
before each load, then KSP started again and the save loaded twelve times more; the view after the last
load, with [KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders) outlining the collider
Parallax gives the rock.*

At every one of those loads the capsule stayed on its rock, where Parallax as released threw a capsule
saved on a rock off at the first load after ten minutes of play. That save was made with the change:
Parallax as released turns the rock under the capsule when it is loaded.

## With this mod, its scatter grows the same at every load

**With the ground of stock KSP, an object of the scatter here and there grows at one load and not at the
next; with this mod, the same objects grow at every load.** Parallax decides where each object of its
scatter grows from the mesh of the terrain quad, and stock builds that mesh a little differently at every
load ([Why it is different at every load](../../the-culprit-ground.md#why-it-is-different-at-every-load)):
an object that sits right on one of the thresholds Parallax applies grows at one load and not at the next.
This mod builds the same mesh at every load, and the object makes the same choice every time.

**The protocol.** KSP 1.12.5 with Parallax Continued 1.0.4 rebuilt with the first commit of our change
([Its rocks turn at every load](#its-rocks-turn-at-every-load)), so that nothing turns from one load to
the next, and KSP Diag - Colliders. Copy
[`rocks-eve-jeb.sfs`](../../../diag/work-in-progress/parallax/its-terrain-and-its-scatter/rocks-eve-jeb.sfs)
into the folder of a sandbox game and load it: a kerbal on the ground of Eve, among rocks and plants. Look
at him from straight above, from some 40 m, and take a screenshot; load the same save again at once, with
no time played, and take the same screenshot; twelve times. Then the same without this mod, and with it.
[`run-rocks-turning.py`](https://github.com/lhervier/KSP-ExtMod-ParallaxContinued/blob/claude/scatter-rotation-tests/docs/scatter-rotation/automation/run-rocks-turning.py)
of our fork of Parallax plays it through KSP-MCPServer:
`--save rocks-eve-jeb --radius 700000 --step 0`.

![Without this mod, the grove at the left of the view, at the first load and at the twelve loads after it: a white plant under the red ones, at the bottom right, shows at loads 1, 7 and 9](../../../imgs/work-in-progress/parallax/its-terrain-and-its-scatter/plant-without-this-mod.jpg)

![With this mod, the same grove at the same thirteen loads: the white plant never shows](../../../imgs/work-in-progress/parallax/its-terrain-and-its-scatter/plant-with-this-mod.jpg)

*The grove at the left of the view, cropped, at the first load (0) and at the twelve loads after it. Top:
without this mod. Bottom: with it. The line of KSP Diag - Floating Origin at each load and the `KSP.log`
of each session:
[`the-same-objects/`](../../../diag/work-in-progress/parallax/its-terrain-and-its-scatter/the-same-objects/).*

Without this mod, the white plant under the red ones shows at 3 loads out of 12; with it, at none. The
same series played three times more with other builds of Parallax gave 9 loads out of 36 without this
mod, and none out of 32 with it.

What still changes on Eve from one load to the next with this mod, the small pebbles drawn in the
texture of the ground, comes from Parallax itself and not from the ground
([The texture of the ground slides](#the-texture-of-the-ground-slides)).

## Read in its source

- **the terrain** — Parallax draws it on the meshes stock builds. Its tessellation and its displacement
  should neither create nor hide the crack stock already has where two subdivision levels meet, and
  that this fix widens
  ([The seam between subdivision levels](../../limits-and-solutions/stock/the-seam-between-subdivision-levels.md#parallax));
- **where its scatter stands** — an object of its scatter is placed on its quad, in the quad's frame,
  and its collider is a child of the quad: it follows the ground wherever this fix places it, its
  orientation aside ([Its rocks turn at every load](#its-rocks-turn-at-every-load)). Neither the gap of
  the stock scatter nor the scatter fix reaches it, and Parallax never names a stock holder
  ([Other mods that look for the holders](../../the-fix-scatter.md#other-mods-that-look-for-the-holders));
- **the stock scatter** — Parallax leaves the stock `LandControl` in place on every body but Eeloo, so
  on a body it does not strip, the stock scatter is still there, hanging from the same holders, with the
  gap this fix widens on Kerbin
  ([The scatter](../../limits-and-solutions/stock/the-scatter.md)), and the scatter
  fix acts on it as without Parallax;
- **where its scatter grows** — Parallax draws each object on a triangle of the quad's mesh, and checks
  the slope and a noise there against thresholds: an object right at one of them follows the mesh stock
  builds a little differently at every load, and this fix builds the same
  ([With this mod, its scatter grows the same at every load](#with-this-mod-its-scatter-grows-the-same-at-every-load)).
