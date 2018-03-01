# author: zzq

# data = open("yesterday", encoding="utf-8").read()
# f = open("yesterday2", 'a', encoding="utf-8")  # 文件句柄
#
# f.write("\nwhen i was young i listen to the radio\n")
#
# data = f.read()
#
# print('------read', data)
# f.close()

# f = open("yesterday2", 'r+', encoding="utf-8")  # 文件句柄
# f = open("yesterday2", 'w+', encoding="utf-8")  # 文件句柄
# f = open("yesterday2", 'a+', encoding="utf-8")  # 文件句柄
# f = open("yesterday2", 'rb')  # 二进制格式读，主要应用socket 网络传输

f = open("yesterday2", 'wb')  # 二进制格式读，主要应用socket 网络传输

f.write("hello binary\n".encode())
f.close()
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.write("----------diao--------\n")
# f.write("----------diao--------\n")
# f.write("----------diao--------\n")
# f.write("----------diao--------\n")
#
# print(f.tell())
# f.seek(10)
# print(f.tell())
# print(f.readline())
# f.write("should be at the begging of the line")
#
# f.close()

# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
#
# print(f.fileno())
#
# print(f.flush())


# for i in range(5):
#     print(f.readline())

# # low loop
# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print('===我是分割线====')
#         continue
#     print(line.strip())

# # high bige
# count = 0
# for line in f:
#     if count == 9:
#         print("======我是分割线======")
#         count += 1
#         continue
#     print(line)
#     count += 1



