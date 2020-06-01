import redis
import time
import json

r=redis.Redis(
    host='localhost',
    db=0)

sub_count=r.publish('nlp_test_pub',json.dumps({"type":"ping"}))

# while True:
#     time.sleep(2)
message=int(time.time())

_time=int(time.time())
task_name=f"nlp_test_pub_{_time}"
uid_list=task_name+'_list'

print('sub_count',sub_count)
for i in range(sub_count):
    print('push',i)
    r.lpush(uid_list,i)

r.expire(f"nlp_test_pub_{_time}",60)

r.publish('nlp_test_pub',json.dumps(
    {
        "type":"initialize",
        "code":200,
        "data":{
            "task_name":f"nlp_test_pub_{_time}",
            "uid_list":uid_list,
            "sub_count":sub_count,
            "user_id":9999
        }
    }
)
)