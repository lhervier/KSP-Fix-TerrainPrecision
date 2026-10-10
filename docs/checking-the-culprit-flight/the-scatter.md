# Checking the scatter: in flight

Part of [Terrain Precision Fix](../../README.md), one page of
[Checking the culprit: in flight](../checking-the-culprit-flight.md): the measurements that check the third
culprit, [the scatter](../the-culprit-scatter.md), along a flight over the Mun, with the terrain fix alone and
with the scatter fix as well.

[KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter) measures the terrain scatter against
the ground: for every quad carrying scatter, the height of its holders and of the matrices they are drawn
with, and for the objects of the quad nearest to the craft, the height of their vertices above the ground.
After a load, it is read in
[Checking the scatter: loading the same save](../checking-the-culprit-loading/the-scatter.md).
In flight, the world origin follows the craft, and the terrain keeps building quads ahead of it and
destroying those behind it: [the scatter fix](../the-fix-scatter.md) leaves each holder to follow its quad
through all of that, without doing anything more.

The scatter fix is off by default, so the flight is measured with the terrain fix alone — this mod as
installed by default — and with the scatter fix as well. **The flight with the scatter fix was taken when
it was a mod of its own**, Rock Precision Fix 0.1.0, installed next to Terrain Precision Fix 0.1.0: the
same two patches as this mod's scatter fix, whose lines in its log are tagged `[RockPrecisionFix]`.

The instrument reads the rocks along a flight, following
[its protocol](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/measuring-the-rocks.md#over-a-flight),
in KSP 1.12.5 with Harmony, ModuleManager and KSP Community Fixes 1.41.1:
the save
[`ref-mune-5km.sfs`](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/diag/README.md#the-saves),
a Mk1 command pod in a circular equatorial orbit 5 km over the Mun, loaded once, one record 30 s into the
flight, then every two minutes, and one after the pod crashed into the relief. The records with both
fixes are in [`diag/runs`](../../diag/README.md#the-scatter-fix-the-rocks-over-a-flight), and those with the
terrain fix alone with
[the instrument](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/diag/README.md#the-rocks-over-a-flight).

## The readings

Flown the same way, both flights passed over the same ground: every record names the same quads as its
counterpart in the other flight, 1,600 in all, and the same nearest quad, whose 20 rocks and 200 vertices
compare one by one. The pod is 5 km up, so every quad is at least that far from the world origin, where
single precision coordinates step by about half a millimetre: the same quads' centres, and the ground under
the same vertices, come out up to 0.7 mm and 1.6 mm apart from one flight to the other.

| record | nearest quad | *up* of its holder, the terrain fix alone | its vertices above the ground, the terrain fix alone minus both fixes | *up* of all the holders, both fixes |
|---|---|---|---|---|
| 1 | `Mun Zp200000011` | +0.8 mm | +0.5 to +1.0 mm | 0.000 mm, 344 holders |
| 2 | `Mun Xn231111111` | +17.5 mm | +17.3 to +18.1 mm | 0.000 mm, 168 holders |
| 3 | `Mun Xn211311311` | −3.5 mm | −3.5 to −2.0 mm | 0.000 mm, 144 holders |
| 4 | `Mun Xn122020000` | +1.5 mm | +1.2 to +1.7 mm | 0.000 mm, 224 holders |
| 5 | `Mun Xn013331113` | −1.5 mm | −1.9 to −0.5 mm | 0.000 mm, 152 holders |
| 6, after the crash | `Mun Zn200000011` | −15.8 mm | −16.9 to −16.3 mm | 0.000 mm, 568 holders |

**With the terrain fix alone**, no holder is drawn on its quad, at any record: over the 1,600, the
*up* of their matrices runs from −26.5 to +21.1 mm, never 0, 9.0 mm on average (root mean square), about
what the twelve loads of the Mun gave. The offset does not grow along the flight, but it does not go away
either.

**With both fixes**, at every record, every holder, 1,600 in all, stands at the height of its quad's
centre, to the micrometre, and its matrix too, neither shifted from it, up or across: 0.000 mm. Those
built minutes into the flight and those still there after the crash alike.

On the nearest quad, every vertex stands higher or lower against the ground with the terrain fix alone
than with both fixes, by nearly the same amount for the 200 of them, and that amount is the *up* of their
holder in the first flight: taking it off leaves 0.2 mm (median over the vertices), 1.5 mm at most,
within the precision of the reading at that distance.

## What the measurements say

**The scatter follows its quads along a flight with the scatter fix, and only with it.** With the
terrain fix alone, no holder is drawn on its quad at any record, by up to 26.5 mm over the Mun, and the
objects move with their holder and only with it. With the scatter fix as well, every holder of the flight
is drawn exactly on its quad, those built minutes into the flight and those left after the crash alike:
along a flight, the scatter is drawn on its quads just as after a load.
