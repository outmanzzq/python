# author: zzq

# _*_coding:utf-8_*_

user_status = False

def login(auth_type):

    def auth(func):
        def inner(*args, **kwargs):
            if auth_type == "qq":
                _username = "alex"
                _password = "abc!23"

                global user_status

                if user_status == False:
                    username = input("user:")
                    password = input("password:")

                    if username == _username and password == _password:
                        print("welcome login...")
                        user_status = True
                    else:
                        print("wrong username or password")
                        exit(0)

                if user_status == True:
                    return func(*args, **kwargs)
            else:
                print("only support qq! ")
        return inner
    return auth

def home():
    print("-----首页------")

@login("qq")
def america():
    print("------欧美专区------")

def japan():
    print("------日韩专区------")

@login("weibo")
def henan(style):
    print("------河南专区------")

home()

america()

japan()

henan("3p")

