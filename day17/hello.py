#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
#

print(u'中文测试正常')


bmi = 30.232864329827276

if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >=28 and bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
