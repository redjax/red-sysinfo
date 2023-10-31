from typing import NamedTuple, Tuple
from enum import Enum
import platform


class EnumUnix(Enum):
    LIBC_VER: Tuple[str] = platform.libc_ver()


class EnumLinux(Enum):
    OS_RELEASE: dict[str, str] = platform.freedesktop_os_release()
