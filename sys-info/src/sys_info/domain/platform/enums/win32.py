from typing import NamedTuple, Tuple
from enum import Enum
import platform


class EnumWin32(Enum):
    VERSION: Tuple[str] = platform.win32_ver()
    EDITION: str = platform.win32_edition()
    IS_IOT: bool = platform.win32_is_iot()
