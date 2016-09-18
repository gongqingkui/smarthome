import serial
from time import sleep

def serialRead():
    t = serial.Serial('/dev/ttyUSB1',9600)
    print t.isOpen()
    with t:
        while(1):
            s = t.readline()
            print s
            #if s[0]=='T':
                
            #elif s[0]=='H':
                
            #elif s[0]=='F':
            sql = "insert into hcho values(,%s,%s)"%('2011','22')
            print sql

if __name__ == '__main__':
    serialRead()
