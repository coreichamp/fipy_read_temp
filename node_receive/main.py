from network import LoRa
import socket
import time
from machine import Pin
import pycom

lora = LoRa(mode=LoRa.LORA, frequency=863000000, bandwidth=LoRa.BW_125KHZ, tx_power=14, sf=12)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
pycom.heartbeat(False)

while True:
    data = s.recv(64)
    pycom.rgbled(0x101010)
    time.sleep(0.02)
    pycom.rgbled(0x101010)
    print(data)
    time.sleep(1)