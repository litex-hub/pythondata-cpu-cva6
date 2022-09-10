import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post421"
version_tuple = (4, 2, 0, 421)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post421")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post279"
data_version_tuple = (4, 2, 0, 279)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post279")
except ImportError:
    pass
data_git_hash = "e60330ce902619a291ae5b8c632fe6cf9e739540"
data_git_describe = "v4.2.0-279-ge60330ce"
data_git_msg = """\
commit e60330ce902619a291ae5b8c632fe6cf9e739540
Author: JeanRochCoulon <jean-roch.coulon@thalesgroup.com>
Date:   Mon Sep 5 23:40:15 2022 +0200

    Design Spec initial commit: description of introduction, system and frontend (#949)

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
