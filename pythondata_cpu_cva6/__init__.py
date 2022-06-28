import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post402"
version_tuple = (4, 2, 0, 402)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post402")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post260"
data_version_tuple = (4, 2, 0, 260)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post260")
except ImportError:
    pass
data_git_hash = "a9c7b4f1e127688b3e8de03a54a31abcdae2bda4"
data_git_describe = "v4.2.0-260-ga9c7b4f1"
data_git_msg = """\
commit a9c7b4f1e127688b3e8de03a54a31abcdae2bda4
Author: JeanRochCoulon <jean-roch.coulon@thalesgroup.com>
Date:   Tue Jun 28 22:15:55 2022 +0200

    Cvvdev/dev/formating4 (#920)
    
    Several format cleanings:
    - split load_store_unit.sv to create lsu_bypass.sv
    - add several "begin" and "end"

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
