import cryptocode
import array
from services.CommunicationMethods.Radio import Radio

class Communication:
    encryptPassword = None
    coreHandle = None
    method = None
    methodHandle = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        coreHandle.writeLog("Initializing communication system.")

    def handle(self):
        self.methodHandle.handle()

    def loadConfig(self, config):
        Communication.encryptPassword = config['encryptPassword']
        Communication.method = config['method']
        if Communication.method == 'radio':
            self.methodHandle = Radio(self.coreHandle)
        self.methodHandle.loadConfig(config)
        self.methodHandle.init(self.coreHandle)

    def write(self, messagePayload):
        Event.callEvents('out-communication-payload', {"payload": message})
        message = self.startLine + Communication.encryptString(message) + self.endLine
        self.methodHandle.write(array.array('B', json.dumps(message)))

    def read(self):
        data = self.methodHandle.read()
        if data != None:
            Event.callEvents('in-communication-payload', {"payload": payload})
            return data

    def encryptString(message):
        return cryptocode.encrypt(message, Communication.encryptPassword)

    def decryptString(message):
        return cryptocode.decrypt(message, Communication.encryptPassword)

    def close(self):
        self.methodHandle.close()