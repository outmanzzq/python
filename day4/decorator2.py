# author: zzq
import time

# def bar():
#     time.sleep(3)
#     print('in the bar')
#
# def test1(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#
#     print("the func run time is %s " %(stop_time - start_time))
#
# test1(bar)

def bar():
    time.sleep(3)
    print('in the bar')

def test2(func):
    print(func)
    return func

# print(test2(bar))
bar = test2(bar)

bar()