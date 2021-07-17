import botcore
import machine

uart = machine.UART(5,115200)
botcore.motors.enable(True)

cmd = [0,0]
pos = 0

while True:
    data = uart.read(1)
    if not data:
        continue
    for g in data:        
        cmd[pos] = g
        pos+=1
        if pos==2:
            pos = 0
            left = cmd[0] - 128
            right = cmd[1] - 128
            print('motors',left,right)
            botcore.motors.run(0,left)
            botcore.motors.run(1,right)
        