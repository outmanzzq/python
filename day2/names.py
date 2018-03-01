# author: zzq

import copy

names = ["4ZhangYang", "#!Guyun", "xXiangPeng", ["alex", "jack"], "ChenRonghua", "XuLiangchen"]

print(names[:])

for i in names:
    print(i)

"""
names2 = copy.deepcopy(names)

print(names)
print(names2)

names[2] = "向鹏"
names[3][0] = "ALEXANDER"

print(names)
print(names2)



names.append("LeiHaidong")
names.insert(1, "ChenRonghua")
names.insert(3, "Xinzhiyu")

#names[2] = "XieDi"

print(names)
# print(names[0], names[2])
# print(names[1:3])   # 切片
# print(names[0:3])   # 切片
# print (names[3])   # 切片#
# print(names[-1])   # 切片
# print(names[-2])   # 切片
# print(names[-2:])   # 切片
# print(names[:3])   # 切片

# delete
# names.remove("ChenRonghua")
# del names[1]

# names.pop(1)

names.reverse()
names.sort()
print(names)
# print(names[names.index("XieDi")])
# print(names.count("ChenRonghua"))

names2 = [1, 2, 3, 4]

#names.extend(names2)
print(names, names2)
"""