"""Quit to Main Menu, the game resumed at the space centre, and loaded back into the flight of the craft.

Leaving for the main menu saves the game as persistent, with the craft on the launchpad. Resume Game opens that
save at the space centre, as it does for a player, and loading it there opens the flight on the craft. After it,
KSP no longer reverts the flight.
"""
import sys

import common
from common import call


def play(session):
    call("go_to_scene", scene="MAINMENU")
    session.shoot("main-menu")
    call("open_game", folder=session.options.folder)
    common.at_space_centre()
    call("load_save", folder=session.options.folder, save="persistent")
    session.arrived("loaded from the space centre, after the main menu")


if __name__ == "__main__":
    common.run_alone(sys.modules[__name__])
