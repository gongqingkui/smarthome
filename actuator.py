from serialPort import serialSend
def activer(name,value):
    print name,value
    serialSend(name,value)
    return 

