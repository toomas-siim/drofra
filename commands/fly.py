
class Fly:
    def handle(self, parent, payload):
        parent.flightStatus = True
        parent.cameraSystem.startRecording()