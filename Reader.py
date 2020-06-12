from SerialCom import SerialCommunication
import time
import threading


class Reader:

    serialComObj = SerialCommunication()

    resDataDict = serialComObj.getResourceData()
    print(serialComObj.getRoomConData() + ' L/m')
    serialComObj.setPowState('Off')
    # print(resDataDict)
    # print(resDataDict['coldWater'])
    # print(resDataDict['hotWater'])
    # print(resDataDict['fuel'])
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
