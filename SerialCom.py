import serial
import time
from multiprocessing import Process
from threading import Thread

from GlobalVars import GlobalVariables

try:
    # On Linux
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    
    #On Windows
    #ser = serial.Serial('COM4', 9600, timeout=1)
except:
    print('Cannot Open Serial Port')


class SerialCommunication:

    def __init__(self):
        pass

    # Get Dirty Room State Data
    def getStDirtyState(self):
        # print('Ok From Serial Communication 2')
        try:
            ser.write(str('a').encode())
            dataSer = ser.readline()[:-2].decode()

            while dataSer == '':
                ser.write(str('a').encode())
                dataSer = ser.readline()[:-2].decode()

            if dataSer:
                # ser.close()
                return dataSer
        except:
            pass

        return 'no-data'

    # Get Shower Room State Data
    def getStShowerState(self):
        # print('Ok From Serial Communication 2')
        try:
            ser.write(str('b').encode())
            dataSer = ser.readline()[:-2].decode()

            while dataSer == '':
                ser.write(str('b').encode())
                dataSer = ser.readline()[:-2].decode()

            if dataSer:
                # ser.close()
                return dataSer
        except:
            pass

        return 'no-data'

    # Get Clean Room State Data
    def getStCleanState(self):
        # print('Ok From Serial Communication 2')
        try:
            ser.write(str('c').encode())
            dataSer = ser.readline()[:-2].decode()

            while dataSer == '':
                ser.write(str('c').encode())
                dataSer = ser.readline()[:-2].decode()

            if dataSer:
                # ser.close()
                return dataSer
        except:
            pass

        return 'no-data'

    def getResourceData(self):
        try:
            ser.write(str('d').encode())
            dataSer = ser.readline()[:-2].decode()

            while dataSer == '':
                ser.write(str('d').encode())
                dataSer = ser.readline()[:-2].decode()

            if dataSer:
                dataResource = dataSer
                cw, hw, fuel = dataResource.split()

                dictData = dict()
                dictData['coldWater'] = cw
                dictData['hotWater'] = hw
                dictData['fuel'] = fuel

                return dictData
        except:
            pass

    def getRoomConData(self):
        try:
            ser.write(str('e').encode())
            dataSer = ser.readline()[:-2].decode()

            while dataSer == '':
                ser.write(str('e').encode())
                dataSer = ser.readline()[:-2].decode()

            if dataSer:
                return dataSer
        except:
            pass

    def setPowState(self, var):
        if var == 'On':
            st = 'p'
        elif var == 'Off':
            st = 'f'

        try:
            ser.write(str(st).encode())
        except:
            pass
    # Thread(target=startSerialData).start()
