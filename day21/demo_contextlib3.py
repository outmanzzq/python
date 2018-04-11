#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 
from contextlib import closing, contextmanager
from urllib.request import urlopen


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()