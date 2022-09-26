import socket

#ローカルipアドレス
ip = socket.gethostbyname(socket.gethostname())
print(ip)

#グローバルipアドレス
ip = socket.gethostbyname("www.enat.org")
print(ip)