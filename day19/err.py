#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# if __name__ == '__main__':
#     bar('0')

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s ' % s)
#     return 10 / n
#
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('Value!')
#         raise
#
#
# bar()

# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
#
# if __name__ == '__main__':
#     foo('0')

# import logging
#
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

import pdb

s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)