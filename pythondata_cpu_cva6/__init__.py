import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post410"
version_tuple = (4, 2, 0, 410)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post410")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post268"
data_version_tuple = (4, 2, 0, 268)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post268")
except ImportError:
    pass
data_git_hash = "011edf49bdbc08b3ef62283406cf129d48c29372"
data_git_describe = "v4.2.0-268-g011edf49"
data_git_msg = """\
commit 011edf49bdbc08b3ef62283406cf129d48c29372
Author: Moritz Schneider <Moschn@users.noreply.github.com>
Date:   Fri Jul 8 10:21:57 2022 +0200

    Fix exception type on PMP check during PTW (#908)
    
    Fixes #906
    
    According to the spec:
    > If accessing pte violates a PMA or PMP check, raise an access-fault
    > exception corresponding to the original access type.
    
    Found by @Phantom1003 and @ProjectDimlight
    
    Signed-off-by: Moritz Schneider <moritz.schneider@inf.ethz.ch>

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
