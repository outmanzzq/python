# author: zzq
# 队列

import queue
import time

q = queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)

while q.qsize() > 0:
    print(q.get())
    time.sleep(1)

