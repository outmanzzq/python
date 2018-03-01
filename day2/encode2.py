# author: zzq
# -*-coding:gbk-*-
import sys
print(sys.getdefaultencoding())

s = "你好"
print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))
