"""Plays the protocol of "Real Solar System: the runway fix": the runway at Cape Canaveral is not at the same
height twice, whatever the height of the ground beside it, and that makes a step on it.

It drives KSP through KSP-Util-MCPServer, a mod that answers HTTP requests on 127.0.0.1, and needs nothing but
Python 3: no AI, no package to install. Start KSP with KSP-Util-MCPServer, KSP Diag - Colliders and KSP Diag -
Terrain Height installed on Real Solar System, wait for the main menu, put the rover's craft file in
saves/<folder>/Ships/SPH, then run:

    python run-runway-fix.py --folder <a new game> --ut 64800 --out out

It starts that game itself from the main menu, in sandbox, then:

0. with --taxi, launches the rover alone, taxis it --taxi metres east along the runway at --taxi-speed, stops
   and reads it there, looks at it from beside, then drives it south off the runway onto the grass, reads it and
   looks at it again, and recovers it: played first, before any other craft is landed, which, kept loaded,
   would keep the floating origin from moving;
1. launches a first rover from the SPH, and parks it on the grass north of the runway, level with the edge
   between the end of the runway (End09) and its fourth section (Section4): the witness of the ground;
2. for each of --launches launches, launches the rover that measures from the SPH onto the runway, drives it to
   just before the fourth section, stops, and saves (F5), then loads that save --reloads times (F9). At each
   load, it reads the witness on the grass, then the rover before the step, looks at its wheels from beside,
   drives across the edge at --cross-speed and stops on the fourth section, reads it there, then backs the rover
   until its back wheels stand on the end of the runway and its front wheels on the fourth section, down the
   step if there is one, which never stops a wheel, and looks at it from beside again, the navball in sight: a
   step between the two sections tilts the rover, nose up when the fourth section stands higher. When the step
   is more than the rover can climb, it looks at the rover stuck against it, then goes round by the grass:
   south down the bank of End09, east on the grass past the edge, north up the bank of Section4, which rises
   from the grass with no step, and on to the same stop on the fourth section;
3. recovers the rover that measures, and launches it again.

With --launches 0, the taxi is all it plays.

A reading is a press on Record in the window of KSP Diag - Terrain Height: the ground under the craft, the
surface the physics touches straight down, and the ground KSP computes for the same spot, in millimetres above
sea level. The witness is read with it as the target, which the window then reads under. Each load adds three
lines to the table, in this order: the grass, before the step, past it. Every --table-every loads, and at the
end of each launch, it shows the window alone and takes a screenshot of the table, then clears it. KSP Diag -
Colliders draws the colliders where the physics has them, in every screenshot of the rover: the step is seen
there. Nothing is written to the log.

It writes every reading to readings.json, prints them, ends at the space centre, and leaves KSP running (unless
--quit is given). The pitch it prints is read from KSP-Util-MCPServer, only to follow the run: the navball of the
screenshot is what shows it.
"""
import argparse
import json
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "scene-changes"))
import common  # noqa: E402
from common import call, close, log  # noqa: E402

# The runway at Cape Canaveral runs east along this latitude from its 09 end, where a craft launched from the SPH
# appears. Read with KSP Diag - Colliders on 2026-10-11: with the rover's centre at EDGE_LONGITUDE, its wheels stand
# on both End09 and Section4.
RUNWAY_LATITUDE = 28.612855
EDGE_LONGITUDE = -80.615353

# Where the rover that measures stops, in metres east of the edge: before it, with all its wheels on End09; past
# it, with all its wheels on Section4. The rover is about 4 m long.
BEFORE_EDGE = -8.0
PAST_EDGE = 10.0

# Where the witness is parked, in metres north of the runway's axis: on the grass, past the bank, which ends
# about 58 m from the axis on that side.
WITNESS_NORTH = 70.0

