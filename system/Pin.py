from pyGPIO2.gpio import gpio

class Pin:
    def init(self):
        gpio.init()

    def setPinType(self, pin, type):
        gpio.setcfg(pin, type)

    def setPinOutput(self, pin, output):
        # @TODO: Validate min / max values
        gpio.output(pin, output)

    def getPinInput(self, pin):
        return gpio.input(pin)