import serial
#def serialSend(t,str):
def serialSend(str):
    #print  t.portstr
    t = serial.Serial('/dev/ttyACM0',9600)
    print "SerialSend:",str
    n = t.write(str)
    t.close()
    return n

if __name__ == '__main__':

    print serialSend('hello/n/r')
