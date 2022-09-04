
class Bye:
    def handle(self, parent, payload):
        if Command.myHostKey not None:
            if Command.myHostKey is payload.hostKey:
                Command.myHostKey = None
                parent.flightStatus = False