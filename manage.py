# -*- encoding:utf-8 -*-
import os
import sys
import builtins

from commands import bootstrap

builtins.u_ROOT_PATH=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1,u_ROOT_PATH)
if __name__ == "__main__":
    bootstrap()
    # version v1.1.2