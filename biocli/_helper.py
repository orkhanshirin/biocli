#!/usr/bin/env python3

"""
Helper functions defined here.
"""


def _new_name(seq_type: str) -> str:
    
    """
    Creates a new file name based on the sequence type.
    """

    from datetime import datetime

    tstamp = datetime.now().strftime("%Y_%m_%d-%I-%M-%S_%p")
    
    if seq_type.lower() == 'dna':
        return f'dna_sequence_{tstamp}.txt'
    elif seq_type.lower() == 'rna':
        return f'rna_sequence_{tstamp}.txt'
    else:
        print('Invalid sequence type. Choose RNA or DNA.')


def save(seq_type, text) -> None:
    """
    Save the sequence to a file.
    """

    with open(_new_name(seq_type), 'w+') as file:
        file.write(text)
    print('Saved successfully!')