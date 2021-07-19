import socket
import time
import network
from nunchuck import Nunchuck

# Create a WiFi network for the CodeBot to join
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='CodeBot', password='FiriaFiria')

# Use this socket to send values to the robot
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Nunchuck controllers
nun_left = Nunchuck(sda=4,scl=5)
nun_right =Nunchuck(sda=12,scl=14)

def scale(joy):
    joy = joy - 128
    joy = joy / 3
    joy = joy + 128
    return int(joy)

last_left = None
last_right = None

while True:
    # Get the Y stick values for left and right
    data_left = nun_left.get_raw()
    data_right = nun_right.get_raw()        
    joy_left = Nunchuck.get_joystick(data_left)[1]        
    joy_right = Nunchuck.get_joystick(data_right)[1]

    # Scale the values to a reasonable motor speed
    joy_left = scale(joy_left)
    joy_right = scale(joy_right)        

    # Only send a packet if things changed
    if joy_left != last_left or joy_right != last_right:
        last_left = joy_left
        last_right = joy_right
        s.sendto(bytes([joy_left,joy_right]), ('192.168.4.2',1234))
