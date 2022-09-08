class Circle:
    coreHandle = None
    circlePoint = None
    rotationPoints = []
    currentPoint = 0

    def init(self, coreHandle):
        self.coreHandle = coreHandle
        Event.addListener("in-communication-payload", self.gpsChange)

    def gpsChange(self, eventData):
        if eventData.payload.command is "host-gps-location":
            self.circlePoint = eventData.payload.coordinates

    def calcRotationPoints(self):
        # 100 m radius
        latLengthInKm = ((1/111) / 1000) * 100
        lonLengthInKm = ((1/111.321) / 1000) * 100
        circlePoint = self.circlePoint
        self.rotationPoints = []
        self.rotationPoints.push({ lat: circlePoint.lat - latLengthInKm, lon: circlePoint.lat - lonLengthInKm })
        self.rotationPoints.push({ lat: circlePoint.lat + latLengthInKm, lon: circlePoint.lat - lonLengthInKm })
        self.rotationPoints.push({ lat: circlePoint.lat + latLengthInKm, lon: circlePoint.lat + lonLengthInKm })
        self.rotationPoints.push({ lat: circlePoint.lat - latLengthInKm, lon: circlePoint.lat + lonLengthInKm })

    def handle(self):
        if self.circlePoint is None:
            self.circlePoint = GPS.getPositionData()
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