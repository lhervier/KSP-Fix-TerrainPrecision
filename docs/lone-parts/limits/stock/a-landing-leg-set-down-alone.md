# A landing leg set down alone

Part of [Terrain Precision Fix](../../../../README.md), [parts lying alone](../../README.md#limits-and-solutions): one limit, on stock.

**Status: solved by [Suspension Bounce Fix](https://github.com/lhervier/KSP-Fix-SuspensionBounce) — played on Kerbin
and on Minmus.**

*What you see.* In EVA construction, an engineer takes an LT-1 landing leg off a lander and sets it down on the
ground, foot down.

- **On Kerbin**, without this mod, the leg tips over onto its side and stays there. With this mod, it leaves the
  ground at once, spinning, rises a few metres and is destroyed when it lands (`landingLeg1 (…) Exploded!!` in
  `KSP.log`).
- **On Minmus**, the leg is thrown with or without this mod. Without it, it tips over slowly, lies on its side for a
  few seconds, then leaves the ground and climbs tens of metres. With this mod, it leaves the ground at once.

*Why.* Stock makes a part lying alone weigh 4 t for its first 3 seconds, 20 t on Minmus
([The culprit: parts lying alone](../../the-culprit.md#stocks-answer-the-extra-mass)). Under that weight, the
suspension of the leg is sized for tons and does nothing to it: the leg simply tips over, and it lies on its flat
side, with its foot, where its spring is, off the ground. When its own mass comes back, nothing presses that spring.

- On Kerbin, the leg is lying still by then: it stays where it is.
- On Minmus, gravity is twenty times weaker, and the leg is still rolling when its own mass comes back. As it rolls,
  its foot touches the ground again, and its suspension throws it.

This mod gives the leg its own mass from the start (`fixLonePartMass`): its foot is on the ground when its
suspension is sized for its own mass, and that suspension throws it at once, on either body.

*What throws it.* Not the extra mass, but a stock flaw of the suspensions, which the extra mass hid on Kerbin:
`SuspensionLoadBalancer` never sizes a suspension for less than half a ton, and
`ModuleWheelSuspension.SuspensionSpringUpdate` sizes its damper from that spring alone, without the mass it
carries. On a leg of 50 kg, that damper does not slow the leg down: it throws it. The same flaw throws a light
probe standing on its landing legs on the runway, with no part lying alone and without this mod: it is the subject
of [Suspension Bounce Fix](https://github.com/lhervier/KSP-Fix-SuspensionBounce), which explains it in full.

*The solution.* Install [Suspension Bounce Fix](https://github.com/lhervier/KSP-Fix-SuspensionBounce) next to this
mod, in its default `Minimal` mode. The leg then stands up and tips over onto its side, on Kerbin as on Minmus,
where it still makes a small hop. A wheel set down alone is fixed by this mod alone (see
[Checking parts lying alone: a wheel dropped in EVA construction](../../checking/wheel-drop.md)), and settles the
same way with both mods.

*The saves.* [`landing-leg-kerbin.sfs`](../../../../diag/lone-parts/limits/landing-leg/landing-leg-kerbin.sfs) and
[`landing-leg-minmus.sfs`](../../../../diag/lone-parts/limits/landing-leg/landing-leg-minmus.sfs): Bill Kerman on
EVA next to a lander with eight LT-1 landing legs, four of them on the ground. Copy a save into the folder of a
sandbox game and load it from that game; take one of the legs that do not touch the ground with the *Place* tool,
and set it down on its foot, away from Bill and the lander. Played with KSP 1.12.5 and KSP Community Fixes 1.41.1:
without this mod; with this mod; with this mod and Suspension Bounce Fix.
