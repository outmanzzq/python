# -*- coding:utf-8 -*-
# author: zzq
# 


import redis

pool = redis.ConnectionPool(host='localhost', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'wupeiqi')

pipe.set('role', 'sb')

pipe.execute()


