# Settings

Part of [Terrain Precision Fix](../../README.md), [what the fixes share](README.md).

`GameData/TerrainPrecisionFixMod/PluginData/settings.cfg` holds nine values, read when KSP starts. To
change one: quit KSP, edit the file, start KSP again.

| setting | what it does |
|---|---|
| `fixTerrain` | `true` (default) places the terrain in double precision; `false` leaves it as stock builds it |
| `fixStatics` | `true` (default) places the statics in double precision; `false` leaves them where stock places them |
| `fixScatter` | `true` (default) draws the terrain scatter from the terrain quads it was built on; `false` leaves it where stock draws it, a few centimetres off the corrected ground, and jumping against it every 500 m while you drive. It moves stock objects other mods may look for: turn it off if one of them misbehaves around rocks, grass or trees. See [On by default: when to turn it off](../scatter/the-fix.md#on-by-default-when-to-turn-it-off) |
| `fixRocs` | `true` (default) draws Breaking Ground's surface features (ROCs) from the terrain quads they were built on; `false` leaves them where stock draws them, a few centimetres off the corrected ground, differently at each load, and with their collider: a kerbal or a part resting on one is moved with it. It moves stock objects other mods may look for: turn it off if one of them misbehaves around surface features. See [Other mods that look for the holders](../rocs/the-fix.md#other-mods-that-look-for-the-holders) |
| `fixGroundAnchorModel` | `true` (default) brings the collider of the stock ground anchor down to the bottom of the anchor, so that a load puts it back where it was placed; `false` leaves the stock collider, which stops 2 cm above it |
| `fixGroundAnchorLoad` | `true` (default) loads a vessel holding a stock ground anchor where it was saved; `false` lets stock raise it to the height it computes for the terrain, where the anchor then holds it |
| `fixGroundAnchorRivet` | `true` (default) freezes a loaded anchor from the moment it is loaded, until stock rivets it again; `false` lets stock rivet it one frame late, which below 50 frames per second lets it move by under a millimetre first, a base in the air sinking a little at every load |
| `patchKopernicus` | `true` (default) patches Kopernicus, when installed, to cope with the statics fix. With `false` and the statics fix on, Kopernicus' flag fix throws when a facility is upgraded in flight near the KSC, which only a Making History mission does: an error in the log whose stack trace names Kopernicus, and nothing else, since the statics fix keeps the flags steady there. Meant only to see what the patch is for |
| `patchKerbalKonstructs` | `true` (default) patches Kerbal Konstructs, when installed, to cope with the statics fix. With `false` and the statics fix on, moving a group with its group editor in flight sends it elsewhere on its body, and saves it there: meant only to see what the patch is for |
| `logLevel` | what goes to `KSP.log`, below |

| `logLevel` | what goes to `KSP.log` |
|---|---|
| `Info` (default) | a few lines at startup, then one line per body the first time its terrain, then its statics, then its scatter, then its surface features, are corrected |
| `Debug` | adds one line per quad placed, with how far it was moved, one line per static taken out of its sphere or put back under it, one line per scatter or surface feature holder hung from its quad, one line per vessel holding a ground anchor loaded, with how far stock would have raised it, and one line per anchor frozen as it is loaded |
| `Trace` | adds, per quad, how far its vertices were moved within it, and one line per scatter or surface feature holder handed back to its pool — slower, meant for measuring |

`Error` and `Warning` are accepted too.
