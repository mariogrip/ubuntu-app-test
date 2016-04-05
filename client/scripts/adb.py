# portscraft's adb wrapper

import subprocess as sub
import re

def isDeviceOnline():
    return re.sub(r'\W', '', getState()) == "device"

def getState():
    return sub.check_output(["adb", "get-state"]).decode("utf-8")

def getDevices():
    devices = []
    rawDevices = sub.check_output(["adb", "devices"]).decode("utf-8")
    rawDevices = rawDevices.split("\n")
    del rawDevices[0]
    for device in rawDevices:
        if device != "":
            devices.append(device.split("\t")[0])
    return devices

def shell(cmd, deviceId=False):
    if deviceId: run = ["adb", "-s", deviceId, "shell", cmd]
    else: run = ["adb", "shell", cmd]
    return sub.check_output(run).decode("utf-8")
