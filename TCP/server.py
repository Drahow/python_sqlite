#!/usr/bin/env python3
#-*-coding:utf-8-*-

import socket
import time
import threading

#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取树莓派主机名
#host = socket.gethostname()
host = '127.0.0.1'
#设置端口号
port = 9999

#绑定服务器地址和端口号
s.bind((host,port))

#监听，指定等待最大连接数5
s.listen(5)

def tcplink(sock, addr):
    print('Accept new connection from %s:%s ' %addr)
    msg_recv = sock.recv(1024)
    sock.send(('Welcome %s' %msg_recv.decode('utf-8')).encode('utf-8'))
    while True:
        time.sleep(1)
        if msg_recv.decode('utf-8') == 'end':
            break

    sock.close()
while True:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args=(sock, addr))
    t.start()
  
