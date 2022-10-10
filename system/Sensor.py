class Sensor:
    SENSOR_TYPES = ["SENS_COMPASS", "SENS_ULTRASONIC", "SENS_GYRO", "SENS_GPS", "SENS_ATMOS", "SENS_ACCELERO"]
    sensors = []
    coreHandle = None

    def initSensorSystem(self, coreHandle):
        self.coreHandle = coreHandle

    def handle():
        for sensorData in Sensor.sensors:
            sensorData.handle.handle()

    def getSensorHandleByType(self, type):
        for sensor in self.sensors:
            if sensor.sensorType == type:
                return type
        return None

    def addSensor(self, pinData, sensorType):
        sensorHandle = None
        if sensorType == "SENS_COMPASS":
            sensorHandle = Compass()
        elif sensorTyoe == "SENS_ULTRASONIC":
            sensorHandle = Ultrasonic()
        elif sensorType == "SENS_GYRO":
            sensorHandle = Gyro()
        elif sensorType == "SENS_GPS":
            sensorHandle = GPS()
        elif sensorType == "SENS_ATMOS":
            sensorHandle = AtmosPressure()
        elif sensorType == "SENS_ACCELERO":
            sensorHandle = Accelerometer()

        if sensorHandle != None:
            sensorHandle.sensorData = {pinData: pinData, sensorType: sensorType, handle: sensorHandle}
            sensorHandle.init(self.coreHandle)
            self.sensors.append(sensorHandle.sensorData)
            self.coreHandle.writeLog("Registered new sensor: ", sensorType)
        else:
            self.coreHandle.writeLog("Failed to register new sensor: ", sensorType)

    def loadConfig(self, config):
        for configData in config:
            configData = configData.split(',')
            sensorData = []
            sensorType = None
            for pinData in configData:
                pinData = pinData.split(':')
                if sensorType == None:
                    sensorType = pinData[2]
                sensorData.append({pin: pinData[0], type: pinData[1]})
                print(sensorData)
            if sensorType != None:
                self.addSensor(sensorData, sensorType)