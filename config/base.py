# -*- encoding: utf-8 -*-


class BaseConfig(object):
    # mysql数据库链接

    MYSQL_HOST = ''
    MYSQL_ACCOUNT = ''
    MYSQL_PASSWORD = ''
    MYSQL_DATABASE = ''
    MYSQL_PORT = 3306

    # redis链接
    REDIS_SUB = 'nlp_task_pub'
    REDIS_HOST = ''
    REDIS_SENTIENEL = []
    REDIS_MASTER = ""    
    REDIS_ACCOUNT = ''
    REDIS_PASSWORD = ''
    REDIS_PORT = 6379
    REDIA_DB = 0

    # log
    LOG_LEVEL = 'INFO'
    LOG_FILE = None

    NLP_URL = ""
    NLP_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'nlp.beta.1datatech.cn',
        'Content-Type': 'application/json'
    }

    def __init__(self):
        pass
