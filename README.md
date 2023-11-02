# Red-Sys

Access platform details from a single object.

## Description

This module has a number of class objects, with properties derived from the [`platform`](https://docs.python.org/3/library/platform.html) and [`sys`](https://docs.python.org/3/library/sys.html) modules (part of Python's `stdlib`).

The cross-platform, main object of `red-sys` is the `PlatformInfo` class (defined in [domain.platform.schemas](./src/red_sysinfo/domain/platform/schemas.py)). This class has properties like `machine`, which prints the machine's architecture (i.e. `x86_x84`), system (i.e. `Linux`), and more.

`PlatformInfo` also has details about the Python interpreter running a script where `PlatformInfo` is called. `PlatformInfo.python` has details like the interpreter's version, implementation, path, and more. You can view the class at [domain.platform.schemas.PlatformPython](./src/red_sysinfo/domain/platform/schemas.py).

## Usage

Import the `PlatformInfo` object. 2 methods:

- An initialized CONSTANT
  - Import with: `from red_sys import PLATFORM`
  - The `PLATFORM` instance will be initialized from the environment.
    - Equivalent to `PLATFORM = PlatformInfo()`
- Use the `.get_platform()` function
  - Import the function with `from red_sysinfo.utils import platform_utils`
  - Define a variable, i.e. `PLATFORM = platform_utils.get_platform()`
    - Variable will contain an initialized instance of `PlatformInfo`
- Initialize an instance of the `PlatformInfo` class
  - ```
    from red_sys import PlatformInfo

    p: PlatformInfo = PlatformInfo()

    print(p.system())
    ```

To print a pre-formatted platform report, import the `print_platform()` function from `red_sysinfo.domain.platform.utils` and pass a `PlatformInfo` object.

Example:

```
from red_sysinfo import PLATFORM, print_platform()

print_platform(p=PLATFORM)
```

Optionally, call `print_platform(print_large_values=True)` to print values with a large output, like `PLATFORM.python.modules`.

The `PlatformInfoBase` class defines a number of functions and properties that children classes (classes inheriting from `PlatformInfoBase`, i.e. "`PlatformInfo(PlatformInfoBase):`") can access.

- `.is_<platform>()` functions, which return a bool if platform is detected
  - `.is_linux()`
  - `.is_unix()`
  - `.is_win()`
  - `.is_mac()`
  - `.is_java()`
- `.is_<arch>` functions, which return a bool if CPU architecture is detected
  - `.is_32bit()`
  - `.is_64bit()`
- `.as_dict()` function
  - Returns representation of class as a Python `dict`
  - Usage: `PLATFORM.is_dict()`

### Enums

`red-sys` also has a number of enumerators for constants. These are defined in [domain.enums.platform](./src/red_sysinfo/domain/enums/platform/), and are separated by platform.

# Links

- [Get the OS and its version where Python is running](https://note.nkmk.me/en/python-platform-system-release-version/)
- [Platform Module Docs](https://docs.python.org/3/library/platform.html)
- [Docs: `platform` module](https://docs.python.org/3/library/platform.html)
- [Docs: `sys` module](https://docs.python.org/3/library/sys.html)
