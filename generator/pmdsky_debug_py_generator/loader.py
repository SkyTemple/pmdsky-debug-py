#  Copyright 2020-2022 Capypara and the SkyTemple Contributors
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations
import os
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import TypeVar, Optional

import yaml

OVERLAY_REGEX = re.compile(r"overlay(\d+)")
C_TYPE_REGEX = re.compile(r"(((enum )|(struct ))?[a-z0-9_*]+) ([A-Z0-9_]+)(\[\d+])*;")
PMDSKY_DEBUG_YAML_DIR = "symbols"
PMDSKY_DEBUG_DATA_HEADERS_DIR = "headers/data"


T = TypeVar('T')


class Region(Enum):
    NA = "na"
    EU = "eu"
    JP = "jp"
    NA_ITCM = "na-itcm"
    EU_ITCM = "eu-itcm"
    JP_ITCM = "jp-itcm"

    @classmethod
    def from_str(cls, region_str: str) -> Optional[Region]:
        region_str = region_str.lower()
        if region_str == "na":
            return Region.NA
        if region_str == "eu":
            return Region.EU
        if region_str == "jp":
            return Region.JP
        if region_str == "na-itcm":
            return Region.NA_ITCM
        if region_str == "eu-itcm":
            return Region.EU_ITCM
        if region_str == "jp-itcm":
            return Region.JP_ITCM
        if region_str == "na-wram":
            return None
        if region_str == "eu-wram":
            return None
        if region_str == "jp-wram":
            return None
        if region_str == "na-ram":
            return None
        if region_str == "eu-ram":
            return None
        if region_str == "jp-ram":
            return None
        raise ValueError(f"Unknown region string: {region_str}")

    @classmethod
    def fill_missing(cls, dic: dict[Region, T | None]):
        if cls.NA not in dic:
            dic[cls.NA] = None
        if cls.EU not in dic:
            dic[cls.EU] = None
        if cls.JP not in dic:
            dic[cls.JP] = None
        if cls.NA_ITCM not in dic:
            dic[cls.NA_ITCM] = None
        if cls.EU_ITCM not in dic:
            dic[cls.EU_ITCM] = None
        if cls.JP_ITCM not in dic:
            dic[cls.JP_ITCM] = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.__class__.__name__}.{self.name}"

    def file_name(self):
        return self.value.replace("-", "_")

    def class_prefix(self):
        if self == Region.NA:
            return "Na"
        if self == Region.EU:
            return "Eu"
        if self == Region.JP:
            return "Jp"
        if self == Region.NA_ITCM:
            return "NaItcm"
        if self == Region.EU_ITCM:
            return "EuItcm"
        if self == Region.JP_ITCM:
            return "JpItcm"


@dataclass
class Symbol:
    name: str
    addresses: dict[Region, list[int] | None] = field(default_factory=dict)
    lengths: dict[Region, int | None] = field(default_factory=dict)
    description: str = field(default_factory=str)
    type: str = field(default_factory=str)


@dataclass
class Binary:
    name: str
    class_name: str
    loadaddresses: dict[Region, int | None] = field(default_factory=dict)
    lengths: dict[Region, int | None] = field(default_factory=dict)
    functions: list[Symbol] = field(default_factory=list)
    data: list[Symbol] = field(default_factory=list)
    description: str = field(default_factory=str)

    @classmethod
    def get(
        cls, pool: list[Binary], name: str
    ) -> Binary:
        for e in pool:
            if e.name == name:
                return e
        newobj = Binary(name, name.capitalize())
        pool.append(newobj)
        return newobj


def _read_symbol(symbol_def: dict) -> Symbol:
    if "name" in symbol_def:
        name = symbol_def["name"]
    else:
        raise ValueError("Symbol is missing its name.")

    sym = Symbol(name, description=symbol_def.get("description", ""))

    if "address" in symbol_def:
        for region_str, value in symbol_def["address"].items():
            region = Region.from_str(region_str)
            if region is not None:
                if isinstance(value, list):
                    sym.addresses[region] = [int(x) for x in value]
                else:
                    sym.addresses[region] = [int(value)]
        Region.fill_missing(sym.addresses)
    else:
        raise ValueError(f"Symbol {name} is missing an address.")

    if "length" in symbol_def:
        for region_str, value in symbol_def["length"].items():
            region = Region.from_str(region_str)
            if region is not None:
                sym.lengths[region] = int(value)
    Region.fill_missing(sym.lengths)

    return sym


