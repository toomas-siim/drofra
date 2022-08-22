import time

class Core:
    pinSystem = null
    cameraSystem = null
    communication = null

    def init(self):
        self.pinSystem = new Pin()
        self.cameraSystem = new Camera()
        self.communication = new Communication()

    def run(self):
        run = True
        while run is True:
            time.sleep(0.01) # Sleep for a bit
            Command.handle(self)