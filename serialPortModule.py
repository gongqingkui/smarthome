def serialSend(name,value):
    #print "serialSend ",value," to ",name
    serialSend("SerialSend",value,"to",name)
    return 


def serialInit():  
    import serial
    t = serial.Serial('/dev/ttyACM0',9600)
    print  t.portstr
    return t
    

def serialSend(str):
    t = serialInit()
    n = t.write(str)
    str = t.read(20)
    return n
def serialSend(str1,str2):
    t = serialInit()
    n = t.write(str1+str2)
    str = t.read(20)
    return n
