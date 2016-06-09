from __future__ import print_function

import importlib
import sys

from . import flatten


def main():
    if len(sys.argv) != 2:
        print("Usage: {} [cls]")
    loc, clsnm = sys.argv[1].rsplit('.', 1)
    importlib.import_module(loc)
    cls = getattr(sys.modules[loc], clsnm)
    print(flatten(cls))


if __name__ == '__main__':
    main()
