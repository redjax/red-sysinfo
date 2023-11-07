from __future__ import annotations

from dataclasses import asdict, dataclass, field
from types import ModuleType
from typing import Any, Generic, NamedTuple, Tuple, TypeVar, Union

from datetime import datetime

from red_sysinfo.domain.enums.sysinfo import EnumCPUCores, EnumBasicSysInfo

import psutil

## Generic type for dataclass classes
T = TypeVar("T")


def get_last_boot() -> datetime:
    last_boot: datetime.fromtimestamp(psutil.boot_time())

    return last_boot


def get_cpu_info() -> CPUInfo:
    physical = EnumCPUCores.PHYSICAL.value
    total = EnumCPUCores.TOTAL.value

    # return {"physical": physical, "total": total}
    return CPUInfo(physical_cores=physical, total_cores=total)


@dataclass
class DictMixin:
    """Mixin class to add "as_dict()" method to classes. Equivalent to .__dict__.

    Add a .as_dict() method to classes that inherit from this mixin. For example,
    to add .as_dict() method to a parent class, where all children inherit the .as_dict()
    function, declare parent as:

    @dataclass
    class Parent(DictMixin):
        ...

    and call like:

        p = Parent()
        p_dict = p.as_dict()
    """

    def as_dict(self: Generic[T]):
        """Return dict representation of a dataclass instance."""
        try:
            return self.__dict__.copy()

        except Exception as exc:
            raise Exception(
                f"Unhandled exception converting class instance to dict. Details: {exc}"
            )


@dataclass
class CPUFrequency(DictMixin):
    last_updated: datetime = field(default=datetime.now())
    current: str = field(default=None)
    min: str = field(default=None)
    max: str = field(default=None)


@dataclass
class CPUCore(DictMixin):
    last_updated: datetime = field(default=datetime.now())
    core_num: int = field(default=0)
    usage: float = field(default=0.0)


@dataclass
class CPUCoreUsage(DictMixin):
    cores: list[CPUCore] = field(default=None)


@dataclass
class CPUInfo(DictMixin):
    physical_cores: int = field(default=EnumCPUCores.PHYSICAL.value)
    total_cores: int = field(default=EnumCPUCores.TOTAL.value)

    def frequency(self) -> CPUFrequency:
        cpu_freq = psutil.cpu_freq()

        min: str = f"{cpu_freq.min:.2f}Mhz"
        max: str = f"{cpu_freq.max:.2f}Mhz"
        current: str = f"{cpu_freq.current:.2f}Mhz"

        return_obj: CPUFrequency = CPUFrequency(current=current, min=min, max=max)

        return return_obj

    def core_usage(self) -> CPUCoreUsage:
        _cores: list[CPUCore] = []

        for i, percent in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            core: CPUCore = CPUCore(core_num=i, usage=percent)
            _cores.append(core)

        return_obj: CPUCoreUsage = CPUCoreUsage(cores=_cores)

        return return_obj


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
