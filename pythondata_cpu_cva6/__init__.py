import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post425"
version_tuple = (4, 2, 0, 425)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post425")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post283"
data_version_tuple = (4, 2, 0, 283)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post283")
except ImportError:
    pass
data_git_hash = "6d263a6023298bf9d83aba44ddb1f30fd3ed90a9"
data_git_describe = "v4.2.0-283-g6d263a60"
data_git_msg = """\
commit 6d263a6023298bf9d83aba44ddb1f30fd3ed90a9
Author: Zbigniew Chamski <107464696+zchamski@users.noreply.github.com>
Date:   Thu Sep 22 19:49:19 2022 +0200

    compressed_decoder.sv: Fix FP word L/S decompression as per ISA spec v2.2. (#957)
    
    * compressed_decoder.sv: Fix of word L/S as per ISA spec v2.2.
    * core/compressed_decoder.sv: Use word L/S patterns in FLW/FSW/FLWSP/FSWSP
      expansions on RV32C.

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
