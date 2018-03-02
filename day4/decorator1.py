# author: zzq


def foo():
    print('in the foo')
    bar()

def bar():
    print('in the bar')

foo()


# 匿名函数
calc = lambda x:x*3

print(calc(3))
