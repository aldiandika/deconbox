class GlobalVariables:

    def __init__(self, dataTest=0):
        self._dataTest = dataTest

    def get_dataTest(self):
        return self._dataTest

    def set_dataTest(self, setData):
        self._dataTest = setData
