import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post412"
version_tuple = (4, 2, 0, 412)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post412")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post270"
data_version_tuple = (4, 2, 0, 270)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post270")
except ImportError:
    pass
data_git_hash = "b6c1d04b6fa022c2e2df0b287865d28a0d42e756"
data_git_describe = "v4.2.0-270-gb6c1d04b"
data_git_msg = """\
commit b6c1d04b6fa022c2e2df0b287865d28a0d42e756
Author: Guillaume Chauvon <94678394+Gchauvon@users.noreply.github.com>
Date:   Wed Jul 20 17:03:06 2022 +0200

    decoder.sv: fix sfence.vma when rs1 != 0 (#933)
    
    unlike other instructions with minor opcode == PRIV,
    SFENCE.VMA do not check for rs1 != 0.
    Only check for rd !=0 to raise illegal instruction
    
    Signed-off-by: Guillaume Chauvon <guillaume.chauvon@thalesgroup.com>

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
