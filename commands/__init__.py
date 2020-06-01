import argparse
import os
import sys
import builtins

# path=lambda *a:os.path.join(u_ROOT_PATH,*a)

__all__=['bootstrap']

def get_options():
    parser = argparse.ArgumentParser(description='Process some integers.')
    
    # 环境
    parser.add_argument('-e','--env',dest='environment',default='localhost',type=str)

    args=parser.parse_args()
    
    return args

def bootstrap():
    from importlib import import_module
    args=get_options()
    os.environ['environment']=args.environment
    os.environ['main']=str(os.getpid())         # 区分主进程
    
    import config
    config.config_initialize()

    from . import router
    router.run()