import smbus
import time

# Create an instance of the I2C bus
bus = smbus.SMBus(1)  # Raspberry Pi uses bus 1

# Function to scan and list I2C devices
def scan_i2c_devices():
    print("Scanning for I2C devices...")
    devices = []
    for address in range(3, 128):
        try:
            bus.write_byte(address, 0)
            devices.append(hex(address))
        except IOError:
            # No device at this address
            pass
    return devices

# Main execution
if __name__ == "__main__":
    i2c_devices = scan_i2c_devices()
    if i2c_devices:
        print("Found I2C devices at addresses:", ", ".join(i2c_devices))
    else:
        print("No I2C devices found.")
