"""Plays "The protocol: a launch pad of Making History".

It drives KSP through KSP-Util-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Install KSP-Util-MCPServer and KSP Diag - Terrain Height in a KSP that has
the Making History expansion, copy Capsule.craft into the Ships/VAB folder of a sandbox game, make sure KSP is
not running, then run:

    python run-launch-pad.py --folder <your sandbox game> --launches 6 --out out

It starts the KSP of the environment variable KSPDIR, or the one given with --ksp <KSP folder>.

The launch pad sets itself on the ground once per session of the game, so each launch is played in a
session of its own, as the protocol asks a player to do: start KSP, open the game, set a time of day in
daylight at the launch site, launch the craft from the Desert Launch Site, wait for the digits to stop
moving, record, take a screenshot of the table and one of a foot of the launch pad, quit KSP. It keeps the KSP.log of each session, prints
what it read, and writes it to lines.json.
"""
import argparse
import json
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.request

URL = None


def call(tool, http_timeout=900, **args):
    """Calls one tool of KSP-Util-MCPServer and returns its answer, decoded from JSON when it is JSON."""
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": tool, "arguments": args}}).encode()
    request = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=http_timeout) as response:
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


def running():
    out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq KSP_x64.exe"], capture_output=True, text=True).stdout
    return "KSP_x64.exe" in out


def start_game(ksp):
    """Starts KSP and waits for its main menu."""
    if running():
        raise RuntimeError("KSP is already running")
    subprocess.Popen([os.path.join(ksp, "KSP_x64.exe")], cwd=ksp)
    start = time.time()
    while time.time() - start < 900:
        try:
            if call("get_state", http_timeout=10).get("scene") == "MAINMENU":
                return
        except (urllib.error.URLError, ConnectionError, OSError, RuntimeError):
            pass
        time.sleep(5)
    raise RuntimeError("no main menu after 900 s")


def quit_game(ksp, log_copy):
    """Quits KSP, waits for it to end, and keeps its KSP.log, which the next start overwrites."""
    try:
        call("quit_game", http_timeout=30)
    except Exception:
        pass
    for _ in range(120):
        if not running():
            break
        time.sleep(1)
    shutil.copy2(os.path.join(ksp, "KSP.log"), log_copy)


def wait_for_digits_to_settle():
    """What the protocol asks: wait for the ground under the craft to stop moving (within 0.0005 mm over 2 s)."""
    last = None
    still = 0
    start = time.time()
    while time.time() - start < 30 and still < 4:
        value = call("terrainheight_read")["live"]["CollisionSurfaceMm"]
        still = still + 1 if last is not None and value is not None and abs(value - last) < 0.0005 else 0
        last = value
        time.sleep(0.5)


def main():
    global URL
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ksp", default=os.environ.get("KSPDIR"),
                        help="the KSP folder (default: the environment variable KSPDIR)")
    parser.add_argument("--folder", required=True, help="the sandbox game under saves/ holding the craft")
    parser.add_argument("--craft", default="VAB/Capsule.craft", help="the craft, relative to the Ships folder")
    parser.add_argument("--site", default="Desert_Launch_Site", help="the launch site")
    parser.add_argument("--launches", type=int, default=6, help="how many launches, one session each")
    parser.add_argument("--ut", type=float, default=48955.0,
                        help="the time of the first launch, in seconds; daytime at the Desert Launch Site")
    parser.add_argument("--step", type=float, default=317.0, help="seconds of game time between two launches")
    parser.add_argument("--out", default="out", help="where lines.json, the screenshots and the logs go")
    parser.add_argument("--screen-width", type=float, default=1280, help="the width of KSP's window, in pixels")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-Util-MCPServer")
    options = parser.parse_args()
    if not options.ksp:
        parser.error("give the KSP folder with --ksp, or in KSPDIR")
    URL = "http://127.0.0.1:%d/mcp/" % options.port
    out = os.path.abspath(options.out)
    os.makedirs(out, exist_ok=True)

    rows = []
    for launch in range(1, options.launches + 1):
        start_game(options.ksp)
        call("open_game", folder=options.folder)
        # Daylight at the launch site, for the screenshot of the foot.
        call("set_time", ut=options.ut + (launch - 1) * options.step)
        call("launch_vessel", craft=options.craft, site=options.site)
        call("terrainheight_clear")
        call("terrainheight_show_window", visible=False)
        call("wait", seconds=3)
        wait_for_digits_to_settle()
        line = call("terrainheight_record")
        rows.append(dict(launch=launch, ut=call("get_state")["ut"], terrain_height=line))
        log("launch %d: ground under craft %.3f mm, ground KSP computes %.3f mm"
            % (launch, line["CollisionSurfaceMm"], line["ComputedTerrainMm"]))

        # The table, the window alone in the middle of the screen.
        call("terrainheight_show_window", visible=True)
        size = call("terrainheight_move_window", x=0, y=60)
        call("terrainheight_move_window", x=(options.screen_width - size["width"]) / 2, y=60)
        call("wait", seconds=1)
        call("screenshot", path=os.path.join(out, "launch-%d-table.png" % launch), return_image=False)
        call("terrainheight_show_window", visible=False)

        # A foot of the launch pad, the one nearest the camera, from the south-west of the craft.
        call("set_ui", visible=False)
        call("set_camera", distance=40, heading=45, pitch=3, fov=12, aim_heading=0, aim_pitch=6)
        call("wait", seconds=1)
        call("screenshot", path=os.path.join(out, "launch-%d-foot.png" % launch), return_image=False)

        quit_game(options.ksp, os.path.join(out, "launch-%d-KSP.log" % launch))

    with open(os.path.join(out, "lines.json"), "w", newline="") as f:
        json.dump(rows, f, indent=1)
    log("done")


if __name__ == "__main__":
    main()
