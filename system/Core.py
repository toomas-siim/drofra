import time
from datetime import datetime
import configparser

# Packages
from system.Pin import Pin
from system.Camera import Camera
from system.Communication import Communication

class Core:
    flightStatus = False
    droneType = None
    shutdown = False

    pinSystem = None
    cameraSystem = None
    communication = None
    motorSystem = None
    servoSystem = None
    timingSystem = None
    healthSystem = None
    neuralNetwork = None

    def init(self):
        self.pinSystem = Pin()
        self.cameraSystem = Camera()
        self.communication = Communication()
        self.motorSystem = Motor()
        self.servoSystem = Servo()
        self.timingSystem = Time()
        self.healthSystem = Health()
        self.neuralNetwork = NeuralNetwork()
        self.loadConfig()
        self.communication.init(self)
        self.timingSystem.init(self)
        self.healthSystem.init(self)
        self.neuralNetwork.init(self)
        Navigation.init(self)
        Sensor.initSensorSystem()
        Script.importAllScripts()

    def initTimedFunctions(self):
        self.timingSystem.addTimedFunction(1000, Command.handle)
        self.timingSystem.addTimedFunction(10, self.communication.handle)
        self.timingSystem.addTimedFunction(100, Script.handleScripts)
        self.timingSystem.addTimedFunction(30, Navigation.handle)
        self.timingSystem.addTimedFunction(50, Sensor.handleSensors)
        self.timingSystem.addTimedFunction(3000, self.healthSystem.handle)
        self.timingSystem.addTimedFunction(1000, self.neuralNetwork.handle)

    def loadConfig(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read('../drone.ini')
        self.droneType = config.general.type.lower()
        self.communication.loadConfig(config.communication)
        self.motorSystem.loadConfig(config.motors)
        self.servoSystem.loadConfig(config.servos)

    def writeLog(self, message):
        print(datetime.now(), message)

    def run(self):
        # Run the looper
        # Mostly consists of timed functions.
        while self.shutdown is False:
            time.sleep(0.01) # Sleep for a bit
            self.timingSystem.handle()

        self.communication.close()