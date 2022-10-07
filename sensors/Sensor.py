class Sensor(object):
    name = None
    type = None
    parentHandle = None

    def __init__(self, name, type):
        self.type = type
        self.name = type

    def init(self):
        self.parentHandle.writeLog("Sensor init not overwritten. Sensor type: ", self.type)

    def handle(self):
        self.parentHandle.writeLog("Sensor handle not overwritten. Sensor type: ", self.type)