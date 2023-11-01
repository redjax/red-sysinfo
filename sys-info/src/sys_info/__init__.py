from __future__ import annotations

from sys_info.utils.platform_utils import get_platform

from . import domain

PLATFORM: domain.platform.PlatformInfo = domain.platform.PlatformInfo()
