class Altitude:
    method = None
    sensorHandle = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        self.sensorHandle = self.coreHandle.sensorSystem.getSensorByPurpose("altitude")

    def loadConfig(self, config):
        if 'altitude-method' in config:
            self.method = config['altitude-method'].lower()

    def handle(self):
        if self.sensorHandle != None:
            Navigation.currentHeight = self.sensorHandle.getDistance()