import time
import RPi.GPIO as GPIO
from sensors.Sensor import Sensor

class Ultrasonic(Sensor):
    waitingForSignal = False
    signalStart = 0
    latestDistance = 0
    readPin = 0
    writePin = 1

    def init(self, coreHandle):
        self.writePin = self.getPinByType("write")
        self.readPin = self.getPinByType("read")
        self.coreHandle = coreHandle

    def handle(self):
        print(self.latestDistance)
        if self.waitingForSignal == False and time.time() - self.signalStart >= 1:
            self.waitingForSignal = True
            self.signalStart = time.time()
            self.coreHandle.pinSystem.setPinType(self.writePin, GPIO.OUT)
            self.coreHandle.pinSystem.setPinType(self.readPin, GPIO.IN)
            self.coreHandle.pinSystem.setPinOutput(self.writePin, 1)
        elif self.waitingForSignal == True:
            if time.time() - self.signalStart >= 0.1:
                self.coreHandle.pinSystem.setPinOutput(self.writePin, 0)
            if self.coreHandle.pinSystem.getPinInput(self.readPin) == 1:
                self.waitingForSignal = False
                self.latestDistance = ((time.time() - self.signalStart) * 34300) / 2

    # Fetch distance
    def getDistance(self):
        return self.latestDistance