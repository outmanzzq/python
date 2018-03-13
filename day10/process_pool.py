# author: zzq
# 


from multiprocessing import Process, Pool
import time
import os


def foo(i):
    time.sleep(2)
    print("in process %s" % os.getpid())
    return i + 100


def bar(arg):
    print('-->exec done:', arg, os.getpid())


if __name__ == '__main__':
    pool = Pool(3)
    print("主进程", os.getpid())

    for i in range(10):
        pool.apply_async(func=foo, args=(i,), callback=bar)
        # pool.apply(func=foo, args=(i,))

    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。

