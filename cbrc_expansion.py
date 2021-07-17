import machine
import network
import socket

uart = machine.UART(1,115200)

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('CodeBot','FiriaFiria')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',1234))

def loop():
    while True:
        data,_ = s.recvfrom(2)
        uart.write(data)
        print(data)

if __name__ == '__main__':
    loop()
