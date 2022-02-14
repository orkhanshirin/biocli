#!/usr/bin/env python3


"""
Pattern feature for finding given pattern in the given DNA or RNA sequence.
"""


from biocli._helper import Sequence, _default_sample_
from biocli._errors import EmptyFileError


__version__ = ' 1.0'
__all__ = ['match']


def match(pattern: str, text_file: str=_default_sample_):
    """
    Checks for the presence of a pattern in the sequence.

    Args:
        pattern (str): The pattern to search for.
        text_file (str): The full file path to the sequence file.

    Print: Position indices of the pattern in the sequence.
    """
    seq = Sequence(text_file)
    if len(seq) == 0:
        raise EmptyFileError

    positions = []

    for i in range(len(seq) - len(pattern)+1):
        if seq[i:i + (len(pattern))] == pattern:
            positions.append(i)

    print(positions, sep='\t')
