"""Oddworld: Abe's Oddysee"""

from protonfixes import util


def main() -> None:
    util.protontricks('cnc_ddraw')  # Videos are laggy without this
