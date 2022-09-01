from picamera import PiCamera
from time import sleep

class Camera:
    handle = null

    def init(self):
        self.handle = PiCamera()
        camera.resolution = (1920, 1080)
        camera.start_preview()
        sleep(2)

    def capture(self, filePath):
        camera.capture(filePath)