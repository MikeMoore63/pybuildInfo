"""Setup for checksig package"""
from io import open

from setuptools import Extension, setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pygobuildinfo',
    version='0.1.3',
    author="Mike Moore",
    author_email="z_z_zebra@yahoo.com",
    description="A utility to extract go build info information fro go executables and shared libraries",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT",
    url="https://github.com/Mikemoore63/pybuildInfo",
    py_modules=['pygobuildinfo'],
    build_golang={'root': 'github.com/MikeMoore63/pybuildInfo'},
    ext_modules=[Extension('_pyGoBuildinfo', ['pyGoBuildInfo.go'])],
    setup_requires=['setuptools-golang'],
    zip_safe=False,
    scripts=['get_go_info'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    options={
        "entry_points": {
            "hook-dirs": "pygobuildinfo.__pyinstaller.get_hook_dirs"
        }
    }
)
