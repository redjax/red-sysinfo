from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime

from red_sysinfo.domain.mixins import DictMixin
from red_sysinfo.domain.enums.sysinfo import EnumCPUCores, EnumBasicSysInfo
from red_sysinfo.utils.conversion_utils import convert_bytes

import psutil

from .methods import get_last_boot

from .cpu import CPUInfo, get_cpu_info

# def get_virtual_mem() ->


@dataclass
class MemoryInfo(DictMixin):
    pass
    # total

    # def frequency(self) -> CPUFrequency:
    #     cpu_freq = psutil.cpu_freq()

    #     min: str = f"{cpu_freq.min:.2f}Mhz"
    #     max: str = f"{cpu_freq.max:.2f}Mhz"
    #     current: str = f"{cpu_freq.current:.2f}Mhz"

    #     return_obj: CPUFrequency = CPUFrequency(current=current, min=min, max=max)

    #     return return_obj

    # def core_usage(self) -> CPUCoreUsage:
    #     _cores: list[CPUCore] = []

    #     for i, percent in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    #         core: CPUCore = CPUCore(core_num=i, usage=percent)
    #         _cores.append(core)

    #     return_obj: CPUCoreUsage = CPUCoreUsage(cores=_cores)

    #     return return_obj


@dataclass
class SystemInfoBase(DictMixin):
    """Store system information gleaned from psutil module."""

    last_boot: datetime = field(default=EnumBasicSysInfo.LAST_BOOT.value)
    cpu: CPUInfo = field(default_factory=get_cpu_info)
    # disk
    # network
    # memory


@dataclass
class SystemInfo(SystemInfoBase):
    pass
