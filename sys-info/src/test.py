import sys

sys.path.append(".")

from sys_info.utils.platform_utils import get_platform
from sys_info import PLATFORM

if __name__ == "__main__":
    print(f"Platform:\n\n{PLATFORM}")
