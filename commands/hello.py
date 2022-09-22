
class Hello:
    def handle(self, parent, payload):
        if Command.myHostKey not None:
            parent.writeLog("Host already exists.")
            parent.communication.write({ exception: "Host already exists." })
        else:
            parent.writeLog("Host found and registered.")
            Command.myHostKey = payload.hostKey