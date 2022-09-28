class Sensor(object):
    SENSOR_TYPES = ["SENS_COMPASS", "SENS_ULTRASONIC", "SENS_GYRO", "SENS_GPS", "SENS_ATMOS", "SENS_ACCELERO"]
    sensors = []

    name = None
    type = None
    parentHandle = None

    def __init__(self, name, type):
        self.type = type
        self.name = type

    def initSensorSystem(coreHandle):
        Sensor.parentHandle = coreHandle

    def init(self):
        Sensor.parentHandle.writeLog("Sensor init not overwritten. Sensor type: ", self.type)

    def handleSensors():
        for sensorData in Sensor.sensors:
            sensorData.handle.handle()

    def handle(self):
        Sensor.parentHandle.writeLog("Sensor handle not overwritten. Sensor type: ", self.type)

    def addSensor(pinData, sensorType):
        sensorHandle = None
        if sensorType == "SENS_COMPASS":
            sensorHandle = Compass()
        elif sensorTyoe == "SENS_ULTRASONIC":
            sensorHandle = Ultrasonic()
        elif sensorType == "SENS_GYRO"
            sensorHandle = Gyro()
        elif sensorType == "SENS_GPS":
            sensorHandle = GPS()
        elif sensorType == "SENS_ATMOS"
            sensorHandle = AtmosPressure()
        elif sensorType == "SENS_ACCELERO":
            sensorHandle = Accelerometer()

        if sensorHandle != None:
            sensorHandle.init()
            Sensor.sensors.push({pinData: pinData, sensorType: sensorType, handle: sensorHandle})
            Sensor.parentHandle.writeLog("Registered new sensor: ", sensorType)
        else:
            Sensor.parentHandle.writeLog("Failed to register new sensor: ", sensorType)

    def loadConfig(config):
        for configData in config:
            configData = configData.split(',')
            sensorData = []
            sensorType = None
            for pinData in configData:
                pinData = pinData.split(':')
                if sensorType == None:
                    sensorType = pinData[2]
                sensorData.push({pin: pinData[0], pinType: pinData[1]})
            if sensorType not None:
                Sensor.addSensor(sensorData, sensorType)