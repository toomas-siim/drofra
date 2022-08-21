class Sensor(object):
    SENSOR_TYPES = ["SENS_COMPASS", "SENS_ULTRASONIC", "SENS_TILT", "SENS_GPS"]

    name = null
    type = null
    parentHandle = null

    def __init__(self, name, type):
        self.type = type
        self.name = type

    def setParent(self, parent):
        self.parentHandle = parent