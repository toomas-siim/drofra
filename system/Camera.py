from picamera import PiCamera
from time import sleep, time

class Camera:
    handle = None
    recordPath = None
    cameraServoX = None
    cameraServoY = None
    cameraServoPosition = None
    recording = False
    videoPath = "/home/drofra/videos/"
    screenPath = "/home/drofra/screenshots/"

    def init(self):
        self.handle = PiCamera()
        self.handle.resolution = (1920, 1080)
        self.handle.start_preview()
        sleep(2)

    def startRecording(self):
        self.recording = True
        self.handle.start_recording(self.videoPath + "recording." + time() + ".h624")

    def stopRecording(self):
        self.recording = False
        self.handle.stop_recording()

    def close(self):
        self.handle.stop_preview()

    def handleServoPositions(self):
        # @TODO: For object tracking.

    def loadConfig(self, config):
        if 'camera-servo-x-pin' in config:
            self.cameraServoX = config['camera-servo-x-pin']
        if 'camera-servo-y-pin' in config:
            self.cameraServoY = config['camera-servo-y-pin']
        if 'camera-servo-position-pin' in config:
            self.cameraServoPosition = config['camera-servo-position-pin']