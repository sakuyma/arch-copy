"""Game fix for Horizon Zero Dawn"""

from protonfixes import util


def main() -> None:
    # C++ runtime is not provided in the manifest
    util.protontricks('vcrun2022')
    # Set SteamGameId so that non-steam versions can pick up steam-specific fixes in proton's wine code
    util.set_environment('SteamGameId', '1151640')
