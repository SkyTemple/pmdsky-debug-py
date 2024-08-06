import os
from dataclasses import dataclass
from typing import Optional, Any, Union

import toml
from black import format_str, FileMode
from jinja2 import Environment, PackageLoader

from pmdsky_debug_py_generator.loader import Binary, Region


def has_all_else_optional(value: dict[Region, Any | None], typ: str):
    has_all = not any(x is None for x in value.values())
    has_none = all(x is None for x in value.values())
    if has_none:
        return "None"
    if has_all:
        return typ
    return f"Optional[{typ}]"


def make_relative(value: None | int | list[int], based_on: int | None) -> None | int | list[int]:
    if value is None or based_on is None:
        return None
    if isinstance(value, int):
        return value - based_on
    if any(x is None for x in value):
        return None
    return [x - based_on for x in value]


def as_hex(value: None | int | list[int]) -> str:
    if value is None:
        return "None"
    if isinstance(value, int):
        return f"0x{value:0x}"
    joined = ",".join(f"0x{x:0x}" for x in value)
    return f"[{joined}]"


def escape_py(value: str) -> str:
    return value.replace('\n', r'\n').replace('"', "'")


J2ENV = Environment(
    loader=PackageLoader(__package__)
)
J2ENV.filters['has_all_else_optional'] = has_all_else_optional
J2ENV.filters['make_relative'] = make_relative
J2ENV.filters['as_hex'] = as_hex
J2ENV.filters['escape_py'] = escape_py


@dataclass
class File:
    template_name: str
    output_name: str
    region: Region | None


def generate(
        binaries: list[Binary],
        pkg_path: str,
        pkg_name: str,
        release: str
):
    files = [
        File('protocol.py.jinja2', 'protocol.py', None)
    ]

    for region in Region:
        files.append(File('region.py.jinja2', f'{region.file_name()}.py', region))

    for file in files:
        template = J2ENV.get_template(file.template_name)
        with open(os.path.join(pkg_path, file.output_name), 'w', encoding="utf-8") as f:
            f.write(format_str(template.render(
                binaries=binaries,
                region=file.region,
                pkg_name=pkg_name
            ), mode=FileMode(preview=True)))

    with open(os.path.join(pkg_path, '_release.py'), 'w') as f:
        f.write(f'RELEASE = "{release}"\n')


def update_version(pyproject_toml: dict, out_version: str, pptml_path: str):
    pyproject_toml['project']['version'] = out_version
    with open(pptml_path, 'w', encoding="utf-8") as f:
        toml.dump(pyproject_toml, f)
