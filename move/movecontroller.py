import serial
from time import sleep

def move ():
	PORT = "/dev/ttyACM1"
	BAUD = 115200
	
	s = serial.Serial(PORT)
	s.baudrate = BAUD
	s.parity = serial.PARITY_NONE
	s.databits = serial.EIGHTBITS
	s.stopbits = serial.STOPBITS_ONE
	
	while True:
		data = s.readline().decode('UTF-8')
		data_list = data.rtrip().split(' ')
		try:
			x, y, z, a, b = data_list
			print(x, y, z, a, b)
		
		except:
			pass
	
	s.close()
	
	
if __name__ == "__main__":
	move()
