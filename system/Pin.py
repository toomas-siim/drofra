import RPi.GPIO as GPIO

class Pin:
    def init(self):
        GPIO.setmode(GPIO.BOARD)

    def setPinType(self, pin, type):
        GPIO.setup(pin, type)

    def setPinOutput(self, pin, output):
        # @TODO: Validate min / max values
        # @TODO: Handle PWM as well?
        GPIO.output(pin, output)

    def getPinInput(self, pin):
        return GPIO.input(pin)