# The way round by the grass, from 8 m before the edge, as legs of a heading and a distance in metres, each turning
# as it goes, as driven on 2026-10-11; then a drive to the stop past the edge. South of the runway, west of the
# edge, the shoulder and the bank belong to End09; east of it, to Section4, whose bank rises from the grass with no
# step. Section4 is bordered by End09 on its other sides, with the same step as at the edge. A drive to a point
# turning this much would see no progress while it turns, and stop as if stuck.
ROUND_BY_THE_GRASS = [
    (180.0, 64.0),   # south, down the bank of End09, onto the grass 66 m from the axis
    (90.0, 25.0),    # east on the grass, past the edge
    (0.0, 54.0),     # north, up the bank of Section4, onto it 11 m from the axis
]

# The runway's heading, from its 09 end: the rover drives along it from one stop to the next. A drive to a point
# this close would steer to make up a few centimetres sideways, and leave the rover askew.
RUNWAY_HEADING = 90.0

# How far south the rover leaves the runway at the end of the taxi, in metres: past the bank, onto the grass, as
# for the witness on the other side.
OFF_THE_RUNWAY = 80.0

OPTIONS = None


def longitude_at(metres):
    """The longitude of the point of the runway <metres> east of the edge."""
    radius = OPTIONS.radius * math.cos(math.radians(RUNWAY_LATITUDE))
    return EDGE_LONGITUDE + math.degrees(metres / radius)


def drive_to(latitude, longitude):
    """Drives the rover to a point and stops there, brakes on, or where it gets stuck. Returns why it stopped:
    "arrived", or "stalled" when stuck."""
    return call("drive_to", latitude=latitude, longitude=longitude, speed=OPTIONS.speed)["stoppedBecause"]


def drive(heading, metres, speed=None, reverse=False):
    """Drives the rover <metres> along <heading>, backing away when <reverse>, its front facing the heading, and
    stops there, brakes on, or where it gets stuck. Returns why it stopped: "distance", or "stalled" when stuck."""
    return call("drive", heading=heading, speed=speed or OPTIONS.speed, distance=metres,
                reverse=reverse)["stoppedBecause"]


class Run:
    """The readings of the protocol, in the order they are taken, and the screenshots."""

    def __init__(self, out):
        self.out = out
        self.readings = []
        self.shots = 0
        self.witness = None

    def save(self):
        with open(os.path.join(self.out, "readings.json"), "w", newline="") as f:
            json.dump(self.readings, f, indent=1)

    def record(self, what, launch, load, route=None):
        """Lets the rover settle, then presses Record in the window of KSP Diag - Terrain Height, under the
        witness when <what> is "grass", under the rover that measures otherwise. Returns the line recorded."""
        call("wait", seconds=OPTIONS.settle)
        if what == "grass":
            call("set_target", vessel=self.witness)
        line = call("terrainheight_record")
        if what == "grass":
            call("set_target")
        vessel = call("get_state").get("vessel", {})
        self.readings.append({"launch": launch, "load": load, "what": what, "route": route, "line": line,
                              "pitch": vessel.get("pitch"), "heading": vessel.get("heading")})
        self.save()
        above = line["CollisionSurfaceMm"] - line["ComputedTerrainMm"]
        log("launch %d load %2d %-7s ground under craft %.3f mm, KSP computes %.3f mm: %+.3f mm%s" % (
            launch, load, what, line["CollisionSurfaceMm"], line["ComputedTerrainMm"], above,
            ", " + route if route else ""))
        return line

    def shoot(self, name, launch, load):
        """Takes a screenshot from beside the rover that measures, the colliders drawn, no window shown."""
        self.shots += 1
        path = os.path.join(self.out, "%03d-launch%d-load%02d-%s.png" % (self.shots, launch, load, name))
        call("set_camera", distance=OPTIONS.camera_distance, heading=OPTIONS.camera_heading,
             pitch=OPTIONS.camera_pitch)
        call("wait", seconds=2)
        call("screenshot", path=path, return_image=False)
        vessel = call("get_state").get("vessel", {})
        log("screenshot %s, heading %.1f, pitch %+.2f deg" % (os.path.basename(path), vessel.get("heading"),
                                                            vessel.get("pitch")))

    def shoot_table(self, launch, load):
        """Takes a screenshot of the table of KSP Diag - Terrain Height, its window alone, then clears it."""
        self.shots += 1
        path = os.path.join(self.out, "%03d-launch%d-load%02d-table.png" % (self.shots, launch, load))
        call("terrainheight_show_window", visible=True)
        call("wait", seconds=1)
        call("screenshot", path=path, return_image=False)
        call("terrainheight_show_window", visible=False)
        call("terrainheight_clear")
        log("screenshot %s" % os.path.basename(path))


