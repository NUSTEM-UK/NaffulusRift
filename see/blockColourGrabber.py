#This programme was written to identify all the various RGB colours in Minecraft for the Raspberry Pi 
# I'm 100% confident there's an easier way to do it but... damned if I can find it

import os
from PIL import Image
from mcpi.minecraft import Minecraft
from mcpi import *
import pyscreenshot as ImageGrab

im = ImageGrab()
ImageGrab.grab_to_file('/home/pi/Desktop/desk.png')