from SerialCom import SerialCommunication
import time
import threading


class Reader:

    serialComObj = SerialCommunication()
    # x = 12

    # dataResource = '12 15 17'

    # cw, hw, fuel = dataResource.split()

    # dictData = dict()
    # dictData['coldWater'] = cw
    # dictData['hotWater'] = hw
    # dictData['fuel'] = fuel
    # cwData = [dataRList[i] for i in dataRList]
    # print(cw)

    # for x in dictData:
    #     print(dictData[x])
