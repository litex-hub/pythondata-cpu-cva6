import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post430"
version_tuple = (4, 2, 0, 430)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post430")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post288"
data_version_tuple = (4, 2, 0, 288)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post288")
except ImportError:
    pass
data_git_hash = "df920cda7e4a8a0db7b6bcd0d2270a1b5a7521d2"
data_git_describe = "v4.2.0-288-gdf920cda"
data_git_msg = """\
commit df920cda7e4a8a0db7b6bcd0d2270a1b5a7521d2
Author: JeanRochCoulon <jean-roch.coulon@thalesgroup.com>
Date:   Thu Oct 13 08:02:01 2022 +0200

    Remove verilator_work files (#975)

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
