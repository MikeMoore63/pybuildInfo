"""Setup for checksig package"""
from io import open

from setuptools import Extension, setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pyGoBuildInfo',
    version='0.1.0',
    author="Mike Moore",
    author_email="z_z_zebra@yahoo.com",
    description="A utility to extract go build info information fro go executables and shared libraries",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT",
    py_modules=['pyGoBuildInfo'],
    build_golang={'root': 'github.com/MikeMoore63/pybuildInfo'},
    ext_modules=[Extension('_pyGoBuildinfo', ['pyGoBuildInfo.go'])],
    setup_requires=['setuptools-golang'],
    zip_safe=False,
)
