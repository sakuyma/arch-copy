"""Game fix for Plain Sight"""

from protonfixes import util


def main() -> None:
    """Installs XNA 3.1 to avoid crash when loading levels"""
    util.protontricks('xna31')
