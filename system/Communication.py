import cryptocode
import array
from services.CommunicationMethods.Radio import Radio
from services.CommunicationMethods.Bluetooth import Bluetooth

class Communication:
    encryptPassword = None
    coreHandle = None
    method = None
    methodHandle = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        coreHandle.writeLog("Initializing communication system.")

        if self.methodHandle != None:
            self.methodHandle.init(self.coreHandle)
        else:
            self.coreHandle.writeLog("Communication system not available (no valid communication methods)")

    def handle(self):
        self.methodHandle.handle()

    def loadConfig(self, config):
        Communication.encryptPassword = config['encryptPassword']
        Communication.method = config['method']
        if Communication.method == 'radio':
            self.methodHandle = Radio()
        elif Communication.method == 'bluetooth':
            self.methodHandle = Bluetooth()
        self.methodHandle.loadConfig(config)

    def write(self, messagePayload):
        if self.methodHandle != None:
            Event.callEvents('out-communication-payload', {"payload": message})
            message = self.startLine + Communication.encryptString(message) + self.endLine
            self.methodHandle.write(array.array('B', json.dumps(message)))

    def read(self):
        if self.methodHandle != None:
            data = self.methodHandle.read()
            if data != None:
                Event.callEvents('in-communication-payload', {"payload": payload})
                return data

    def encryptString(message):
        return cryptocode.encrypt(message, Communication.encryptPassword)

    def decryptString(message):
        return cryptocode.decrypt(message, Communication.encryptPassword)

    def close(self):
        if self.methodHandle != None:
            self.methodHandle.close()