"""Sets up and plays one move of the floating origin under a rover, for filming the scatter as it happens.

It drives KSP through KSP-MCPServer, and needs nothing but Python 3. Start KSP with KSP-MCPServer, KSP Diag -
Scatter, KSP Diag - Floating Origin and the mod to film installed, terrain scatter on, copy cactus-kerbin.sfs
into a sandbox game, then run it twice, starting the recording in between:

    python film-scatter-driving.py prepare --folder <your sandbox game>
    python film-scatter-driving.py cross

or, for takes one after the other until a large one, filming all along:

    python film-scatter-driving.py prepare --folder <your sandbox game>
    python film-scatter-driving.py loop --at-least 30

prepare loads the save, where the floating origin settles on the rover, and drives to --stop-short metres
before the target (by default, the cactus of cactus-kerbin.sfs, 497 m away), on the straight line from where
the rover started, so that the origin is still about 494 m behind. It then shows the window of KSP Diag -
Floating Origin, hides the interface, frames the rover with the flight camera, and records the rocks. cross
drives on along the same line until the origin moves, stops, waits --hold seconds for the film to show the
scene after the move, records the rocks again, and prints how far the scatter moved against the ground: the
move of each holder's matrix, the same for all of them. The rover drives forward or in reverse, whichever it
faces, and never turns around. loop plays takes without loading again: after each move by the target, the rover
drives back along the line until the origin moves again, out of the picture, then comes back to its stop short
of the target; each move draws other roundings. With --reload, each take loads the save again instead, and drives the same way
to the same stop. It stops after the first move whose scatter moved by at least
--at-least millimetres, or after --takes takes, printing the time of each move. With --wait-for-brakes, each take
waits for the brakes to be let off in the game (B): one short recording per take. With --screentogif, the
script records the takes itself into a single recording, with the shortcuts of ScreenToGif's recorder, which has
to be open over the game: F7 starts or resumes it before each move and pauses it after, F8 stops it after the
last take.
"""
import argparse
import json
import math
import os
import re
import tempfile
import time
import urllib.request

URL = None

HOLDER = re.compile(r"holder '[^']+': built, height [\d.]+ m, matrix [\d.]+ m, up ([-+\d.]+) mm")

# Where prepare leaves what cross needs: the heading of the line driven along.
STATE = os.path.join(tempfile.gettempdir(), "film-scatter-driving.json")


def call(tool, **args):
    """Calls one tool of KSP-MCPServer and returns its answer, decoded from JSON when it is JSON."""
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": tool, "arguments": args}}).encode()
    request = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=900) as response:
        result = json.loads(response.read())["result"]
    text = result["content"][0].get("text", "") if result["content"] else ""
    if result.get("isError"):
        raise RuntimeError(tool + ": " + text)
    try:
        answer = json.loads(text)
    except ValueError:
        return text
    # The tools another mod adds answer inside "returned".
    if isinstance(answer, dict) and list(answer) == ["returned"]:
        return answer["returned"]
    return answer


def log(*parts):
    print(time.strftime("%H:%M:%S"), *parts, flush=True)


def holder_ups(ksp_log, number):
    """The up of every holder in record <number> of KSP.log, in the order of the record."""
    ups = []
    inside = False
    with open(ksp_log, encoding="utf-8", errors="replace") as f:
        for line in f:
            if "[KSPDiagScatter] Record %d on " % number in line:
                inside = True
            elif inside:
                match = HOLDER.search(line)
                if match:
                    ups.append(float(match.group(1)))
                if "[KSPDiagScatter] End of record %d:" % number in line:
                    break
    return ups


def record():
    line = call("scatter_record_rocks")
    return int(re.search(r"End of record (\d+):", line).group(1))


def drive_along(heading, **args):
    """Drives the rover along a heading, forward or in reverse, whichever its front faces: it never turns around."""
    facing = call("get_state")["vessel"]["heading"]
    if abs((heading - facing + 180) % 360 - 180) > 90:
        return call("drive", heading=(heading + 180) % 360, reverse=True, **args)
    return call("drive", heading=heading, **args)


