import bluetooth

class Bluetooth:
    coreHandle = None
    serverSock = None
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""
    activeClient = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        try:
            devices = self.lookUpNearbyBluetoothDevices()
            for device in devices:
                print("Bluetooth> name: {}, address: {}\n".format(bluetooth.lookup_name(device), str(device)))
            self.serverSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            port = 1
            self.serverSock.bind(("",port))
            self.serverSock.listen(1)
        except:
            print("Failed initializing bluetooth.")

    def handle(self):
        try:
            self.handleIncoming()
            self.handlePayloads()
        except BaseException as err:
            self.coreHandle.writeLog("Error handling bluetooth: " + str(err))

    def loadConfig(self, config):
        # @TODO
        print("Loading bluetooth config")

    def lookUpNearbyBluetoothDevices(self):
      return bluetooth.discover_devices()

    def handlePayloads(self):
        if self.activeClient != None:
            data = self.activeClient.recv(1024)
            self.currentLine += data

    def handleIncoming(self):
        if self.serverSock != None:
            client_sock,address = self.serverSock.accept()
            self.activeClient = {"socket": client_sock, "address": address}

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