import spidev

class Radio:
    coreHandle = None
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""
    spi = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        device = 0
        self.spi = spidev.SpiDev()
        try:
            self.spi.open(0, device)
            self.spi.max_speed_hz = 500000
            self.spi.mode = 0
        except:
            coreHandle.writeLog("Failed opening radio component")

    def loadConfig(self, config):
        self.spiPath = config["device-spi-path"]

    def handle(self):
        self.currentLine += self.spi.read(2).decode("utf-8")

    def write(self, message):
        self.spi.write(message)

    def read(self):
        if self.endLine in self.currentLine:
            payload = json.loads(Communication.decryptString(self.currentLine.replace(self.startLine, '').replace(self.endLine, '')))
            if payload == None:
                self.coreHandle.writeLog("Invalid payload: ", self.currentLine)
            self.currentLine = ""
            return payload
        return None

    def close(self):
        self.spi.close()