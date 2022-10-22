import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post432"
version_tuple = (4, 2, 0, 432)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post432")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post290"
data_version_tuple = (4, 2, 0, 290)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post290")
except ImportError:
    pass
data_git_hash = "f346d6604f158a60a77e032f7396d5ac6a78e4aa"
data_git_describe = "v4.2.0-290-gf346d660"
data_git_msg = """\
commit f346d6604f158a60a77e032f7396d5ac6a78e4aa
Author: Jérôme Quévremont <jerome.quevremont@thalesgroup.com>
Date:   Sat Oct 22 08:22:21 2022 +0200

    Scratchpad can also be separate from caches (#981)
    
    To ease the implementation. As we'll target FPGA and ASIC (not ASSP), we do not need a "one size fits all" solution.

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cva6."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cva6".format(f))
    return fn
