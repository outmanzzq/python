# author: zzq

# from module_alex import  logger as  logger_alex

# from module_alex import logger as logger_alex

import sys
import os

def logger():
    print('in the main')

print(sys.path)


x = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(x)

say_hello()
