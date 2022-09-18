import time
from datetime import datetime
import configparser

class Core:
    flightStatus = False
    droneType = None
    shutdown = False

    pinSystem = null
    cameraSystem = null
    communication = null
    motorSystem = null
    servoSystem = null
    timingSystem = null
    healthSystem = null

    def init(self):
        self.pinSystem = new Pin()
        self.cameraSystem = new Camera()
        self.communication = new Communication()
        self.motorSystem = new Motor()
        self.servoSystem = new Servo()
        self.timingSystem = new Time()
        self.healthSystem = new Health()
        self.loadConfig()
        self.communication.init(self)
        self.timingSystem.init(self)
        self.healthSystem.init(self)
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