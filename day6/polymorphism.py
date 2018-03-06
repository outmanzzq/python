# author: zzq


class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


d = Dog("Chen")
# d.talk()

c = Cat("Xuliangwei")
# c.talk()


Animal.animal_talk(c)
Animal.animal_talk(d)



