"""
The command line tool for `pyclsflatten`.
"""
from __future__ import print_function

import importlib
import sys

from . import flatten


def main(clspath):
    """
    Get flattened representation based on class name as string.
    """
    loc, clsname = clspath.rsplit('.', 1)
    importlib.import_module(loc)
    cls = getattr(sys.modules[loc], clsname)
    print(flatten(cls))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} [cls]")
    main(sys.argv[1])
