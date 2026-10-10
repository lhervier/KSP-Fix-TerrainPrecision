"""Plays "The protocol: the runway and the grass, while the world moves".

It drives KSP through KSP-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-MCPServer, KSP Diag - Terrain Height and
Diag FloatingOrigin installed, wait for the main menu, then run:

    python run-driving-runway.py --folder <your sandbox game> --moves 2 --out screenshots

For each move of the floating origin it does what the protocol asks a player to do, in the same order:
record at G (grass) and P (deck), come back to both with no move, drive on until the origin moves, come
back to both again. It records in both Diag windows at every stop, takes a screenshot of each table after
each move, prints what it read, and quits KSP at the end (unless --keep-running is given). The windows
of the instruments are hidden once the flight opens, so that the scene shows, and each is shown only for
its screenshot.
"""
import argparse
import json
import math
import os
import time
import urllib.request

# The radius of the body, only to turn the metres between the waypoints below into degrees: Kerbin's unless
# --radius says otherwise.
radius = 600000.0

# Where the spots lie, in metres. The quarter turn south from the edge of the runway ends on the bank that
# rises to the deck: G is put back on the flat grass north of it, and P on the deck, south of G.
G_NORTH_OF_TURN_END = 12.0
P_SOUTH_OF_G = 52.0
# A waypoint north-west of G, driven to after the move so that G is reached along the same line as before.
WAYPOINT_NORTH_OF_G = 15.0
WAYPOINT_WEST_OF_G = 5.0

# How far from the floating origin to stop before the quarter turn, which adds a few metres: G ends about
# 480 m from it, under the 500 m at which KSP moves it.
STOP_BEFORE_TURN = 455.0

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
        return json.loads(text)
    except ValueError:
        return text


def log(*parts):
    print(time.strftime("%H:%M:%S"), *parts, flush=True)


def offset(lat, lon, north_m, east_m):
    """A point a few metres north and east of another, in degrees."""
    return (lat + math.degrees(north_m / radius),
            lon + math.degrees(east_m / (radius * math.cos(math.radians(lat)))))


def difference_in_progress():
    line = call("terrainheight_read")["returned"]["live"]
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


def record(tag, rows):
    """Presses Record in Diag TerrainHeight, then in Diag FloatingOrigin."""
    wait_for_digits_to_settle()
    line2 = call("terrainheight_record")["returned"]
    line3 = call("floatingorigin_record")["returned"]
    difference = line2["CollisionSurfaceMm"] - line2["ComputedTerrainMm"]
    rows.append(dict(tag=tag, difference=difference, computed=line2["ComputedTerrainMm"],
                     origin_distance=line3["OriginDistance"], shifts=line3["Shifts"]))
    log("  %-7s Difference %10.3f mm  Ground KSP computes %10.3f mm  Origin distance %6.1f m  Shifts %s"
        % (tag, difference, line2["ComputedTerrainMm"], line3["OriginDistance"], line3["Shifts"]))


def go(spot, name):
    answer = call("drive_to", latitude=spot[0], longitude=spot[1], speed=2)
    log("  at %s, %.2f m from the spot" % (name, answer["missedBy"]["metres"]))


def screenshots(directory, move):
    """One screenshot per Diag table, each window alone in the middle of the screen: the windows stay hidden
    but for their own screenshot."""
    width = 1280
    # The files keep the names the published pages use: diag3 for Diag FloatingOrigin, diag2 for Diag
    # TerrainHeight.
    for shown, name in (("floatingorigin", "diag3"), ("terrainheight", "diag2")):
        call(shown + "_show_window", visible=True)
        size = call(shown + "_move_window", x=0, y=60)["returned"]
        call(shown + "_move_window", x=(width - size["width"]) / 2, y=60)
        call("wait", seconds=1)
        call("screenshot", path=os.path.join(os.path.abspath(directory), "move%d-%s.png" % (move, name)),
             return_image=False)
        call(shown + "_show_window", visible=False)


def main():
    global URL, radius
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ the save was copied into")
    parser.add_argument("--save", default="driving-runway-kerbin", help="the save, without .sfs")
    parser.add_argument("--moves", type=int, default=2, help="how many moves of the floating origin")
    parser.add_argument("--out", default="screenshots", help="where the screenshots go")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-MCPServer")
    parser.add_argument("--radius", type=float, default=600000.0,
                        help="the radius of the body in metres (default Kerbin's; 6371000 for Earth in Real Solar System)")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    radius = options.radius
    os.makedirs(options.out, exist_ok=True)

    call("load_save", folder=options.folder, save=options.save)
    call("wait", seconds=5)
    call("terrainheight_clear")
    call("floatingorigin_clear")
    call("terrainheight_show_window", visible=False)
    call("floatingorigin_show_window", visible=False)
    rows = []
    for move in range(1, options.moves + 1):
        # East along the north edge of the runway, then a quarter turn south. The origin lies (n0, e0)
        # metres from the rover; after d metres east it lies at (n0, e0 - d), STOP_BEFORE_TURN away when
        # d = e0 + sqrt(STOP_BEFORE_TURN^2 - n0^2).
        origin = call("get_floating_origin")
        n0, e0 = origin["north"], origin["east"]
        call("drive", heading=90, speed=20, distance=max(0.0, e0 + math.sqrt(max(0.0, STOP_BEFORE_TURN ** 2 - n0 ** 2))))
        turned = call("drive", heading=180, speed=2, distance=12)
        g = offset(turned["vessel"]["latitude"], turned["vessel"]["longitude"], G_NORTH_OF_TURN_END, 0.0)
        p = offset(g[0], g[1], -P_SOUTH_OF_G, 0.0)
        waypoint = offset(g[0], g[1], WAYPOINT_NORTH_OF_G, -WAYPOINT_WEST_OF_G)
        log("move %d: G at %.7f, %.7f" % (move, g[0], g[1]))

        # Steps 1 and 2: G, P, then back to both with no move, and G once more.
        go(g, "G"); record("G%d-b1" % move, rows)
        go(p, "P"); record("P%d-b1" % move, rows)
        go(g, "G"); record("G%d-b2" % move, rows)
        go(p, "P"); record("P%d-b2" % move, rows)
        go(g, "G"); record("G%d-b3" % move, rows)

        # Step 3: on, east, until the origin moves.
        moved = call("drive", heading=90, speed=2, distance=200, until_shift=True)
        if moved.get("stoppedBecause") != "shift":
            raise RuntimeError("the floating origin did not move")
        log("move %d: the origin moved by %.3f m" % (move, moved["floatingOrigin"]["lastShift"]))

        # Step 4: back to G and P, twice.
        go(waypoint, "the waypoint")
        go(g, "G"); record("G%d-a1" % move, rows)
        go(p, "P"); record("P%d-a1" % move, rows)
        go(g, "G"); record("G%d-a2" % move, rows)
        go(p, "P"); record("P%d-a2" % move, rows)
        go(g, "G")

        screenshots(options.out, move)
        call("terrainheight_clear")
        call("floatingorigin_clear")

    with open(os.path.join(options.out, "lines.json"), "w") as f:
        json.dump(rows, f, indent=1)
    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
