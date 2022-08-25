import json

class Command:
    def handle(parent):
        comms = parent.communication
        readLine = comms.read()

        # @TODO: Verify host is recognized.

        if readLine:
            payload = json.loads(readLine)
            if payload.command is "hello":
                handle = new Hello()
            elif payload.command is "bye":
                handle = new Bye()
            elif payload.command is "fly":
                handle = new Fly()
            handle.handle(parent, payload)