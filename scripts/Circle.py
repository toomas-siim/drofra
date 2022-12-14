from services.Event import Event


class Circle:
    name = "Circle"

    coreHandle = None
    circlePoint = None
    rotationPoints = []
    currentPoint = 0

    REQUIREMENTS = [
        { "system": "sensor", "requirement": { "purpose": "altitude" }, "required": True },
        { "system": "sensor", "requirement": { "purpose": "rotation" }, "required": True },
        { "system": "sensor", "requirement": { "purpose": "direction" }, "required": True },
        { "system": "sensor", "requirement": { "purpose": "position" }, "required": True },
    ]

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        coreHandle.writeLog("Circle script initiated.")
        Event.addListener("in-communication-payload", self.gpsChange)

    def gpsChange(self, eventData):
        if eventData.payload.command == "host-gps-location":
            self.circlePoint = eventData.payload.coordinates

    def calcRotationPoints(self):
        # 100 m radius
        latLength = ((1/111) / 1000) * 100
        lonLength = ((1/111.321) / 1000) * 100
        circlePoint = self.circlePoint
        if circlePoint != None:
            self.rotationPoints = []
            self.rotationPoints.append({ "lat": circlePoint["lat"] - latLength, "lon": circlePoint["lon"] - lonLength })
            self.rotationPoints.append({ "lat": circlePoint["lat"] + latLength, "lon": circlePoint["lon"] - lonLength })
            self.rotationPoints.append({ "lat": circlePoint["lat"] + latLength, "lon": circlePoint["lon"] + lonLength })
            self.rotationPoints.append({ "lat": circlePoint["lat"] - latLength, "lon": circlePoint["lon"] + lonLength })

    def handle(self):
        if self.circlePoint == None:
            self.circlePoint = self.coreHandle.navigationSystem.position
            if self.circlePoint != None:
                self.calcRotationPoints()
                self.currentPoint = 0
        if len(self.rotationPoints) > 0:
            distance = self.coreHandle.navigationSystem.distanceFrom(self.rotationPoints[self.currentPoint]["lat"], self.rotationPoints[self.currentPoint]["lon"]) / 1000
            if distance < 5:
                self.currentPoint += 1
                if self.currentPoint >= len(self.rotationPoints):
                    self.currentPoint = 0
            self.coreHandle.navigationSystem.targetPosition = self.rotationPoints[self.currentPoint]