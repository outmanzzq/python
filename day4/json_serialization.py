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
# f.write(json.dump(info))

# print(json.dumps(info))
f.write(pickle.dumps(info))

f.close()