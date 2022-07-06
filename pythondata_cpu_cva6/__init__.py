import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post406"
version_tuple = (4, 2, 0, 406)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post406")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post264"
data_version_tuple = (4, 2, 0, 264)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post264")
except ImportError:
    pass
data_git_hash = "c23eed54152cd881d6f73a29a39c2bb7d637531c"
data_git_describe = "v4.2.0-264-gc23eed54"
data_git_msg = """\
commit c23eed54152cd881d6f73a29a39c2bb7d637531c
Author: M-Ijaz-10x <muhammad.ijaz@10xengineers.ai>
Date:   Wed Jul 6 22:12:40 2022 +0500

    Adding Support for Zba, Zbb, Zbc and Zbs extensions to CVA6 (#878)

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
