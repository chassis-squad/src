import logging

from lib.arduino.commandToArduino import ArduinoCommands
from lib.lidar.lidarObjectModel import *
from lib.wifi.wifiScan import scan

# LOGGING PLATFORM
LOGGING_FILE = "./log/log.log"
logging.basicConfig(filename=LOGGING_FILE, encoding="utf-8", level=logging.DEBUG)

destinazione = input("Inserisci posizione di destinazione:--> ")

while True:
        scan.wifiPositioning(destinazione)
