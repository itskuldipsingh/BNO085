#1Start
import sys
import math
import datetime
import os  # Import the os module for file path operations
#1Stop
import time
import board
import busio
from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_MAGNETOMETER,
    BNO_REPORT_ROTATION_VECTOR,
)
from adafruit_bno08x.i2c import BNO08X_I2C

# Create a directory if it doesn't exist
output_directory = "BNO085 Output"
os.makedirs(output_directory, exist_ok=True)

#2Start
program = sys.argv[0]
fc = program[0]
now = datetime.datetime.now()
StartTS = now.strftime("%Y%b%H%M%S")
outputfile = os.path.join(output_directory, program + "_" + str(StartTS) + ".txt")
fout = open(outputfile, 'w', encoding='utf-8')
print("Output File:", outputfile)

#2Stop

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
bno = BNO08X_I2C(i2c)

bno.enable_feature(BNO_REPORT_ACCELEROMETER)
bno.enable_feature(BNO_REPORT_GYROSCOPE)
bno.enable_feature(BNO_REPORT_MAGNETOMETER)
bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)

start_time = datetime.datetime.now()

while True:
    elapsed_time = datetime.datetime.now() - start_time
    timestamp = "{:02d}:{:02d}:{:02d}:{:05d}".format(
        elapsed_time.seconds // 3600,
        (elapsed_time.seconds % 3600) // 60,
        elapsed_time.seconds % 60,
        elapsed_time.microseconds // 1000,
    )
    time.sleep(0.5)

    accel_x, accel_y, accel_z = bno.acceleration  # pylint:disable=no-member
    position = accel_x * 0.5 * 0.5
    s = "{} - Acceleration:: X: {:.6f}  Y: {:.6f} Z: {:.6f}  m/s^2 Position: {:.6f}".format(
        timestamp, accel_x, accel_y, accel_z, position
    )
    print(s)
    fout.write(s)
    print("")

    gyro_x, gyro_y, gyro_z = bno.gyro  # pylint:disable=no-member
    s = "{} - Gyro:: X: {:.6f}  Y: {:.6f} Z: {:.6f} rads/s".format(
        timestamp, gyro_x, gyro_y, gyro_z
    )
    print(s)
    fout.write(s)
    print("")

    mag_x, mag_y, mag_z = bno.magnetic  # pylint:disable=no-member
    s = "{} - Magnetometer:: X: {:.6f}  Y: {:.6f} Z: {:.6f} uT".format(
        timestamp, mag_x, mag_y, mag_z
    )
    print(s)
    fout.write(s)
    print("")
    quat_i, quat_j, quat_k, quat_real = bno.quaternion  # pylint:disable=no-member
    s = "{} - Rotation Vector Quaternion:: I: {:.6f}  J: {:.6f} K: {:.6f}  Real: {:.6f}".format(
        timestamp, quat_i, quat_j, quat_k, quat_real
    )
    print(s)
    fout.write(s)
    fout.write("\n")
    print("")

fout.close()
