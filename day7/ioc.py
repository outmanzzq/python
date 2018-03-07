# author: zzq


def bulk(self):
    print("%s is bulking..." % self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating..." % self.name, food)


d =Dog("NiuHanYang")
choice = input(">>:").strip()


if hasattr(d, choice):
    # func = getattr(d, choice)
    # func("ChenRonghua")
    # attr = getattr(d, choice)
    # setattr(d, choice, "Ronghua")
    delattr(d, choice)
else:
    # setattr(d, choice, bulk)
    # d.talk(d)
    setattr(d, choice, 22)
    print(getattr(d, choice))

print(d.name)