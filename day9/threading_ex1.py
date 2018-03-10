# author: zzq
# 多线程demo

import threading
import time


def run(n):
    print("task", n)
    time.sleep(2)
    print("task done", n)


start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i, ))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("------- all threads has finished...")
print("cost time", time.time() - start_time)

