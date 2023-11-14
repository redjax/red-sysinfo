from __future__ import annotations

import sys

sys.path.append(".")

from red_sysinfo import PLATFORM, print_platform
from red_sysinfo.domain.userinfo import UserInfo

if __name__ == "__main__":
    print_platform(p=PLATFORM)

    print(f"User info: {UserInfo()}")
    print(f"User info (dict): {UserInfo().as_dict()}")
