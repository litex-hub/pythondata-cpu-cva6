import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post405"
version_tuple = (4, 2, 0, 405)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post405")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post263"
data_version_tuple = (4, 2, 0, 263)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post263")
except ImportError:
    pass
data_git_hash = "0cfa94b8c663c2c5c0f47499853ad058d5eaac7a"
data_git_describe = "v4.2.0-263-g0cfa94b8"
data_git_msg = """\
commit 0cfa94b8c663c2c5c0f47499853ad058d5eaac7a
Author: Kevin Eyssartier <kevin.eyssartier@thalesgroup.com>
Date:   Tue Jul 5 07:18:55 2022 +0200

    Adding a Bug issue template  (#930)
    
    * Create bug.yaml
    
    * Update bug.yaml - Case consistency
    
    * Spelling mistakes

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
