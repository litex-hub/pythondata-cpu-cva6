import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "4.2.0.post427"
version_tuple = (4, 2, 0, 427)
try:
    from packaging.version import Version as V
    pversion = V("4.2.0.post427")
except ImportError:
    pass

# Data version info
data_version_str = "4.2.0.post285"
data_version_tuple = (4, 2, 0, 285)
try:
    from packaging.version import Version as V
    pdata_version = V("4.2.0.post285")
except ImportError:
    pass
data_git_hash = "871be7c7943820ebe72c85c72f9af1164a50dc32"
data_git_describe = "v4.2.0-285-g871be7c7"
data_git_msg = """\
commit 871be7c7943820ebe72c85c72f9af1164a50dc32
Author: Zbigniew Chamski <107464696+zchamski@users.noreply.github.com>
Date:   Tue Sep 27 14:53:06 2022 +0200

    [tracing] VCS and Verilator support of waveform dumps. (#965)
    
    Usage of the macros:
        * If defined, VM_TRACE enables tracing. If macro VM_TRACE_FST is not defined (the default), waveform generation will use VCD format. If the command-line option -v FILE or --vcd=FILE is given to the compiled simulator, the VCD output will be written to file named FILE in the current working dir of the verilated simulator. If no -v/--vcd= option is given on cmdline, or an FST-specific trace option is used, the simulator will generate a VCD trace according to the settings in the RTL code.
        * if VM_TRACE_FST is defined as well, then FST format is used instead of VCD. If the command line option -f FILE or --fst=FILE is given to the simulator, the trace will be stored in file FILE in the current working dir of the verilated simulator. If no -f/--fst= option is given, or a VCD-specific trace option is used, the simulator will generate an FST trace according to the settings in the RTL code.

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
