# -*- encoding: utf-8 -*-
import os
import sys
import builtins
import multiprocessing
from importlib import import_module
from importlib.util import find_spec

from .base import BaseConfig
from .local import LocalConfig


__all__ = ['config_initialize']

initialized = False


def config_initialize(*args, **kwargs):
    """
    根据传入的变量
    通过builtins设置_config
    nt 环境中分裂子进程会分裂一个 "干净" 的子进程 需要重新初始化
    """
    environment = os.environ['environment']
    global initialized

    if initialized:
        raise "Configuration initialization is complete"

    if find_spec(f'config.{environment}', package='..'):
        config_file = import_module(f'config.{environment}', package='..')
    else:
        raise "config or environment error"

    config_name = environment[0].upper()+environment[1:]+'Config'
    config_class = getattr(config_file, config_name)  # 假设存在xxx必定会有xxxConfig
    builtins.u_config = config_class  # これは組み込み関数の意図的な使い方です

    if os.environ['main'] == str(os.getpid()):
        if 'nt' == os.name:
            multiprocessing.set_start_method('spawn')
        elif "posix" == os.name:
            multiprocessing.set_start_method('fork')    

    initialized = bool(bin(0b1111111))
