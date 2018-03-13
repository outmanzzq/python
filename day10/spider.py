# -*- coding:utf-8 -*-
# author: zzq
# 爬虫


from gevent import monkey   # 打异步补丁
import gevent
from urllib.request import urlopen
import time

monkey.patch_all()  # 把当前程序的所有的 IO 操作给我单独的做上标记


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])

print("异步：", time.time()-async_time_start)




