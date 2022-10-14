import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post431"
version_tuple = (4, 2, 0, 431)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post431")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post289"
data_version_tuple = (4, 2, 0, 289)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post289")
except ImportError:
    pass
data_git_hash = "4c01614f83cd9dd91d115aa190bd4fc6a284b59e"
data_git_describe = "v4.2.0-289-g4c01614f"
data_git_msg = """\
commit 4c01614f83cd9dd91d115aa190bd4fc6a284b59e
Author: Tianrui Wei <tianrui@tianruiwei.com>
Date:   Thu Oct 13 22:38:42 2022 -0700

    Bump CVA6 for OpenPiton, fix mmu issues (#968)
    
    This PR does the following
        1. Bump the filelist for OpenPiton for new directory layout
        2. Remove AXI Interface for OpenPiton in the top level
        3. Fix several issues in MMU discovered during address translation last year, the changes in core/mmu_sv39/mmu.sv are a joint effort between Jbalkind minho-pulp zarubaf niwis acostillado tianrui-wei
        4. disable bitmanip by default
        5. separate an ariane config package for openpiton synthesis. Some of  the previous changes makes ariane too big for openpiton, so we need to revert these changes
        6. Don't increase number of writeback ports (NR_WB_PORTS) when cvxif is  not enabled

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
