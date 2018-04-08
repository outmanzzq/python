#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simson', 59)
lisa = Student('Lisa Simson', 87)

bart.print_score()
lisa.print_score()

print(bart.get_score())

bart.__score = 99

print(bart.__score)

print(bart.get_score())

