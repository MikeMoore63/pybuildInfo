This package uses setuptools-golang for installation and to build manylinux wheels.

Build is currently
```shell
setuptools-golang-build-manylinux-wheels --golang=1.18.4 --pythons 'cp36-cp36m cp37-cp37m cp38-cp38 cp39-cp39 cp310-cp310'
```
So builds for linux x86 images for python versions 3.6 through to 3.10

NB On environments that prebuilt libraries are not supported go >= 1.8 MUST be installed and on the path.