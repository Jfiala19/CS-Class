#Jack Fiala
#10/21/18
#Using Mandelbrot Sets and other fractals to assign colors to pixels, generating artwork
#https://www.atopon.org/mandel/
#https://docs.python.org/2/library/colorsys.html
#http://answers.opencv.org/question/184281/how-are-hsv-values-interpreted-in-python/

from PIL import Image
import math as m
import colorsys #import color sys function
from PIL import ImageFilter #import filter library



#xmin, xmax = -.3829037428734658,  -.37
#ymin, ymax = -.651238745612374, -.64
xmin, xmax = -.778180596923828, -.7682921905517578
ymin, ymax = .12040606689453121, .130296260351562
imgx, imgy = 512,512

maxIt = 256

image = Image.new("RGB", (imgx, imgy))
image = image.filter(ImageFilter.SMOOTH_MORE)

for y in range(imgy):
	cy = y * (ymax-ymin) / (imgy-1 )+ ymin
	for x in range(imgx):
		cx = x * (xmax-xmin) / (imgx-1) + xmin
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c
		h = ((1.3*i**5)%256)/256
		s = 1 - i/256
		v = 1 - i/500
		r,g,b = colorsys.hsv_to_rgb(h,s,v)
		r,g,b = r*255, g*255, b*255
		image.putpixel((x,y), (int(r),int(g),int(b)))
	print("Graphing "+str(int(((y/512)*100)))+"% complete")




image.show()



