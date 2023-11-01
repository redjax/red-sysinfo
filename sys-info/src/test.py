from __future__ import annotations

import sys

sys.path.append(".")

import platform

from sys_info import PLATFORM
from sys_info.domain.platform import PlatformInfo, PlatformPython, PlatformUname
from sys_info.utils.platform_utils import get_platform

def test_platform(platform: PlatformInfo = PLATFORM) -> None:
    _dict = platform.as_dict()
    _python = platform.python
    _python_dict = _python.as_dict()
    _uname = platform.uname
    _uname_dict = _uname.as_dict()

    print(f"--- [Main Platform Object] - {type(platform)}\n")
    print(platform)

    print(f"\n--- [Dict Repr] - {type(_dict)}\n")
    print(_dict)

    print(f"\n--- [Python] - {type(_python)}\n")
    print(_python)

    print(f"\n--- [Python Dict Repr] - {type(_python_dict)}\n")
    print(_python_dict)

    print(f"\n--- [Uname] - {type(_uname)}\n")
    print(_uname)

    print(f"\n--- [Uname Dict] - {type(_uname_dict)}\n")
    print(_uname_dict)


if __name__ == "__main__":
    # print(f"Platform:\n\n{PLATFORM}")
    print(f"Is Windows: {PLATFORM.is_win()}")
    print(f"Is Unix: {PLATFORM.is_unix()}")
    print(f"Is Linux: {PLATFORM.is_linux()}")
    print(f"Is Mac: {PLATFORM.is_mac()}")

    print(f"Is 32-bit: {PLATFORM.is_32bit()}")
    print(f"Is 64-bit: {PLATFORM.is_64bit()}")

    print("\n")

    print(f"Python info: {PLATFORM.python}")

    print("\n")

    test_platform()
