import logging
import pandas
import time
import os
import pickle
import numpy as np

from scapy.all import *
from threading import Thread


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

#model
model_filename = "wifi_model.pkl"
with open(model_filename, "rb") as file:
    wifi_m = pickle.load(file)

interface = "wlan1mon"
networks = {'itis-pvt',
            'itis-wifi',
            'wifi-itis',
            'itis-pvt',
            'itis-wifi2',
            'AP_SMART25',
            'wifi-lab01',
            'AP_ITISLI03_2.5',
            'AP_SMART50',
            'AP_ITISLI03_5.0',
            'AP_ITISLI02'}
net_dict = {}

class scan():
    def __init__(self, destinazione):
        self.destinazione = destinazione

    def callback(self, packet):
        if packet.haslayer(Dot11Beacon):
            # get the name of it
            ssid = packet[Dot11Elt].info.decode()
            try:
                dbm_signal = packet.dBm_AntSignal
            except:
                dbm_signal = "N/A"
            if ssid in newtorks:
                net_dict[ssid] = dbm_signal

    def wifi(self):
        global net_dict, interface, networks
        net_dict = {i : None for i in networks}
        sniff(prn=self.callback, iface=interface, count=100)
        lan = np.array([[]])
        for net in newtorks:
            if net_dict[net] is None:
                np.append(lan, "-120")
            else: 
                np.append(lan,net_dict[net])
        
        return lan

    def wifiPositioning(self):
        actual_scan = self.wifi()
        actual_pos = wifi_m.predict(actual_scan)

        if actual_pos == self.destinazione:
            print("Sono arrivato")
        else:
            print("Non sono arrivato")
        