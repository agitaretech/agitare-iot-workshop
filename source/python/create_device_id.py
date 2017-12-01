#!/usr/bin/env python

import sys
from iothub_service_client import IoTHubRegistryManager, IoTHubRegistryManagerAuthMethod
from iothub_service_client import IoTHubDeviceStatus, IoTHubError

# get Python version
VERSION = sys.version_info[0]

# redefine the input() function if older version
if VERSION == 2:
    input = raw_input

def print_device_info(iothub_device):
    """Prints device information on the console

    :param: `iothub_device` The IoT Hub device information

    :type: `iothub_device` dict
    """
    print("IoT Hub Device:")
    print("  iothubDevice.deviceId                    = {0}".format(iothub_device.deviceId))
    print("  iothubDevice.primaryKey                  = {0}".format(iothub_device.primaryKey))
    print("  iothubDevice.secondaryKey                = {0}".format(iothub_device.secondaryKey))
    print("  iothubDevice.connectionState             = {0}".format(iothub_device.connectionState))
    print("  iothubDevice.status                      = {0}".format(iothub_device.status))
    print("  iothubDevice.lastActivityTime            = {0}".format(iothub_device.lastActivityTime))
    print("  iothubDevice.cloudToDeviceMessageCount   = {0}".format(iothub_device.cloudToDeviceMessageCount))
    print("  iothubDevice.isManaged                   = {0}".format(iothub_device.isManaged))
    print("  iothubDevice.authMethod                  = {0}".format(iothub_device.authMethod))
    print("")

def create_iothub_device(connection_string, device_id="AgitareTechIoTWorkshopDevice"):
    """Creates device in Azure IoT Hub using the specified identifier

    :param: `connection_string` A connection string used to connect to IoT Hub

    :param: `device_id` The device identifier to use; defaults to _AgitareTechIoTWorkshopDevice_

    :type: `connection_string` str

    :type: `device_id` str
    """
    try:
        iothub_registry_manager = IoTHubRegistryManager(connection_string)
        auth_method = IoTHubRegistryManagerAuthMethod.SHARED_PRIVATE_KEY
        new_device = iothub_registry_manager.create_device(device_id, "", "", auth_method)
        print_device_info(new_device)

    except IoTHubError as iothub_error:
        print("Unexpected error {0}".format(iothub_error))
        return
    except KeyboardInterrupt:
        print("Creation of IoT Hub device stopped")

if __name__ == '__main__':
    print("")
    print("Python {0}".format(sys.version))
    print("")

    # ask for user input
    CONNECTION_STRING = input("Please enter Azure IoT Hub connection string: ")
    DEVICE_ID = input("Please enter device identifier              : ")
    print("")

    # show the information used to create the device
    print("Creating device using the Azure IoT Hub Service SDK for Python")
    print("    Connection string = {0}".format(CONNECTION_STRING))
    print("    Device ID         = {0}".format(DEVICE_ID))

    # create the device
    create_iothub_device(CONNECTION_STRING, DEVICE_ID)
