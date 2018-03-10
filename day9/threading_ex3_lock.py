# author: zzq
#

import threading
import time


def run(n):
    lock.acquire()
    global num
    num += 1
    lock.release()


t_objs = []
num = 0
lock = threading.Lock()

for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" % i, ))
    t.setDaemon(True)   # 把当前线程设置为守护线程
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()


print("------- all threads has finished...", threading.current_thread(), threading.active_count())
time.sleep(3)
print("num:", num)

