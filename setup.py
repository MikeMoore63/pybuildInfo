
from setuptools import Extension, setup
import os

if __name__ == '__main__':
    setup(
        build_golang={'root': 'github.com/MikeMoore63/pybuildInfo'},
        ext_modules=[Extension('pygobuildinfo._pyGoBuildinfo', ['src/pygobuildinfo/pyGoBuildInfo.go'])]
          )
