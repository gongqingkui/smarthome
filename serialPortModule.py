import serial
from time import sleep

def serialSend(str):
    #t = serial.Serial('/dev/ttyACM0',9600)
    t = serial.Serial('/dev/ttyUSB0',9600)
    with t:
        n = t.write(str)
    t.close()
    return n

if __name__ == '__main__':
    print serialSend('sgongqingkui/n/r')
