import gpsd

class GPS(Sensor):
    def handle():
        Navigation.position = GPS.getPositionData()

    def getPositionData():
    	nx = gpsd.next()
    	if nx['class'] == 'TPV':
            latitude = getattr(nx, 'lat', 0)
            longitude = getattr(nx, 'lon', 0)
            return {"lat": latitude, "lon": longitude}