import json

class Command:
    def handle(parent):
        comms = parent.communication
        readLine = comms.read()

        if readLine:
            payload = json.loads(readLine)
            if payload.command is "hello":
                handle = new Hello()
            elif payload.command is "bye":
                handle = new Bye()
            handle.handle(parent, payload)