#!/usr/bin/env python3

"""

Helper functions and Sequence class defined here.
"""

from biocli._errors import WrongFormatError


_default_sample_ = '../sample.txt'


def _new_name(seq_type: str) -> str:
    
    """
    
    Creates a new file name based on the sequence type
    """

    from datetime import datetime

    tstamp = datetime.now().strftime("%Y_%m_%d-%I-%M-%S_%p")
    
    if seq_type.lower() == 'dna':
        return f'dna_sequence_{tstamp}.txt'
    elif seq_type.lower() == 'rna':
        return f'rna_sequence_{tstamp}.txt'
    else:
        print('Invalid sequence type. Choose RNA or DNA.')


def _load_sequence(text_file: str) -> str:
    """

    Loads the sequence from the file.
    """

    with open(text_file, 'r') as file:
        symbol_list = [x for x in file.read()]
    
    return ''.join(symbol_list)


class Sequence:
    """

    Class for DNA and RNA sequences and their methods.

    """

    def __init__(self, file: str):
        self.file = file
        self.seq = _load_sequence(file)

    def __repr__(self):
        return self.seq

    def __eq__(self, other):
        return self.seq == other.seq

    def __hash__(self):
        return hash(self.seq)

    def __len__(self):
        return len(self.seq)

    def __iter__(self):
        return iter(self.seq)

    def __getitem__(self, slice):
        return self.seq[slice]

    def __str__(self):
        if 'U' in self.seq:
            return f'RNA -- {self.seq}'
        else:
            return f'DNA -- {self.seq}'

    def is_dna(self):
        if 'U' in self.seq:
            return False
        else:
            return True
    
    def is_rna(self):
        if 'T' in self.seq:
            return False
        else:
            return True

