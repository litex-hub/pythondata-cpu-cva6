import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post428"
version_tuple = (4, 2, 0, 428)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post428")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post286"
data_version_tuple = (4, 2, 0, 286)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post286")
except ImportError:
    pass
data_git_hash = "cfb81565b7f3e2a0537ea206927470cd41471137"
data_git_describe = "v4.2.0-286-gcfb81565"
data_git_msg = """\
commit cfb81565b7f3e2a0537ea206927470cd41471137
Author: Tamas Olaszi <62057357+tolaszi@users.noreply.github.com>
Date:   Thu Oct 6 12:53:36 2022 +0200

    Add CV32A6 CSR specification in .rst and IP-XACT format (#952)

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
