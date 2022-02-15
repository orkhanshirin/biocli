#!/usr/bin/env python3


"""
Count feature to count the nucleotides and patterns in the given DNA or RNA sequence.
"""


from collections import Counter
from . _sequence import Sequence


__version__ = ' 1.0'
__all__ = ['nucleotide', 'pattern', 'frequency']


def nucleotide(text_file: str) -> Counter:
    """
    Counts all the nucleotides in the sequence separately.

    Args:
        text_file (str): The full file path to the sequence file.

    Return:  Nucleotides and their counts.
    """

    seq = Sequence(text_file)

    counts = Counter([x for x in seq])

    for symbol, count in sorted(counts.items()):
            print(f'{symbol} -- {count}')

    return counts

def pattern(pattern: str, text_file: str) -> int:
    """
    Counts the number of occurance of the pattern in given text file.
    
    Args:
        pattern (str): The pattern to search for.
        text_file (str): The full file path to the sequence file.
    
    Return: Count of pattern.
    """

    seq = Sequence(text_file)
    
    return f'{str(seq).count(pattern)} patterns found.'


def frequency(window_len: int, text_file: str) -> dict:
    """
    
    Counts all the possible nucleotide combinations of given length in the sequence.

    Args:
        text_file (str): The full file path to the sequence file
        window_len (int): The length of the nucleotide combination.

    Return: Nucleotide combinations and their counts.
    """

    seq = Sequence(text_file)
    
    frequency = {}

    for i in range(len(seq) - window_len + 1):
        pattern = seq[i:i + window_len]
        frequency[pattern] = 0

        for j in range(len(seq) - window_len + 1):
            if seq[j:j + window_len] == pattern:
                frequency[pattern] +=  1

    for freq, value in frequency.items():
        print(f'{freq} -- {value}')

    return frequency
