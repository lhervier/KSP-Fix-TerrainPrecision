"""Plays "The protocol: the scatter, while the world moves" with KSP Diag - Scatter installed.

It drives KSP through KSP-Util-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-Util-MCPServer and KSP Diag - Scatter installed, terrain
scatter on and LOG_INSTANT_FLUSH = True in settings.cfg, copy the save into a sandbox game, wait for the main
menu, then run:

    python run-scatter-driving.py --folder <your sandbox game> --save driving-kerbin --loads 6 --out out

For each loading of the save, it drives a single move of the floating origin, due south: it stops when the
rover is --before metres from the origin and records the rocks; creeps on until the origin moves, stops and
records; creeps on as far again, with no move, and records. A record is taken once every holder is built and
the counts no longer change, as after a load. With --scene-shots, a screenshot of the scene follows each
record, the window hidden. The records go to KSP.log; lines.json lists, stop by stop, the number and the
closing line of each, with how far the origin is. It never saves the game, and quits KSP at the end (unless
--keep-running is given).
"""
import argparse
import json
import math
import os
import re
import time
import urllib.request

URL = None

# The closing line of a record of the rocks.
CLOSING = re.compile(r"End of record (\d+): (\d+) quads with rocks, (\d+) holders \((\d+) not built yet\);"
                     r" nearest quad '([^']*)': (\d+) rocks, (\d+) vertices measured")


def call(tool, **args):
    """Calls one tool of KSP-Util-MCPServer and returns its answer, decoded from JSON when it is JSON."""
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


def position():
    vessel = call("get_state")["vessel"]
    return vessel["latitude"], vessel["longitude"]


def metres_between(a, b, radius):
    north = math.radians(b[0] - a[0]) * radius
    east = math.radians(b[1] - a[1]) * radius * math.cos(math.radians(a[0]))
    return math.hypot(north, east)


def record_once_settled(attempts, pause):
    """Presses Record the rocks until a record has every holder built and the same counts as the one before it.
    Returns the closing line of the last record and whether it settled."""
    previous = None
    line = None
    for _ in range(attempts):
        line = call("scatter_record_rocks")
        match = CLOSING.search(line)
        if match:
            # Everything but the record's number.
            counts = match.groups()[1:]
            if counts[2] == "0" and counts == previous:
                return line, True
            previous = counts
        call("wait", seconds=pause)
    return line, False


def record(tag, rows, options):
    line, settled = record_once_settled(options.attempts, options.pause)
    match = CLOSING.search(line or "")
    origin = call("get_floating_origin")
    rows.append(dict(load=options.current_load, tag=tag, settled=settled, closing=line,
                     record=int(match.group(1)) if match else None, origin_distance=origin["distance"]))
    if options.scene_shots:
        name = "%s-load%d-%s.png" % (options.save, options.current_load, tag)
        call("screenshot", path=os.path.join(os.path.abspath(options.out), name), return_image=False)
    with open(os.path.join(options.out, "lines.json"), "w", newline="") as f:
        json.dump(rows, f, indent=1)
    log("  load %d %-6s origin %6.1f m  %s%s" % (options.current_load, tag, origin["distance"], line,
                                                 "" if settled else "  (NOT SETTLED)"))


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ the save was copied into")
    parser.add_argument("--save", default="driving-kerbin", help="the save, without .sfs")
    parser.add_argument("--loads", type=int, default=6, help="how many loadings, one move of the origin each")
    parser.add_argument("--before", type=float, default=498.0,
                        help="how far from the origin to stop before the move, in metres")
    parser.add_argument("--radius", type=float, default=600000.0, help="the radius of the body, in metres")
    parser.add_argument("--out", default="out", help="where lines.json and the screenshots go")
    parser.add_argument("--attempts", type=int, default=20, help="records at most per stop")
    parser.add_argument("--pause", type=float, default=3, help="seconds between two records of a stop")
    parser.add_argument("--scene-shots", action="store_true", help="a screenshot of the scene after each stop")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-Util-MCPServer")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    os.makedirs(options.out, exist_ok=True)

    rows = []
    # KSP-Util-MCPServer loads a save from the space centre or in flight only, as a player does: from the main
    # menu, the game is opened at the space centre first.
    if call("get_state")["scene"] == "MAINMENU":
        call("open_game", folder=options.folder)
    for load in range(1, options.loads + 1):
        options.current_load = load
        call("load_save", folder=options.folder, save=options.save)
        call("set_cheats", infinite_electricity=True)
        if load == 1:
            call("scatter_show_window", visible=False)
        call("wait", seconds=5)
        # The game moves the origin as the scene opens: wait for it to be on the rover before reading how far
        # there is to drive.
        start = time.time()
        while call("get_floating_origin")["distance"] > 100 and time.time() - start < 60:
            time.sleep(1)

        # 1. Just before: due south until the origin, behind the rover, is --before metres away. Fast until
        # 20 m short, then at walking pace, for the stop to fall short of the move.
        distance = call("get_floating_origin")["distance"]
        if distance < options.before - 20:
            call("drive", heading=180, speed=15, distance=options.before - 20 - distance)
        distance = call("get_floating_origin")["distance"]
        if distance < options.before:
            call("drive", heading=180, speed=1, distance=options.before - distance)
        record("before", rows, options)
        before = position()

        # 2. Just after: creep on until the origin moves, and stop.
        moved = call("drive", heading=180, speed=1, distance=50, until_shift=True)
        if moved.get("stoppedBecause") != "shift":
            raise RuntimeError("the floating origin did not move")
        record("after", rows, options)
        after = position()

        # 3. The same distance again, with no move: what driving alone changes in a record.
        step = metres_between(before, after, options.radius)
        call("drive", heading=180, speed=1, distance=step)
        record("again", rows, options)
        log("load %d: %.2f m from before to after, %.2f m from after to again" % (
            load, step, metres_between(after, position(), options.radius)))

    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
