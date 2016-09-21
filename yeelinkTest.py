import json
import urllib2
import time
import random

apikey = 'b6984ebdde615e36eda3c7420e4a422b'
sensorURL = 'http://api.yeelink.net/v1.0/device/350986/sensor/394218/datapoints'
timeFormat = '%Y-%m-%dT%X'
timeString = time.strftime(timeFormat,time.localtime())
values = {'timestamp':timeString,'value':random.randint(-30,30)}
jdata = json.dumps(values)
print jdata

r = urllib2.Request(sensorURL,jdata)
r.add_header('U-ApiKey',apikey)

resp = urllib2.urlopen(r)
