"""Plays the protocol of "The scatter holders" with KSP Diag - Scatter installed: the holder pools over a flight,
or across scene switches.

It drives KSP through KSP-Util-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-Util-MCPServer and KSP Diag - Scatter installed, terrain
scatter on and LOG_INSTANT_FLUSH = True in settings.cfg, copy the saves into a sandbox game, wait for the main
menu, then run one of:

    python run-scatter-holders.py flight --folder <your sandbox game> --out out
    python run-scatter-holders.py scenes --folder <your sandbox game> --out out

flight loads ref-mune-5km and presses Record the holder pools 30 s into the flight, then every two minutes, as
many times as --records says, then once more after the crash. scenes opens the game at the Space Center, loads
reference-mune and presses it once the terrain has settled, goes back to the Space Center and presses it there,
then loads reference-kerbin and presses it once the terrain has settled. The records go to KSP.log; lines.json
lists the number and the closing line of each. It never saves the game, and quits KSP at the end (unless
--keep-running is given).
"""
import argparse
import json
import os
import re
import time
import urllib.request

URL = None

CLOSING = re.compile(r"End of holder record (\d+):")


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


def record(tag, rows, out, **extra):
    line = call("scatter_record_holders")
    match = CLOSING.search(line or "")
    rows.append(dict(load=1, tag=tag, closing=line, record=int(match.group(1)) if match else None, **extra))
    with open(os.path.join(out, "lines.json"), "w", newline="") as f:
        json.dump(rows, f, indent=1)
    log("  %-12s %s" % (tag, line))


def wait_for_terrain(attempts=20, pause=3):
    """Waits for the terrain to settle, as a player does before pressing: the counts of a record of the rocks
    the same twice in a row, every holder built."""
    previous = None
    for _ in range(attempts):
        line = call("scatter_record_rocks")
        match = re.search(r"(\d+) quads with rocks, (\d+) holders \((\d+) not built yet\)", line or "")
        if match:
            if match.group(3) == "0" and match.groups() == previous:
                return
            previous = match.groups()
        call("wait", seconds=pause)


def flight(options, rows):
    # KSP-Util-MCPServer loads a save from the space centre or in flight only, as a player does: from the main
    # menu, the game is opened at the space centre first.
    if call("get_state")["scene"] == "MAINMENU":
        call("open_game", folder=options.folder)
    call("load_save", folder=options.folder, save=options.save)
    start = time.time()
    call("scatter_show_window", visible=False)
    for number in range(1, options.records + 1):
        moment = options.first + (number - 1) * options.every
        while time.time() - start < moment:
            time.sleep(min(1.0, moment - (time.time() - start)))
        record("record%d" % number, rows, options.out, seconds=round(time.time() - start, 1))

    # The pod flies into the relief. The game keeps the dead vessel as the active one, frozen where it died, and
    # pauses a while later to show the flight results: a vessel gone, or one whose position no longer changes
    # while the game runs, has crashed.
    limit = time.time() + options.crash_timeout
    last = None
    while True:
        state = call("get_state")
        vessel = state.get("vessel")
        if vessel is None:
            break
        where = (vessel["latitude"], vessel["longitude"], vessel["altitude"])
        if not state["paused"]:
            if where == last:
                break
            last = where
        if time.time() > limit:
            raise RuntimeError("no crash within %d s of the last record" % options.crash_timeout)
        time.sleep(2)
    if call("get_state")["paused"]:
        call("set_pause", paused=False)
    log("  crashed %.1f s into the flight" % (time.time() - start))
    call("wait", seconds=5)
    record("crash", rows, options.out, seconds=round(time.time() - start, 1))


def scenes(options, rows):
    call("open_game", folder=options.folder)
    call("load_save", folder=options.folder, save=options.mun_save)
    call("scatter_show_window", visible=False)
    call("wait", seconds=3)
    wait_for_terrain()
    record("mun", rows, options.out)
    call("go_to_scene", scene="SPACECENTER")
    call("wait", seconds=5)
    record("spacecenter", rows, options.out)
    call("load_save", folder=options.folder, save=options.kerbin_save)
    call("wait", seconds=3)
    wait_for_terrain()
    record("kerbin", rows, options.out)


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("case", choices=["flight", "scenes"])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ the saves were copied into")
    parser.add_argument("--save", default="ref-mune-5km", help="flight: the save, without .sfs")
    parser.add_argument("--mun-save", default="reference-mune", help="scenes: the save on the Mun, without .sfs")
    parser.add_argument("--kerbin-save", default="reference-kerbin", help="scenes: the save on Kerbin, without .sfs")
    parser.add_argument("--records", type=int, default=5, help="flight: records before the crash, two minutes apart")
    parser.add_argument("--first", type=float, default=30, help="flight: seconds into the flight of the first record")
    parser.add_argument("--every", type=float, default=120, help="flight: seconds between two records")
    parser.add_argument("--crash-timeout", type=float, default=1200,
                        help="flight: seconds to wait for the crash after the last record")
    parser.add_argument("--out", default="out", help="where lines.json goes")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-Util-MCPServer")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    os.makedirs(options.out, exist_ok=True)

    rows = []
    if options.case == "flight":
        flight(options, rows)
    else:
        scenes(options, rows)
    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
