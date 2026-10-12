# The protocol: the scatter, while the world moves

Part of [Terrain Precision Fix](../../README.md), for
[Checking the scatter: driving on while the world moves](the-scatter.md): how the scatter around a rover that
keeps driving is read by [KSP Diag - Scatter](https://github.com/lhervier/KSP-Diag-Scatter), just before and
just after the game moves its whole world. What each reading is, and what a record holds, are in
[its page](https://github.com/lhervier/KSP-Diag-Scatter/blob/main/docs/what-it-measures.md). The protocol is
the same on stock, with this mod, and with its scatter fix turned off.

KSP keeps the craft you fly near the centre of Unity's world. Every 500 m it drives, the game moves the
whole world back under it: this is called the *floating origin*, and
[KSP Diag - Floating Origin](https://github.com/lhervier/KSP-Diag-FloatingOrigin) explains it and shows how
far the craft is from it. This protocol reads the scatter on either side of one such move, a few metres
apart, then the same few metres farther on, with no move in between, to tell what the move does from what
the few metres do.

## The save

[`driving-kerbin.sfs`](../../diag/checking-the-culprit-driving/driving-kerbin.sfs), the save of
[the protocol of the ground](the-protocol.md#the-save): a sandbox game of KSP 1.12.5, a rover alone on the
flat grass south of the runway of the KSC, facing due south. The scatter there is grass. Copy it into the
folder of a sandbox game and load it from that game.

## The protocol

1. **Scatter on, and the log written at once**: steps 1 and 2 of
   [the protocol load after load](../checking-the-culprit-loading/the-scatter-protocol.md#the-protocol).
   No other landed craft may be loaded: while one is, the game does not move the origin.
2. **Load the save**, and wait for the scene to settle: the game moves the origin onto the rover as the
   scene opens.
3. **Drive due south until the rover is about 498 m from the origin**, and stop. *Origin distance* in the
   window of Diag FloatingOrigin tells how far it is; without it, 498 m from where the rover started.
4. **Press *Record the rocks*** in the window of Diag Scatter, and again while holders are not built yet or
   the counts still change, as after a load.
5. **Creep on until the origin moves**, and stop: *Origin distance* drops back near zero. Record again.
6. **Drive on as far again**, with no move, and record a third time.
7. **Load the save again**, and play steps 3 to 6 once more: each load draws other roundings. Six loads.

Compare the three records of a load object by object, as in
[Reading the records](../checking-the-culprit-loading/the-scatter-protocol.md#reading-the-records): between
the first and the second, the move of the world; between the second and the third, a few metres of driving
alone.

## Played by a script

[`run-scatter-driving.py`](../../diag/automation/run-scatter-driving.py) plays this protocol through
[KSP-MCPServer](https://github.com/lhervier/KSP-MCPServer), with nothing but Python 3: start KSP with
KSP-MCPServer and Diag Scatter installed, copy the save into a sandbox game, wait for the main menu, then
run `python run-scatter-driving.py --folder <your sandbox game> --loads 6 --out out`. It stops 498 m from
the origin, records each time once the counts have settled, writes the number and the closing line of each
record to `lines.json`, and never saves the game. The records stay in `KSP.log`;
[`extract-scatter-records.py`](../../diag/automation/extract-scatter-records.py) copies them out, one file
per record.

## Filming it

The grass is too small to see a jump of a few centimetres. The film on
[the page of measurements](the-scatter.md#seen-in-the-game) was taken on a cactus in a desert of Kerbin, with
[`cactus-kerbin.sfs`](../../diag/checking-the-culprit-driving/scatter/cactus-kerbin.sfs): the same rover,
497 m north of a cactus, facing it. The jump to film is the one the terrain fix leaves alone, so this mod
is installed with its scatter fix turned off, `fixScatter = false` in its settings. Diag FloatingOrigin is
installed as well, its window at the bottom of the screen, so that *Origin distance* shows in the film.

[`film-scatter-driving.py`](../../diag/automation/film-scatter-driving.py) plays it through KSP-MCPServer:

- `prepare --folder <your sandbox game>` loads the save, drives to a metre short of the cactus, on the
  straight line from where the rover starts, 495.8 m from the origin, shows the window of Diag
  FloatingOrigin, hides the interface and sets the camera;
- `loop --reload --folder <your sandbox game> --screentogif` plays the takes: it creeps on at 0.15 m/s
  until the origin moves, holds still for 3 s, records the rocks before and after, prints how far the
  scatter moved, then loads the save again for the next take. With `--screentogif`, it records each take
  itself into a single recording of [ScreenToGif](https://www.screentogif.com/), whose recorder has to be
  open over the game: F7 before each move and after it, F8 after the last take.

Creeping matters: the camera follows the rover, and at 1 m/s the whole scene slides by about 3 cm a frame
at 30 frames per second, as much as the scatter jumps.
