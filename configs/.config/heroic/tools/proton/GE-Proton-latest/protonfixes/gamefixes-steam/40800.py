"""Game fix for Super Meat Boy"""

#
from protonfixes import util


def main() -> None:
    """Installs d3dcompiler, xact"""
    util.protontricks('d3dcompiler_47')
    util.protontricks('xact')
