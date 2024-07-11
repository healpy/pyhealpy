#!/usr/bin/env python

import os
import errno
import fnmatch
import sys
import shlex
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

exec(open("healpy/version.py").read())


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="healpy",
    version=__version__,
    description="Healpix tools package for Python",
    long_description=readme(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: POSIX",
        "Programming Language :: C++",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    author="C. Rosset, A. Zonca",
    author_email="cyrille.rosset@apc.univ-paris-diderot.fr",
    url="http://github.com/healpy",
    packages=["healpy", "healpy.test"],
    py_modules=[
        "healpy.pixelfunc",
        "healpy.sphtfunc",
        "healpy.visufunc",
        "healpy.fitsfunc",
        "healpy.projector",
        "healpy.rotator",
        "healpy.projaxes",
        "healpy.version",
    ],
    package_data={
        "healpy": [
            "data/*.fits",
            "data/totcls.dat",
            "test/data/*.fits",
            "test/data/*.fits.gz",
            "test/data/*.sh",
        ]
    },
    install_requires=["matplotlib", "numpy>=1.13", "astropy", "scipy"],
    tests_require=["pytest", "pytest-cython", "pytest-doctestplus", "requests"],
    test_suite="healpy",
    license="GPLv2",
    scripts=["bin/healpy_get_wmap_maps.sh"],
    python_requires=">=3.7",
)
