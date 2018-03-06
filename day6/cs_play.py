# author: zzq

class Role(object):

    n = 123  # 类变量
    name = "我是类name"
    n_list = []

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        # 构造函数
        #
        self.name = name    # 实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def __del__(self):
        pass  # print("%s 彻底死了……" % self.name)

    def show_status(self):
        print("name: %s weapon: %s life_val: %s" %(self.name,
                                                   self.weapon,
                                                   self.__life_value))


    def shot(self): # 类的方法（动态属性）
        print("shooting...")

    def got_shot(self):
        self.__life_value -= 50
        print("%s ah...,I got shot..." % self.name)

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name, gun_name))
#
# print(Role.n)
#
#
# r1 = Role('Alex', 'police', 'AK47')
# r1.name = "陈荣华"
# r1.bullet_prove = True
#
# r1.n = "改类变量"
# r1.n_list.append("from r1")
#
#
# # print(r1.weapon)
# # del r1.weapon
# # print(r1.weapon)
#
# print("r1: %s"% r1.n, r1.name, r1.bullet_prove)
#
# r2 = Role('Jack', 'terrorist', 'B22')
#
# r2.n_list.append("from r2")
#
# print(r2.n, r2.name)
# # r2.got_shot()
#
# # r1.got_shot()
# # r1.buy_gun("AK47")
#
#
# print(r2.n_list)
#
# Role.n = "ABC"
#
# print(r1.n, r2.n)
#
# print(Role.n_list)

r1 = Role('Alex', 'police', 'AK47')
r1.buy_gun("AK47")
r1.got_shot()

print(r1.show_status())


r2 = Role('Jack', 'terrorist', 'B22')
r2.got_shot()


