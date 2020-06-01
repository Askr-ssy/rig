#-*- encoding: utf-8 -*-

import redis

r=redis.Redis(host='localhost',db=0)
p=r.pubsub()
p.subscribe('test')
for message in p.listen():
    print(message)