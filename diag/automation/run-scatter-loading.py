"""Plays "The protocol: the scatter, load after load" with KSP Diag - Scatter installed.

It drives KSP through KSP-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-MCPServer and KSP Diag - Scatter installed, terrain
scatter on and LOG_INSTANT_FLUSH = True in settings.cfg, copy the save into a sandbox game, wait for the main
menu, then run:

    python run-scatter-loading.py --folder <your sandbox game> --save reference-kerbin --loads 12 --out out

For each loading it does what the protocol asks a player to do, in the same order: load the save, press Record
the rocks, and press it again while holders are not built yet or the counts still change. The records go to
KSP.log; lines.json lists, load by load, the number and the closing line of the last record, the one the
protocol keeps (extract-scatter-records.py copies those records out of KSP.log). With --scene-shots, a
screenshot of the scene is taken after each last record, the window hidden, the interface too, and the flight
camera set by --camera if it is given, so that every picture is taken from the same viewpoint. It never saves the game, and quits
KSP at the end (unless --keep-running is given).
"""
import argparse
import json
import os
import re
import time
import urllib.request

URL = None

# The closing line of a record of the rocks.
CLOSING = re.compile(r"End of record (\d+): (\d+) quads with rocks, (\d+) holders \((\d+) not built yet\);"
                     r" nearest quad '([^']*)': (\d+) rocks, (\d+) vertices measured")


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


def record_once_settled(attempts, pause):
    """Presses Record the rocks until a record has every holder built and the same counts as the one before it,
    as the protocol asks. Returns the closing line of the last record and whether it settled."""
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


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ the save was copied into")
    parser.add_argument("--save", required=True, help="the save, without .sfs")
    parser.add_argument("--loads", type=int, default=12, help="how many loadings")
    parser.add_argument("--out", default="out", help="where lines.json and the screenshots go")
    parser.add_argument("--attempts", type=int, default=20, help="records at most per loading")
    parser.add_argument("--pause", type=float, default=3, help="seconds between two records of a loading")
    parser.add_argument("--scene-shots", action="store_true", help="a screenshot of the scene after each loading")
    parser.add_argument("--camera", type=float, nargs=4, metavar=("DISTANCE", "HEADING", "PITCH", "FOV"),
                        help="the flight camera for the screenshots: metres, and degrees")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-MCPServer")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    os.makedirs(options.out, exist_ok=True)

    rows = []
    # KSP-MCPServer loads a save from the space centre or in flight only, as a player does: from the main
    # menu, the game is opened at the space centre first.
    if call("get_state")["scene"] == "MAINMENU":
        call("open_game", folder=options.folder)
    for load in range(1, options.loads + 1):
        state = call("load_save", folder=options.folder, save=options.save)
        if load == 1:
            call("scatter_show_window", visible=False)
        call("wait", seconds=3)
        line, settled = record_once_settled(options.attempts, options.pause)
        match = CLOSING.search(line or "")
        row = dict(load=load, situation=state["vessel"]["situation"], settled=settled, closing=line,
                   record=int(match.group(1)) if match else None)
        if options.scene_shots:
            call("set_ui", visible=False)
            if options.camera:
                distance, heading, pitch, fov = options.camera
                call("set_camera", distance=distance, heading=heading, pitch=pitch, fov=fov)
                call("wait", seconds=1)
            name = "%s-load%d.png" % (options.save, load)
            call("screenshot", path=os.path.join(os.path.abspath(options.out), name), return_image=False)
        rows.append(row)
        # Written at every loading, so that a run cut short keeps what it read.
        with open(os.path.join(options.out, "lines.json"), "w", newline="") as f:
            json.dump(rows, f, indent=1)
        log("  load %d  %s%s" % (load, line, "" if settled else "  (NOT SETTLED)"))

    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
