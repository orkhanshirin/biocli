#!/usr/bin/env python3


"""

BioCLI for Computational Biology
"""

import sys
import os


__version__ = "1.0"


cwd = os.path.dirname(__file__)
# The list of the paths for searching packages and modules by DynaCLI
# This is a simplest possible configuration. Look at [TBD]() for complete list
# of configuration options and typical use cases for each one.
search_path = [cwd]
# This needs to be done only if your sys.path does not already include it
# Here, we also include the src/python to enable dynacli import
sys.path.extend([*search_path, f'{cwd}/src'])

from dynacli import main
main(search_path)