from time import time
from math import radians, cos, sin, asin, sqrt

from services.DroneType.Plane.PlaneNavigation import PlaneNavigation
from services.DroneType.Quadcopter.QuadcopterNavigation import QuadcopterNavigation

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

    def init(self, parent):
        self.coreHandle = parent
        if parent.droneType == "quadcopter":
            self.navigationHandle = QuadcopterNavigation()
        elif parent.droneType == "plane":
            self.navigationHandle = PlaneNavigation()
        self.navigationHandle.level(parent)

    def handle(self):
        if self.coreHandle.flightStatus == True:
            self.moveToTarget(self.coreHandle)
            self.alignToTarget(self.coreHandle)
            self.navigationHandle.heightRegulation(self.coreHandle)
            self.navigationHandle.rotationRegulation(self.coreHandle)
            self.updateSpeedData(self.coreHandle)

    def stop(self):
        self.navigationHandle.stop()

    def moveToTarget(self, parent):
        distance = self.distanceFrom(self.targetPosition["lat"], self.targetPosition["lon"]) * 1000 # in meters
        if distance > 1 or distance < -1:
            self.navigationHandle.moveForward()

    def alignToTarget(self, parent):
        targetDirection = self.calculateTargetDirection()
        myDirection = self.compassDirection

        if targetDirection - 5 > myDirection:
            self.navigationHandle.rotateLeft(parent)
        elif targetDirection + 5 < myDirection:
            self.navigationHandle.rotateRight(parent)

    def calculateTargetDirection(self):
        latDifference = self.position["lat"] - self.targetPosition["lat"]
        lonDifference = self.position["lon"] - self.targetPosition["lon"]
        direction = 0

        if latDifference < 0:
            direction = -90
        elif latDifference > 0:
            direction = 90

        if direction == 0:
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
        if time.time() - self.speedTracker.lastCheck > speedCheckInterval:
            distanceTraveled = self.distanceFrom(self.speedTracker.lastPos["lat"], self.speedTracker.lastPos["lon"])
            distancePerHour = (distanceTraveled / speedCheckInterval) * 60 * 60
            self.speed = round(distancePerHour, 2)

            # Update data
            self.speedTracker.lastCheck = time.time()
            self.speedTracker.lastPos = self.position

    def distanceFrom(self, targetLat, targetLon):
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [self.position["lon"], self.position["lat"], targetLon, targetLat])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371 # Radius of earth in kilometers.
        return c * r