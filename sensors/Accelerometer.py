import smbus
from time import sleep

class Accelerometer(Sensor):
    PWR_MGMT_1   = 0x6B
    SMPLRT_DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_ENABLE   = 0x38

    ACCEL_XOUT_H = 0x3B
    ACCEL_YOUT_H = 0x3D
    ACCEL_ZOUT_H = 0x3F

    AcceleroPos = {"x":0,"y":0,"z":0}

    def init(self, coreHandle):
        #write to sample rate register
        bus.write_byte_data(Device_Address, self.SMPLRT_DIV, 7)

        #Write to power management register
        bus.write_byte_data(Device_Address, self.PWR_MGMT_1, 1)

        #Write to Configuration register
        bus.write_byte_data(Device_Address, self.CONFIG, 0)

        #Write to Gyro configuration register
        bus.write_byte_data(Device_Address, self.GYRO_CONFIG, 24)

        #Write to interrupt enable register
        bus.write_byte_data(Device_Address, self.INT_ENABLE, 1)

    def read_raw_data(addr):
    	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

    def handle(self):
        #Read Accelerometer raw value
        gyro_x = read_raw_data(self.ACCEL_XOUT_H)
        gyro_y = read_raw_data(self.ACCEL_YOUT_H)
        gyro_z = read_raw_data(self.ACCEL_ZOUT_H)
        self.AcceleroPos.x = gyro_x/16384.0
        self.AcceleroPos.y = gyro_y/16384.0
        self.AcceleroPos.z = gyro_z/16384.0