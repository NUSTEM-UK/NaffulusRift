for i in len(prevImage):
    a,b,c,d = prevImage[i]
    mc.setBlock(a,b,c,d)
prevImage[:]=[]     #clear the previous image data

for y in range(height):
    for x in range(width):
        block = mc.getBlock(pos.x-(width/2)+x, height-y, pos.z-10)
        prevImage.append(pos.x-(width/2)+x, height-y, pos.z-10, block)
        rgb = rgb_im.getpixel((x,y))
        