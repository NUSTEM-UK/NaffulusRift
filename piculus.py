# Requires sudo pip3 install pyuserinput python3-xlib 

import serial
from time import sleep
from pykeyboard import PyKeyboard
from gpiozero import Button


def move ():
	deadzone_x = 200
	deadzone_y = 200
	key_delay = 0.4
	
	if jumpPad.is_pressed:
		# It's set to pullup then shorted to ground, so we're working backwards here.
		keyboard.press_key('space')
		time.sleep(key_delay)
		keyboard.release_key('space')
	data = s.readline().decode('UTF-8')
	data_list = data.rstrip().split(' ')
	try:
		x, y, z, a, b = data_list
		if int(x) < (0 - deadzone_x) :
			keyboard.press_key('a')
			time.sleep(key_delay)
			keyboard.release_key('a')
		if int(x) > deadzone_x:
			keyboard.press_key('d')
			time.sleep(key_delay)
			keyboard.release_key('d')
		if int(y) < (0 - deadzone_y):
			keyboard.press_key('w')
			time.sleep(key_delay)
			keyboard.release_key('w')
		if int(y) > deadzone_y:
			keyboard.press_key('s')
			time.sleep(key_delay)
			keyboard.release_key('s')
		else:
			keyboard.release_key('a')
			keyboard.release_key('d')
			keyboard.release_key('w')
			keyboard.release_key('s')
		#~ print(x, y, z, a, b)
	except:
		pass
		
	
	
	
if __name__ == "__main__":

	# Set up serial connection to Micro:Bit (move controller)
	PORT = "/dev/ttyACM2"
	# may need to `ls /dev/ttyA*` to find the right Micro:Bit, and sub in line above
	BAUD = 115200
	
	s = serial.Serial(PORT)
	s.baudrate = BAUD
	s.parity = serial.PARITY_NONE
	s.databits = serial.EIGHTBITS
	s.stopbits = serial.STOPBITS_ONE
	
	keyboard = PyKeyboard()
	jumpPad = Button(11, pull_up=True)
	
	while True:
		move()	# read serial and process move controller commands
	
	s.close() # Close connection to Micro:Bit (move controller)
