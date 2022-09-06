class Sensor(object):
    SENSOR_TYPES = ["SENS_COMPASS", "SENS_ULTRASONIC", "SENS_GYRO", "SENS_GPS", "SENS_ATMOS", "SENS_ACCELERO"]
    sensors = []

    name = null
    type = null
    parentHandle = null

    def __init__(self, name, type):
        self.type = type
        self.name = type

    def init(self, coreHandle):
        self.parentHandle = coreHandle

    def addSensor(pinData, sensorType):
        Sensor.sensors.push({pinData: pinData, sensorType: sensorType})

    def loadConfig(config):
        for configData in config:
            configData = configData.split(',')
            sensorData = []
            sensorType = None
            for pinData in configData:
                pinData = pinData.split(':')
                if sensorType is None:
                    sensorType = pinData[2]
                sensorData.push({pin: pinData[0], pinType: pinData[1]})
            if sensorType not None:
                Sensor.addSensor(sensorData, sensorType)



    def setParent(self, parent):
        self.parentHandle = parent