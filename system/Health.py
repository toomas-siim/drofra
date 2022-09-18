class Health:
    coreHandle = None
    def init(self, coreHandle):
        self.coreHandle = coreHandle

    def handle(self):
        if self.coreHandle.droneType is None:
            self.coreHandle.writeLog("Drone system fatal failure, drone type unconfigured. Check drone.ini file.")
            self.coreHandle.shutdown = True