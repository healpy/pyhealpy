#!/usr/bin/env python

import os
import errno
import fnmatch
import sys
import shlex
import shutil
from setuptools import setup

TEST_HELP = """
Note: running tests is no longer done using 'python setup.py test'. Instead
you will need to run:
    pytest
to also run the doctests:
    pytest --doctest-plus --doctest-cython
"""

if "test" in sys.argv:
    print(TEST_HELP)
    sys.exit(1)


setup(
)
