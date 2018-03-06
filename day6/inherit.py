# author: zzq


# class People: # 经典类
class People(object):   # 新式类
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eating..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

class Relation(object):
    def make_friends(self, obj):
        print("%s is making friends with %s " % (self.name, obj.name))
        self.friends.append(obj)


class Man(People, Relation):

    # def __init__(self, name, age, money):
    #     # People.__init__(self, name, age)
    #     super(Man, self).__init__(name, age)
    #     self.money = money
    #     print("%s 一出生就有 %s money" % (self.name, self.money))

    def piao(self):
        print("%s is piaoing ...20s...done." % self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping...")


class Woman(Relation, People):

    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("NiuHanyang", 22)
# m1.eat()
# m1.piao()
# m1.sleep()

w1 = Woman("ChenRonghua", 26)
# w1.get_birth()

m1.make_friends(w1)

w1.name = "陈三炮"

print(m1.friends[0].name)