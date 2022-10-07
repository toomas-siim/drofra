from services.Navigation import Navigation

class QuadcopterNavigation:
    def launch(self, parent):
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_FRONT, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_FRONT, Motor.SPEED_HIGH)

    def stop(self):
        Navigation.coreHandle.motorSystem.setAllMotors(0)

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

    # Rotation regulation has 3 degree allowed error margin.
    def rotationRegulation(self, parent):
        # @TODO: Should use a spectrum of motor power instead of fixed values.
        # Ie moving forward needs a stable balanced speed of rotors, not jumps between high and low.
        motorBaseValue = Motor.SPEED_MID
        differenceX = Navigation.rotation.x - Navigation.targetRotation.x
        differenceY = Navigation.rotation.y - Navigation.targetRotation.y
        differenceMultiplier = 2 # Multiplies difference of degrees to motor power required to corrigate
        # Ignore regulation if less than 3 degree difference
        if differenceX > -3 and differenceX < 3 and differenceY > -3 and differenceY < 3:
            parent.motorSystem.setAllMotors(motorBaseValue)
            return True

        # Motor base values
        motorLeftFront = motorBaseValue
        motorRightFront = motorBaseValue
        motorRightBack = motorBaseValue
        motorLeftBack = motorBaseValue

        # X Axis
        if differenceX < 0:
            motorRightBack += (-differenceX * differenceMultiplier)
            motorRightFront += (-differenceX * differenceMultiplier)
            motorLeftBack -= (-differenceX * differenceMultiplier)
            motorLeftFront -= (-differenceX * differenceMultiplier)
        elif differenceX > 0:
            motorRightBack -= (differenceX * differenceMultiplier)
            motorRightFront -= (differenceX * differenceMultiplier)
            motorLeftBack += (differenceX * differenceMultiplier)
            motorLeftFront += (differenceX * differenceMultiplier)

        # Y Axis
        if differenceY < 0:
            motorRightBack += (-differenceY * differenceMultiplier)
            motorRightFront -= (-differenceY * differenceMultiplier)
            motorLeftBack += (-differenceY * differenceMultiplier)
            motorLeftFront -= (-differenceY * differenceMultiplier)
        elif differenceY > 0:
            motorRightBack -= (differenceY * differenceMultiplier)
            motorRightFront += (differenceY * differenceMultiplier)
            motorLeftBack -= (differenceY * differenceMultiplier)
            motorLeftFront += (differenceY * differenceMultiplier)

        # Set the values
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_BACK, motorRightBack)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_BACK, motorLeftBack)
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_FRONT, motorRightFront)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_FRONT, motorLeftFront)

    def level(self, parent):
        Navigation.targetRotation.x = 0
        Navigation.targetRotation.y = 0