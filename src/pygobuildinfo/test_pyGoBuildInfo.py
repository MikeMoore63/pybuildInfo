import pygobuildinfo
import json


def test_get_info(file):
    res = pygobuildinfo.get_go_build_info(file)
    print(json.dumps(res,indent=4))

test_get_info("foo/bar")
test_get_info("/usr/bin/du")
test_get_info("/usr/local/bin/docker")
test_get_info("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.elf")
test_get_info("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.exe")
test_get_info("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider")
test_get_info("/_pyGoBuildinfo.cpython-39-darwin.so")