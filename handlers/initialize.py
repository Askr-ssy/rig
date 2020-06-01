# -*- encoding: utf-8 -*-
import pymysql
import time
import builtins
import os
import sys
import requests
import json
import time

import config
from .base import BaseHandler

__all__ = []


def spell_sql(*args, **kwargs):
    """
    list=[]
    """
    if len(args[0]) <= 0:
        return None
    sql = "SELECT * from `emotion_data` WHERE id ={}".format(args[0][0])
    for index in args[0][1:]:
        sql += " or id ={}".format(index)
    return sql


def run(*args, **kwargs):
    """
    """
    start_time = time.time()

    if 'nt' == os.name and os.environ['main'] != str(os.getpid()):
        config.config_initialize()

    from utils.RedisHelper import RedisHelper
    from utils.MysqlHelper import MysqlHelper

    context = args[0]
    uid = args[1]
    r = RedisHelper()
    p = MysqlHelper()

    # prod,beta,
    print(context["data"]["user_id"], 'start uid is ', uid, context)
    sql = "SELECT `id` FROM `emotion_data` where userid='{}'".format(
        context["data"]["user_id"])
    try:
        p.cursor.execute(sql)
        datas = p.cursor.fetchall()
    except Exception as e:
        print(repr(e))
        datas = []
        # 日志报错 #
    finally:
        pass
        # datas=datas[0]
    # 映射id 待优化 通用型
    datas_list = [value[0] for index, value in enumerate(
        datas) if index % context["data"]["sub_count"] == uid]  # 根据uid分配测试数据条例
    sql = spell_sql(datas_list)
    if not sql:
        return
    try:
        p.cursor.execute(sql)
        datas = p.cursor.fetchall()
    except Exception as e:
        print(repr(e))
        datas = []
    print('datas has ', len(datas))
    Result = [[], [], []]
    for data in datas:
        request_data = {
            "title": data[2],
            "content": data[3],
            "type": data[7],
            "cid": data[9],
            "is_debug": 1,
            "data": context["data"]["config_data"]
        }
        index = datas.index(data)
        index = datas_list[index]
        # 请求待优化至通用
        request_data = json.dumps(request_data)
        try:
            time.sleep(0.01)
            response = requests.post(url=u_config.NLP_URL,
                                     data=request_data, headers=u_config.NLP_HEADERS)
            if response.status_code != 200:
                print(request_data)
                print('continue')

            sentiment = json.loads(response.text)
            label = sentiment["emotion"]
        except Exception as e:
            print("error continue", repr(e))
            # 优化error
            continue
        try:
            p.cursor.execute(
                f"UPDATE emotion_data SET lastEmotion='{label}' WHERE id={index}")
            p.conn.commit()
        except Exception as e:
            print("UPDATE error", repr(e))

        r.conn.hset(context["data"]["task_name"],
                    data[0], json.dumps(sentiment))
        Result[0].append(label)    # 结果聚合待优化通用     #新机器
        Result[1].append(data[1] if "" != data[1] else data[-1])  # 人工
        Result[2].append(data[0])   # id
    r.conn.expire(context["data"]["task_name"],2592000)# 定时一周
    r.conn.hset(context["data"]["task_name"], f"info_{uid}", json.dumps(
        Result
    ))
    print(time.time()-start_time)
    # 待优化结果获取    字符串获取
