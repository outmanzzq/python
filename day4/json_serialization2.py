# author: zzq

import pickle

def sayhi(name):
    print("hello,", name)

info = {
    'name': 'alex',
    'age': 22,
    'func': sayhi
}

f = open("test.txt", "wb")

pickle.dump(info, f)

f.close()