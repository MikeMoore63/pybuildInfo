from __future__ import absolute_import

from pygobuildinfo._pyinstaller import get_hook_dirs, get_PyInstaller_tests

__all__ = ["get_hook_dirs", "get_PyInstaller_tests", "get_go_build_info"]

"""Extract buildinfo from go built binaries"""

import ctypes
import json
import os

from sysconfig import get_config_var

from pathlib import Path


# Location of shared library
here = Path(__file__).absolute().parent
ext_suffix = get_config_var("EXT_SUFFIX")
so_file = os.path.join(here, ("_pyGoBuildinfo" + ext_suffix))

# Load functions from shared library set their signatures
so = ctypes.cdll.LoadLibrary(so_file)
get_go_build_info_so = so.getgobuildinfo
get_go_build_info_so.argtypes = [ctypes.c_char_p]
get_go_build_info_so.restype = ctypes.c_void_p
get_go_mod_so = so.getgomod
get_go_mod_so.argtypes = [ctypes.c_char_p]
get_go_mod_so.restype = ctypes.c_void_p
free = so.free
free.argtypes = [ctypes.c_void_p]


def get_go_build_info(file_name):
    """Check (in parallel) digital signature of all files in root_dir.
    We assume there's a sha1sum.txt file under root_dir
    """
    res = get_go_build_info_so(file_name.encode("utf-8"))
    if res is not None:
        result = {"error": "Error converting result to json"}
        try:
            result = json.loads(ctypes.string_at(res).decode("utf-8"))
        except json.JSONDecodeError as e:
            pass
        finally:
            free(res)
        return result


def get_go_mod(file_name):
    """Check (in parallel) digital signature of all files in root_dir.
    We assume there's a sha1sum.txt file under root_dir
    """
    res = get_go_mod_so(file_name.encode("utf-8"))
    if res is not None:
        result = {"error": "Error converting result to json"}
        try:
            temp_result = json.loads(ctypes.string_at(res).decode("utf-8"))
            if "error" not in temp_result:
                actual_result = {"Deps": []}
                if (
                    "Module" in temp_result
                    and "Mod" in temp_result["Module"]
                    and "Path" in temp_result["Module"]["Mod"]
                ):
                    actual_result["Path"] = temp_result["Module"]["Mod"]["Path"]
                if "Go" in temp_result and "Version" in temp_result["Go"]:
                    actual_result["GoVersion"] = f"go{temp_result['Go']['Version']}"
                for module_required in temp_result.get("Require", []):
                    if "Mod" not in module_required:
                        continue
                    if "Path" not in module_required["Mod"]:
                        continue
                    if "Version" not in module_required["Mod"]:
                        continue
                    actual_result["Deps"].append(
                        {
                            "Path": module_required["Mod"]["Path"],
                            "Version": module_required["Mod"]["Version"],
                            "Indirect": module_required.get("Indirect", False),
                        }
                    )
                result = actual_result
            else:
                result = temp_result
        except json.JSONDecodeError as e:
            pass
        finally:
            free(res)
        return result


def get_go_sum(file_name):
    result = {"error": "not a valid go sum file"}
    with open(file_name, mode="rt", encoding="utf-8") as gsf:
        data = {}
        for line in gsf.readlines():
            sumfields = line.strip().split()
            if len(sumfields) < 3:
                continue
            if sumfields[1].endswith("/go.mod"):
                sumfields[1] = sumfields[1][:-7]
            data[sumfields[0]] = {"Version": sumfields[1], "Sum": sumfields[2]}
        data = {
            "Deps": [
                {"Path": k, "Version": data[k]["Version"], "Sum": data[k]["Sum"]}
                for k in data
            ]
        }
    if data:
        return data
    return result
