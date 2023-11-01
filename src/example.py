from __future__ import annotations

import sys

sys.path.append(".")

import platform

from red_sys import PLATFORM
from red_sys.domain.platform import (
    PlatformInfo,
    PlatformPython,
    PlatformUname,
    print_platform,
)

if __name__ == "__main__":
    print_platform(p=PLATFORM)
