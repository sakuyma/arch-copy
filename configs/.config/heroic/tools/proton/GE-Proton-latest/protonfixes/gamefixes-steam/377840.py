"""Game fix for FINAL FANTASY IX"""

from protonfixes import util


def main() -> None:
    # Fix crackling audio
    util.set_environment('PULSE_LATENCY_MSEC', '60')
