# The scatter

Part of [Terrain Precision Fix](../../../README.md), one limit of [Limits and solutions](../../limits-and-solutions.md), on [stock](../../limits-and-solutions.md#stock).

**Status: checked on Kerbin and on the Mun, a stock gap the terrain fix widens on Kerbin at loading, and a
jump it adds while you drive, both closed by the scatter fix of this mod, on by default — visual only on a
stock install.** Terrain scatter — the rocks, and around the KSC the grass and the trees — is
already drawn off the ground in stock, differently at every load. The terrain fix does not move it, so it
does not open that gap, but the scatter does not share the ground's correction: on Kerbin the gap gets
wider, and while you drive, the scatter now jumps against the ground every time the world moves, where in
stock it moves with the ground. The scatter fix closes both; turned off (`fixScatter = false`), both come back.

## What goes wrong

The objects of a quad are built from its vertices, in the quad's own coordinates, and hang from a
*holder* that stays under the terrain sphere, placed and drawn from a 600 km vector in a float
([The culprit: the scatter](../../the-culprit-scatter.md)). In stock, the quad is placed from the same
vector, and the two often round the same way: the holder is drawn exactly on its quad about a third of
the time on Kerbin, and within a tenth of a millimetre of it three times out of four on the Mun. When the
world moves under a rover, every 500 m, stock places the quad again and Unity draws the holder anew,
through the same frame: the two move together.

The terrain fix places the quad in double precision and leaves the holder as stock placed it, so the two
never agree any more. The ground stops moving; the scatter does not, and all of what moves it against the
ground now comes from its holder: at every load, and at every move of the world while you drive.

## Measured

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) measures it, on stock, with the terrain fix alone — this mod with its scatter fix turned off — and with this mod as
installed:

- **Loading the same save**, twelve times on Kerbin and on the Mun
  ([the readings](../../checking-the-culprit-loading/the-scatter.md#the-objects-over-twelve-loads)): the
  height of a measured point of an object above the ground under it comes back 61 mm apart for half of
  those points on Kerbin on stock, and 178 mm with the terrain fix alone; on the Mun, 31 mm and 23 mm.
- **Driving on while the world moves**, a rover on the grass south of the runway of the KSC, one move of
  the world per load, six loads
  ([the readings](../../checking-the-culprit-driving/the-scatter.md#the-objects-across-a-move-of-the-world)):
  on stock, the ground jumps by up to 49.5 mm and the scatter with it, within 0.13 mm; with the terrain fix alone, the ground holds and the scatter jumps against it, every holder at once, by −54 to +19 mm depending on the
  load.

Stock scatter has no collider, so on a stock install this is visual only. A mod that gives the scatter
colliders makes it a physical gap, between the rock a craft hits and the rock its pilot sees: what that
changes, and when to turn the scatter fix off, is in
[On by default: when to turn it off](../../the-fix-scatter.md#on-by-default-when-to-turn-it-off)

## The solution: the scatter fix

The scatter fix of this mod, on by default, hangs each holder from its own terrain quad, so that the objects are drawn in
the frame they were built in: [The fix: the scatter](../../the-fix-scatter.md). With it, every holder is
drawn exactly on its quad, and no vertex moves by more than 0.132 mm over the twelve loads
([Checking the scatter: loading the same save](../../checking-the-culprit-loading/the-scatter.md)), nor by
more than 0.18 mm across a move of the world
([Checking the scatter: driving on while the world moves](../../checking-the-culprit-driving/the-scatter.md)),
nor along a flight ([Checking the scatter: in flight](../../checking-the-culprit-flight/the-scatter.md)).

Parallax's own scatter is not stock scatter, and is a point of Work in progress:
[Parallax: its terrain and its scatter](../../work-in-progress/parallax/its-terrain-and-its-scatter.md).
