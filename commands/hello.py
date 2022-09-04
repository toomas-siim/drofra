
class Hello:
    def handle(self, parent, payload):
        if Command.myHostKey not None:
            parent.communication.write({ exception: "Host already exists." })
        else:
            Command.myHostKey = payload.hostKey