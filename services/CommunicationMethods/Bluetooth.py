import bluetooth

class Bluetooth:
    serverSock = None
    startLine = "<start>"
    endLine = "<end>"
    currentLine = ""

    def init(self):
        self.serverSock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)

    def handle(self):
        self.handleIncoming()

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