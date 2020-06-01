# -*- encoding: utf-8 -*-

import redis
from redis.sentinel import Sentinel

import os
import builtins
import config


class RedisHelper(object):
    def __init__(self):
        # self.pool=redis.ConnectionPool(host=u_config.REDIS_HOST,port=u_config.REDIS_PORT,password=u_config.REDIS_PASSWORD,db=u_config.REDIA_DB)
        # self.conn=redis.Redis(connection_pool=self.pool)
        self.sentinel = Sentinel(u_config.REDIS_SENTIENEL)
        host = self.sentinel.discover_master(u_config.REDIS_MASTER)
        self.conn = redis.Redis(
            host=host[0], port=host[1], password=u_config.REDIS_PASSWORD, db=u_config.REDIA_DB)
        # self.master = self.sentinel.master_for(u_config.REDIS_MASTER, socket_timeout=0.5, port=u_config.REDIS_PORT,
        #                                        password=u_config.REDIS_PASSWORD, db=u_config.REDIA_DB)
        # self.slave = self.sentinel.slave_for(u_config.REDIS_MASTER, socket_timeout=0.5, port=u_config.REDIS_PORT,
        #                                      password=u_config.REDIS_PASSWORD, db=u_config.REDIA_DB)
        # self.conn = self.master
        self.sub_name = u_config.REDIS_SUB
        print(self.sub_name)
        if not self.conn.ping():
            raise "redis conn error"
