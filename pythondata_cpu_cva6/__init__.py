import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post396"
version_tuple = (4, 2, 0, 396)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post396")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post254"
data_version_tuple = (4, 2, 0, 254)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post254")
except ImportError:
    pass
data_git_hash = "909d85a56cc5ace65765a63d7ed56b7ac2026f99"
data_git_describe = "v4.2.0-254-g909d85a5"
data_git_msg = """\
commit 909d85a56cc5ace65765a63d7ed56b7ac2026f99
Author: Guillaume Chauvon <94678394+Gchauvon@users.noreply.github.com>
Date:   Mon May 30 22:50:50 2022 +0200

    Fix tc_srams paths (#892)
    
    * cva6_synth.tcl: fix set_input_delay and set_output_delay tc_sram paths
    * ariane_tb.cpp;.sv: [Fix tc_srams] change path for user memory preload
    
    Signed-off-by: Guillaume Chauvon <guillaume.chauvon@thalesgroup.com>
    Co-authored-by: Jean-Roch Coulon <jean-roch.coulon@thalesgroup.com>

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
