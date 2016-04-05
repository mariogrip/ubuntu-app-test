# portscraft's utils

import os, time

homeDir = os.getenv("HOME")
dateStart = time.strftime("%Y%m%d%H%M%S")
defaultLogDir = "%s/.cache/marvin/%s" % (homeDir, dateStart)
defaultLogFile = "bootstrap.log"

def log(message, file=defaultLogFile, dir=defaultLogDir):
    message = "%s: %s" % (time.strftime("%Y%m%d%H%M%S"), message)
    print(message)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open("%s/%s" % (dir, file), "a") as logFile:
        logFile.write(message)
