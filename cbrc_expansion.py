import machine
import network
import socket

uart = machine.UART(1,115200)

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('TopherNet','NetTopher1')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',1234))

def loop():
    while True:
        data,_ = s.recvfrom(3)
        uart.write(data)
        print(data)