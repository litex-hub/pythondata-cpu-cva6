import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post435"
version_tuple = (4, 2, 0, 435)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post435")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post293"
data_version_tuple = (4, 2, 0, 293)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post293")
except ImportError:
    pass
data_git_hash = "c5947082c48a673b822d51b1deb2cafc2cecab31"
data_git_describe = "v4.2.0-293-gc5947082"
data_git_msg = """\
commit c5947082c48a673b822d51b1deb2cafc2cecab31
Author: sébastien jacq <57099003+sjthales@users.noreply.github.com>
Date:   Tue Nov 8 23:15:02 2022 +0100

    Optimize FPGA memories (#989)

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
