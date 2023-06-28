from pygobuildinfo import get_go_build_info, get_go_mod, get_go_sum
import glob
import sys
import json
import concurrent.futures


def test_get_info(file):
    res = get_go_build_info(file)
    print(json.dumps(res,indent=4))


def test_go_mod(file):
    res = get_go_mod(file)
    print(json.dumps(res,indent=4))

def test_go_sum(file):
    res = get_go_sum(file)
    print(json.dumps(res,indent=4))


test_go_mod("/Users/mike/go/src/pygobuildInfo/go.mod")
test_go_mod("foo/bar")
test_go_mod("/usr/bin/du")
test_go_sum("/Users/mike/go/src/pygobuildInfo/go.sum")
test_go_sum("/Users/mike/go/src/pygobuildInfo/go.mod")
test_get_info("foo/bar")
test_get_info("/usr/bin/du")
test_get_info("/usr/local/bin/docker")
test_get_info("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.elf")
test_get_info("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.exe")
test_get_info("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider")
test_get_info("src/_pyGoBuildinfo.cpython-39-darwin.so")

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    futures = []
    for arg  in sys.argv[1:]:
        for file in glob.glob(arg,recursive=True):
            futures.append(executor.submit(get_go_build_info,file))

    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(json.dumps(result,indent=4))
    print(f"processed {len(futures)} files")
