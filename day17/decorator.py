#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

import functools, types


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text, types.FunctionType):
                print('call %s():' % func.__name__)
            else:
                print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    if not isinstance(text, types.FunctionType):
        return decorator
    else:
        return decorator(text)


@log
def now1():
    print('2019-04-05')


now1()


@log('execute')
def now():
    print('2018-04-05')


now()
