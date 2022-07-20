import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post411"
version_tuple = (4, 2, 0, 411)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post411")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post269"
data_version_tuple = (4, 2, 0, 269)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post269")
except ImportError:
    pass
data_git_hash = "56ccf8089e80e5c7950038cad5796e50c64aa0c2"
data_git_describe = "v4.2.0-269-g56ccf808"
data_git_msg = """\
commit 56ccf8089e80e5c7950038cad5796e50c64aa0c2
Author: Kevin Eyssartier <kevin.eyssartier@thalesgroup.com>
Date:   Fri Jul 8 14:13:28 2022 +0200

    Associated PRs in task.yaml (#929)
    
    * Removing CVA6-SDK from task.yaml
    
    * Associated PRs in task.yaml
    
    This commit provide a new textarea to fill links to PRs used to complete the task.
    
    * Create bug.yaml
    
    * Update bug.yaml - Case consistency
    
    Co-authored-by: JeanRochCoulon <jean-roch.coulon@thalesgroup.com>

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
