# author: zzq


# class Foo(object):
#
#     def __init__(self, name):
#         self.name = name
#
#
# f = Foo("alex")
#
# print(type(f))
# print(type(Foo))

def func(self):
    print('hello alex')


def __init__(self, name, age):
    self.name = name
    self.age = age


Foo = type('Foo', (), {'talk': func, '__init__': __init__})
# type第一个参数：类名
# type第二个参数：当前类的基类
# type第三个参数：类的成员

print(type(Foo))

f = Foo("Chrn", 22)
f.talk()
