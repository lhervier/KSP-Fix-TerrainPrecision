# Non-regression tests: Real Solar System

Part of [Terrain Precision Fix](../../README.md), one mod of [Non-regression tests](../non-regression.md): what works without this mod still works with it, with Real Solar System.

Unless a page says otherwise, each test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1 and this mod, plus the instrument and the mods it names. Each test has a page of
its own.

The defect grows with the body: a float's step is 62.5 mm at the radius of Kerbin, 125 mm on the Moon,
500 mm on Earth. [Real Solar System](https://github.com/KSP-RO/RealSolarSystem) ships two workarounds for
what it does to a craft, and adds statics of its own. The measurements on the Moon and on Earth, and
their install, are in [Checking the culprit: loading the same save](../checking-the-culprit-loading.md) and
[Checking the culprit: driving on while the world moves](../checking-the-culprit-driving.md); the logs of
every session with this mod in [`diag/runs`](../../diag/README.md#on-real-solar-system).

## The ground workaround

**Checked on the Moon and on Earth — with this mod, it has nothing left to correct for this defect.** Real
Solar System moves a landed craft back onto the ground when it is more than 10 cm off. Over 75 loads in
a row with this mod, the craft never moved, and the workaround never had anything to correct; with Real
Solar System built without it, this mod keeps the craft in place on its own.

**→ Full chapter: [Real Solar System: the ground workaround](real-solar-system/the-ground-workaround.md)**

## The runway fix

**Checked on Earth — with this mod, the runway is where it is drawn, with no step.** Real Solar System
turns off the colliders of the runway's sections and holds the floating origin on it. Built without that
fix, with this mod, the runway stood within 0.3 mm over thirty loads, and a move of the origin moved nothing.

**→ Full chapter: [Real Solar System: the runway fix](real-solar-system/the-runway-fix.md)**

## This mod's safeguard

**Checked on the Moon, Earth, Venus, Mars and Mercury — it never refused a correction.** This mod
refuses any correction larger than sixteen float steps, a limit that grows with the body. The largest
correction, on Earth, was 4.4 steps, 2.2 m, a quarter of the limit; a first version, a fixed metre,
refused part of Earth's terrain.

**→ Full chapter: [Real Solar System: this mod's safeguard](real-solar-system/this-mods-safeguard.md)**

## A CommNet ground station

**Checked on Earth, no problem.** Real Solar System adds 63 CommNet ground stations, statics this mod
takes out of their sphere. Driven toward the one of Kourou, a rover sees it taken out on the way, and
CommNet keeps linking the rover to it.

**→ Full chapter: [Real Solar System: a CommNet ground station](real-solar-system/a-commnet-ground-station.md)**

## Coming back to a craft left parked, on the Moon

**Checked on the Moon, no problem.** A craft left parked is unloaded while a rover drives away, and its
quads are built again when the rover comes back, after the origin has moved. Over six round trips, the
ground under the parked capsule came back within 0.042 mm with this mod, against 31.9 mm without it.

**→ Full chapter: [Real Solar System: coming back to a craft left parked, on the Moon](real-solar-system/coming-back-to-a-craft-left-parked-on-the-moon.md)**
