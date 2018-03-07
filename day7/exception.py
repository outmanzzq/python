# author: zzq

names = ['alex', 'jack']
data = {}
# names[3]

try:
    # names[3]
    # data['name']
    # open("tes.txt")
    a = 1
    print(a)
except KeyError as e:
    print("没有这个key %s", e)
except IndexError as e:
    print("列表操作错误", e)
except Exception as e:
    print("未知错误", e)
else:
    print("一切正常")

finally:
    print("不管有没错，都执行。。。")




