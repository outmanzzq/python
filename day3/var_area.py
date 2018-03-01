# author: zzq

school = "Oldboy edu."

# def change_name(name):
#     global school
#     school = "Mage school"
#     print("before change", name, school)
#     name = "Alex li"
#     print("after change", name)
# print(name)
# print("school:", school)

# 列表及字典可以在函数内部修改
names = ["Alex", "Jack", "Rain"]
def change_name():
    names[0] = "金角大王"
    print("inside func", names)

change_name()

print(names)



