# author: zzq


class Foo(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()


obj['k2'] = 'alex'  # 自动触发执行 __setitem__
# result = obj['k1']  # 自动触发执行 __getitem__
del obj['k1']