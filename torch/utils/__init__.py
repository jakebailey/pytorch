
from .throughput_benchmark import ThroughputBenchmark

import os.path as _osp
import sys

# Set the module for a given object for nicer printing
def set_module(obj, mod):
    if not isinstance(mod, str):
        raise TypeError("The mod argument should be a string")
    obj.__module__ = mod

if sys.executable == "torch_deploy":
    # not valid inside torch_deploy interpreter, no paths exists for frozen modules
    cmake_prefix_path = None
else:
    cmake_prefix_path = _osp.join(_osp.dirname(_osp.dirname(__file__)), 'share', 'cmake')


# Re-export submodules

from torch.utils import backcompat as backcompat
# cannot export data , as this would cause recursive import
# from torch.utils import data as data
