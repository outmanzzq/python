#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


class Student(object):
    def __init__(self, name):
        self.name = name


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)


if __name__ == '__main__':
    s = Student('Michael')
    s()

    callable(Student('Michael'))
    # True
    callable(max)
    # True
    callable([1, 2, 3])
    # False
    callable(None)
    # False
    callable('str')
    # False