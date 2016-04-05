import adb

# Obtain the code name "mako/krillin/arale" from the device
def getProductName(deviceId=False):
    if deviceId:
        return adb.shell("getprop ro.product.device", deviceId).replace("\r", "").replace("\n", "")
    else:
        return adb.shell("getprop ro.product.device").replace("\r", "").replace("\n", "")

def getDevices():
    return adb.getDevices()
