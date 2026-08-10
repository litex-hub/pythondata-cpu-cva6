import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post5856"
version_tuple = (4, 2, 0, 5856)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post5856")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post5714"
data_version_tuple = (4, 2, 0, 5714)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post5714")
except ImportError:
    pass
data_git_hash = "c4c412a9f8c3b9f21ca7f7b6c58b612ec2afe724"
data_git_describe = "v4.2.0-5714-gc4c412a9"
data_git_msg = """\
commit c4c412a9f8c3b9f21ca7f7b6c58b612ec2afe724
Author: Misbahud Din <72780676+Misbahud-Din@users.noreply.github.com>
Date:   Wed Aug 6 11:50:17 2026 +0200

    Fixed classifications of c.jr and c.jalr instruction in instr_scan (#3444)

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
