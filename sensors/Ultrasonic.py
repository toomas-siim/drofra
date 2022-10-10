import time

class Ultrasonic(Sensor):
    waitingForSignal = False
    signalStart = None
    latestDistance = 0
    readPin = 0
    writePin = 1

    def init(self, coreHandle):
        self.writePin = self.getPinByType("write")
        self.readPin = self.getPinByType("read")

    def handle(self):
        print(latestDistance)
        if self.waitingForSignal == False and time.time() - self.signalStart >= 1:
            self.waitingForSignal = True
            self.signalStart = time.time()
            self.pinSystem.setPinType(self.writePin, GPIO.OUT)
            self.pinSystem.setPinType(self.readPin, GPIO.IN)
            self.pinSystem.setPinOutput(self.writePin, 1)
        elif self.waitingForSignal == True:
            if time.time() - self.signalStart >= 0.1:
                self.pinSystem.setPinOutput(self.writePin, 0)
            if coreHandle.pinSystem.getPinInput(self.readPin) == 1:
                self.waitingForSignal = False
                self.latestDistance = ((time.time() - self.signalStart) * 34300) / 2

    # Fetch distance
    def getDistance(self):
        return self.latestDistance