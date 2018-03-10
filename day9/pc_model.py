# author: zzq
# 生产者与消费者模型

import threading
import queue
import time


def producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头", count)
        count += 1
        time.sleep(1)


def consumer(name):
    while True:
        print("[%s] 取到[ %s],并且吃了它。。。" % (name, q.get()))
        time.sleep(1)


q = queue.Queue()

p = threading.Thread(target=producer, args=("Alex",))
c = threading.Thread(target=consumer, args=("ChenRonghua",))
c1 = threading.Thread(target=consumer, args=("王森",))

p.start()
c.start()
c1.start()
