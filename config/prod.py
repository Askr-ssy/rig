# -*- encoding: utf-8 -*-

from .base import BaseConfig

class ProdConfig(BaseConfig):
    MYSQL_HOST='192.168.1.80'
    MYSQL_ACCOUNT='ssy'
    MYSQL_PASSWORD='ssy@1data.info201811'
    MYSQL_DATABASE='nlpm'
    MYSQL_PORT=3306

    # redis链接
    REDIS_HOST='redis.service'
    REDIS_SENTIENEL = [('192.168.1.135', 26379), ('192.168.1.224', 26379), ('192.168.1.53',26379)]
    REDIS_MASTER = "mymaster"    
    REDIS_ACCOUNT=''
    REDIS_PASSWORD="redis1datainfo"
    REDIS_PORT=6379
    REDIA_DB=0

    # log 
    LOG_LEVEL='INFO'
    LOG_FILE=None

    NLP_URL="http://mynlp:5000"
