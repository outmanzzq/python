# author: zzq


class Dog(object):

    def __init__(self, name):
        self.name = name

    @staticmethod   # 实际上跟类没什么关系
    def eat(self):
        print("%s is eating %s" % (self.name, 'dd'))


d = Dog("ChenRonghua")
d.eat(d)

