# author: zzq

import pickle

def sayhi(name):
    print("hello2,", name)


f = open("test.txt", "rb")

data = pickle.load(f)

print(data["func"]("alex"))

