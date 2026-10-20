"""Plays "The protocol: driving on while the world moves".

It drives KSP through KSP-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-MCPServer, KSP Diag - Terrain Height and Diag
FloatingOrigin installed, copy driving-kerbin.sfs into a sandbox game, wait for the main menu, then run:

    python run-driving.py --folder <your sandbox game> --moves 3 --out out

It loads the save once and never changes scene. For each move of the floating origin it does what the protocol
asks a player to do, driving due south: stop when the rover is --before metres from the origin (490 on Kerbin,
499 on Earth) and record; creep on until the origin moves, stop and record; creep on as far again, with no
move, and record. Both instruments record at every stop. At the end it takes a screenshot of each table, that
window alone. It prints what it read, writes it to lines.json, and quits KSP (unless --keep-running is given).
The windows of the instruments are hidden once the flight opens, so that the scene shows, and each is
shown only for its screenshot.
"""
import argparse
import json
import math
import os
import time
import urllib.request

URL = None


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


def difference_in_progress():
    line = call("terrainheight_read")["live"]
    return line["CollisionSurfaceMm"] - line["ComputedTerrainMm"]


def wait_for_digits_to_settle():
    """What the protocol asks: wait for the digits to stop moving (within 0.01 mm over 3 s)."""
    values = []
    start = time.time()
    while time.time() - start < 30:
        values = (values + [difference_in_progress()])[-7:]
        if len(values) == 7 and max(values) - min(values) < 0.01:
            return
        time.sleep(0.5)


def position():
    vessel = call("get_state")["vessel"]
    return vessel["latitude"], vessel["longitude"]


def metres_between(a, b, radius):
    north = math.radians(b[0] - a[0]) * radius
    east = math.radians(b[1] - a[1]) * radius * math.cos(math.radians(a[0]))
    return math.hypot(north, east)


def record(tag, rows):
    """Presses Record in Diag TerrainHeight, then in Diag FloatingOrigin, without moving in between."""
    wait_for_digits_to_settle()
    terrain = call("terrainheight_record")
    origin = call("floatingorigin_record")
    difference = terrain["CollisionSurfaceMm"] - terrain["ComputedTerrainMm"]
    rows.append(dict(tag=tag, difference=difference, computed=terrain["ComputedTerrainMm"],
                     origin_distance=origin["OriginDistance"], shifts=origin["Shifts"]))
    log("  %-9s Difference %10.3f mm  Ground KSP computes %12.3f mm  Origin distance %6.1f m  Shifts %s"
        % (tag, difference, terrain["ComputedTerrainMm"], origin["OriginDistance"], origin["Shifts"]))


def screenshots(directory, name, instruments, width):
    """One screenshot per table, each window alone in the middle of the screen: the windows stay hidden but
    for their own screenshot."""
    for shown in instruments:
        call(shown + "_show_window", visible=True)
        size = call(shown + "_move_window", x=0, y=60)
        call(shown + "_move_window", x=(width - size["width"]) / 2, y=60)
        call("wait", seconds=1)
        call("screenshot", path=os.path.join(os.path.abspath(directory), "%s-%s.png" % (name, shown)),
             return_image=False)
        call(shown + "_show_window", visible=False)


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ the save was copied into")
    parser.add_argument("--save", default="driving-kerbin", help="the save, without .sfs")
    parser.add_argument("--moves", type=int, default=3, help="how many moves of the floating origin")
    parser.add_argument("--before", type=float, default=490.0,
                        help="how far from the origin to stop before a move, in metres (499 on Earth)")
    parser.add_argument("--radius", type=float, default=600000.0,
                        help="the radius of the body, in metres (6371000 for the Earth of Real Solar System)")
    parser.add_argument("--out", default="out", help="where lines.json and the screenshots go")
    parser.add_argument("--screen-width", type=float, default=1280, help="the width of KSP's window, in pixels")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-MCPServer")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    os.makedirs(options.out, exist_ok=True)

    # KSP-MCPServer loads a save from the space centre or in flight only, as a player does: from the main
    # menu, the game is opened at the space centre first.
    if call("get_state")["scene"] == "MAINMENU":
        call("open_game", folder=options.folder)
    call("load_save", folder=options.folder, save=options.save)
    call("set_cheats", infinite_electricity=True)
    call("wait", seconds=5)
    # The game moves the origin as the scene opens, more than once on Earth: wait for it to be on the rover
    # before reading how far there is to drive.
    start = time.time()
    while call("get_floating_origin")["distance"] > 100 and time.time() - start < 60:
        time.sleep(1)
    call("terrainheight_clear")
    call("floatingorigin_clear")
    call("terrainheight_move_window", x=0, y=40)
    call("floatingorigin_move_window", x=640, y=40)
    call("terrainheight_show_window", visible=False)
    call("floatingorigin_show_window", visible=False)
    rows = []
    for move in range(1, options.moves + 1):
        # 1. Just before: due south until the origin, behind the rover, is --before metres away.
        # Fast until 20 m short, then at walking pace: on Earth the stop has to fall between 498 and 500 m, and
        # the rover does not stop that precisely from 15 m/s.
        distance = call("get_floating_origin")["distance"]
        if distance < options.before - 20:
            call("drive", heading=180, speed=15, distance=options.before - 20 - distance)
        distance = call("get_floating_origin")["distance"]
        if distance < options.before:
            call("drive", heading=180, speed=1, distance=options.before - distance)
        record("move%d-1" % move, rows)
        before = position()

        # 2. Just after: creep on until the origin moves, and stop.
        moved = call("drive", heading=180, speed=1, distance=50, until_shift=True)
        if moved.get("stoppedBecause") != "shift":
            raise RuntimeError("the floating origin did not move")
        record("move%d-2" % move, rows)
        after = position()

        # 3. The same distance again, with no move.
        step = metres_between(before, after, options.radius)
        call("drive", heading=180, speed=1, distance=step)
        record("move%d-3" % move, rows)
        log("move %d: %.2f m from 1 to 2, %.2f m from 2 to 3" % (
            move, step, metres_between(after, position(), options.radius)))

    screenshots(options.out, options.save, ["terrainheight", "floatingorigin"], options.screen_width)
    with open(os.path.join(options.out, "lines.json"), "w", newline="") as f:
        json.dump(rows, f, indent=1)
    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
