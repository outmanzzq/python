# author: zzq


class Dog(object):
    """这个类的描述"""
    # n = 333
    name = "huazai"

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print("set to food:", food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

    def __call__(self, *args, **kwargs):
        print("running the call method", args, kwargs)

    def __str__(self):
        return "<obj:%s>" % self.name


d = Dog("ChenRonghua")

print(d)
# d(1, 2, 3, name=333)
# d.eat
# d.eat = "包子"
#
# d.eat
#
# del d.eat

# print(Dog.__dict__)  # 打印类里的所有属性，不包括实例属性
#
# print(d.__dict__)   # 打印所有实例属性，不包括类属性



