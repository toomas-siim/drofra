class Altitude:
    method = None
    sensorHandle = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        if self.method == "ultrasonic":
            self.sensorHandle = self.coreHandle.sensorSystem.getSensorByType("SENS_ULTRASONIC")

    def loadConfig(self, config):
        if 'altitude-method' in config:
            self.method = config['altitude-method'].lower()

    def handle(self):
        Navigation.currentHeight = self.sensorHandle.getDistance()