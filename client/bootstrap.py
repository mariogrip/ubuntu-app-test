#!/usr/bin/env python
# python bootstrap script which seeks devices and launches one worker per device

from scripts import utils, device
import os, sys, threading, re
import worker
# Default orientation for all devices, dunno how we detect this yet
# Maybe we flash it then poke some dbus thing
defaultOrientation = "portrait"
protocol = "http://"
serverHost = "localhost:12346"
currentDir = os.getcwd()
regex = re.compile('[^a-zA-Z]')
friendlyNames = {"mako": {"name": "LG_Nexus_4"}, "krillin": {"name": "bq_Aquaris_E4.5_Ubuntu_Edition"}, "vegetahd": {"name": "bq_Aquaris_E5_Ubuntu_Edition"}, \
                "flo": {"name": "Asus_Nexus_7_2013", "orientation": "landscape"}, "arale": {"name": "Meizu_MX4_Ubuntu_Edition"}, "bacon": {"name": "OnePlus One"}}

def getFriendlyName(productId):
    if productId in friendlyNames:
        if not "orientation" in friendlyNames[productId]:
            friendlyNames[productId]["orientation"] = defaultOrientation
        return friendlyNames[productId]
    else:
        return {"name": "Unidentified_Device"}


# Identify all the devices attached (assume they exist)

utils.log("Bootstrap starting")
devices = False
for deviceId in device.getDevices():
    devices = True
    utils.log("Device found: %s" % deviceId)
    productId = device.getProductName(deviceId)
    utils.log("Product: %s" % productId)
    friendlyName = getFriendlyName(productId)
    utils.log("Friendly name: %s" % friendlyName["name"])
    utils.log("Orientation: %s" % friendlyName["orientation"])

    params = [deviceId, productId, friendlyName["orientation"]]
    args = ["%s%s" % (protocol, serverHost), friendlyName["name"], params, True]
    threading.Thread(target=worker.check_forever, args=args).start()
    #worker.check_forever("%s%s" % (protocol, serverHost), friendlyName["name"], params, True)


# If no devices are found, we spit out a status and die
# Ideally we should reboot the device assuming there is one
# but can't, because it's inaccessible. (need usb switch thing)
if not devices:
    utils.log("ERROR: No devices found, aborting")
    sys.exit()
