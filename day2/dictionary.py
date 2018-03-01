# author: zzq


info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya"
}
#
# b = {
#     'stu1101': "Alex",
#     1: 3,
#     2: 5
# }
#
# info.update(b)
#
# print(info)
#
# c = dict.fromkeys([6, 7, 8], [1, {"name": "alex"}, 444])
# print(c)
#
# c[7][1]['name'] = "Jack Chen"
# print(c)
#print(info.items())

"""
print(info.get('stu1104'))

print('stu1103' in info)


# print(info["stu1101"])
info["stu1101"] = "武藤兰"
info["stu1104"] = "CangJingkong"

# del
# del info["stu1101"]
# info.pop("stu1101")
# info.popitem()

print(info)

"""
"""
av_catalog = {
    "欧美": {
        "www.abc.com": ["质量一般，片源很多", "访问速度慢"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚", "个人不喜欢日韩"]
    },
    "大陆": {
        "1024": ["全部免费，真好，好人一生平安", "服务器在国外，慢"]
    }
}

av_catalog["大陆"]["1024"][1] = "可以在国内做镜像"

av_catalog.setdefault("大陆", {"www.baidu.com":[1,2]})

print(av_catalog)
"""

for i in info:
    print(i, info[i])
