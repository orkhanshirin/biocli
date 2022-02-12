#!/usr/bin/env python3


"""

Count feature to count the nucleotides and patterns in the given DNA or RNA sequence.
"""


from collections import Counter
from src.helper import Sequence, _default_sample_


__version__ = ' 1.0'
__all__ = ['nucleotide', 'pattern', 'frequency']


def nucleotide(text_file: str=_default_sample_) -> Counter:
    """

    Counts the nucleotides in the sequence.

    :param  text_file: The full file path to the sequence file. (str)

    :print  Nucleotides and their counts.
    """

    counts = Counter([x for x in Sequence(text_file)])

    for sym, count in sorted(counts.items()):
        if sym == '\n':
            continue
        else:
            print(f'{sym} -- {count}')


def pattern(pattern: str, text_file: str=_default_sample_) -> int:
    """

    Counts the number of times the pattern appears in the text.
    
    :param  pattern: The pattern to search for.

    :param  text_file: The full file path to load the sequence from.
    
    :print  The number of times the pattern appears in the text.
    """

    seq = Sequence(text_file)
    pattern_count = str(seq).count(pattern)

    print(f'{pattern_count} patterns found.')


def frequency(window_len: int, text_file: str=_default_sample_) -> dict:
    """
    
    Counts all the possible nucleotide sequences of given length in the sequence.

    :param text_file: The full file path to load the sequence from.

    :param window_len: The length of the nucleotide sequence to count.

    :print Count of count of every possible nucleotide sequence of given length.
    """

    seq = Sequence(text_file)
    frequency = {}

    for i in range(len(seq) - window_len + 1):
        pattern = seq[i:i + window_len]
        frequency[pattern] = 0

        for j in range(len(seq) - window_len + 1):
            if seq[j:j + window_len] == pattern:
                frequency[pattern] = frequency[pattern] + 1

    for freq, value in frequency.items():
        print(f'{freq} -- {value}')