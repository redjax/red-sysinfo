from __future__ import annotations

import sys

sys.path.append(".")

import pytest

from src.red_sysinfo import PLATFORM
from src.red_sysinfo.domain.enums.platform import (
    EnumLinux,
    EnumMac,
    EnumPlatform,
    EnumPython,
    EnumSystemTypes,
    EnumUname,
    EnumUnix,
    EnumWin32,
)
from src.red_sysinfo.domain.platform import PlatformInfo


@pytest.mark.platform
def test_platform_not_null(platform_info: PlatformInfo):
    assert platform_info is not None, "platform_info object should not be None"


@pytest.mark.platform
def test_platform_is_platforminfo(platform_info: PlatformInfo):
    assert isinstance(
        platform_info, PlatformInfo
    ), f"platform_info object should be of type red_sys.PlatformInfo, not {type(platform_info)}"


@pytest.mark.platform
def test_platform_dict_not_null(platform_dict: dict):
    assert platform_dict is not None, "platform_dict should not be None"


@pytest.mark.platform
def test_platform_dict_is_dict(platform_dict: dict):
    assert isinstance(
        platform_dict, dict
    ), f"platform_dict should be of type dict, not {type(platform_dict)}"


@pytest.mark.platform
def test_system_str_is_valid(platform_info: PlatformInfo, system_types: list[str]):
    assert (
        platform_info.system in system_types
    ), f"System should be one of [{system_types}], not {platform_info.system}"


@pytest.mark.platform
def test_arch_is_valid(platform_info: PlatformInfo):
    assert (
        "32bit" or "64bit" in platform_info.arch
    ), f"Architecture string should contain '32bit' or '64bit'. Invalid architecture string: {platform_info.arch}"
