import time
import machine

# Micropython on ESP8266

class Nunchuck:

    """
       raw[0]   raw[1]   raw[2]   raw[3]   raw[4]   raw[5]
       aaaaaaaa bbbbbbbb cccccccc dddddddd eeeeeeee ffffffff gggggggg hhhhhhhh
       XXXXXXXX YYYYYYYY xxxxxxxx yyyyyyyy zzzzzzzz xxyyzzCZ

       X = Joystick X
       Y = Joystick Y
       x = Accelerometer X
       y = Accelerometer Y
       z = Accelerometer Z
       C = Button C (0=pressed)
       Z = Button Z (0=pressed)
    """

    def __init__(self,scl,sda):
        self._i2c = machine.I2C(scl=machine.Pin(scl),sda=machine.Pin(sda))
        self._i2c.writeto(0x52,b'\xF0\x55')
        time.sleep(.1)
        self._i2c.writeto(0x52,b'\xFB\x00')

    def get_raw(self):
        self._i2c.writeto(0x52,b'\x00')
        time.sleep(.1)
        ret = bytearray(8)
        self._i2c.readfrom_into(0x52,ret)
        return ret

    @staticmethod
    def get_joystick(raw):
        return (raw[0],raw[1])

    @staticmethod
    def get_buttons(raw):
        z = (raw[5]&1)==0
        c = (raw[5]&2)==0
        return (c,z)

    @staticmethod
    def get_accelerometer(raw):
        x = (raw[2]<<2) | ((raw[5]>>6) & 3)
        y = (raw[3]<<2) | ((raw[5]>>4) & 3)
        z = (raw[4]<<2) | ((raw[5]>>2) & 3)
        return (x,y,z)    


def test():
    nun1 = Nunchuck(sda=4,scl=5)   
    #nun2 = Nunchuck(sda=12,scl=13) 
    while True:
        raw1 = nun1.get_raw()
        #raw2 = nun2.get_raw()
        print(nun1.get_joystick(raw1))
        time.sleep(0.5)
