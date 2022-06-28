import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post401"
version_tuple = (4, 2, 0, 401)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post401")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post259"
data_version_tuple = (4, 2, 0, 259)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post259")
except ImportError:
    pass
data_git_hash = "767c465cfbac8e5e9112e3b067199963d6a89cfd"
data_git_describe = "v4.2.0-259-g767c465c"
data_git_msg = """\
commit 767c465cfbac8e5e9112e3b067199963d6a89cfd
Author: Mike Thompson <mike@openhwgroup.org>
Date:   Tue Jun 28 08:04:06 2022 -0400

    Introduce CV32A60X as first release (#916)

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
