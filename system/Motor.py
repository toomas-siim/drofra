import RPi.GPIO as GPIO

class Motor:
    motors = []
    parentHandle = None
    TYPE_LEFT_BACK = "left_back"
    TYPE_LEFT_FRONT = "left_front"
    TYPE_RIGHT_FRONT = "right_front"
    TYPE_RIGHT_BACK = "right_back"
    TYPE_FRONT = "front"

    SPEED_LOW = 25
    SPEED_MID = 125
    SPEED_HIGH = 250

    def init(self, parentHandle):
        self.parentHandle = parentHandle

    def setAllMotors(self, value):
        for motor in self.motors:
            self.parentHandle.pinSystem.setPinOutput(motor.pin, value)

    def setValueByType(self, type, value):
        for motor in self.motors:
            if motor.type == type:
                self.parentHandle.pinSystem.setPinOutput(motor.pin, value)

    def setBackMotors(self, value):
        for motor in self.motors:
            if motor.type == self.TYPE_LEFT_BACK or motor.type == self.TYPE_RIGHT_BACK:
                self.parentHandle.pinSystem.setPinOutput(motor.pin, value)

    def setFrontMotors(self, value):
        for motor in self.motors:
            if motor.type == self.TYPE_LEFT_FRONT or motor.type == self.TYPE_RIGHT_FRONT:
                self.parentHandle.pinSystem.setPinOutput(motor.pin, value)

    def setLeftMotors(self, value):
        for motor in self.motors:
            if motor.type == self.TYPE_LEFT_FRONT or motor.type == self.TYPE_LEFT_BACK:
                self.parentHandle.pinSystem.setPinOutput(motor.pin, value)

    def setRightMotors(self, value):
        for motor in self.motors:
            if motor.type == self.TYPE_RIGHT_FRONT or motor.type == self.TYPE_RIGHT_BACK:
                self.parentHandle.pinSystem.setPinOutput(motor.pin, value)

    def setForwardMotors(self, value):
            for motor in self.motors:
                if motor.type == self.TYPE_FRONT:
                    self.parentHandle.pinSystem.setPinOutput(motor.pin, value)

    def loadConfig(self, config):
        if 'motor-left-front-pins' in config:
            for motor in config['motor-left-front-pins']:
                pins = motor.split(",")
                for pin in pins:
                    self.addMotor(self.TYPE_LEFT_FRONT, pin)
        if 'motor-left-back-pins' in config:
            for motor in config['motor-left-back-pins']:
                pins = motor.split(",")
                for pin in pins:
                    self.addMotor(self.TYPE_LEFT_BACK, pin)
        if 'motor-right-front-pins' in config:
            for motor in config['motor-right-front-pins']:
                pins = motor.split(",")
                for pin in pins:
                    self.addMotor(self.TYPE_RIGHT_FRONT, pin)
        if 'motor-right-back-pins' in config:
            for motor in config['motor-right-back-pins']:
                pins = motor.split(",")
                for pin in pins:
                    self.addMotor(self.TYPE_RIGHT_BACK, pin)
        if 'motor-front-pins' in config:
            for motor in config['motor-front-pins']:
                print(motor)
                pins = motor.split(",")
                for pin in pins:
                    self.addMotor(self.TYPE_FRONT, pin)

    def addMotor(self, type, pin):
        self.parentHandle.pinSystem.setPinType(pin, GPIO.OUT)
        motors.append({"type": type, "pin": pin})