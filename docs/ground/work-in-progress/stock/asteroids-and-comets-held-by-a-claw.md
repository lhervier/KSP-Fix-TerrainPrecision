# Asteroids and comets held by a claw

Part of [Terrain Precision Fix](../../../../README.md), [the ground](../../README.md#work-in-progress): one point of the work in progress, on stock.

**Status: planned.**

## Why it is a question

An asteroid or a comet brought down to the ground and held by a claw is a heavy mass on the other end of
a joint. On the first load with this mod, the ground under it moves once, by up to the stock spread. If
that went wrong, the player would see the object jump or slide at the load, the claw joint flex hard, or
the craft and the object come apart. On the following loads, the ground should no longer move at all.

## What is already known

- **They are craft like any other.** An asteroid or a comet is a vessel, put back in place at each load
  like any craft. `ModuleAsteroid` and `ModuleComet` never read the terrain.
- **Their shape does not go through the code this mod changes.** Their mesh is built with the same kind
  of terrain modifiers as a planet (`ProceduralSpaceObject.CreateMeshCollider`), but called one by one on
  a sphere of their own, outside the planet's terrain system: none of the methods this mod patches runs.
- **The claw does not touch the ground.** `ModuleGrappleNode.Grapple` moves the grabbing craft onto the
  point it touched, then joins the two. The ray that finds that point looks for parts, not terrain; so
  does the one of the asteroid and comet drills.
- **Their exact collider is built over several frames.** The game first gives the object a convex shell,
  larger than the rock, then cuts the rock into convex pieces a few per frame
  (`SpaceObjectCollider`), and switches the shell off at the end. The farther the object is from the
  craft you fly, the slower; when the object is part of the craft you fly, which is the case once held
  by a claw, it is done at once. A loose object resting on the ground and unpacked before the end sits on
  its shell, then drops onto the pieces: a movement at the load that does not come from the ground.
- **A comet is loaded from 150 km away, and only unpacked at 1 km.** `CometVessel` gives a comet's craft
  those distances in every situation, landed included, where a landed craft normally loads at 2250 m and
  unpacks at 200 m. At 1 km the ground under it is built to its finest level on the Mun, where this test
  is played; on a body as small as Gilly, it may not be.
- **A landed comet keeps the floating origin from moving.** KSP moves the origin back onto the craft you
  fly every 500 m, but not while another landed craft is loaded (`Krakensbane.SafeToEngage`). With a
  comet on the ground, that holds as long as you stay within 150 km of it. This mod places the ground
  near your craft in short vectors, which a float holds to a fraction of a millimetre; tens of kilometres
  from the origin, the float step is millimetres. Still well under the stock step, but no longer the
  precision the [checked loads](../../README.md#checked) show.
- **Under Real Solar System**, asteroids, and any craft holding one, are loaded from 100 km and unpacked
  at 2.5 km: the same questions, with a longer reach.

## To test

**The object held by a claw.** On the Mun, a small craft holding an asteroid with a claw, resting on the
ground, and the same with a comet. Fly the craft, so that the object's collider is built at once.
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel) on the craft, six loads
of the save without this mod, then six with it. Expected: with this mod, the craft moves once at the
first load, then no more; nothing comes apart.

**The ground far from a landed comet.** The comet left landed on the Mun, a rover driven 50 km away from
it, so that the origin has not moved since. [KSP Diag - Terrain Height](https://github.com/lhervier/KSP-Diag-TerrainHeight)
under the rover, then the same reading at the same spot with the comet gone. Expected: with this mod, a
difference of a few millimetres at most, the float step at that distance.