def park_witness(run, options):
    """Launches the witness and parks it on the grass north of the runway, level with the edge. The sections are off
    just after a launch, so nothing stops it on the runway."""
    call("launch_vessel", craft=options.craft, site="Runway")
    common.brake()
    run.witness = call("get_state")["vessel"]["id"]
    drive_to(RUNWAY_LATITUDE, EDGE_LONGITUDE)
    drive(0.0, WITNESS_NORTH)
    vessel = call("get_state")["vessel"]
    log("witness parked at %.6f, %.6f" % (vessel["latitude"], vessel["longitude"]))
    call("go_to_scene", scene="SPACECENTER")


def cross(run, launch, load):
    """Takes the rover that measures from before the step to past it, across, or round by the grass when the step
    is more than it can climb. Returns the way it went."""
    if not OPTIONS.round_by_the_grass:
        if drive(RUNWAY_HEADING, PAST_EDGE - BEFORE_EDGE, speed=OPTIONS.cross_speed) != "stalled":
            return "across"
        run.shoot("stuck", launch, load)
        log("launch %d load %d: stuck against the step, round by the grass" % (launch, load))
        # Back to where the way round starts, 8 m before the edge.
        drive_to(RUNWAY_LATITUDE, longitude_at(BEFORE_EDGE))
    for heading, metres in ROUND_BY_THE_GRASS:
        if drive(heading, metres) == "stalled":
            raise RuntimeError("stuck on the way round by the grass, heading %g" % heading)
    # Facing along the runway again, east of the stop, then back to it: the rover then backs onto the edge as when
    # it crosses.
    drive(RUNWAY_HEADING, 20.0)
    if drive_to(RUNWAY_LATITUDE, longitude_at(PAST_EDGE)) == "stalled":
        raise RuntimeError("stuck on the way from the bank of Section4 to the stop past the edge")
    return "by the grass"


def taxi(run, options):
    """Launches the rover onto the runway, the only craft of the game, taxis it along the runway and reads it there,
    then drives it off the runway onto the grass and reads it again, with a look from beside at each stop and a
    screenshot of the table at the end. Starts and ends at the space centre."""
    # Played before the witness is parked: a landed craft kept loaded would keep the floating origin from moving.
    launch = 0
    call("launch_vessel", craft=options.craft, site="Runway")
    common.brake()
    call("colliders_show_window", visible=False)
    call("terrainheight_show_window", visible=False)
    call("terrainheight_clear")
    stopped = drive(RUNWAY_HEADING, options.taxi, speed=options.taxi_speed)
    run.record("taxied", launch, 0, "%.0f m east, %s" % (options.taxi, stopped))
    run.shoot("taxied", launch, 0)
    stopped = drive(180.0, OFF_THE_RUNWAY)
    run.record("off", launch, 0, "%.0f m south, %s" % (OFF_THE_RUNWAY, stopped))
    run.shoot("off", launch, 0)
    run.shoot_table(launch, 0)
    call("recover_vessel")
    close(dialogs_only=False)


