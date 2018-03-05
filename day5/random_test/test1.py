# author: zzq
# 使用 random 产生随机验证码

import random

checkcode = ''

for i in range(5):
    # current = random.randint(1,9)
    current = random.randrange(0, 5)

    # 字母
    if current == i:
        tmp = chr(random.randint(65, 90))
    # 数字
    else:
        tmp = random.randint(0, 9)

    checkcode += str(tmp)

print(checkcode)