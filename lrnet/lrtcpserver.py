# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket
import socket
import threading

import time

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('waiting for connection..')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)


while True:
    sock, addr = s.accept()

    t = threading.Thread(target=tcplink, args=(sock,addr))
    t.start()


