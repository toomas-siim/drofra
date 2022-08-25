import time
import configparser

class Core:
    flightStatus = False

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

    def loadConfig(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read('../drone.ini')
        self.motorSystem.loadConfig(config['motors'])

    def run(self):
        run = True
        while run is True:
            time.sleep(0.01) # Sleep for a bit
            Command.handle(self)
            if self.flightStatus is True:
                Navigation.handle(self)