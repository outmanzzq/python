#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

from contextlib import contextmanager


@contextmanager
def tag(name):
    print("<%s>" %name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")
