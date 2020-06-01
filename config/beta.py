# -*- encoding: utf-8 -*-
from .base import BaseConfig

class BetaConfig(BaseConfig):
    MYSQL_HOST='192.168.2.16'
    MYSQL_ACCOUNT='ssy'
    MYSQL_PASSWORD='ssy@1data.info201811'
    MYSQL_DATABASE='nlpm'
    MYSQL_PORT=3306

    # redis链接
    REDIS_HOST='redis.service'
    REDIS_ACCOUNT=''
    REDIS_PASSWORD=None
    REDIS_PORT=6379
    REDIA_DB=0

    # log 
    LOG_LEVEL='INFO'
    LOG_FILE=None

    NLP_URL="http://nlp.default:5000"