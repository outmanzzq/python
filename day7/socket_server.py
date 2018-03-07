# author: zzq


import socket
import os

server = socket.socket()
server.bind(('localhost', 6969))    # 绑定要监听端口
server.listen()     # 监听

print("我要开始等电话了")

while True:
    conn, addr = server.accept()     # 等电话打进来

    while True:
        # conn 就是客户端连过来，而在服务器端为其生成的一个连接实例
        # print(conn, addr)

        print("电话来了")

        data = conn.recv(1024)

        print("recv:", data)

        if not data:
            print("client has lost...")
            break
        # res = os.popen(data).read()
        conn.send(data)

server.close()