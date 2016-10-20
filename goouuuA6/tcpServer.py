import socket
host=""
port=1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print "Listening..."
while 1:
    i=1
    sock,addr=s.accept()
    print "got connection form ",sock.getpeername()
    while 1:
        data=sock.recv(1024)
        if not data:
            break
        else:
            print "Line",i,":",data
        i+=1
    print "Connection form ",sock.getpeername()," Over"
    print "Listening..."
