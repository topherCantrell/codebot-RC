import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('ON')
s.sendto(b'\xFF\xA0\xA0', ('192.168.1.157',1234))

time.sleep(5)

print('OFF')
s.sendto(b'\xFF\x80\x80', ('192.168.1.157',1234))

time.sleep(5)
print('ON')
s.sendto(b'\xFF\xA0\xA0', ('192.168.1.157',1234))

time.sleep(5)

print('OFF')
s.sendto(b'\xFF\x80\x80', ('192.168.1.157',1234))