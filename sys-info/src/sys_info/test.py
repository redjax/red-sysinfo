import sys

sys.path.append(".")

import platform

from sys_info.domain.platform import PlatformInfo, PlatformWinInfo

if __name__ == "__main__":
    # _platform = PlatformInfo()
    # print(f"Platform: {_platform}")

    _win_platform = PlatformWinInfo()
    print(f"Windows platform: {_win_platform}")
