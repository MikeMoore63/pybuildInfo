
from setuptools import Extension, setup

if __name__ == '__main__':
    setup(
        build_golang={'root': 'github.com/MikeMoore63/pybuildInfo'},
        ext_modules=[Extension('_pyGoBuildinfo', ['src/pygobuildinfo/pyGoBuildInfo.go'])]
          )
