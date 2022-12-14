import RPi.GPIO as GPIO

class Servo:
    servos = []
    parentHandle = None

    def init(self, parentHandle):
        self.parentHandle = parentHandle

    def setValueByType(self, type, value):
        for servo in self.servos:
            if servo["type"] == type:
                self.parentHandle.pinSystem.setPinOutput(servo["pin"], int(value))

    def addServo(self, pin, type, centerPos):
        self.parentHandle.pinSystem.setPinType(pin, GPIO.OUT)
        self.servos.append({"type": type, "pin": pin, "centerPos": centerPos})

    def loadConfig(self, config):
        for configKey in config.keys():
            if 'servo-' in configKey:
                pins = config[configKey].split(",")
                for pin in pins:
                    servoData = pin.split(":")
                    self.addServo(servoData[0], servoData[1], servoData[2])