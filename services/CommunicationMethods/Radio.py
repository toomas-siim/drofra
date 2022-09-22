from pyGPIO2 import spi

class Radio:
    coreHandle = None
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""
    spiPath = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        spi.open(self.spiPath, mode=1)

    def loadConfig(self, config):
        self.spiPath = config["device-spi-path"]

    def handle(self):
        self.currentLine += spi.read(2).decode("utf-8")

    def write(self, message):
        spi.write(message)

    def read(self):
        if self.endLine in self.currentLine:
            payload = json.loads(Communication.decryptString(self.currentLine.replace(self.startLine, '').replace(self.endLine, '')))
            if payload is None:
                self.coreHandle.writeLog("Invalid payload: ", self.currentLine)
            self.currentLine = ""
            return payload
        return None

    def close(self):
        spi.close()