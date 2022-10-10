class PlaneNavigation:
    coreHandle = None

    def launch(self, parent):
        self.coreHandle = parent
        parent.motorSystem.setForwardMotors(Motor.SPEED_HIGH)

    def stop(self):
        self.coreHandle.motorSystem.setAllMotors(0)

    def moveForward(self, parent):
        navSystem = parent.navigationSystem
        navSystem.targetRotation.x = 0
        navSystem.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", 0)

    def rotateRight(self, parent):
        navSystem = parent.navigationSystem
        navSystem.targetRotation.x = 0
        navSystem.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", 20)

    def rotateLeft(self, parent):
        navSystem = parent.navigationSystem
        navSystem.targetRotation.x = 0
        navSystem.targetRotation.y = 0
        parent.servoSystem.setValueByType("tail", -20)

    def heightRegulation(self, parent):
        navSystem = parent.navigationSystem
        if navSystem.currentHeight < navSystem.targetHeight - 3:
            navSystem.targetRotation.x = 0
            navSystem.targetRotation.y = 20
        elif navSystem.currentHeight > navSystem.targetHeight + 3:
            navSystem.targetRotation.x = 0
            navSystem.targetRotation.y = -20

    # Rotation regulation has 5 degree allowed error margin.
    def rotationRegulation(self, parent):
        # @TODO: Should use a spectrum of motor power instead of fixed values.
        # Ie moving forward needs a stable balanced speed of rotors, not jumps between high and low.
        navSystem = parent.navigationSystem
        # X Axis
        if navSystem.rotation["x"] < navSystem.targetRotation["x"] - 5:
            parent.servoSystem.setValueByType("left", -20)
            parent.servoSystem.setValueByType("right", 20)
            return True
        elif navSystem.rotation["x"] > navSystem.targetRotation["x"] + 5:
            parent.servoSystem.setValueByType("left", 20)
            parent.servoSystem.setValueByType("right", -20)
            return True
        else:
            parent.servoSystem.setValueByType("left", 0)
            parent.servoSystem.setValueByType("right", 0)

        # Y Axis
        if navSystem.rotation["y"] < navSystem.targetRotation["y"] - 5:
            parent.servoSystem.setValueByType("left", 20)
            parent.servoSystem.setValueByType("right", 20)
            return True
        elif navSystem.rotation["y"] > navSystem.targetRotation["y"] + 5:
            parent.servoSystem.setValueByType("left", 20)
            parent.servoSystem.setValueByType("right", 20)
            return True
        else:
            parent.servoSystem.setValueByType("left", 0)
            parent.servoSystem.setValueByType("right", 0)

        return False

    def level(self, parent):
        parent.navigationSystem.targetRotation["x"] = 0
        parent.navigationSystem.targetRotation["y"] = 0