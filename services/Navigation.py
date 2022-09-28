from time import time
from math import radians, cos, sin, asin, sqrt

class Navigation:
    navigationHandle = None
    coreHandle = None

    currentHeight = 0 # expected in cm
    targetHeight = 0 # expected in cm
    position = {"lat": 0, "lon": 0}
    targetPosition = {"lat": 0, "lon": 0}
    rotation = {"x": 0, "y": 0} # Gyro rotations
    targetRotation = {"x": 0, "y": 0} # Target Gyro rotations
    compassDirection = 0 # Most likely degrees from north to north: 0 - 360 or -180 to 180
    speed = 0 # expected in km/h
    speedTracker = {"lastCheck": 0, "lastPos": {"lat": 0, "lon": 0}}

    def init(parent):
        Navigation.coreHandle = parent
        if parent.droneType is "quadcopter":
            Navigation.navigationHandle = Quadcopter.QuadcopterNavigation()
        elif parent.droneType is "plane":
            Navigation.navigationHandle = Plane.PlaneNavigation()
        Navigation.navigationHandle.level(parent)

    def handle():
        # @TODO: Load altitude
        if Navigation.coreHandle.flightStatus is True:
            Navigation.moveToTarget(Navigation.coreHandle)
            Navigation.alignToTarget(Navigation.coreHandle)
            Navigation.navigationHandle.heightRegulation(Navigation.coreHandle)
            Navigation.navigationHandle.rotationRegulation(Navigation.coreHandle)
            Navigation.updateSpeedData(Navigation.coreHandle)
        else:
            Navigation.navigationHandle.stop()

    def moveToTarget(parent):
        distance = Navigation.distanceFrom(Navigation.targetPosition.lat, Navigation.targetPosition.lon) * 1000 # in meters
        if distance > 1 or distance < -1:
            Navigation.navigationHandle.moveForward()

    def alignToTarget(parent):
        targetDirection = Navigation.calculateTargetDirection()
        myDirection = Navigation.compassDirection

        if targetDirection - 5 > myDirection:
            Navigation.navigationHandle.rotateLeft(parent)
        elif targetDirection + 5 < myDirection:
            Navigation.navigationHandle.rotateRight(parent)

    def calculateTargetDirection():
        latDifference = Navigation.position.lat - Navigation.targetPosition.lat
        lonDifference = Navigation.position.lon - Navigation.targetPosition.lon
        direction = 0

        if latDifference < 0:
            direction = -90
        elif latDifference > 0:
            direction = 90

        if direction is 0:
            if lonDifference < 0:
                direction = 0
            elif lonDifference > 0:
                direction = 180
        else:
            if lonDifference < 0:
                direction -= 45
            elif lonDifference > 0:
                direction += 45
        return direction

    def updateSpeedData(parent):
        speedCheckInterval = 3 # update every 3 sec
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