import socket
host="192.168.1.3"
port=1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send("hello from client")
s.close()
