import bluetooth

class Bluetooth:
    coreHandle = None
    serverSock = None
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        devices = self.lookUpNearbyBluetoothDevices()
        for device in devices:
            print("Bluetooth> name: {}, address: {}\n".format(bluetooth.lookup_name(device), str(device)))
        self.serverSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        port = 1
        self.serverSock.bind(("",port))
        self.serverSock.listen(1)

    def handle(self):
        self.handleIncoming()

    def loadConfig(self, config):
        # @TODO

    def lookUpNearbyBluetoothDevices(self):
      return bluetooth.discover_devices()

    def handleIncoming(self):
        client_sock,address = server_sock.accept()
        data = client_sock.recv(1024)
        self.currentLine += data

    def read(self):
        if self.endLine in self.currentLine:
            payload = json.loads(Communication.decryptString(self.currentLine.replace(self.startLine, '').replace(self.endLine, '')))
            if payload == None:
                self.coreHandle.writeLog("Invalid payload: ", self.currentLine)
            self.currentLine = ""
            return payload
        return None

    def write(self, message):
        self.serverSock.send(message)

    def close(self):
        self.serverSock.close()