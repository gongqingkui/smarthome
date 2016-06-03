import serial
t = serial.Serial('/dev/ttyACM0',9600)
print t.portstr
n = t.write('AT')
str = t.read(20)
print str
t.close()
