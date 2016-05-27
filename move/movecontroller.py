# Requires `sudo apt-get install libudev-dev`
# Then:
# `sudo pip3 install python-uinput`
# &:
# `sudo modprobe uinput`
# Code heavily based on https://www.raspberrypi.org/learning/microbit-game-controller/worksheet/


import serial
from time import sleep

def move ():	
    deadzone_x = 200
    deadzone_y = 200
        
    PORT = "/dev/ttyACM0"
    #~ PORT = "/dev/ttyACM1"
    #~ PORT = "/dev/serial/by-id/usb-MBED_MBED_CMSIS-DAP_9900023431864e45001210060000003700000000cc4d28bd-if01"
    BAUD = 115200
    
    s = serial.Serial(PORT)        
    s.baudrate = BAUD
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    
    while True:
        data = s.readline().decode('UTF-8')
        data_list = data.rstrip().split(' ')
        try:
            x, y, z, a, b = data_list
            if int(x) < (0 - deadzone_x) :
                print("a")
            if int(x) > deadzone_x:
                print("d")
            if int(y) < (0 - deadzone_y):
                print("w")
            if int(y) > deadzone_y:
                print("s")		
        except:
            pass
    s.close()
	
	
if __name__ == "__main__":
    move()
