from PIL import Image
imgx = 512
imgy = 512
import math
import random as r 
image = Image.new("RGB", (imgx, imgy))
image.putpixel((0,0), (255, 0, 0))
s = int(input("Number of streamers"))


for x in range(s):
	xi = r.randint(0, 511)
	yi = 0
	R,G,B = r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
	image.putpixel((xi,yi), (R, G, B))
	for z in range(512):
		deltax = r.randint(-1, 1)	
		xi = xi + deltax
		if 0<=xi<=511:
			image.putpixel((xi,z), (R, G, B))
		else:
			xi = xi - (2*deltax)
			image.putpixel((xi,z), (R, G, B))
image.save("snakes.png", "PNG")