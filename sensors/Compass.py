class Compass(Sensor):
    compassDirection = None
    def handle():
        print("Handling compass")
        Navigation.compassDirection = Compass.compassDirection