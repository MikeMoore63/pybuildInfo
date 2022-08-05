"""Setup for checksig package"""
from distutils.errors import CompileError
from subprocess import call
from io import open
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

class build_go_ext(build_ext):
    """Custom command to build extension from Go source files"""
    def build_extension(self, ext):
        ext_path = self.get_ext_fullpath(ext.name)
        cmd = ['go', 'build', '-buildmode=c-shared', '-o', ext_path]
        cmd += ext.sources
        out = call(cmd)
        if out != 0:
            raise CompileError('Go build failed')

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
    ext_modules=[Extension('_pyGoBuildinfo', ['pyGoBuildinfo.go'])],
    setup_requires=['setuptools-golang'],
    #ext_modules=[
    #    Extension('_pyGoBuildinfo', ['pyGoBuildinfo.go','export.go'])
    #],
    #cmdclass={'build_ext': build_go_ext},
    zip_safe=False,
)