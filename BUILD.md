
This package uses [setuptools-golang](https://pypi.org/project/setuptools-golang-examples/) for installation and to build manylinux wheels. 
The code is modified [this line](https://github.com/asottile/setuptools-golang/blob/main/setuptools_golang.py#L234) needs adjusting we replace docker image with a more modern version to get support for 3.10 and 3.11.

Currently using quay.io/pypa/manylinux_2_24_x86_64:latest as latest image this gets us 3.6 - 3.11 on linu


Build is currently
```shell
setuptools-golang-build-manylinux-wheels --golang=1.21.1 --pythons 'cp36-cp36m cp37-cp37m cp38-cp38 cp39-cp39 cp310-cp310 cp311-cp311'
cd src/pygobuildinfo
env GOOS="windows" GOARCH="amd64" CGO_ENABLED="1" CC="x86_64-w64-mingw32-gcc" go build -buildmode=c-shared -o pygo.dll
```
So builds for linux x86 images for python versions 3.6 through to 3.10

NB On environments that prebuilt libraries are not supported go >= 1.8 MUST be installed and on the path.