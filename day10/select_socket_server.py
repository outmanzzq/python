# -*- coding:utf-8 -*-
# author: zzq
# socket server，存在客户端断开，server 死循环问题

import select
import socket
import queue


server = socket.socket()
server.bind(('localhost', 9000))
server.listen(1000)

server.setblocking(False)   # 不阻塞

msg_dic = {}

inputs = [server, ]
# inputs = [server, conn, conn2]
outputs = []

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    print(readable, writeable, exceptional)

    for r in readable:

        if r is server: # 代表来了一个新连接
            conn, addr = server.accept()
            print("来来个新连接", addr)
            inputs.append(conn)     # 是因为这个新建立的连接还没发数据过来，现在接收的话就报错
            # 所以，要想实现这个客户端发数据来时server端能知道，就需要让select再检测这个连接
            msg_dic[conn] = queue.Queue()   # 初始化一个队列，后面存要返回给这个客户端的数据
        else:
            data = r.recv(1024)
            print("收到数据", data)
            msg_dic[r].put(data)

            outputs.append(r)
            # r.send(data)
            # print("send data done")

    for w in writeable:     # 要返回给客户端的连接列表
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)  # 返回给客户端源数据
        outputs.remove(w)   # 确保下次循环的时候 writeable 不返回已经处理完的连接

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)

        inputs.remove(e)

        del msg_dic[e]
