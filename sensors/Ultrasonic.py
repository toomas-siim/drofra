import time

class Ultrasonic(Sensor):
    waitingForSignal = False
    signalStart = None
    latestDistance = 0
    # @TODO: load pins dynamically.
    readPin = 0
    writePin = 1

    def handle(self, coreHandle):
        if self.waitingForSignal is False and time.time() - self.signalStart >= 1:
            self.waitingForSignal = True
            self.signalStart = time.time()
            self.pinSystem.setPinType(self.writePin, GPIO.OUT)
            self.pinSystem.setPinType(self.readPin, GPIO.IN)
        elif self.waitingForSignal is True:
            if coreHandle.pinSystem.getPinInput(self.readPin) is 1:
                self.waitingForSignal = False
                self.latestDistance = ((time.time() - self.signalStart) * 34300) / 2

    # Fetch distance
    def getDistance(self):
        return self.latestDistance