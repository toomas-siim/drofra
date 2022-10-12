from sensors.Ultrasonic import Ultrasonic
from sensors.Gyro import Gyro

class Sensor:
    SENSOR_TYPES = ["SENS_COMPASS", "SENS_ULTRASONIC", "SENS_GYRO", "SENS_GPS", "SENS_ATMOS", "SENS_ACCELERO"]
    sensors = []
    coreHandle = None

    def initSensorSystem(self, coreHandle):
        self.coreHandle = coreHandle
        for sensor in Sensor.sensors:
            try:
                sensor["handle"].init(self.coreHandle)
            except:
                self.coreHandle.writeLog("Failed starting sensor: " + sensor["sensorType"])

    def handle():
        for sensorData in Sensor.sensors:
            try:
                sensorData["handle"].handle()
            except:
                return False
        return True

    def getSensorHandleByType(self, type):
        for sensor in self.sensors:
            if sensor["sensorType"] == type:
                return type
        return None

    def getSensorHandleByPurpose(self, purpose):
            for sensor in self.sensors:
                if sensor["sensorPurpose"] == purpose:
                    return purpose
            return None

    def addSensor(self, pinData, sensorType, purpose):
        sensorHandle = None
        if sensorType == "SENS_COMPASS":
            sensorHandle = Compass()
        elif sensorType == "SENS_ULTRASONIC":
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
            sensorHandle.sensorData = {"pinData": pinData, "sensorType": sensorType, "sensorPurpose": purpose, "handle": sensorHandle}
            self.sensors.append(sensorHandle.sensorData)
        else:
            print("Failed to register new sensor: ", sensorType)

    def loadConfig(self, config):
        for sensorKey in config:
            configData = config[sensorKey]
            configData = configData.split(',')
            sensorData = []
            sensorType = None
            purpose = None
            for pinData in configData:
                pinData = pinData.split(':')
                if sensorType == None:
                    sensorType = pinData[2]
                    purpose = pinData[3]
                sensorData.append({"pin": pinData[0], "type": pinData[1]})
            if sensorType != None:
                self.addSensor(sensorData, sensorType, purpose)