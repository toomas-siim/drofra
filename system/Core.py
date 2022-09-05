import time
import configparser

class Core:
    flightStatus = False
    droneType = "quadcopter"

    pinSystem = null
    cameraSystem = null
    communication = null
    motorSystem = null
    servoSystem = null

    def init(self):
        self.pinSystem = new Pin()
        self.cameraSystem = new Camera()
        self.communication = new Communication()
        self.motorSystem = new Motor()
        self.servoSystem = new Servo()
        self.loadConfig()
        Navigation.init(self)
        Script.importAllScripts()

    def loadConfig(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read('../drone.ini')
        self.droneType = config.general.type.lower()
        self.communication.loadConfig(config.communication)
        self.motorSystem.loadConfig(config.motors)
        self.servoSystem.loadConfig(config.servos)

    def run(self):
        run = True
        while run is True:
            time.sleep(0.01) # Sleep for a bit
            Command.handle(self)
            Script.handleScripts()
            if self.flightStatus is True:
                Navigation.handle(self)