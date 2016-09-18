import serialPortModule
import time
import random


def sensor(name):
    value = random.random()
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    r = (555,date,value)
    return r
