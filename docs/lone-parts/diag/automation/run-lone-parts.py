"""Plays "The protocol: loading parts left alone" with KSP Diag - Landed Vessel installed.

It drives KSP through KSP-Util-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-Util-MCPServer and KSP Diag - Landed Vessel installed,
copy the save into a sandbox game, wait for the main menu, then run:

    python run-lone-parts.py --folder <your sandbox game> --save lone-parts-mun --loads 10 --out out
        --skip "Base Mu Grue" "Camion Mu"

For each loading it does what the protocol asks a player to do, in the same order: load the save, wait for the
parts to come to rest, then, part by part, set it as target and record. The parts are the crafts landed around
the craft being flown, but those named by --skip. It never saves the game.
After each loading it takes a screenshot of the table, that window alone, and empties the table; with --shot-at,
it also takes a screenshot of the scene that long after the loading, the window hidden, the camera where --camera
puts it. At the end it prints
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
    parser.add_argument("--loads", type=int, default=10, help="how many loadings")
    parser.add_argument("--skip", nargs="*", default=[], help="crafts that are not parts left alone")
    parser.add_argument("--rest", type=float, default=15,
                        help="seconds after the loading before the first record: the parts have come to rest")
    parser.add_argument("--shot-at", type=float, default=0,
                        help="seconds after the loading to take a screenshot of the scene at, 0 for none")
    parser.add_argument("--camera", type=float, nargs=2, metavar=("DISTANCE", "PITCH"),
                        help="where to put the camera after the loading, in metres from the craft and degrees")
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
    for load in range(1, options.loads + 1):
        call("load_save", folder=options.folder, save=options.save)
        loaded = time.time()
        call("set_target")
        call("landedvessel_clear")
        call("landedvessel_show_window", visible=False)
        if options.camera:
            call("set_camera", distance=options.camera[0], pitch=options.camera[1])
        if options.shot_at:
            call("wait", seconds=max(0.0, options.shot_at - (time.time() - loaded)))
            call("screenshot", path=os.path.join(out, "%s-load%02d-scene.png" % (options.save, load)),
                 return_image=False)
        call("wait", seconds=max(0.0, options.rest - (time.time() - loaded)))
        parts = [v for v in call("list_vessels")
                 if v["loaded"] and not v["active"] and v["name"] not in options.skip and v["body"]]
        log("load %d" % load)
        for vessel in parts:
            call("set_target", vessel=vessel["id"])
            # The instrument reads its target once per frame.
            call("wait", seconds=0.5)
            line = call("landedvessel_record")
            rows.append(dict(load=load, part=vessel["name"], id=vessel["id"], situation=vessel["situation"],
                             **line))
            log("  %-40s Moved %8s mm  Highest %9s mm" % (vessel["name"], mm(line["MovedMm"]), mm(line["HighestMm"])))
        call("set_target")
        table_screenshot(os.path.join(out, "%s-load%02d-table.png" % (options.save, load)), options.screen_width)

    with open(os.path.join(out, "lines.json"), "w", newline="") as f:
        json.dump(rows, f, indent=1)
    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
