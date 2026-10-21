# Real Solar System: the runway fix

Part of [Terrain Precision Fix](../../../../README.md), [the statics](../../README.md#non-regression-tests): one non-regression test, on Real Solar System.

**Status: checked on Earth — with this mod, the runway of the KSC stands at the same height at every load,
with no step on it, and the runway no longer moves when the floating origin does; so neither half of Real
Solar System's runway fix has anything left to correct for this defect. With the runway fix as released,
this mod also removes what it cannot: the runway at another height at each load, and the step the game
still draws between its sections.** The runway is a static, placed
like the buildings of the KSC ([The culprit: the statics](../../the-culprit.md)), and this mod
places it in double while a craft is near ([The fix: the statics](../../the-fix.md)).

## What Real Solar System does

Real Solar System ships a component of its own for the runway of the KSC, `RSSRunwayFix`
([its source, release 20.1.3.0](https://github.com/KSP-RO/RealSolarSystem/blob/v20.1.3.0/Source/RSSRunwayFix.cs)).
It does two things:

- **It turns off the colliders of the runway's sections.** Stock builds the runway in sections, each
  with a deck and a collider of its own, and gives the whole runway one more collider, `runway_collider`,
  in one piece (`RunwayCollisionHandler`). Once the sections are loaded, Real Solar System turns their
  colliders off, and leaves `runway_collider` alone to hold a craft.
- **It holds the floating origin while a craft rolls on the runway.** While the active craft is landed
  or in prelaunch, and a ray cast down from it hits `runway_collider`, it raises the distance at which
  KSP moves the floating origin back onto the craft to 2,700 m, and calls
  `FloatingOrigin.SetSafeToEngage(false)` every 25 physics frames: the origin does not move.

No setting turns either half off.

## What the runway does without it

The decks and colliders of the runway are separate objects hanging from the KSC, and each is placed
through a float `Transform` at planet scale, so each is rounded on its own — on Earth, by up to a float
step of 500 mm at that distance from the centre. Each is rounded twice, too: once where the game draws
it, once where the physics places it, two computations of the same position that do not round the same
way. Both change at every load. Depending on the load, a craft on the runway then finds:

- **the runway it touches above or below the runway it sees**: it rests in the air above the deck, or
  with its wheels sunk into it;
- **a step between the colliders of two sections**, which a wheel climbs.

Turning the sections' colliders off removes the step: only `runway_collider` is left, in one piece. It
cannot bring that piece back to the deck the game draws.

## The test

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1 and
[Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 with what it requires (Kopernicus
248, Modular Flight Integrator, KSPTextureLoader, the RSS textures), and two instruments:

- [KSP Diag - Colliders](https://github.com/lhervier/KSP-Diag-Colliders) draws the colliders around the
  active craft where the physics places them, each in a colour of its own: here the end of the runway,
  `End09`, in magenta, and its fourth section, `Section4`, in cyan. It shows the step;
- [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight) reads, under a craft,
  the ground the physics touches and the ground KSP computes for the same spot. Every figure below is
  one of its lines: the first minus the second, in millimetres.

To see the runway without the runway fix, Real Solar System is built from the sources of its release
20.1.3.0 with `RSSRunwayFix` kept from doing anything: it returns at the top of its `Start`, so it
leaves the sections as stock does, never touches the floating origin, and never holds it. The version
of the assembly is set to that of the release
([`rss-20.1.3-without-its-runway-fix.diff`](../../../../diag/statics/non-regression/real-solar-system/the-runway-fix/rss-20.1.3-without-its-runway-fix.diff)).

The craft is the rover of the driving protocol,
[`Diag2-Rover.craft`](../../../../diag/ground/checking/driving/Diag2-Rover.craft), twice. In a new
sandbox game, at noon at Cape Canaveral:

1. a first rover, launched from the SPH onto the runway, is driven to the edge between `End09` and
   `Section4`, then 70 m north, down the bank, onto the grass: the witness of the ground, left there;
2. a second rover is launched from the SPH, driven east along the runway to 8 m before that edge, and
   saved (F5);
3. that save is loaded ten times (F9). At each load, Diag Terrain Height records three lines: under the
   witness on the grass (set as the target), under the rover 8 m before the edge, on `End09`, and under
   it 10 m past the edge, on `Section4`, where it drives at 2 m/s. Then the rover backs up until its back
   wheels stand on `End09` and its front wheels on `Section4`, and the camera looks at it from beside;
4. the rover is recovered, and 2 and 3 are played again, twice: three launches, thirty loads.

When a step stops the rover at the edge, it goes round by the grass: south down the bank of `End09`, east
on the grass past the edge, then north up the bank of `Section4`, which rises from the grass with no step,
and on to the same spot 10 m past the edge. In the sessions below, no step stopped it.

That is played without this mod, then with it at its defaults with `logLevel = Debug`, then with Real
Solar System as released, without this mod and with it: one launch, six loads, and a taxi along the
runway (`--launches 1 --reloads 6 --taxi 1500`).

*Played by a script.* [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer) plays the test through
[`diag/statics/automation/run-runway-fix.py`](../../../../diag/statics/automation/run-runway-fix.py), the rover in the
`Ships/SPH` folder of the game: it starts the game itself from the main menu, and takes a screenshot of
the table of Diag Terrain Height every four loads. Every step is one a player can take: the test plays
just as well by hand.

## Seeing it

### Without the runway fix, without this mod

The runway is never at the same height twice, and the grass beside it does not follow. Over the thirty
loads, as Diag Terrain Height reads them:

| | lowest | highest |
|---|---|---|
| the grass, under the witness | −29.503 mm | +683.012 mm |
| the runway, 8 m before the edge | +3 433.022 mm | +4 674.030 mm |
| the runway, 10 m past the edge | +3 549.503 mm | +4 790.597 mm |

Past the edge, the runway stands **116.5 mm higher** than before it at 26 loads of the 30. At the four
others, it stands 0.5 to 3.2 mm lower: no step.

![The table of Diag Terrain Height after four loads](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/20-without-runway-fix-table.png)

*Without the runway fix, without this mod: the table of Diag Terrain Height after the first four loads of
the first launch, three lines a load: the grass, before the edge, past it.*

![The rover astride the edge, nose up](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/21-without-runway-fix-step.png)

*The same session: a load with the step, the rover backed onto the edge, its back wheels on `End09`
(magenta), its front wheels on `Section4` (cyan).*

![The rover astride the edge, Section4 below End09](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/22-without-runway-fix-step-down.png)

*The same session: a load where the collider of `Section4` (cyan) lies below that of `End09` (magenta).*

![The rover astride the edge, in the air above the deck](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/23-without-runway-fix-step-in-the-air.png)

*The same session, another launch: a load with the step, the runway at its highest of the thirty loads.*

### Without the runway fix, with this mod

The runway stands at the same height at every load, and so does the grass:

| | lowest | highest |
|---|---|---|
| the grass, under the witness | +7.184 mm | +7.749 mm |
| the runway, 8 m before the edge | +3 778.051 mm | +3 778.344 mm |
| the runway, 10 m past the edge | +3 774.873 mm | +3 775.180 mm |

Past the edge, the runway stands 3.1 or 3.2 mm lower than before it at every load: the slope of the deck
over 18 m, with no step.

![The table of Diag Terrain Height after four loads, with this mod](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/30-with-this-mod-table.png)

*Without the runway fix, with this mod: the table of Diag Terrain Height after the first four loads of the
first launch.*

![The rover astride the edge, level](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/31-with-this-mod-astride.png)

*The same session: the rover backed onto the edge, at the first load.*

### Real Solar System as released

The runway fix turns the sections' colliders off: `runway_collider` alone holds the rover, and no step is
left to climb. It does not bring `runway_collider` back to the deck the game draws, nor the decks of the
sections back in line. One launch, six loads:

| | the runway, 8 m before the edge | 10 m past it |
|---|---|---|
| without this mod | +3 715.454 to +4 096.876 mm, a spread of 381.422 mm | +3 712.287 to +4 093.738 mm, a spread of 381.450 mm |
| with this mod | +3 777.968 to +3 778.238 mm, a spread of 0.271 mm | +3 774.860 to +3 775.161 mm, a spread of 0.301 mm |

Without this mod, the runway stands at another height at each load, in one piece: the two readings move
together, 3.1 mm apart at every load. With this mod, it stands where it stood at every load without the
runway fix, within 0.4 mm.

**The step the game still draws.** The colliders are off, but the decks the game draws are still
rounded one by one: without this mod, the step stays in sight at the edge, and the wheels sink into the
higher deck without meeting it. With this mod, the two decks meet flush. Seen from beside, the rover
astride the edge, at the first load, the edge under it three times as large:

![Real Solar System as released, without this mod: the edge under the rover](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/12-as-released-edge-stock.jpg)

*Real Solar System as released, without this mod: the rover astride the edge between `End09` and
`Section4`, at the first load; the sections' colliders off, in pale blue.*

![Real Solar System as released, with this mod: the edge under the rover](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/12-as-released-edge-with-this-mod.jpg)

*Real Solar System as released, with this mod: the same.*

<p class="thumbs">
<a href="../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/13-as-released-edge-six-loads-stock.jpg"><img src="../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/13-as-released-edge-six-loads-stock.jpg" alt="Without this mod, the edge at each of the six loads" width="96"></a>
<a href="../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/13-as-released-edge-six-loads-with-this-mod.jpg"><img src="../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/13-as-released-edge-six-loads-with-this-mod.jpg" alt="With this mod, the edge at each of the six loads" width="96"></a>
</p>

<details>
<summary>The edge at each of the six loads</summary>

![Without this mod, the edge at each of the six loads](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/13-as-released-edge-six-loads-stock.jpg)

*Without this mod, loads 1 to 6, from top to bottom.*

![With this mod, the edge at each of the six loads](../../../../imgs/statics/non-regression/real-solar-system/the-runway-fix/13-as-released-edge-six-loads-with-this-mod.jpg)

*With this mod, loads 1 to 6, from top to bottom.*

</details>

**Taxiing along the runway.** The rover alone in the game, before the witness is parked, taxied
1,500 m east along the runway at 8 m/s, then 80 m south onto the grass, read at each stop, without this
mod and with it. The runway fix raises the distance at which the floating origin moves to 2,700 m on the
runway, and, by its source, gives it back only when the craft stops being landed or goes on rails: on the
grass too, 1.5 km from where it started, the rover is still under it. In both sessions, the rover stayed
on its wheels, and `KSP.log` holds no error from Real Solar System.

## What the results show

**Without this mod, the runway is not where it is drawn, and not in the same place twice.** Without the
runway fix, it stands more than a metre higher at one load than at another, and a step of 116.5 mm lies
between two of its sections at most loads; the grass beside it moves too, but not with it. As released,
with only `runway_collider` left, there is no step to climb, but the runway is still where the physics
rounded it, at another height at each load, and the game still draws the decks of its sections out of
line: a craft rests with its wheels sunk into the deck. The runway fix removes the step a wheel meets, the
only part of the defect it can reach.

**With this mod, the runway is where it is drawn, in one piece.** The KSC and everything under it are
placed in double while a craft is near, so what the game draws and what the physics touches come from
the same position, and the sections line up. For this defect, the half of the runway fix that turns the
sections' colliders off has nothing left to correct. It may have other uses, outside the scope of this
fix.

**The hold on the floating origin: with this mod, a move of the origin moves nothing.** A rover alone by
the runway, Real Solar System built without its runway fix, reads a spot on the deck and a spot on the
grass beside it just before and just after each move of the origin, two moves a run, with the protocol
of the runway and the grass while the world moves of KSP Diag - Terrain Height. Without this mod, the
deck moves by −231.84 and +33.84 mm, together with the grass: what the runway fix holds the origin
against. With this mod, the deck moves by 0.034 mm at most, and the grass by 0.119 mm, within the spread
of the lines taken at the same spot. The readings are in
[Checking the statics: driving on while the world moves](../../checking/driving.md#by-the-runway-of-the-ksc-at-cape-canaveral).
For this defect, the hold has nothing left to correct either.

The logs, what the script printed, every line of Diag Terrain Height and the screenshots of its table, for
every session, are in
[`diag/statics/non-regression/real-solar-system/the-runway-fix/`](../../../../diag/statics/README.md#on-real-solar-system).
