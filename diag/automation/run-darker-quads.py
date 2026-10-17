"""Plays the test of "BurstPQS: darker quads on the Mun": the flight of ref-mune-5km, filmed in screenshots.

It drives KSP through KSP-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start a fresh KSP with KSP-MCPServer installed, copy ref-mune-5km.sfs
into a sandbox game, wait for the main menu, then run:

    python run-darker-quads.py --folder <your sandbox game> --save ref-mune-5km --out out
    python run-darker-quads.py --folder <your sandbox game> --save ref-mune-5km --distance 80000 --out out

It loads the save once, sets the camera as asked as soon as the flight shows (left as the game opens it when
no option is given), then takes a screenshot every --every seconds for --duration seconds, counted from the end
of the load: shot-<seconds>s.png in --out. lines.json lists each screenshot with when it was taken and where the
camera and the vessel were. It never saves the game, and quits KSP at the end (unless --keep-running is given).
"""
import argparse
import json
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


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ the save was copied into")
    parser.add_argument("--save", default="ref-mune-5km", help="the save, without .sfs")
    parser.add_argument("--distance", type=float, help="metres from the vessel to put the camera at")
    parser.add_argument("--heading", type=float, help="degrees, the direction the camera looks in")
    parser.add_argument("--pitch", type=float, help="degrees")
    parser.add_argument("--every", type=float, default=5, help="seconds between two screenshots")
    parser.add_argument("--duration", type=float, default=300, help="seconds into the flight of the last one")
    parser.add_argument("--out", default="out", help="where the screenshots and lines.json go")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-MCPServer")
    parser.add_argument("--keep-running", action="store_true", help="leave KSP running at the end")
    options = parser.parse_args()
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    out = os.path.abspath(options.out)
    os.makedirs(out, exist_ok=True)

    # KSP-MCPServer loads a save from the space centre or in flight only, as a player does: from the main
    # menu, the game is opened at the space centre first.
    if call("get_state")["scene"] == "MAINMENU":
        call("open_game", folder=options.folder)
    call("load_save", folder=options.folder, save=options.save)
    # The moments are counted from the end of the load, as a player counts them from the flight showing.
    start = time.time()
    camera = {k: getattr(options, k) for k in ("distance", "heading", "pitch") if getattr(options, k) is not None}
    camera = call("set_camera", **camera)
    log("  camera", json.dumps(camera))

    rows = []
    moment = 0.0
    while moment <= options.duration:
        while time.time() - start < moment:
            time.sleep(min(1.0, moment - (time.time() - start)))
        seconds = time.time() - start
        name = "shot-%03ds.png" % round(moment)
        call("screenshot", path=os.path.join(out, name), return_image=False)
        state = call("get_state")
        vessel = state.get("vessel") or {}
        rows.append(dict(shot=name, seconds=round(seconds, 1), camera=call("set_camera"),
                         latitude=vessel.get("latitude"), longitude=vessel.get("longitude"),
                         altitude=vessel.get("altitude"), localTime=state.get("localTime")))
        with open(os.path.join(out, "lines.json"), "w", newline="") as f:
            json.dump(rows, f, indent=1)
        log("  %s  %6.1f s" % (name, seconds))
        moment += options.every

    log("done")
    if not options.keep_running:
        call("quit_game")


if __name__ == "__main__":
    main()
