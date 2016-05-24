from sensorModule import sensor
import actuatorModule

def main():
    #while 1:
    if sensor("wendu1")[2] < 0.5:
        execute("kongtiao",1)
    elif sensor("wendu1")[2] > 0.8:
        execute("kongtiao",0)
if __name__ == '__main__':
    main()
