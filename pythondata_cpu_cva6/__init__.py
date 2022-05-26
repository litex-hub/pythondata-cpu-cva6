import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post389"
version_tuple = (4, 2, 0, 389)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post389")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post253"
data_version_tuple = (4, 2, 0, 253)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post253")
except ImportError:
    pass
data_git_hash = "75807530f26ba9a0ca501e9d3a6575ec375ed7ab"
data_git_describe = "v4.2.0-253-g75807530"
data_git_msg = """\
commit 75807530f26ba9a0ca501e9d3a6575ec375ed7ab
Author: Steffen Persvold <spersvold@users.noreply.github.com>
Date:   Thu May 12 10:46:40 2022 +0200

    Add support for "high" counter CSRs in 32-bit mode (#847)
    
    * Add support for "high" counter CSRs in 32-bit mode
    
    In 32bit mode MCYCLEH, MINSTRETH, CYCLEH, TIMEH and INSTRETH are
    used to return the most significant 32-bit value of the counters
    which are now always 64-bit wide.
    
    Signed-off-by: Steffen Persvold <spersvold@gmail.com>
    
    * Enable writing of MCYCLEH and MINSTRETH CSRs
    
    Signed-off-by: Steffen Persvold <spersvold@gmail.com>

"""

# Tool version info
tool_version_str = "0.0.post136"
tool_version_tuple = (0, 0, 136)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post136")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cva6."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cva6".format(f))
    return fn
