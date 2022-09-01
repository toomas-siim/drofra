class QuadcopterNavigation:
    def launch(self, parent):
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_FRONT, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_FRONT, Motor.SPEED_HIGH)

    def moveForward(self, parent):
        Navigation.targetRotation.x = 0
        Navigation.targetRotation.y = -45

    def rotateRight(self, parent):
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_FRONT, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_BACK, Motor.SPEED_LOW)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_FRONT, Motor.SPEED_LOW)

    def rotateLeft(self, parent):
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_FRONT, Motor.SPEED_LOW)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_BACK, Motor.SPEED_LOW)
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_FRONT, Motor.SPEED_HIGH)

    def heightRegulation(self, parent):
        if Navigation.currentHeight < Navigation.targetHeight - 3:
            parent.motorSystem.setFrontMotors(Motor.SPEED_HIGH)
            parent.motorSystem.setBackMotors(Motor.SPEED_HIGH)
        elif Navigation.currentHeight > Navigation.targetHeight + 3:
            parent.motorSystem.setFrontMotors(Motor.SPEED_LOW)
            parent.motorSystem.setBackMotors(Motor.SPEED_LOW)

    # Rotation regulation has 5 degree allowed error margin.
    def rotationRegulation(self, parent):
        # @TODO: Should use a spectrum of motor power instead of fixed values.
        # Ie moving forward needs a stable balanced speed of rotors, not jumps between high and low.

        # X Axis
        if Navigation.rotation.x < Navigation.targetRotation.x - 5:
            parent.motorSystem.setLeftMotors(Motor.SPEED_HIGH)
            parent.motorSystem.setRightMotors(Motor.SPEED_LOW)
            return True
        elif Navigation.rotation.x > Navigation.targetRotation.x + 5:
            parent.motorSystem.setLeftMotors(Motor.SPEED_LOW)
            parent.motorSystem.setRightMotors(Motor.SPEED_HIGH)
            return True
        else:
            parent.motorSystem.setLeftMotors(Motor.SPEED_MID)
            parent.motorSystem.setRightMotors(Motor.SPEED_MID)

        # Y Axis
        if Navigation.rotation.y < Navigation.targetRotation.y - 5:
            parent.motorSystem.setFrontMotors(Motor.SPEED_HIGH)
            parent.motorSystem.setBackMotors(Motor.SPEED_LOW)
            return True
        elif Navigation.rotation.y > Navigation.targetRotation.y + 5:
            parent.motorSystem.setFrontMotors(Motor.SPEED_LOW)
            parent.motorSystem.setBackMotors(Motor.SPEED_HIGH)
            return True
        else:
            parent.motorSystem.setFrontMotors(Motor.SPEED_MID)
            parent.motorSystem.setBackMotors(Motor.SPEED_MID)

        return False

    def level(self, parent):
        Navigation.targetRotation.x = 0
        Navigation.targetRotation.y = 0