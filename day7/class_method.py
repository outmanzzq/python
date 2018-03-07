# author: zzq


class Dog(object):

    # n = 333
    name = "huazai"

    def __init__(self, name):
        self.name = name
        # self.n = 333

    @classmethod
    def eat(self):
        print("%s is eating %s" % (self.name, 'dd'))


d = Dog("ChenRonghua")
d.eat()