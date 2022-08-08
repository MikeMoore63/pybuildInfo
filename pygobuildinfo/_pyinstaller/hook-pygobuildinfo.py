from PyInstaller.utils.hooks import collect_dynamic_libs
from distutils.sysconfig import get_config_var
from pathlib import Path
import os

here = Path(__file__).absolute().parent.parent
print(here)
ext_suffix = get_config_var('EXT_SUFFIX')
so_file = os.path.join(here, ('_pyGoBuildinfo' + ext_suffix))

binaries = [(so_file,'.')]
