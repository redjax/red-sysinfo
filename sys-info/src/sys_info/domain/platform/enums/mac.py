from typing import NamedTuple, Tuple
from enum import Enum
import platform


class EnumMac(Enum):
    VERSION: Tuple[str] = platform.mac_ver()
