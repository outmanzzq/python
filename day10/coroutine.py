# author: zzq
# 协程

import time
import greenlet



def home():
    print("in func 1")
    time.sleep(5)   # get data from db
    print("home exec done")


def bbs():
    print("in func 1")
    time.sleep(2)


def login():
    print("in func 1")



