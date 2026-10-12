# Non-regression tests: Kerbal Konstructs

Part of [Terrain Precision Fix](../../README.md), one mod of [Non-regression tests](../non-regression.md): what works without this mod still works with it, with Kerbal Konstructs.

Unless a page says otherwise, each test is played in KSP 1.12.5 with Harmony, ModuleManager, KSP
Community Fixes 1.41.1 and this mod, plus the instrument and the mods it names. Each test has a page of
its own.

[Kerbal Konstructs](https://github.com/KSP-RO/Kerbal-Konstructs) plants statics of its own, which this
mod takes out of their sphere in flight like the KSC, and can turn one into a CommNet ground station while
the player is flying beside it. Its group editor needs a patch of this mod:
[Limits and solutions](../limits-and-solutions.md#kerbal-konstructs).

## A ground station opened in flight

**Checked on Kerbin, no problem.** A ground station finds its body among the parents of its static, which
this mod lends back to it. Opened in flight beside a craft, while its static is out of its sphere, a
ground station of Kerbal Konstructs becomes the craft's first CommNet hop.

**→ Full chapter: [Kerbal Konstructs: a ground station opened in flight](kerbal-konstructs/a-ground-station-opened-in-flight.md)**
