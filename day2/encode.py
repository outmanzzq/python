# -*- coding:gbk -*-
# author: zzq
import sys

print(sys.getdefaultencoding())

s = "你好"
s_gbk = s.encode("gbk")

print(s)
print(s.encode())

gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print("utf8", gbk_to_utf8)
