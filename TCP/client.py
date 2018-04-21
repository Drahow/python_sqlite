#!/usr/bin/env python3
#-*-coding=utf-8-*-

import socket
import sys
import time

host = '127.0.0.1'
#设置主机名端口号
port = 9999
#s.connect((host,port))
while True:
#创建TCP套接字，基于IPV4协议
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务器
    s.connect((host,port))
    time.sleep(1)
    msg_send = input('Info want to send: ')
    if msg_send == 'end':
        break
    else:    
        s.send(('%s'%msg_send).encode('utf-8'))
        msg_recv = s.recv(1024)
        print(msg_recv.decode('utf-8'))
    
s.close()
