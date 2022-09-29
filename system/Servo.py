class Servo:
    servos = []
    parentHandle = None

    def init(self, parentHandle):
        self.parentHandle = parentHandle

    def setValueByType(self, type, value):
        for servo in self.servos:
            if servo.type == type:
                self.parentHandle.pinSystem.setPinOutput(servo.pin, servo.centerPos + value)

    def addServo(pin, type, centerPos):
        self.parentHandle.pinSystem.setPinType(pin, GPIO.OUT)
        servos.append({"type": type, "pin": pin, "centerPos": centerPos})

    def loadConfig(self, config):
        for configKey in config.keys():
            if 'servo-' in configKey:
                for servo in config[configKey]:
                    pins = servo.split(",")
                    for pin in pins:
                        servoData = servo.split(":")
                        self.addServo(servoData[0], servoData[1], servoData[2])