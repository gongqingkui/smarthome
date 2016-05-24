from serialPortModule import serialSend


def execute(name,value):
    print "execute",name,value
    serialSend(name,value)
    return 