def _read(binaries: list[Binary], yml: dict):
    for bin_name, definition in yml.items():
        assert isinstance(bin_name, str)
        binary = Binary.get(binaries, bin_name)
        # TODO: Do something special with "versions"?
        #       For now we will just assume all symbols are for all regions
        #       and just treat missing load-addresses and symbol addresses/lengths.
        if "address" in definition:
            for region_str, value in definition["address"].items():
                region = Region.from_str(region_str)
                if region is not None:
                    binary.loadaddresses[region] = int(value)
            Region.fill_missing(binary.loadaddresses)
        if "length" in definition:
            for region_str, value in definition["length"].items():
                region = Region.from_str(region_str)
                if region is not None:
                    binary.lengths[region] = int(value)
            Region.fill_missing(binary.lengths)
        if "functions" in definition:
            for symbol_def in definition["functions"]:
                binary.functions.append(_read_symbol(symbol_def))
        if "data" in definition:
            for symbol_def in definition["data"]:
                binary.data.append(_read_symbol(symbol_def))
        if "description" in definition:
            if binary.description == "":
                binary.description = definition["description"]


def load_binaries(pmdsky_debug_dir: str) -> list[Binary]:
    binaries: list[Binary] = []

    yml_dir = os.path.join(pmdsky_debug_dir, PMDSKY_DEBUG_YAML_DIR)
    data_headers_dir = os.path.join(pmdsky_debug_dir, PMDSKY_DEBUG_DATA_HEADERS_DIR)

    files = list(Path(yml_dir).rglob("*.yml"))

    # Make sure the arm and overlay files are read this: These are the main files.
    # They will contain the address, length and description.
    # Make sure sub-files are read last.
    files.sort(
        key=lambda key: (
            len(key.parts),
            -1 if key.name.startswith("arm") or key.name.startswith("overlay") else 1,
        )
    )

    for yml_path in files:
        with yml_path.open("r") as f:
            _read(binaries, yaml.safe_load(f))

    binaries.sort(key=lambda b: b.name)
    add_types(binaries, data_headers_dir)
    return binaries


def get_binary_by_name(name: str, binaries: list[Binary]) -> Optional[Binary]:
    """
    Given a list of binaries, returns the first one that has the specified name
    :return The first binary with the given name, or None if none of the binaries has that name.
    """
    for binary in binaries:
        if binary.name == name:
            return binary
    return None


def get_data_symbol_by_name(name: str, binary: Binary) -> Optional[Symbol]:
    """
    Given a symbol name and a binary, returns the first data symbol in the binary with the specified name, or
    None if no symbol with that name is found.
    """
    for symbol in binary.data:
        if symbol.name == name:
            return symbol
    return None


def add_types(binaries: list[Binary], data_headers_dir: str):
    """
    Loads type information for data symbols from the pmdsky-debug C headers
    :param binaries: List of binaries. Its items will be modified to include type information.
    :param data_headers_dir: Directory where the C headers for data fields is located
    """
    files = list(Path(data_headers_dir).rglob("*.h"))

    for header_path in files:
        binary_name = header_path.name.split(".")[0]
        binary = get_binary_by_name(binary_name, binaries)

        if binary is not None:
            with open(header_path) as f:
                for line in f:
                    if not line.startswith("#"):
                        match = re.search(C_TYPE_REGEX, line)
                        if match:
                            symbol_type = match.group(1)
                            array_notation = match.group(6)
                            if array_notation:
                                # Append array notation to the type string, if present
                                symbol_type += array_notation
                            symbol_name = match.group(5)

                            symbol = get_data_symbol_by_name(symbol_name, binary)
                            if symbol:
                                symbol.type = symbol_type


if __name__ == '__main__':
    for _binary in load_binaries(os.path.join(os.path.dirname(__file__), "..", "..", "pmdsky-debug", "symbols")):
        print("==============")
        print(f"{_binary.name}")
        print(f"loads: {_binary.loadaddresses}")
        print(f"lengths: {_binary.lengths}")
        print(f"fns:")
        for _fn in _binary.functions:
            print(f"  > {_fn.name} @ {_fn.addresses} - lengths: {_fn.lengths}")
        print(f"datas:")
        for _data in _binary.data:
            print(f"  > {_data.name} @ {_data.addresses} - lengths: {_data.lengths}")
