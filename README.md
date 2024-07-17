A python package that extracts go build information from go based executables, go.mod and go.sum files  and shared libraries. The package leverages the golang debug/buildinfo and golang.org/x/mod/modfile packages to extract the information hence relies on a shared library to do this work.

Example usage 

```python

from pygobuildinfo import get_go_build_info, get_go_mod, get_go_sum
import json


def test_get_info(file):
    res = get_go_build_info(file)
    print(json.dumps(res, indent=4))

def test_go_mod(file):
    res = get_go_mod(file)
    print(json.dumps(res,indent=4))

def test_go_sum(file):
    res = get_go_sum(file)
    print(json.dumps(res,indent=4))

test_get_info("foo/bar")
test_get_info("/usr/bin/du")
test_get_info("/Users/auser/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.elf")
test_get_info("/Users/auser/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.exe")
test_get_info("/Users/auser/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider")
test_get_info("/Users/auser/go/pygobuildinfo/pybuildInfo/_pyGoBuildinfo.cpython-39-darwin.so")
test_go_mod("/Users/auser/go/src/pygobuildInfo/go.mod")
test_go_sum("/Users/auser/go/src/pygobuildInfo/go.sum")
```

The result returned is always a dict object for errors  the dictionary returned contains a key;
"error" like;
```python
{
    "error": "path error:foo/bar"
}
```
or 
```python
{
    "error": "/usr/bin/du: could not read Go build info from /usr/bin/du: unrecognized file format"
}
```
on success a python dict of the buildinfo struct is returned
```python
{
    "GoVersion": "go1.18.4",
    "Path": "github.com/spiffe/spire/support/oidc-discovery-provider",
    "Main": {
        "Path": "github.com/spiffe/spire",
        "Version": "(devel)",
        "Sum": "",
        "Replace": null
    },
    "Deps": [
        {
            "Path": "github.com/DataDog/datadog-go",
            "Version": "v3.2.0+incompatible",
            "Sum": "h1:qSG2N4FghB1He/r2mFrWKCaL7dXCilEuNEeAn20fdD4=",
            "Replace": null
        },
        {
            "Path": "github.com/andres-erbsen/clock",
            "Version": "v0.0.0-20160526145045-9e14626cd129",
            "Sum": "h1:MzBOUgng9orim59UnfUTLRjMpd09C5uEVQ6RPGeCaVI=",
            "Replace": null
        },
        {
            "Path": "github.com/armon/go-metrics",
            "Version": "v0.4.0",
            "Sum": "h1:yCQqn7dwca4ITXb+CbubHmedzaQYHhNhrEXLYUeEe8Q=",
            "Replace": null
        },
        {
            "Path": "github.com/beorn7/perks",
            "Version": "v1.0.1",
            "Sum": "h1:VlbKKnNfV8bJzeqoa4cOKqO6bYr3WgKZxO8Z16+hsOM=",
            "Replace": null
        },
        {
            "Path": "github.com/cespare/xxhash/v2",
            "Version": "v2.1.2",
            "Sum": "h1:YRXhKfTDauu4ajMg1TPgFO5jnlC2HCbmLXMcTG5cbYE=",
            "Replace": null
        },
        {
            "Path": "github.com/fatih/color",
            "Version": "v1.13.0",
            "Sum": "h1:8LOYc1KYPPmyKMuN8QV2DNRWNbLo6LZ0iLs8+mlH53w=",
            "Replace": null
        },
        {
            "Path": "github.com/felixge/httpsnoop",
            "Version": "v1.0.2",
            "Sum": "h1:+nS9g82KMXccJ/wp0zyRW9ZBHFETmMGtkk+2CTTrW4o=",
            "Replace": null
        },
        {
            "Path": "github.com/golang/protobuf",
            "Version": "v1.5.2",
            "Sum": "h1:ROPKBNFfQgOUMifHyP+KYbvpjbdoFNs+aK7DXlji0Tw=",
            "Replace": null
        },
        {
            "Path": "github.com/gorilla/handlers",
            "Version": "v1.5.1",
            "Sum": "h1:9lRY6j8DEeeBT10CvO9hGW0gmky0BprnvDI5vfhUHH4=",
            "Replace": null
        },
        {
            "Path": "github.com/hashicorp/go-hclog",
            "Version": "v1.2.1",
            "Sum": "h1:YQsLlGDJgwhXFpucSPyVbCBviQtjlHv3jLTlp8YmtEw=",
            "Replace": null
        },
        {
            "Path": "github.com/hashicorp/go-immutable-radix",
            "Version": "v1.3.1",
            "Sum": "h1:DKHmCUm2hRBK510BaiZlwvpD40f8bJFeZnpfm2KLowc=",
            "Replace": null
        },
        {
            "Path": "github.com/hashicorp/golang-lru",
            "Version": "v0.5.4",
            "Sum": "h1:YDjusn29QI/Das2iO9M0BHnIbxPeyuCHsjMW+lJfyTc=",
            "Replace": null
        },
        {
            "Path": "github.com/hashicorp/hcl",
            "Version": "v1.0.1-0.20190430135223-99e2f22d1c94",
            "Sum": "h1:LaH4JWe6Q7ICdxL5raxQjSRw7Pj8uTtAENrjejIYZIg=",
            "Replace": null
        },
        {
            "Path": "github.com/mattn/go-colorable",
            "Version": "v0.1.12",
            "Sum": "h1:jF+Du6AlPIjs2BiUiQlKOX0rt3SujHxPnksPKZbaA40=",
            "Replace": null
        },
        {
            "Path": "github.com/mattn/go-isatty",
            "Version": "v0.0.14",
            "Sum": "h1:yVuAays6BHfxijgZPzw+3Zlu5yQgKGP2/hcQbHb7S9Y=",
            "Replace": null
        },
        {
            "Path": "github.com/matttproud/golang_protobuf_extensions",
            "Version": "v1.0.2-0.20181231171920-c182affec369",
            "Sum": "h1:I0XW9+e1XWDxdcEniV4rQAIOPUGDq67JSCiRCgGCZLI=",
            "Replace": null
        },
        {
            "Path": "github.com/pkg/errors",
            "Version": "v0.9.1",
            "Sum": "h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=",
            "Replace": null
        },
        {
            "Path": "github.com/prometheus/client_golang",
            "Version": "v1.12.2",
            "Sum": "h1:51L9cDoUHVrXx4zWYlcLQIZ+d+VXHgqnYKkIuq4g/34=",
            "Replace": null
        },
        {
            "Path": "github.com/prometheus/client_model",
            "Version": "v0.2.0",
            "Sum": "h1:uq5h0d+GuxiXLJLNABMgp2qUWDPiLvgCzz2dUR+/W/M=",
            "Replace": null
        },
        {
            "Path": "github.com/prometheus/common",
            "Version": "v0.32.1",
            "Sum": "h1:hWIdL3N2HoUx3B8j3YN9mWor0qhY/NlEKZEaXxuIRh4=",
            "Replace": null
        },
        {
            "Path": "github.com/prometheus/procfs",
            "Version": "v0.7.3",
            "Sum": "h1:4jVXhlkAyzOScmCkXBTOLRLTz8EeU+eyjrwB/EPq0VU=",
            "Replace": null
        },
        {
            "Path": "github.com/sirupsen/logrus",
            "Version": "v1.8.1",
            "Sum": "h1:dJKuHgqk1NNQlqoA6BTlM1Wf9DOH3NBjQyu0h9+AZZE=",
            "Replace": null
        },
        {
            "Path": "github.com/spiffe/go-spiffe/v2",
            "Version": "v2.0.1-0.20220414143532-2ed460a8b9d3",
            "Sum": "h1:FpqM5PfWHs4Ze36HwzMpRefrv8kkmxFgtG9Qc6hL7Dc=",
            "Replace": null
        },
        {
            "Path": "github.com/spiffe/spire-api-sdk",
            "Version": "v1.2.2-0.20220317172821-e2705b35aa09",
            "Sum": "h1:2oavALIvyKv+M9Q2CWoz3UlJn4DT+oAhVO1qIgaq0GA=",
            "Replace": null
        },
        {
            "Path": "github.com/twmb/murmur3",
            "Version": "v1.1.6",
            "Sum": "h1:mqrRot1BRxm+Yct+vavLMou2/iJt0tNVTTC0QoIjaZg=",
            "Replace": null
        },
        {
            "Path": "github.com/uber-go/tally/v4",
            "Version": "v4.1.2",
            "Sum": "h1:NlU/4j+AAaPHG7yxQVmu0QY7H0W9FFDjFznwAU0t+rE=",
            "Replace": null
        },
        {
            "Path": "github.com/zeebo/errs",
            "Version": "v1.3.0",
            "Sum": "h1:hmiaKqgYZzcVgRL1Vkc1Mn2914BbzB0IBxs+ebeutGs=",
            "Replace": null
        },
        {
            "Path": "go.uber.org/atomic",
            "Version": "v1.9.0",
            "Sum": "h1:ECmE8Bn/WFTYwEW/bpKD3M8VtR/zQVbavAoalC1PYyE=",
            "Replace": null
        },
        {
            "Path": "golang.org/x/crypto",
            "Version": "v0.0.0-20220511200225-c6db032c6c88",
            "Sum": "h1:Tgea0cVUD0ivh5ADBX4WwuI12DUd2to3nCYe2eayMIw=",
            "Replace": null
        },
        {
            "Path": "golang.org/x/net",
            "Version": "v0.0.0-20220624214902-1bab6f366d9e",
            "Sum": "h1:TsQ7F31D3bUCLeqPT0u+yjp1guoArKaNKmCr22PYgTQ=",
            "Replace": null
        },
        {
            "Path": "golang.org/x/sys",
            "Version": "v0.0.0-20220624220833-87e55d714810",
            "Sum": "h1:rHZQSjJdAI4Xf5Qzeh2bBc5YJIkPFVM6oDtMFYmgws0=",
            "Replace": null
        },
        {
            "Path": "golang.org/x/text",
            "Version": "v0.3.7",
            "Sum": "h1:olpwvP2KacW1ZWvsR7uQhoyTYvKAupfQrRGBFM352Gk=",
            "Replace": null
        },
        {
            "Path": "google.golang.org/genproto",
            "Version": "v0.0.0-20220624142145-8cd45d7dbd1f",
            "Sum": "h1:hJ/Y5SqPXbarffmAsApliUlcvMU+wScNGfyop4bZm8o=",
            "Replace": null
        },
        {
            "Path": "google.golang.org/grpc",
            "Version": "v1.47.0",
            "Sum": "h1:9n77onPX5F3qfFCqjy9dhn8PbNQsIKeVU04J9G7umt8=",
            "Replace": null
        },
        {
            "Path": "google.golang.org/protobuf",
            "Version": "v1.28.0",
            "Sum": "h1:w43yiav+6bVFTBQFZX0r7ipe9JQ1QsbMgHwbBziscLw=",
            "Replace": null
        },
        {
            "Path": "gopkg.in/square/go-jose.v2",
            "Version": "v2.6.0",
            "Sum": "h1:NGk74WTnPKBNUhNzQX7PYcTLUjoq7mzKk2OKbvwk2iI=",
            "Replace": null
        }
    ],
    "Settings": [
        {
            "Key": "-compiler",
            "Value": "gc"
        },
        {
            "Key": "CGO_ENABLED",
            "Value": "0"
        },
        {
            "Key": "GOARCH",
            "Value": "amd64"
        },
        {
            "Key": "GOOS",
            "Value": "linux"
        },
        {
            "Key": "GOAMD64",
            "Value": "v1"
        },
        {
            "Key": "vcs",
            "Value": "git"
        },
        {
            "Key": "vcs.revision",
            "Value": "6cdc33ac0c19ca30b9e76313e8f17cfba0c86996"
        },
        {
            "Key": "vcs.time",
            "Value": "2022-07-13T19:09:00Z"
        },
        {
            "Key": "vcs.modified",
            "Value": "true"
        }
    ]
}
```
For go_sum and go_mod the structure will be similar with less info a go.sum does not know the module its part of nor go versions so just has dependencies, versions and hashes. For a go.mod it may have go version will have module path and dependencies but no hashes.
