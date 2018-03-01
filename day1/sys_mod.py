# author: zzq

"""
import sys

#print(sys.path)

print(sys.argv)
print(sys.argv[2])
"""

"""
import os

# cmd_res = os.system("ls")
cmd_res = os.popen("ls").read()

print("-->", cmd_res)

# os.mkdir("new_dir")
"""

msg = "我爱北京天安门"

print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))
