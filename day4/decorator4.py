# author: zzq

import time

def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time %s" %(stop_time-start_time))
    return deco

@timer
def test1():
    time.sleep(3)
    print('in the test1')

# @timer
# def test2():
#     time.sleep(3)
#     print('in the test2')


test1()
# test2()

# test1 = deco(test1)
# test1()
#
# test2 = deco(test2)
# test2()
