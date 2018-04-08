#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 使用 __slots__ 变量，来限制class实例能添加的属性


class Student(object):
    __slots__ = ('name', 'age')


