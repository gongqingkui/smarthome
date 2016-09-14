from serialPortModule import serialSend


def execute(name,value):
    s = '%s%s'%(name,value)
    print 'execute:%s'%s
    return serialSend(bytes(s))
