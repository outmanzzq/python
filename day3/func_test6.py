# author: zzq

def test(x, y=2):
    print(x)
    print(y)

test(1,3)

# 默认参数特点： 调用函数的时候，默认参数非必须传递
# 用途：1. 默认安装值 2. 数据库连接默认端口号