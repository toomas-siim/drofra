import time
from datetime import datetime
import configparser

# Packages
from system.Pin import Pin
from system.Camera import Camera
from system.Communication import Communication
from system.Motor import Motor
from system.Servo import Servo
from system.Time import Time
from system.Health import Health
from system.Altitude import Altitude
from services.Navigation import Navigation
from system.Sensor import Sensor
# from system.NeuralNetwork import NeuralNetwork

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
    altitudeSystem = None

    def init(self):
        self.writeLog(" --- Initializing Drofra framework ---")
        self.pinSystem = Pin()
        self.cameraSystem = Camera()
        self.communication = Communication()
        self.motorSystem = Motor()
        self.servoSystem = Servo()
        self.timingSystem = Time()
        self.healthSystem = Health()
        self.altitudeSystem = Altitude()
        self.navigationSystem = Navigation()
        self.sensorSystem = Sensor()
        # self.neuralNetwork = NeuralNetwork()
        self.pinSystem.init()
        self.motorSystem.init(self)
        self.servoSystem.init(self)
        self.loadConfig()
        self.communication.init(self)
        self.timingSystem.init(self)
        self.healthSystem.init(self)
        self.altitudeSystem.init()
        self.navigationSystem.init(self)
        self.sensorSystem.initSensorSystem(self)
        # self.neuralNetwork.init(self)
        Script.importAllScripts()

    def initTimedFunctions(self):
        self.timingSystem.addTimedFunction(1000, Command.handle)
        self.timingSystem.addTimedFunction(10, self.communication.handle)
        self.timingSystem.addTimedFunction(100, Script.handleScripts)
        self.timingSystem.addTimedFunction(30, Navigation.handle)
        self.timingSystem.addTimedFunction(50, Sensor.handleSensors)
        self.timingSystem.addTimedFunction(3000, self.healthSystem.handle)
        self.timingSystem.addTimedFunction(1000, self.altitudeSystem.handle)
        # self.timingSystem.addTimedFunction(1000, self.neuralNetwork.handle)

    def loadConfig(self):
        config = configparser.ConfigParser()
        config.read('drone.ini')
        config.sections()
        self.droneType = config['general']['type'].lower()
        if 'communication' in config:
            self.communication.loadConfig(config['communication'])
        if 'motors' in config:
            self.motorSystem.loadConfig(config['motors'])
        if 'servos' in config:
            self.servoSystem.loadConfig(config['servos'])
        if 'camera' in config:
            self.cameraSystem.loadConfig(config['camera'])
        self.altitudeSystem.loadConfig(config['general'])

    def writeLog(self, message):
        print(datetime.now(), message)

    def run(self):
        # Run the looper
        # Mostly consists of timed functions.
        while self.shutdown == False:
            time.sleep(0.01) # Sleep for a bit
            self.timingSystem.handle()

        self.communication.close()
        self.cameraSystem.close()