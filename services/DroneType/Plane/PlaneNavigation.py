class PlaneNavigation:
    def launch(self, parent):
        parent.motorSystem.setForwardMotors(Motor.SPEED_HIGH)

    def stop(self):
        Navigation.coreHandle.motorSystem.setAllMotors(0)

    def moveForward(self, parent):
        parent.targetRotation.x = 0
        parent.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", 0)

    def rotateRight(self, parent):
        parent.targetRotation.x = 0
        parent.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", 20)

    def rotateLeft(self, parent):
        parent.targetRotation.x = 0
        parent.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", -20)

    def heightRegulation(self, parent):
        if parent.currentHeight < parent.targetHeight - 3:
            parent.targetRotation.x = 0
            parent.targetRotation.y = 20
        elif parent.currentHeight > parent.targetHeight + 3:
            parent.targetRotation.x = 0
            parent.targetRotation.y = -20

    # Rotation regulation has 5 degree allowed error margin.
    def rotationRegulation(self, parent):
        # @TODO: Should use a spectrum of motor power instead of fixed values.
        # Ie moving forward needs a stable balanced speed of rotors, not jumps between high and low.

        # X Axis
        if parent.rotation.x < parent.targetRotation.x - 5:
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
        if parent.rotation.y < parent.targetRotation.y - 5:
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
        parent.targetRotation.x = 0
        parent.targetRotation.y = 0