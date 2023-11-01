from __future__ import annotations

import sys

sys.path.append(".")

from sys_info.domain.platform import PlatformInfo
from sys_info.utils.platform_utils import get_platform

## Initialize platform object
PLATFORM: PlatformInfo = get_platform()


if __name__ == "__main__":
    print(f"Platform:\n{PLATFORM}")
