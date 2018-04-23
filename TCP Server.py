# coding=utf-8
# 建立一个 TCP Server

import socket
import threading
import time
# import sys

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #建立连接
# s.connect(('www.sina.com.cn',80))

# 监听端口
s.bind(('0.0.0.0', 8088))
s.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
