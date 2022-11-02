import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post434"
version_tuple = (4, 2, 0, 434)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post434")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post292"
data_version_tuple = (4, 2, 0, 292)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post292")
except ImportError:
    pass
data_git_hash = "ec61b89df66b272fbbc9cb4e9d24dccd33d621af"
data_git_describe = "v4.2.0-292-gec61b89d"
data_git_msg = """\
commit ec61b89df66b272fbbc9cb4e9d24dccd33d621af
Author: Guillaume Chauvon <94678394+Gchauvon@users.noreply.github.com>
Date:   Wed Nov 2 10:24:33 2022 +0100

    Flist.cv32a60x: add example coprocessor to Flist (#986)

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
