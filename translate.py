#!/usr/bin/env python3


"""

Translate feature to translate the given DNA sequence to RNA and vice versa.
"""


from src.helper import _new_name, Sequence
from src.errors import WrongNucleotideError, EmptyFileError


__version__ = ' 1.0'
__all__ = ['dna_to_rna', 'rna_to_dna']


def dna_to_rna(text_file: str, to_file: bool = False) -> str:
    """

    Translates the DNA sequence to RNA.

    :param text_file: The full file path to the sequence file. (str)
    
    :param to_file: Defaults to False. If True, the result is saved as a .txt file within the same directory.
    
    :print RNA sequence.
    """

    seq = Sequence(text_file)
    for alt in (('T', 'U'), ('\n', ''), ('DNA', 'RNA')):
        rna_text = str(seq).replace(*alt)

    if len(seq) == 0:
        raise EmptyFileError
    elif seq.is_rna():
        raise WrongNucleotideError
    elif to_file:
        with open(_new_name('rna'), 'w+') as file:
            file.write(rna_text)

    print(rna_text)


def rna_to_dna(text_file: str, to_file: bool = False) -> str:
    """

    Translates the RNA sequence to DNA.

    :param text_file: The full file path to the sequence file. (str)

    :param to_file: Defaults to False. If True, the result is saved as a .txt file within the same directory.

    :print DNA sequence.
    """

    seq = Sequence(text_file)
    for alt in (('U', 'T'), ('\n', ''), ('RNA', 'DNA')):
        dna_text = str(seq).replace(*alt)

    if len(seq) == 0:
        raise EmptyFileError
    elif seq.is_dna():
        raise WrongNucleotideError
    elif to_file:
        with open(_new_name('dna'), 'w+') as file:
            file.write(dna_text)

    print(dna_text)
