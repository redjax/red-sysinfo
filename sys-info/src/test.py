import sys

sys.path.append(".")

import platform

from sys_info.utils.platform_utils import get_platform
from sys_info import PLATFORM

if __name__ == "__main__":
    # print(f"Platform:\n\n{PLATFORM}")
    # print(f"Is Windows: {PLATFORM.is_win()}")
    # print(f"Is Unix: {PLATFORM.is_unix()}")
    # print(f"Is Linux: {PLATFORM.is_linux()}")
    # print(f"Is Mac: {PLATFORM.is_mac()}")

    # print(f"Is 32-bit: {PLATFORM.is_32bit()}")
    # print(f"Is 64-bit: {PLATFORM.is_64bit()}")

    # print(f"Python info: {PLATFORM.python}")

    # print(PLATFORM.python)

    print(PLATFORM.as_dict())
