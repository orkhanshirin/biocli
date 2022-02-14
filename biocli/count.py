#!/usr/bin/env python3


"""
Count feature to count the nucleotides and patterns in the given DNA or RNA sequence.
"""


from collections import Counter
from biocli._helper import Sequence, _default_sample_
from biocli._errors import EmptyFileError


__version__ = ' 1.0'
__all__ = ['nucleotide', 'pattern', 'frequency']


def nucleotide(text_file: str=_default_sample_) -> Counter:
    """
    Counts all the nucleotides in the sequence separately.

    Args:
        text_file (str): The full file path to the sequence file.

    Print:  Nucleotides and their counts.
    """
    seq = Sequence(text_file)
    if len(seq) == 0:
        raise EmptyFileError
    else:
        counts = Counter([x for x in seq])

    for sym, count in sorted(counts.items()):
        if sym == '\n':
            continue
        else:
            print(f'{sym} -- {count}')


def pattern(pattern: str, text_file: str=_default_sample_) -> int:
    """

    Counts the number of occurance of the pattern in given text file.
    
    Args:
        pattern (str): The pattern to search for.
        text_file (str): The full file path to the sequence file.
    
    Print: Count of pattern.
    """

    seq = Sequence(text_file)
    pattern_count = str(seq).count(pattern)

    print(f'{pattern_count} patterns found.')


def frequency(window_len: int, text_file: str=_default_sample_) -> dict:
    """
    
    Counts all the possible nucleotide combinations of given length in the sequence.

    Args:
        text_file (str): The full file path to the sequence file
        window_len (int): The length of the nucleotide combination.

    Print: Nucleotide combinations and their counts.
    """

    seq = Sequence(text_file)
    if len(seq) == 0:
        raise EmptyFileError
    else:
        frequency = {}

    for i in range(len(seq) - window_len + 1):
        pattern = seq[i:i + window_len]
        frequency[pattern] = 0

        for j in range(len(seq) - window_len + 1):
            if seq[j:j + window_len] == pattern:
                frequency[pattern] = frequency[pattern] + 1

    for freq, value in frequency.items():
        print(f'{freq} -- {value}')
