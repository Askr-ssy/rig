# -*- encoding: utf-8 -*-

import pymysql
import os
import config

class MysqlHelper(object):
    def __init__(self):
        self.conn=pymysql.connect(u_config.MYSQL_HOST,u_config.MYSQL_ACCOUNT,u_config.MYSQL_PASSWORD
        ,u_config.MYSQL_DATABASE,u_config.MYSQL_PORT)
        self.cursor=self.conn.cursor()
        
        
        if self.conn.ping():
            raise "mysql conn error"
