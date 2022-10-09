import json

class Command:
    myHostKey = None

    def init(coreHandle):
        Command.coreHandle = coreHandle

    def handle():
        comms = Command.coreHandle.communication
        payload = comms.read()

        if payload.hostKey == Command.myHostKey or Command.myHostKey == None:
            if payload.command == "hello":
                handle = Hello()
            elif payload.command == "bye":
                handle = Bye()
            elif payload.command == "fly":
                handle = Fly()
            handle.handle(parent, payload)