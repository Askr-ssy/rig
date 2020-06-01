# -*- encoding: utf-8 -*-
from .base import BaseConfig


class DevConfig(BaseConfig):
    MYSQL_HOST = '192.168.2.229'
    MYSQL_ACCOUNT = 'web'
    MYSQL_PASSWORD = 'ES$v1J8j'
    MYSQL_DATABASE = 'nlp_m_beta'
    MYSQL_PORT = 3306

    # redis链接
    REDIS_HOST = 'redis.service'
    REDIS_ACCOUNT = ''
    REDIS_SENTIENEL = [('192.168.2.40', 26379),
                       ('192.168.2.115', 26379), ('192.168.2.91', 26379)]
    REDIS_MASTER = "mymaster"
    REDIS_PASSWORD = None
    REDIS_PORT = 6379
    REDIA_DB = 0

    # log
    LOG_LEVEL = 'INFO'
    LOG_FILE = None

    NLP_URL = "http://nlp.default:5000"
