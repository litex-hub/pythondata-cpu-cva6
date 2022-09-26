import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post426"
version_tuple = (4, 2, 0, 426)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post426")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post284"
data_version_tuple = (4, 2, 0, 284)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post284")
except ImportError:
    pass
data_git_hash = "b9cfd53520c5ede0efbcbeab4379f85cd2d11d4c"
data_git_describe = "v4.2.0-284-gb9cfd535"
data_git_msg = """\
commit b9cfd53520c5ede0efbcbeab4379f85cd2d11d4c
Author: JeanRochCoulon <jean-roch.coulon@thalesgroup.com>
Date:   Mon Sep 26 14:52:52 2022 +0200

    Fix Flist.cv32a60x to load the right config package (#964)

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
