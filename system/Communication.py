from pyGPIO2 import spi
import cryptocode
import array

class Communication:
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""
    encryptPassword = None

    def init(self):
        spi.open("/dev/spidev2.0", mode=1)

    def loadConfig(self, config):
        Communication.encryptPassword = config.encryptPassword

    def write(self, messagePayload):
        message = self.startLine + Communication.encryptString(message) + self.endLine
        spi.write(array.array('B', json.dumps(message)))

    def read(self):
        self.currentLine += spi.read(2).decode("utf-8")
        if self.endLine in self.currentLine:
            result = self.currentLine
            self.currentLine = ""
            return json.loads(Communication.decryptString(result.replace(self.startLine, '').replace(self.endLine, '')))
        return ''

    def encryptString(message):
        return cryptocode.encrypt(message, Communication.encryptPassword)

    def decryptString(message):
        return cryptocode.decrypt(message, Communication.encryptPassword)

    def close():
        spi.close()