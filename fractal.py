from PIL import Image
import math as m
import colorsys

x, y = 1,1
imgx, imgy = 512,512


image = Image.new("HSV", (imgx, imgy))
while x < 512:
	x2 = y - m.sin(x)*pow(abs(x), .5)
	y = .4 - x
	x = x2
	if 0<y<512 and 0<x<512:
		image.putpixel((int(x),int(y)), (255,0,0))
image.show()
