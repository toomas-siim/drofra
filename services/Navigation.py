from time import time
from math import radians, cos, sin, asin, sqrt

class Navigation:
    currentHeight = 0 # expected in cm
    targetHeight = 0 # expected in cm
    position = {"lat": 0, "lon": 0}
    targetPosition = {"lat": 0, "lon": 0}
    rotation = {"x": 0, "y": 0}
    speed = 0 # expected in km/h
    speedTracker = {"lastCheck": 0, "lastPos": {"lat": 0, "lon": 0}}

    def handle(parent):
        # @TODO: Load position, rotation, height
        Navigation.level(parent)
        Navigation.heightRegulation(parent)
        Navigation.updateSpeedData(parent)

    def updateSpeedData(parent):
        speedCheckInterval = 3
        if time.time() - Navigation.speedTracker.lastCheck > speedCheckInterval:
            distanceTraveled = Navigation.distanceFrom(Navigation.speedTracker.lastPos.lat, Navigation.speedTracker.lastPos.lon)
            distancePerHour = (distanceTraveled / speedCheckInterval) * 60 * 60
            Navigation.speed = round(distancePerHour, 2)

            # Update data
            Navigation.speedTracker.lastCheck = time.time()
            Navigation.speedTracker.lastPos = Navigation.position

    def distanceFrom(targetLat, targetLon):
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [Navigation.position.lon, Navigation.position.lat, targetLon, targetLat])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # Radius of earth in kilometers.
        return c * r

    def rotateRight(parent):
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_FRONT, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_BACK, Motor.SPEED_LOW)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_FRONT, Motor.SPEED_LOW)

    def rotateLeft(parent):
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_FRONT, Motor.SPEED_LOW)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_BACK, Motor.SPEED_LOW)
        parent.motorSystem.setValueByType(Motor.TYPE_RIGHT_BACK, Motor.SPEED_HIGH)
        parent.motorSystem.setValueByType(Motor.TYPE_LEFT_FRONT, Motor.SPEED_HIGH)

    def heightRegulation(parent):
        if Navigation.currentHeight > Navigation.targetHeight + 3:
            parent.motorSystem.setFrontMotors(Motor.SPEED_HIGH)
            parent.motorSystem.setBackMotors(Motor.SPEED_HIGH)
        elif Navigation.currentHeight < Navigation.targetHeight - 3:
            parent.motorSystem.setFrontMotors(Motor.SPEED_LOW)
            parent.motorSystem.setBackMotors(Motor.SPEED_LOW)

    def level(parent):
        # X Axis
        if Navigation.rotation.x < -5:
            parent.motorSystem.setLeftMotors(Motor.SPEED_HIGH)
            parent.motorSystem.setRightMotors(Motor.SPEED_LOW)
            return True
        elif Navigation.rotation.x > 5:
            parent.motorSystem.setLeftMotors(Motor.SPEED_LOW)
            parent.motorSystem.setRightMotors(Motor.SPEED_HIGH)
            return True
        else:
            parent.motorSystem.setLeftMotors(Motor.SPEED_MID)
            parent.motorSystem.setRightMotors(Motor.SPEED_MID)

        # Y Axis
        if Navigation.rotation.y < -5:
            parent.motorSystem.setFrontMotors(Motor.SPEED_HIGH)
            parent.motorSystem.setBackMotors(Motor.SPEED_LOW)
            return True
        elif Navigation.rotation.y > 5:
            parent.motorSystem.setFrontMotors(Motor.SPEED_LOW)
            parent.motorSystem.setBackMotors(Motor.SPEED_HIGH)
            return True
        else:
            parent.motorSystem.setFrontMotors(Motor.SPEED_MID)
            parent.motorSystem.setBackMotors(Motor.SPEED_MID)

        return False