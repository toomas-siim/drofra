class Sensor(object):
    name = None
    coreHandle = None
    sensorData = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        self.coreHandle.writeLog("Sensor init not overwritten. Sensor type: ", self.type)

    def handle(self):
        self.coreHandle.writeLog("Sensor handle not overwritten. Sensor type: ", self.type)

    def getPinData(self):
        if self.sensorData == None:
            return None
        return self.sensorData["pinData"]

    def getPinByType(self, type):
        for pin in self.getPinData():
            if pin["type"] == type:
                return pin["pin"]