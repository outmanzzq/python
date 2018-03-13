# author: zzq
# greenlet 协程(手动）

from greenlet import greenlet


def test1():
    print(12)       # 1
    gr2.switch()
    print(34)       # 3
    gr2.switch()


def test2():
    print(56)       # 2
    gr1.switch()
    print(78)       # 4


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()    # 0



