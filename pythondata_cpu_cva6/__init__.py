import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post398"
version_tuple = (4, 2, 0, 398)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post398")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post256"
data_version_tuple = (4, 2, 0, 256)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post256")
except ImportError:
    pass
data_git_hash = "d315ddd0f1be27c1b3f27eb0b8daf471a952299a"
data_git_describe = "v4.2.0-256-gd315ddd0"
data_git_msg = """\
commit d315ddd0f1be27c1b3f27eb0b8daf471a952299a
Author: Yannick Casamatta <yannick.casamatta@thalesgroup.com>
Date:   Thu Jun 16 10:37:34 2022 +0200

    gitlab-ci: add workflow for github pull request (#919)

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
