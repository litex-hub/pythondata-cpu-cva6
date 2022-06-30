import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post403"
version_tuple = (4, 2, 0, 403)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post403")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post261"
data_version_tuple = (4, 2, 0, 261)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post261")
except ImportError:
    pass
data_git_hash = "22d29b080db5cfedd54b9de17ad20db2d6c69e0b"
data_git_describe = "v4.2.0-261-g22d29b08"
data_git_msg = """\
commit 22d29b080db5cfedd54b9de17ad20db2d6c69e0b
Author: Yannick Casamatta <yannick.casamatta@thalesgroup.com>
Date:   Thu Jun 30 10:32:08 2022 +0200

    Gitlab-ci: Add way to disable workflow policy (#926)

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
