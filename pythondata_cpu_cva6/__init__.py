import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post433"
version_tuple = (4, 2, 0, 433)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post433")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post291"
data_version_tuple = (4, 2, 0, 291)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post291")
except ImportError:
    pass
data_git_hash = "17743bc7120f1eb24974e5d7eb7f519ef53c4bdc"
data_git_describe = "v4.2.0-291-g17743bc7"
data_git_msg = """\
commit 17743bc7120f1eb24974e5d7eb7f519ef53c4bdc
Author: Nils Wistoff <nwistoff@iis.ee.ethz.ch>
Date:   Wed Oct 26 11:20:19 2022 +0200

    cache_subsystem: Parametrise AXI interface (#982)
    
    Parametrise the AXI interface of CVA6. With this PR, both cache subsystems support variable AXI address widths. The write-through cache furthermore supports variable AXI data widths. Moreover, this PR includes a modular AXI testbench for the WT cache to test the introduced changes. The following configurations of the WT cache have been verified:
    
    XLEN   Cacheline Width   AXI data width   AXI address width
    64                  128                     64                       64
    64                  128                   128                       52
    64                  512                   128                       64
    32                  512                   256                       48
    32                    64                     32                       48

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
