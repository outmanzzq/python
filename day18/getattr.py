#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \' %s \'' % attr)


if __name__ == '__main__':
    s = Student()
    print(s.age())
    print(s.abc)