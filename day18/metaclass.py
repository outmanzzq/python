#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


if __name__ == '__main__':
    L = MyList()
    L.add(1)
    L.add(2)
    print(L)

    L2 = list()
    L2.add(1)
    print(L2)