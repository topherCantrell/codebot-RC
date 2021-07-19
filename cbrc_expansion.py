import machine
import network
import socket

# Connect to the wifi network
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('CodeBot','FiriaFiria')

# Listen for packets on UDP port 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',1234))

# Write motor values to UART1
uart = machine.UART(1,115200)

while True:
    # Wait for a packet from the remote control
    data, _addr = s.recvfrom(2)
    # Send the data over the UART
    uart.write(data)
