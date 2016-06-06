from serialPortModule import serialSend


#def execute(t,name,value):
def execute(name,value):
    print "execute:",name,value
    s = '%s%s'%(name,value)
    #return serialSend(t,bytes(s))
    return serialSend(bytes(s))
