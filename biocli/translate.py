#!/usr/bin/env python3


"""
Translate feature to translate the given DNA sequence to RNA and vice versa.
"""


from biocli._helper import _new_name, Sequence
from biocli._errors import WrongNucleotideError, EmptyFileError


__version__ = ' 1.0'
__all__ = ['dna_to_rna', 'rna_to_dna']


def dna_to_rna(text_file: str, to_file: bool = False) -> str:
    """
    Translates the DNA sequence to RNA.

    Args:
        text_file (str): The full file path to the sequence file.
        to_file (bool): Save to file option. Default is False.
    
    Print: RNA sequence
    """

    seq = Sequence(text_file)
    rna_text = ''.join(['U' if x == 'T' else x for x in seq])

    if rna_text.startswith('DNA -- '):
        rna_text = f'RNA -- {rna_text[7:]}'
    else:
        rna_text = f'RNA -- {rna_text}'

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

    Translates the DNA sequence to RNA.

    Args:
        text_file (str): The full file path to the sequence file.
        to_file (bool): Save to file option. Default is False.
    
    Print: DNA sequence
    """

    seq = Sequence(text_file)
    dna_text = ''.join(['T' if x == 'U' else x for x in seq])

    if dna_text.startswith('RNA -- '):
        dna_text = f'DNA -- {dna_text[7:]}'
    else:
        dna_text = f'DNA -- {dna_text}'

    if len(seq) == 0:
        raise EmptyFileError
    elif seq.is_dna():
        raise WrongNucleotideError
    elif to_file:
        with open(_new_name('dna'), 'w+') as file:
            file.write(dna_text)

    print(dna_text)
