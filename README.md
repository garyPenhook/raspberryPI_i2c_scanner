# rastpberryPI_i2c_scanner

# Raspberry Pi I2C Device Scanner

## Overview
This Python script is designed for the Raspberry Pi 4 to scan and list the addresses of devices connected via the I2C interface. It's a handy tool for verifying connections and debugging I2C communications.

## Requirements
- **Raspberry Pi 4**: This script is tailored for the Raspberry Pi 4.
- **Python 3**: The script is written in Python 3.
- **SMBus Library**: Python SMBus library is required to interact with the I2C bus.

## Setup
Before running the script, ensure your setup meets the following criteria:

1. **Enable I2C on Raspberry Pi**:
   - Run `sudo raspi-config`.
   - Navigate to `Interfacing Options` -> `I2C` and enable it.
   - Reboot the Raspberry Pi if prompted.

2. **Install SMBus**:
   - Install the SMBus library with the command:
     ```
     sudo apt-get install python3-smbus
     ```

3. **Connect I2C Devices**:
   - Connect your I2C devices to the GPIO 2 (SDA) and GPIO 3 (SCL) pins.
   - Ensure proper power and ground connections are made.

## Running the Script
1. Save the script as `i2c_scanner.py` (or another name of your choosing).
2. Run the script using Python 3:
