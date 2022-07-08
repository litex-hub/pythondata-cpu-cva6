import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post409"
version_tuple = (4, 2, 0, 409)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post409")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post267"
data_version_tuple = (4, 2, 0, 267)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post267")
except ImportError:
    pass
data_git_hash = "01c89b7606bc14201e985a0bbca2ca2894b6af6b"
data_git_describe = "v4.2.0-267-g01c89b76"
data_git_msg = """\
commit 01c89b7606bc14201e985a0bbca2ca2894b6af6b
Author: Yan <phantom@zju.edu.cn>
Date:   Fri Jul 8 16:10:37 2022 +0800

    fix sfence.vma decoder (#921)

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
