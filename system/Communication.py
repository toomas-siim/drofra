from pyGPIO2 import spi
import array

# @TODO: Encryption
class Communication:
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""

    def init(self):
        spi.open("/dev/spidev2.0", mode=1)

    def write(self, message):
        message = self.startLine + message + self.endLine
        spi.write(array.array('B', message))

    def read(self):
        self.currentLine += spi.read(2).decode("utf-8")
        if self.endLine in self.currentLine:
            result = self.currentLine
            self.currentLine = ""
            return result.replace(self.startLine, '').replace(self.endLine, '')
        return ''

    def close():
        spi.close()