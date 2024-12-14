from pygobuildinfo import get_go_build_info, get_go_mod, get_go_sum
import glob
import sys
import os
import json
import concurrent.futures


def test_get_info(file):
    if not os.path.isfile(file):
        print(f"{file} does not exist skipping")
        return

    res = get_go_build_info(file)
    print(f"{file}\n{json.dumps(res,indent=4)}")


def test_go_mod(file):
    if not os.path.isfile(file):
        print(f"{file} does not exist skipping")
        return
    res = get_go_mod(file)
    print(f"{file}\n{json.dumps(res,indent=4)}")

def test_go_sum(file):
    if not os.path.isfile(file):
        print(f"{file} does not exist skipping")
        return
    res = get_go_sum(file)
    print(f"{file}\n{json.dumps(res,indent=4)}")




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
            if file.endswith(".sum"):
                futures.append(executor.submit(get_go_sum,file))
            if file.endswith(".mod"):
                futures.append(executor.submit(get_go_mod,file))

    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            print(json.dumps(result,indent=4))
        except Exception as e:
            print(e)

    print(f"processed {len(futures)} files")