# Virtual-key codes of the keys ScreenToGif starts and stops its recorder with, by default.
VK_F7 = 0x76
VK_F8 = 0x77


def press(key):
    """Presses and releases a key, as the keyboard does: a shortcut registered by another program, such as those
    of ScreenToGif, answers it whichever window has the focus. Windows only."""
    import ctypes
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(key, 0, 2, 0)


def frame(options):
    call("floatingorigin_show_window", visible=True)
    # At the bottom of the screen, out of the way of what is filmed.
    size = call("floatingorigin_move_window", x=10, y=0)
    call("floatingorigin_move_window", x=10, y=options.screen_height - size["height"] - 10)
    call("set_ui", visible=False)
    call("set_camera", distance=options.distance, heading=options.heading, pitch=options.pitch, fov=options.fov)


def cross(state, options):
    """Drives on along the line until the origin moves, and returns the move of the scatter, in mm."""
    before = record()
    # Slowly: the camera follows the rover, and at 1 m/s the scene slides by as much per frame as the scatter
    # jumps.
    moved = drive_along(state["heading"], speed=options.creep, distance=30, until_shift=True)
    if moved.get("stoppedBecause") != "shift":
        raise RuntimeError("the floating origin did not move")
    log("the origin moved")
    call("wait", seconds=options.hold)
    after = record()
    a, b = holder_ups(options.ksp_log, before), holder_ups(options.ksp_log, after)
    jumps = [y - x for x, y in zip(a, b)]
    if not jumps:
        log("no holder read")
        return 0.0
    log("the scatter moved against the ground by %+.1f to %+.1f mm (records %d and %d)"
        % (min(jumps), max(jumps), before, after))
    return max(jumps, key=abs)


