# author: zzq
# 通过类调用多线程

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n, sleep_time):
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print("running on number:%s" % self.n)
        time.sleep(self.sleep_time)
        print("task done...", self.n)


t1 = MyThread("t1", 2)
t2 = MyThread("t1", 4)

t1.start()
t2.start()

t1.join()   # 等待子线程执行结果
t2.join()

print("main thread...")





