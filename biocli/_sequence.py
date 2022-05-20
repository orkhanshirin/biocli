#!/usr/bin/env python3


"""
Sequence class defined here.
"""
from typing import Any, Union

from ._errors import EmptyFileError, WrongFormatError

# if text file not provided we use the default value
DEFAULT_SAMPLE = "../samples/sample.txt"


# loads the text file and returns the sequence as a string
def _load_sequence(text_file: str = DEFAULT_SAMPLE) -> Union[str, Any]:
    try:
        with open(text_file, "r", encoding="utf-8") as file:
            symbol_list = [file.read()]
            return "".join(symbol_list).replace("\n", "")
    except WrongFormatError as err:
        if not text_file.endswith(".txt"):
            raise err
        return "Failed!"


class Sequence:
    """
    Class for DNA and RNA sequences and their methods.
    """

    def __init__(self, text_file: str):
        self.__file = text_file
        self.__seq = _load_sequence(self.__file)
        if self._is_empty():
            raise EmptyFileError

    def __repr__(self):
        return self.__seq

    def __eq__(self, other):
        return self.__seq == other.__seq

    def __hash__(self):
        return hash(self.__seq)

    def __len__(self):
        return len(self.__seq)

    def __iter__(self):
        return iter(self.__seq)

    def __getitem__(self, slice_: Union[int, slice]):
        return self.__seq[slice_]

    def __str__(self) -> str:
        return self.__seq

    def _is_dna(self) -> bool:
        return "U" not in self.__seq

    def _is_rna(self) -> bool:
        return "T" not in self.__seq

    def _is_empty(self) -> bool:
        return len(self.__seq) == 0