def main():
    global OPTIONS
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--folder", required=True, help="the new game to start, under saves/")
    parser.add_argument("--craft", default="SPH/Diag2-Rover.craft",
                        help="the rover, both of them, as SPH/<name>.craft (default SPH/Diag2-Rover.craft)")
    parser.add_argument("--launches", type=int, default=3, help="how many times to launch the rover (default 3)")
    parser.add_argument("--reloads", type=int, default=10,
                        help="loads of the save made before the fourth section at each launch (default 10)")
    parser.add_argument("--table-every", type=int, default=4,
                        help="loads between two screenshots of the table of KSP Diag - Terrain Height: three lines a "
                             "load, and twelve still fit on a screen of 720 pixels (default 4)")
    parser.add_argument("--cross-speed", type=float, default=2.0,
                        help="speed at which the rover crosses the edge, in metres per second (default 2)")
    parser.add_argument("--round-by-the-grass", action="store_true",
                        help="go round by the grass at every load, without trying to cross: to try the way round")
    parser.add_argument("--taxi", type=float, default=0.0,
                        help="metres to taxi east along the runway after the last load of each launch (default 0)")
    parser.add_argument("--taxi-speed", type=float, default=8.0, help="speed of the taxi, in metres per second")
    parser.add_argument("--settle", type=float, default=5.0, help="seconds to let the rover settle at each stop")
    parser.add_argument("--speed", type=float, default=2.0, help="top speed of the other drives, in metres per second")
    parser.add_argument("--radius", type=float, default=6371000.0, help="the radius of the body, in metres (Earth's)")
    parser.add_argument("--ut", type=float, help="the universal time to start at, in seconds, for daylight at the KSC")
    parser.add_argument("--camera-distance", type=float, default=12.0, help="metres from the rover")
    parser.add_argument("--camera-heading", type=float, default=0.0, help="degrees; 0 looks at the rover from beside")
    parser.add_argument("--camera-pitch", type=float, default=5.0, help="degrees")
    parser.add_argument("--out", default="out", help="where readings.json and the screenshots go")
    parser.add_argument("--port", type=int, default=8770, help="the port of KSP-Util-MCPServer")
    parser.add_argument("--quit", action="store_true", help="quit KSP at the end")
    parser.add_argument("--keep-running", action="store_true",
                        help="leave KSP running at the end, which it does unless --quit is given")
    options = parser.parse_args()
    common.URL = "http://127.0.0.1:%d/mcp/" % options.port
    OPTIONS = options
    out = os.path.abspath(options.out)
    os.makedirs(out, exist_ok=True)
    run = Run(out)

    call("new_game", folder=options.folder, mode="SANDBOX")
    close(dialogs_only=True)
    if options.ut is not None:
        call("set_time", ut=options.ut)
    if options.taxi:
        taxi(run, options)
    if options.launches:
        park_witness(run, options)

    for launch in range(1, options.launches + 1):
        call("launch_vessel", craft=options.craft, site="Runway")
        common.brake()
        # Only the colliders drawn in the screenshots of the rover, no window.
        call("colliders_show_window", visible=False)
        call("terrainheight_show_window", visible=False)
        call("terrainheight_clear")
        drive_to(RUNWAY_LATITUDE, longitude_at(BEFORE_EDGE))
        before = "runway-fix-launch%d-before-section4" % launch
        call("save_game", save=before)
        if options.reloads == 0:
            run.record("before", launch, 0)
            run.shoot("before", launch, 0)
            run.shoot_table(launch, 0)
        for load in range(1, options.reloads + 1):
            call("load_save", save=before, folder=options.folder)
            run.record("grass", launch, load)
            run.record("before", launch, load)
            run.shoot("before", launch, load)
            route = cross(run, launch, load)
            run.record("past", launch, load, route)
            drive(RUNWAY_HEADING, PAST_EDGE, reverse=True)
            call("wait", seconds=options.settle)
            run.shoot("astride", launch, load)
            if load % options.table_every == 0 or load == options.reloads:
                run.shoot_table(launch, load)

        call("recover_vessel")
        close(dialogs_only=False)

    log("done: %d readings, in %s" % (len(run.readings), out))
    if options.quit:
        call("quit_game")


if __name__ == "__main__":
    main()
