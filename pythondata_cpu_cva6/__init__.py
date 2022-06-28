import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post400"
version_tuple = (4, 2, 0, 400)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post400")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post258"
data_version_tuple = (4, 2, 0, 258)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post258")
except ImportError:
    pass
data_git_hash = "66f158dea03328bc3aefb0177293ca52d4235940"
data_git_describe = "v4.2.0-258-g66f158de"
data_git_msg = """\
commit 66f158dea03328bc3aefb0177293ca52d4235940
Author: Guillaume Chauvon <94678394+Gchauvon@users.noreply.github.com>
Date:   Tue Jun 28 09:59:51 2022 +0200

    FPGA: Add scripts to boot linux fpga (#924)
    
    Signed-off-by: Guillaume Chauvon<guillaume.chauvon@thalesgroup.com>

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
