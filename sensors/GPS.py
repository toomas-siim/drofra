import gpsd

class GPS(Sensor):
    def handle():


    def getPositionData():
    	nx = gpsd.next()
    	if nx['class'] == 'TPV':
        	    latitude = getattr(nx, 'lat', "Unknown")
                    longitude = getattr(nx, 'lon', "Unknown")
        	    print "Your position: lon = " + str(longitude) + ", lat = " + str(latitude)