import json

class Command:
    myHostKey = None

    def handle(parent):
        comms = parent.communication
        payload = comms.read()

        if payload.hostKey is Command.myHostKey or Command.myHostKey is None:
            if payload.command is "hello":
                handle = Hello()
            elif payload.command is "bye":
                handle = Bye()
            elif payload.command is "fly":
                handle = Fly()
            handle.handle(parent, payload)