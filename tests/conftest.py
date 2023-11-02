## https://www.guru99.com/pytest-tutorial.html
#  This file is loaded by pytest. Anything defined here will be available
#  to all tests (i.e. fixtures)
from __future__ import annotations

import sys

sys.path.append(".")
from src.red_sysinfo import PLATFORM, PlatformInfo
from src.red_sysinfo.domain.enums.platform import EnumSystemTypes

import pytest

## Re-useable list of ints for tests
# @pytest.fixture
# def supply_AA_BB_CC() -> list:
#     aa = 25
#     bb = 35
#     cc = 45

#     return [aa, bb, cc]


@pytest.fixture()
def platform_info() -> PlatformInfo:
    return PlatformInfo()


@pytest.fixture()
def platform_dict() -> dict:
    platform = PlatformInfo()
    _dict = platform.as_dict()

    return _dict


@pytest.fixture()
def system_types() -> list[str]:
    """List of all system type enumeration values."""
    lst: list[str] = [
        EnumSystemTypes.LINUX.value,
        EnumSystemTypes.MAC.value,
        EnumSystemTypes.WINDOWS.value,
        EnumSystemTypes.JAVA.value,
    ]

    return lst
