import botcore
import machine

botcore.motors.enable(True)

# UART5 is connected to GPIO0 (rx) and GPIO1 (tx)
uart = machine.UART(5,115200)

while True:

    # Get a value for the left motor
    while not uart.any():
        pass
    left = uart.read(1)
    left = left[0] - 128 # -128 to +127
    
    # Get a value for the right motor
    while not uart.any():
        pass
    right = uart.read(1)
    right = right[0] - 128 # -128 to +127

    # Set the motors
    botcore.motors.run(0,left)
    botcore.motors.run(1,right)
        