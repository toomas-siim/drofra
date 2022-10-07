class Circle(Object):
    coreHandle = None
    circlePoint = None
    rotationPoints = []
    currentPoint = 0

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        Event.addListener("in-communication-payload", self.gpsChange)

    def gpsChange(self, eventData):
        if eventData.payload.command == "host-gps-location":
            self.circlePoint = eventData.payload.coordinates

    def calcRotationPoints(self):
        # 100 m radius
        latLength = ((1/111) / 1000) * 100
        lonLength = ((1/111.321) / 1000) * 100
        circlePoint = self.circlePoint
        self.rotationPoints = []
        self.rotationPoints.push({ lat: circlePoint.lat - latLength, lon: circlePoint.lat - lonLength })
        self.rotationPoints.push({ lat: circlePoint.lat + latLength, lon: circlePoint.lat - lonLength })
        self.rotationPoints.push({ lat: circlePoint.lat + latLength, lon: circlePoint.lat + lonLength })
        self.rotationPoints.push({ lat: circlePoint.lat - latLength, lon: circlePoint.lat + lonLength })

    def handle(self):
        if self.circlePoint == None:
            self.circlePoint = Navigation.position
            if self.circlePoint != None:
                self.calcRotationPoints()
                self.currentPoint = 0
        if len(self.rotationPoints) > 0:
            distance = Navigation.distanceFrom(self.rotationPoints[self.currentPoint].lat, self.rotationPoints[self.currentPoint].lon) / 1000
            if distance < 5:
                if len(self.rotationPoints) <= self.currentPoint:
                    self.currentPoint = 0
                else:
                    self.currentPoint += 1
            Navigation.targetPosition = self.rotationPoints[self.currentPoint]