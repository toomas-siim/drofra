import gpsd

class GPS(Sensor):
    def handle():


    def getPositionData():
    	nx = gpsd.next()
    	if nx['class'] == 'TPV':
            latitude = getattr(nx, 'lat', 0)
            longitude = getattr(nx, 'lon', 0)
            return (latitude, longitude)