def prepare(options):
    """Loads the save and drives to the stop short of the target; returns the line driven along, and the stop."""
    # KSP-MCPServer loads a save from the space centre or in flight only, as a player does: from the main
    # menu, the game is opened at the space centre first.
    if call("get_state")["scene"] == "MAINMENU":
        call("open_game", folder=options.folder)
    call("load_save", folder=options.folder, save=options.save)
    call("set_cheats", infinite_electricity=True)
    call("scatter_show_window", visible=False)
    call("floatingorigin_show_window", visible=False)
    call("wait", seconds=5)
    # The game moves the origin as the scene opens: wait for it to be on the rover.
    start = time.time()
    while call("get_floating_origin")["distance"] > 100 and time.time() - start < 60:
        time.sleep(1)

    # The line from where the rover starts to the target, in metres north and east.
    vessel = call("get_state")["vessel"]
    lat0, lon0 = vessel["latitude"], vessel["longitude"]
    north = math.radians(options.target[0] - lat0) * options.radius
    east = math.radians(options.target[1] - lon0) * options.radius * math.cos(math.radians(lat0))
    length = math.hypot(north, east)
    heading = math.degrees(math.atan2(east, north)) % 360
    # The stop, short of the target on that line: the origin stays behind, under 500 m away.
    k = (length - options.stop_short) / length
    stop_lat = lat0 + math.degrees(north * k / options.radius)
    stop_lon = lon0 + math.degrees(east * k / (options.radius * math.cos(math.radians(lat0))))
    log("target %.1f m away, heading %.1f" % (length, heading))
    call("drive_to", latitude=stop_lat, longitude=stop_lon, speed=options.speed, tolerance=0.5)
    origin = call("get_floating_origin")
    if origin["shiftsThisScene"]:
        raise RuntimeError("the floating origin moved on the way: run prepare again")
    state = {"heading": heading, "stop": [stop_lat, stop_lon]}
    with open(STATE, "w", newline="") as f:
        json.dump(state, f)
    frame(options)
    log("ready, %.1f m from the origin" % origin["distance"])
    return state


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("step", choices=["prepare", "cross", "loop"])
    parser.add_argument("--folder", help="prepare: the sandbox game under saves/ the save was copied into")
    parser.add_argument("--save", default="cactus-kerbin", help="prepare: the save, without .sfs")
    parser.add_argument("--target", type=float, nargs=2, default=[0.35649825523034073, -109.3969651734584],
                        metavar=("LATITUDE", "LONGITUDE"),
                        help="prepare: the point to film, in degrees (default: the cactus of cactus-kerbin.sfs)")
    parser.add_argument("--stop-short", type=float, default=1.0,
                        help="prepare: how far before the target to stop, in metres")
    parser.add_argument("--radius", type=float, default=600000.0, help="prepare: the radius of the body, metres")
    parser.add_argument("--speed", type=float, default=8.0, help="prepare: top speed on the way, m/s")
    parser.add_argument("--distance", type=float, default=22.4, help="prepare: the camera's distance, metres")
    parser.add_argument("--heading", type=float, default=270.2,
                        help="prepare: the direction the camera looks in, degrees (270: west)")
    parser.add_argument("--pitch", type=float, default=17.8, help="prepare: the camera's pitch, degrees")
    parser.add_argument("--fov", type=float, default=50.0, help="prepare: the camera's field of view, degrees")
    parser.add_argument("--screen-height", type=float, default=720, help="the height of KSP's window, pixels")
    parser.add_argument("--creep", type=float, default=0.15,
                        help="cross, loop: the speed across the move of the origin, m/s")
    parser.add_argument("--hold", type=float, default=3.0, help="cross: seconds to stay still after the move")
    parser.add_argument("--ksp-log", default=r"D:\ksp-dev\KSP.log", help="cross: the KSP.log being written")
    parser.add_argument("--at-least", type=float, default=30.0,
                        help="loop: the move of the scatter to stop at, in millimetres either way")
    parser.add_argument("--takes", type=int, default=10, help="loop: the most takes to play")
    parser.add_argument("--reload", action="store_true",
                        help="loop: load the save again for each take, instead of driving back and forth")
    parser.add_argument("--screentogif", action="store_true",
                        help="loop: start and stop ScreenToGif's recorder around each move (F7, F8)")
    parser.add_argument("--wait-for-brakes", action="store_true",
                        help="loop: before each take, wait for the brakes to be let off in the game (B)")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-MCPServer")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port

    if options.step == "prepare" or options.reload:
        if not options.folder:
            parser.error("prepare and --reload need --folder")
    if options.step == "prepare":
        prepare(options)
        record()
        log("start filming, then run: cross")
        return

    with open(STATE) as f:
        state = json.load(f)
    if options.step == "cross":
        cross(state, options)
        log("stop filming")
        return

    take = 1
    while True:
        log("take %d" % take)
        if options.wait_for_brakes:
            # The signal of whoever films: the brakes let off in the game (B), once the recording runs.
            log("ready: start filming, then let the brakes off in the game (B)")
            while call("get_state")["vessel"]["brakes"]:
                time.sleep(0.2)
        # One recording for all the takes: started or resumed before each move, paused after it.
        if options.screentogif:
            press(VK_F7)
            log("ScreenToGif recording (F7)")
            time.sleep(2)
        jump = cross(state, options)
        if options.screentogif:
            press(VK_F7)
            log("ScreenToGif paused (F7)")
        if abs(jump) >= options.at_least or take == options.takes:
            if options.screentogif:
                press(VK_F8)
                log("ScreenToGif stopped (F8)")
            log("stop filming")
            return
        if options.reload:
            # The save again: the origin back on the same point, the same way to the same stop.
            state = prepare(options)
            take += 1
            continue
        # Back along the line, past the next move of the origin, out of the picture; then to the stop again.
        drive_along((state["heading"] + 180) % 360, speed=options.speed, distance=600, until_shift=True)
        call("drive_to", latitude=state["stop"][0], longitude=state["stop"][1], speed=options.speed,
             tolerance=0.5)
        origin = call("get_floating_origin")
        if origin["distance"] >= 500:
            raise RuntimeError("the origin moved on the way back to the stop")
        frame(options)
        log("back at the stop, %.1f m from the origin" % origin["distance"])
        take += 1


if __name__ == "__main__":
    main()
