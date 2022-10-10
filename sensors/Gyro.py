import smbus
from time import sleep
from sensors.Sensor import Sensor

class Gyro(Sensor):
    PWR_MGMT_1   = 0x6B
    SMPLRT_DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_ENABLE   = 0x38

    GYRO_XOUT_H  = 0x43
    GYRO_YOUT_H  = 0x45
    GYRO_ZOUT_H  = 0x47

    GyroPos = {"x":0,"y":0,"z":0}
    bus = None

    def init(self, coreHandle):
        self.bus = smbus.SMBus(0) # @TODO
        #write to sample rate register
        self.bus.write_byte_data(Device_Address, Gyro.SMPLRT_DIV, 7)

        #Write to power management register
        self.bus.write_byte_data(Device_Address, Gyro.PWR_MGMT_1, 1)

        #Write to Configuration register
        self.bus.write_byte_data(Device_Address, Gyro.CONFIG, 0)

        #Write to Gyro configuration register
        self.bus.write_byte_data(Device_Address, Gyro.GYRO_CONFIG, 24)

        #Write to interrupt enable register
        self.bus.write_byte_data(Device_Address, Gyro.INT_ENABLE, 1)

    def read_raw_data(addr):
    	#Accelero and Gyro value are 16-bit
        high = self.bus.read_byte_data(Device_Address, addr)
        low = self.bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

    def handle(self):
        #Read Gyroscope raw value
        gyro_x = read_raw_data(Gyro.GYRO_XOUT_H)
        gyro_y = read_raw_data(Gyro.GYRO_YOUT_H)
        gyro_z = read_raw_data(Gyro.GYRO_ZOUT_H)
        Gyro.GyroPos["x"] = gyro_x/131.0
        Gyro.GyroPos["y"] = gyro_y/131.0
        Gyro.GyroPos["z"] = gyro_z/131.0
        Navigation.rotation = Gyro.GyroPos