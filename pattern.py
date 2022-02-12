#!/usr/bin/env python3


"""

Pattern feature for finding given pattern in the given DNA or RNA sequence.
"""


from src.helper import Sequence, _default_sample_


__version__ = ' 1.0'
__all__ = ['match']


def match(pattern: str, text_file: str=_default_sample_):
    """
    Checks for the presence of a pattern in the sequence and returns the index of the first occurrence.

    :param pattern: The pattern to search for.

    :param text_file: The full file path to the sequence file. (str)

    :print Position indices of the pattern in the sequence.
    """

    positions = []
    seq = Sequence(text_file)

    for i in range(len(seq) - len(pattern)+1):
        if seq[i:i + (len(pattern))] == pattern:
            positions.append(i)

    print(positions, sep='\t')