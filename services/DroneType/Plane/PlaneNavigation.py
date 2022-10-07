from services.Navigation import Navigation

class PlaneNavigation:
    def launch(self, parent):
        parent.motorSystem.setForwardMotors(Motor.SPEED_HIGH)

    def stop(self):
        Navigation.coreHandle.motorSystem.setAllMotors(0)

    def moveForward(self, parent):
        Navigation.targetRotation.x = 0
        Navigation.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", 0)

    def rotateRight(self, parent):
        Navigation.targetRotation.x = 0
        Navigation.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", 20)

    def rotateLeft(self, parent):
        Navigation.targetRotation.x = 0
        Navigation.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", -20)

    def heightRegulation(self, parent):
        if Navigation.currentHeight < Navigation.targetHeight - 3:
            Navigation.targetRotation.x = 0
            Navigation.targetRotation.y = 20
        elif Navigation.currentHeight > Navigation.targetHeight + 3:
            Navigation.targetRotation.x = 0
            Navigation.targetRotation.y = -20

    # Rotation regulation has 5 degree allowed error margin.
    def rotationRegulation(self, parent):
        # @TODO: Should use a spectrum of motor power instead of fixed values.
        # Ie moving forward needs a stable balanced speed of rotors, not jumps between high and low.

        # X Axis
        if Navigation.rotation.x < Navigation.targetRotation.x - 5:
            parent.servoSystem.setValueByType("left", -20)
            parent.servoSystem.setValueByType("right", 20)
            return True
        elif Navigation.rotation.x > Navigation.targetRotation.x + 5:
            parent.servoSystem.setValueByType("left", 20)
            parent.servoSystem.setValueByType("right", -20)
            return True
        else:
            parent.servoSystem.setValueByType("left", 0)
            parent.servoSystem.setValueByType("right", 0)

        # Y Axis
        if Navigation.rotation.y < Navigation.targetRotation.y - 5:
            parent.servoSystem.setValueByType("left", 20)
            parent.servoSystem.setValueByType("right", 20)
            return True
        elif Navigation.rotation.y > Navigation.targetRotation.y + 5:
            parent.servoSystem.setValueByType("left", 20)
            parent.servoSystem.setValueByType("right", 20)
            return True
        else:
            parent.servoSystem.setValueByType("left", 0)
            parent.servoSystem.setValueByType("right", 0)

        return False

    def level(self, parent):
        Navigation.targetRotation.x = 0
        Navigation.targetRotation.y = 0