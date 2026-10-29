# Parts lying alone

Part of [Terrain Precision Fix](../../README.md): a part lying alone on the ground, a craft of a single part,
such as a battery, a strut or a wheel dropped in EVA construction. Unlike the ground, the statics and the
scatter, its culprit is not a rounding: stock makes such a part much heavier for a few seconds, which
softened its pops on the moving ground, and throws the parts with a suspension. What it does, how this mod
takes it away, how that is checked, and what is still to check.

> **A part lying alone on the ground can explode, sink through it or be thrown into the air when its
> physics starts**: at a load, or when you come back within 200 m of it. A part with a suspension — a
> wheel, a landing leg, a landing gear — is very likely to be thrown.

## Why it matters

EVA construction puts parts on the ground all the time: a wheel taken off a rover, a strut or a battery
set down for later. Seeing them bounce into the air and come down on the base is not pleasant.

## The culprit

Every time a part lying alone goes off rails, stock makes it much heavier for 3 seconds: 4 t on Kerbin,
20 t on the Mun. On the moving ground, that makes its pops smaller. But a wheel, a landing leg or a landing
gear tunes its suspension to that mass, and its spring throws it high in the air when its own mass comes
back, with or without the fix of the ground.

**→ Full chapter: [The culprit: parts lying alone](the-culprit.md)**

## The fix

With the ground fixed, no part starts inside it any more, and the extra mass has nothing left to soften.
A setting of its own, `fixLonePartMass`, on by default, gives every part its own mass back as soon as stock
raises it. It does not depend on the fix of the ground: with `fixTerrain = false`, it shows what the extra
mass does on stock's moving ground.

**→ Full chapter: [The fix: parts lying alone](the-fix.md)**

## Checked

Measured on stock, then with this mod and one of its settings turned off, then with this mod as installed,
in an install with [KSP Community Fixes](https://github.com/KSPModdingLibs/KSPCommunityFixes): KSP 1.12.5,
Harmony, ModuleManager, KSP Community Fixes 1.41.1,
[KSP Diag - Landed Vessel](https://github.com/lhervier/KSP-Diag-LandedVessel), which reads how high each part
goes above where it starts (*Highest*), and [KSP-Util-MCPServer](https://github.com/lhervier/KSP-Util-MCPServer),
which plays the protocols.

- **Loading the same save**, ten times, six parts lying alone on the Mun. On stock's ground, the extra mass
  makes the pops smaller: the solar panels pop up 105 mm in the median with it, 303 mm without it. On this
  mod's ground, the parts start where they were, and read the same at every load, with it or without it.
  The wheels are thrown by metres at every load with it, on either ground, and settle within 15 mm without
  it.

  **→ Full chapter: [Checking parts lying alone: loading the same save](checking/loading.md)**

- **A wheel dropped in EVA construction**, five drops on Kerbin and five on the Mun. On stock and with
  `fixLonePartMass = false`, the wheel is thrown 13 to 15 m up on Kerbin whenever it lands on its tyre, 0.7
  to 5.3 m on the Mun at every drop; with this mod as installed, never.

  **→ Full chapter: [Checking parts lying alone: a wheel dropped in EVA construction](checking/wheel-drop.md)**

- **On the runway**, ten loads, six parts lying alone on the runway of the KSC. With this mod, the batteries
  and the panels read the same with the extra mass and without it; the wheels are thrown 13 to 14 m up
  with it, and stay within 23 mm without it.

  **→ Full chapter: [Checking parts lying alone: on the runway](checking/runway.md)**

The saves, the scripts and the `KSP.log` of every session are in
[the runs of parts lying alone](../../diag/lone-parts/README.md).

## Work in progress

What is still to check: why it is a question, and the test planned to answer it.

### Stock

**A large part on a steep slope: planned.** Stock sinks a craft put back onto a slope, whatever the ground,
and a large part alone there could still need the extra mass.

**→ Full chapter: [A large part on a steep slope](work-in-progress/a-large-part-on-a-steep-slope.md)**

### KAS

**A pylon linked to a craft: planned — read in the source, not played.** A pylon of KAS set on the ground is
a part lying alone, linked to another craft: with this mod, whatever pulls on the link at a load pulls on
the pylon's own mass, 20 kg, instead of tons.

**→ Full chapter: [KAS: a pylon linked to a craft](work-in-progress/kas/a-pylon-linked-to-a-craft.md)**
