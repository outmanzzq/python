# author: zzq
# 动态导入模块

import importlib

aa = importlib.import_module('lib.aa')

print(aa.C().name)

