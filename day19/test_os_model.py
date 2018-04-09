#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 


"""
>>>os.path.abspath('.')
'/Users/outman_o/scripts/python'
>>>[x for x in os.listdir('.') if os.path.isdir(x)]
['day4', 'day3', 'day2', 'day5', 'day12', 'day15', 'day14', 'day13', 'day7', 'day9', 'day8', 'day6', 'day1', '.git', 'day18', 'day16', 'day11', 'day10', 'day17', 'day19', '.idea']

>>>[x for x in os.listdir('/Users/outman_o/scripts/python/day19') if os.path.splitext(x)[1] == '.py']
['mydict_test.py', 'mydict.py', 'test_fact.py', 'mydict2.py', 'error_handling.py', 'test_unit.py', 'test_file.py', 'err.py']
"""

