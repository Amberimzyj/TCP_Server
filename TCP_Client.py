# -*- coding: utf-8 -*-
# @Author: Amberimzyj
# @Emial:  amberimzyj@outlook.com
# @Date:   2018-04-23 13:10:31
# @Last Modified by:   Amberimzyj
# @Last Modified time: 2018-04-26 21:06:23
# @License: MIT LICENSE
# 创建一个客户端接收服务器数据
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
ip = socket.gethostbyname(socket.gethostname())
s.connect((ip, 8088))
# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Amber\r\n', b'Susan\r\n', b'Shlll\r\n']:
    # 发送数据
    s.send(data)
    # print(s.recv(1024).decode('utf-8'))
# s.send(b'exit\r\n')
s.close()
