from pyGPIO2 import spi
import cryptocode
import array

class Communication:
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""
    encryptPassword = None
    coreHandle = None

    def init(self, coreHandle):
        spi.open("/dev/spidev2.0", mode=1)
        self.coreHandle = coreHandle

    def handle(self):
        self.updateBufferLine()

    def loadConfig(self, config):
        Communication.encryptPassword = config.encryptPassword

    def write(self, messagePayload):
        message = self.startLine + Communication.encryptString(message) + self.endLine
        spi.write(array.array('B', json.dumps(message)))

    def updateBufferLine(self):
        self.currentLine += spi.read(2).decode("utf-8")

    def read(self):
        if self.endLine in self.currentLine:
            result = self.currentLine
            self.currentLine = ""
            payload = json.loads(Communication.decryptString(result.replace(self.startLine, '').replace(self.endLine, '')))
            return payload
        return ''

    def encryptString(message):
        return cryptocode.encrypt(message, Communication.encryptPassword)

    def decryptString(message):
        return cryptocode.decrypt(message, Communication.encryptPassword)

    def close():
        spi.close()