# BNO085 Sensor Data Logger

This Python script utilizes the Adafruit BNO085 sensor to log accelerometer, gyroscope, magnetometer, and rotation vector data. The data is logged into a text file with a timestamp.

## Dependencies

Make sure to install the necessary libraries before running the script:

```bash
pip install adafruit-circuitpython-bno08x
```

## Usage

1. Connect the Adafruit BNO085 sensor to the appropriate pins on your board.
2. Run the [script](https://github.com/itskuldipsingh/Raspberry-Pi-Asus-Tinkerboard/blob/main/BNO085/BNO085_Data_Logger.py), and it will continuously log sensor data into timestamped text files in the "BNO085 Output" directory.

## Files and Directory Structure

- `BNO085_Output/`: Directory to store output files.
- `BNO085_Data_Logger.py`: Main Python script for data logging.

## How to Run

```bash
python BNO085_Data_Logger.py
```

## Output

The script will generate timestamped text files containing accelerometer, gyroscope, magnetometer, and rotation vector data in the "BNO085 Output" directory.

## Cleanup

The program can be interrupted at any time, and it will close the output file gracefully.

## Note

Ensure proper connections and check the sensor's datasheet for any additional setup requirements.

Feel free to explore and modify the script for your specific use case!
