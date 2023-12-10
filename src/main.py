import smbus
import time
import logging

class I2CScanner:
    """
    A class used to represent an I2C Scanner

    ...

    Attributes
    ----------
    bus : smbus.SMBus
        an instance of the I2C bus

    Methods
    -------
    scan_devices():
        Scans for I2C devices connected to the bus and returns their addresses.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the I2CScanner object.
        """
        self.bus = smbus.SMBus(1)  # Raspberry Pi uses bus 1

    def scan_devices(self):
        """
        Scans for I2C devices connected to the bus.

        It iterates over a range of possible addresses (3 to 127 inclusive), and attempts to write a byte to each address.
        If the write operation is successful, it means there is a device at that address, and the address is added to the list of devices.
        If the write operation fails (IOError), it means there is no device at that address, and the function continues to the next address.

        Returns:
            list: A list of hexadecimal strings representing the addresses of the found I2C devices.
        """
        print("Scanning for I2C devices...")
        devices = []  # Initialize an empty list to store the addresses of the found devices
        for address in range(3, 128):  # Iterate over the range of possible addresses
            try:
                self.bus.write_byte(address, 0)  # Try to write a byte to the current address
                devices.append(hex(address))  # If successful, add the address to the list of devices
            except IOError as e:
                # If an IOError is raised, log the error and continue to the next address
                logging.error(f"Failed to write to address {hex(address)}: {e}")
        return devices  # Return the list of found devices

# Main execution
if __name__ == "__main__":
    scanner = I2CScanner()
    i2c_devices = scanner.scan_devices()
    if i2c_devices:
        print("Found I2C devices at addresses:", ", ".join(i2c_devices))
    else:
        print("No I2C devices found.")