# -*- encoding: utf-8 -*-

from .base import BaseConfig


class LocalConfig(BaseConfig):
    MYSQL_HOST = 'localhost'
    MYSQL_ACCOUNT = 'askr'
    MYSQL_PASSWORD = '3933030'
    MYSQL_DATABASE = 'nlpm'
    MYSQL_PORT = 3306

    # redis链接
    REDIS_HOST = 'localhost'
    REDIS_ACCOUNT = ''
    REDIS_SENTIENEL = [('192.168.1.209', 28379),
                       (',192.168.1.209', 28380),(',192.168.1.209', 28381)]
    REDIS_MASTER = "mymaster"
    REDIS_PASSWORD = '123456'
    REDIS_PORT = 6379
    REDIA_DB = 0

    # log
    LOG_LEVEL = 'INFO'
    LOG_FILE = None

    NLP_URL = "http://127.0.0.1:5000"
    # NLP_URL="http://218.78.13.33:30080/"
