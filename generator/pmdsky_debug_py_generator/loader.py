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
from typing import TypeVar, Optional, Dict, List

import yaml

OVERLAY_REGEX = re.compile(r"overlay(\d+)")
C_TYPE_REGEX = re.compile(r"(extern\s+)?(const\s+)?(?P<symbol_type>((enum|struct)\s+)?[a-z0-9_*]+)\s+(const\s+)?"
                          r"(?P<symbol_name>[A-Z0-9_]+)(?P<array_notation>(\[\d+]\s*)*);")
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
    def from_str(cls, region_str: str) -> Region | None:
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
    aliases: list[str] = field(default_factory=list)


@dataclass
class DeprecatedSymbol:
    oldname: str
    sym: Symbol


@dataclass
class Binary:
    name: str
    class_name: str
    loadaddresses: dict[Region, int | None] = field(default_factory=dict)
    lengths: dict[Region, int | None] = field(default_factory=dict)
    functions: list[Symbol] = field(default_factory=list)
    deprecated_functions: list[DeprecatedSymbol] = field(default_factory=list)
    data: list[Symbol] = field(default_factory=list)
    deprecated_data: list[DeprecatedSymbol] = field(default_factory=list)
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


class Loader:
    """
    Used to load pmdsky-debug symbols and their types
    """
    pmdsky_debug_dir: str
    # Contains all loaded binaries. None if symbols weren't loaded yet.
    _all_binaries: list[Binary] | None
    # Contains all loaded symbols, indexed by name. None if symbols weren't loaded yet.
    _all_symbols: dict[str, Symbol] | None

    def __init__(self, pmdsky_debug_dir: str):
        self.pmdsky_debug_dir = pmdsky_debug_dir
        self._all_binaries = None
        self._all_symbols = None

    def load(self):
        """
        Loads all the symbols present in the specified pmdsky-debug directory.
        The symbols can then be retrieved grouped by binary by calling get_binaries() or grouped by name
        by calling get_symbols().
        """
        yml_dir = os.path.join(self.pmdsky_debug_dir, PMDSKY_DEBUG_YAML_DIR)
        data_headers_dir = os.path.join(self.pmdsky_debug_dir, PMDSKY_DEBUG_DATA_HEADERS_DIR)

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

        self._all_binaries = []
        self._all_symbols = {}

        for yml_path in files:
            with yml_path.open("r", encoding="utf-8") as f:
                self._read_yml(yaml.safe_load(f))

        self._all_binaries.sort(key=lambda b: b.name)
        self.add_types(data_headers_dir)
        return self._all_binaries

    def get_binaries(self) -> list[Binary]:
        """
        Gets all loaded binaries. If symbol information has not been laoded yet, it is loaded before returning
        the result.
        """
        if self._all_binaries is None:
            self.load()
        return self._all_binaries

    def get_symbols(self) -> dict[Symbol]:
        """
        Gets all loaded symbols in a dict. The dict uses symbol names as the key. If symbol information has not been
        laoded yet, it is loaded before returning the result.
        """
        if self._all_binaries is None or self._all_symbols is None:
            self.load()
        # noinspection PyTypeChecker
        # The dict should to be loaded at this point
        return self._all_symbols

    def _read_yml(self, yml: dict):
        for bin_name, definition in yml.items():
            assert isinstance(bin_name, str)
            binary = Binary.get(self._all_binaries, bin_name)
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
                    sym = self._read_symbol(symbol_def)
                    binary.functions.append(sym)
                    self._read_deprecations(binary.deprecated_functions, sym)
            if "data" in definition:
                for symbol_def in definition["data"]:
                    sym = self._read_symbol(symbol_def)
                    binary.data.append(sym)
                    self._read_deprecations(binary.deprecated_data, sym)
            if "description" in definition:
                if binary.description == "":
                    binary.description = definition["description"]

    def _read_symbol(self, symbol_def: dict) -> Symbol:
        """
        Reads a symbol given its definition taken from a yml file. Also adds the symbol to this instance's symbol
        list.
        """

        if "name" in symbol_def:
            name = symbol_def["name"]
        else:
            raise ValueError("Symbol is missing its name.")

        sym = Symbol(name, description=symbol_def.get("description", ""), aliases=symbol_def.get("aliases", []))

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

        # Add to all symbols dict
        self._all_symbols[sym.name] = sym

        return sym

    def _read_deprecations(self, deprecations: list[DeprecatedSymbol], symbol: Symbol):
        for alias in symbol.aliases:
            deprecations.append(DeprecatedSymbol(sym=symbol, oldname=alias))
        return len(deprecations) > 0

    def add_types(self, data_headers_dir: str):
        """
        Loads type information for data symbols from the pmdsky-debug C headers
        :param data_headers_dir: Directory where the C headers for data fields is located
        """
        files = list(Path(data_headers_dir).rglob("*.h"))

        for header_path in files:
            with open(header_path) as f:
                for line in f:
                    if not line.startswith("#"):
                        match = re.match(C_TYPE_REGEX, line)
                        if match:
                            symbol_type = match.group("symbol_type")
                            # Limit whitspace to 1 character
                            symbol_type = re.sub(r"\s+", " ", symbol_type)

                            array_notation = match.group("array_notation")
                            if array_notation:
                                # Remove whitespace
                                array_notation = re.sub(r"\s+", "", array_notation)
                                # Append array notation to the type string
                                symbol_type += array_notation

                            symbol_name = match.group("symbol_name")

                            symbol = self._all_symbols[symbol_name]
                            if symbol:
                                symbol.type = symbol_type
                            else:
                                print("Warning: Symbol \"" + symbol_name + "\" not found while adding types.")


if __name__ == '__main__':
    for _binary in Loader(os.path.join(os.path.dirname(__file__), "..", "..", "pmdsky-debug", "symbols")).get_binaries():
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
