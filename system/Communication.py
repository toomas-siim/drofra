import cryptocode
import array

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
        Communication.encryptPassword = config.encryptPassword
        Communication.method = config.method
        if Communication.method is 'radio':
            self.methodHandle = new Radio()
        self.methodHandle.loadConfig(config)
        self.methodHandle.init(coreHandle)

    def write(self, messagePayload):
        Event.callEvents('out-communication-payload', {"payload": message})
        message = self.startLine + Communication.encryptString(message) + self.endLine
        self.methodHandle.write(array.array('B', json.dumps(message)))

    def read(self):
        data = self.methodHandle.read()
        if data is not None:
            Event.callEvents('in-communication-payload', {"payload": payload})
            return data

    def encryptString(message):
        return cryptocode.encrypt(message, Communication.encryptPassword)

    def decryptString(message):
        return cryptocode.decrypt(message, Communication.encryptPassword)

    def close(self):
        self.methodHandle.close()