from typing import Union, Any, NamedTuple, Tuple
import platform

from .enums.cross_platform import EnumPlatform, EnumUname, EnumPython
from .enums.win32 import EnumWin32
from .enums.mac import EnumMac
from .enums.unix import EnumLinux, EnumUnix

from dataclasses import dataclass, field


@dataclass
class PlatformUname:
    system: str = field(default=EnumUname.SYSTEM.value)
    node: str = field(default=EnumUname.NODE.value)
    release: str = field(default=EnumUname.RELEASE.value)
    version: str = field(default=EnumUname.VERSION.value)
    machine: str = field(default=EnumUname.MACHINE.value)


def get_platform_uname() -> PlatformUname:
    """Return an initalized PlatformUname instance."""
    _uname: PlatformUname = PlatformUname()

    return _uname


@dataclass
class PlatformPython:
    """Information about the Python implementation for the platform."""

    build: Tuple[str, str] = EnumPython.BUILD.value
    compiler: str = EnumPython.COMPILER.value
    branch: str = EnumPython.BRANCH.value
    implementation: str = EnumPython.IMPLEMENTATION.value
    revision: str = EnumPython.REVISION.value
    version: str = EnumPython.VERSION.value
    version_tuple: Tuple[str, str, str] = EnumPython.VERSION_TUPLE.value


def get_platform_python() -> PlatformPython:
    """Return an initalized PlatformPython instance."""
    _python: PlatformPython = PlatformPython()

    return _python


@dataclass
class PlatformInfoBase:
    """Store cross-platform information gleaned from platform module.

    Platform-specific functionality is implemented in Platform<x> children,
    i.e. PlatformWindowsInfo.

    The parameters in this class are initialized from PlatformEnum by default.
    """

    platform: str = field(default=EnumPlatform.PLATFORM.value)
    platform_terse: str = field(default=EnumPlatform.PLATFORM_TERSE.value)
    platform_aliased: str = field(default=EnumPlatform.PLATFORM_ALIASED.value)
    system: str = field(default=EnumPlatform.SYSTEM.value)
    release: str = field(default=EnumPlatform.RELEASE.value)
    version: str = field(default=EnumPlatform.VERSION.value)
    arch: tuple[str, str] = field(default=EnumPlatform.ARCH.value)
    uname: PlatformUname = field(default_factory=get_platform_uname)
    python: PlatformPython = field(default_factory=get_platform_python)

    def is_linux():
        raise NotImplementedError

    def is_unix():
        raise NotImplementedError

    def is_win():
        raise NotImplementedError

    def is_mac():
        raise NotImplementedError

    def is_32bit():
        raise NotImplementedError

    def is_64bit():
        raise NotImplementedError


@dataclass
class PlatformInfo(PlatformInfoBase):
    pass


@dataclass
class PlatformWinInfo(PlatformInfoBase):
    """Windows-specific platform info."""

    win32_ver: Tuple = field(default=EnumWin32.VERSION.value)
    win32_edition: str = field(default=EnumWin32.EDITION.value)
    win32_is_iot: bool = field(default=EnumWin32.IS_IOT.value)


@dataclass
class PlatformMacInfo(PlatformInfoBase):
    """Mac-specific platform info."""

    mac_ver: Tuple[str] = field(default=EnumMac.VERSION.value)


@dataclass
class PlatformUnixInfo(PlatformInfoBase):
    libc_ver: Tuple[str] = field(default=EnumUnix.LIBC_VER.value)


@dataclass
class PlatformLinuxInfo(PlatformInfoBase):
    os_release: dict[str, str] = field(default_factory=EnumLinux.OS_RELEASE.value)
