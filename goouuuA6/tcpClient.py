import socket
#host="192.168.1.3"
#port=1234
host="gongqingkui.vicp.cc"
port=15048
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send("hello from client with gongqingkui.vicp.cc:15048")
s.close()
