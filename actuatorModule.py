from serialPortModule import serialSend


def execute(name,value):
    print name,value
    serialSend(name,value)
    return 

