import picamera
import os
from PIL import Image
from mcpi.minecraft import Minecraft
from mcpi import *

minePalette = {
    (255, 255, 255):0, 	#white 0
    (255,165,0): 1,		#orange 1
    (255,0,255): 2,		#magenta 2
    (173,216,230): 3,	#light blue 3
    (255,255,0): 4,		#yellow 4
    (0,255,0): 5,		#lime 5
    (255,105,180): 6,	#pink 6
    (128,128,128): 7,	#grey 7
    (192,192,192): 8,	#lightgrey 8
    (0,255,255): 9,		#cyan 9
    (128,0,128): 10,		#purple 10
    (0,0,255): 11, 		#blue 11
    (139,69,19): 12,		#brown 12
    (0,128,0): 13,		#green 13
    (255,0,0): 14,		#red 14
    (0,0,0): 15			#black 15
}

# Take the photo using the PiCamera
camera = picamera.PiCamera()
camera.capture('/home/pi/Desktop/orig.jpeg')

# Resize the image using ImageMagick
os.system("convert /home/pi/Desktop/orig.jpeg -resize 64x64 /home/pi/Desktop/resized.jpeg")

# Colourmap the imsage using ImageMagick
os.system("convert /home/pi/Desktop/resized.jpeg -dither FloydSteinberg -remap /home/pi/Desktop/test.gif /home/pi/Desktop/remapped.gif")

# Open the image in Python  and convert to RGB
im = Image.open("/home/pi/Desktop/remapped.gif")
rgb_im = im.convert("RGB")

width, height = im.size		# get the size of the image

mc = Minecraft.create()

#pos = mc.player.getPos()
#previouspos
#currentPos = pos

for y in range(height):
	for x in range(width):
		rgb = rgb_im.getpixel((x,y))	# get the pixel from
		#if currPos.x-prevPos.x > currPos.z-prevPos.z:
			#if currPos.x-prevPos.x > 0:
			#else:
		#else:
			#if currPos.z-prevPos.z >0:
				
		mc.setBlock(x, height-y, 0, block.WOOL.id, minePalette[rgb]) 



