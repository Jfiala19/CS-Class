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

xmin, xmax = -.1320587425231933, -.12319782257080072
ymin, ymax = .9820419273376465, .9909028472900391
imgx, imgy = 512,512

maxIt = 256

image = Image.new("RGB", (imgx, imgy))

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
		r = int(1/(m.sin(m.log(i))))%256
		b = int(m.pow(i, m.e))%256
		g = int(1.1*m.sin(i))%256
		image.putpixel((x,y), (int(r),int(g),int(b)))
	print("Graphing "+str(int(((y/512)*100)))+"% complete")
px = image.load()

for y in range(imgy):
	for x in range(imgx):
		m = 3
		mlx, mmx, mly, mmy = (-1*m), m, (-1*m), m
		if mmx<x<(imgx + mlx) and mmy<y<(imgy+mly):
			for t in range(mly, mmy+1):
				for r in range(mlx, mmx+1):
					a,b,c = px[(x+r), (y+t)]
					w,e,u, = px[x, y]
					r,g,b = ((a+w)/2), ((b+e)/2), ((c+u)/2)
					image.putpixel((x,y), (int(r),int(g),int(b)))
		else:
			yfup = y
			yfdown = 512 - y
			xfright = x
			xfleft = 512 - x
			if (-1* yfup) >= mly:
				if yfup == 0:
					mly = 0
				else:
					mly = yfup-1
			if yfdown <= mmy:
				if yfdown == 0:
					mmy = 0
				else:
					mmy = yfdown -1
			if (-1* xfright) >= mlx:
				if xfright == 0:
					mlx = 0
				else:
					mlx = xfright -1
			if xfleft <= mmx:
				if xfleft == 0:
					mmx = 0
				else:
					mmx = xfleft -1
			for t in range(mly, mmy+1):
				for r in range(mlx, mmx+1):
					a,b,c = px[(x+r), (y+t)]
					w,e,u, = px[x, y]
					r,g,b = ((a+w)/2), ((b+e)/2), ((c+u)/2)
					image.putpixel((x,y), (int(r),int(g),int(b)))

	print("Smoothing " +str(int(((y/512)*100)))+"% complete")


image.show()



