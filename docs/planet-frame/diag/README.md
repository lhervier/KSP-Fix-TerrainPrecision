# The runs: the safeguard

Part of [Terrain Precision Fix](../../../README.md), [Planet Frame](../README.md#the-safeguard): the saves and the
`KSP.log` of [This mod's safeguard](../safeguard.md) on Venus, Mars and Mercury in Real Solar System.

## On Real Solar System

KSP 1.12.5 with Harmony, ModuleManager, KSP Community Fixes 1.41.1, and
[Real Solar System](https://github.com/KSP-RO/RealSolarSystem) 20.1.3.0 with what it requires (Kopernicus,
Modular Flight Integrator, KSPTextureLoader, the RSS textures), as released. This mod ran at
`logLevel = Debug`, so each log also holds one line per quad placed, with how far it was moved. Read in
[This mod's safeguard](../safeguard.md).

- [`reload-venus-mars-rss-fix.log.gz`](safeguard/reload-venus-mars-rss-fix.log.gz) — no instrument, one
  session: six loads of [`reload-venus-rss.sfs`](safeguard/reload-venus-rss.sfs), then six of
  [`reload-mars-rss.sfs`](safeguard/reload-mars-rss.sfs). The six loads after them, on a second site of Mars,
  are not used.
- [`reload-mercury-rss-fix.log.gz`](safeguard/reload-mercury-rss-fix.log.gz) — no instrument: six loads of
  [`reload-mercury-rss.sfs`](safeguard/reload-mercury-rss.sfs). Each one logs KSP moving the craft down 22.4 m,
  the terrain detail its save describes.
