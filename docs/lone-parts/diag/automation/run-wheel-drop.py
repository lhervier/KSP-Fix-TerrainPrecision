"""Plays "The protocol: a wheel dropped in EVA construction" with KSP Diag - Landed Vessel installed.

It drives KSP through KSP-Util-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-Util-MCPServer and KSP Diag - Landed Vessel installed,
copy the save into a sandbox game, wait for the main menu, then run, for the save of Kerbin:

    python run-wheel-drop.py --folder <your sandbox game> --save wheel-drop-kerbin --wheel 4029216261
        --drop 600 460 --camera 12 17.19 25 --drops 3 --out out

For each drop it does what the protocol asks a player to do, in the same order: load the save, open the
construction panel, pick the Place tool, click the wheel on the rover, click the ground where the wheel goes,
wait 15 seconds, set the wheel dropped as target and record. The clicks are those of a window of 1280 x 720
pixels, the camera where --camera puts it (metres from the engineer, heading and pitch in degrees). It never
saves the game.
It takes a screenshot of the scene --shot-at seconds after the drop, and one of the table at the end. It prints
what it read, writes it to lines.json, and quits KSP (unless --keep-running is given).
"""
import argparse
import json
import os
import sys
import time
import urllib.request

URL = None


def call(name, **args):
    """Calls one tool of KSP-Util-MCPServer and returns its answer, decoded from JSON when it is JSON."""
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": name, "arguments": args}}).encode()
    request = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=900) as response:
        result = json.loads(response.read())["result"]
    text = result["content"][0].get("text", "") if result["content"] else ""
    if result.get("isError"):
        raise RuntimeError(name + ": " + text)
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


def mm(value):
    """A value of the instrument, in millimetres to one decimal, or "none" when it recorded none."""
    return "none" if value is None else "%.1f" % value


def table_screenshot(path, width):
    """A screenshot of the table, the window alone in the middle of the screen, hidden again afterwards."""
    call("landedvessel_show_window", visible=True)
    size = call("landedvessel_move_window", x=0, y=60)
    call("landedvessel_move_window", x=(width - size["width"]) / 2, y=60)
    call("wait", seconds=1)
    call("screenshot", path=path, return_image=False)
    call("landedvessel_show_window", visible=False)


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ the save was copied into")
    parser.add_argument("--save", required=True, help="the save, without .sfs")
    parser.add_argument("--wheel", type=int, required=True, help="the id of the wheel taken off the rover")
    parser.add_argument("--drop", type=float, nargs=2, required=True, metavar=("X", "Y"),
                        help="where to click the ground, in pixels from the top left corner of the window")
    parser.add_argument("--camera", type=float, nargs=3, required=True, metavar=("DISTANCE", "HEADING", "PITCH"),
                        help="where to put the camera, in metres from the engineer and degrees")
    parser.add_argument("--drops", type=int, default=3, help="how many drops, the save loaded before each")
    parser.add_argument("--rest", type=float, default=15, help="seconds after the drop before the record")
    parser.add_argument("--shot-at", type=float, default=4.5,
                        help="seconds after the drop to take a screenshot of the scene at")
    parser.add_argument("--out", default="out", help="where lines.json and the screenshots go")
    parser.add_argument("--screen-width", type=float, default=1280, help="the width of KSP's window, in pixels")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-Util-MCPServer")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    # Part names follow the language of the game, accents included, whatever the console is set to.
    sys.stdout.reconfigure(encoding="utf-8")
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    out = os.path.abspath(options.out)
    os.makedirs(out, exist_ok=True)

    rows = []
    # KSP-Util-MCPServer loads a save from the space centre or in flight only, as a player does: from the main
    # menu, the game is opened at the space centre first.
    if call("get_state")["scene"] == "MAINMENU":
        call("open_game", folder=options.folder)
    for drop in range(1, options.drops + 1):
        call("load_save", folder=options.folder, save=options.save)
        if drop == 1:
            call("landedvessel_clear")
        call("landedvessel_show_window", visible=False)
        call("set_target")
        call("set_camera", distance=options.camera[0], heading=options.camera[1], pitch=options.camera[2])
        before = {v["id"] for v in call("list_vessels")}
        call("construction_tool", panel="open", tool="place")
        located = call("locate_part", part=options.wheel)
        point = located["point"]
        call("mouse_click", x=point["x"], y=point["y"])
        call("wait", seconds=1)
        call("mouse_click", x=options.drop[0], y=options.drop[1])
        dropped = time.time()
        call("wait", seconds=max(0.0, options.shot_at - (time.time() - dropped)))
        call("screenshot", path=os.path.join(out, "%s-drop%02d-scene.png" % (options.save, drop)),
             return_image=False)
        call("wait", seconds=max(0.0, options.rest - (time.time() - dropped)))
        # The wheel is the new craft named after it; anything else new (a part knocked off a craft) is logged.
        new = [v for v in call("list_vessels") if v["id"] not in before]
        wheels = [v for v in new if v["name"] == located["title"]]
        others = [v["name"] for v in new if v not in wheels]
        if len(wheels) != 1:
            raise SystemExit("drop %d: %d new crafts named %s" % (drop, len(wheels), located["title"]))
        if others:
            log("drop %d: other new crafts: %s" % (drop, ", ".join(others)))
        new = wheels
        call("construction_tool", panel="close")
        call("set_target", vessel=new[0]["id"])
        # The instrument reads its target once per frame.
        call("wait", seconds=0.5)
        line = call("landedvessel_record")
        rows.append(dict(drop=drop, part=new[0]["name"], id=new[0]["id"], others=others, **line))
        log("drop %d  %-40s Moved %8s mm  Highest %9s mm" % (drop, new[0]["name"], mm(line["MovedMm"]),
                                                            mm(line["HighestMm"])))
    call("set_target")
    table_screenshot(os.path.join(out, "%s-table.png" % options.save), options.screen_width)

    with open(os.path.join(out, "lines.json"), "w", newline="") as f:
        json.dump(rows, f, indent=1)
    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
