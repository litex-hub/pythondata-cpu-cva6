import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post404"
version_tuple = (4, 2, 0, 404)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post404")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post262"
data_version_tuple = (4, 2, 0, 262)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post262")
except ImportError:
    pass
data_git_hash = "b2dc4752e1511488cc5fac2b1a0c9007428d2186"
data_git_describe = "v4.2.0-262-gb2dc4752"
data_git_msg = """\
commit b2dc4752e1511488cc5fac2b1a0c9007428d2186
Author: Guillaume Chauvon <94678394+Gchauvon@users.noreply.github.com>
Date:   Thu Jun 30 11:56:35 2022 +0200

    Enable CVXIF for target cv32a60X and add renaming for cvxif when using 3 operands (#925)
    
    * re_name.sv: add condition related to CVXIF to rename 3rd operand
    * cv32a60x_pkg.sv: set CVXIFEn to 1

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
