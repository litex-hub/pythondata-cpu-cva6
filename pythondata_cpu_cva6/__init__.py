import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post423"
version_tuple = (4, 2, 0, 423)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post423")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post281"
data_version_tuple = (4, 2, 0, 281)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post281")
except ImportError:
    pass
data_git_hash = "9109ff07f67bccc7a75a55d67d8734eedc8344ee"
data_git_describe = "v4.2.0-281-g9109ff07"
data_git_msg = """\
commit 9109ff07f67bccc7a75a55d67d8734eedc8344ee
Author: JeanRochCoulon <jean-roch.coulon@thalesgroup.com>
Date:   Wed Sep 21 13:00:59 2022 +0200

    Cvvdev/dev/rvfi (#959)
    
    * Add load and store information to RVFI
    * Add rs1 and rs2 information to RVFI
    * Condition rvfi mem and rs1/rs2 information generation by RVFI_MEM
    This add-on is requested by ISACOV and test termination.

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
