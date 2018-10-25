#Jack Fiala
#10/21/18

#Using Mandelbrot Sets and other fractals to assign colors to pixels, generating artwork



#https://www.atopon.org/mandel/
#https://docs.python.org/2/library/colorsys.html
#http://answers.opencv.org/question/184281/how-are-hsv-values-interpreted-in-python/
#https://natureofcode.com/book/chapter-8-fractals/   ------ used just for inspiration, no code looked at
#https://pillow.readthedocs.io/en/5.3.x/reference/PixelAccess.html



#OMH

from PIL import Image #picture library
import math
import colorsys #import color sys function
from PIL import ImageFilter #import filter library

maxIt = 256 #Max iterations for all Mandelbrots is 256, prevents infinite looping


xmin, xmax = -.778180596923828, -.7682921905517578 #the scope for the first Mandelbrot graph
ymin, ymax = .12040606689453121, .130296260351562
xmin2, xmax2 = -.1320587425231933, -.12319782257080072  #the scope for the second Mandelbrot graph
ymin2, ymax2 = .9820419273376465, .9909028472900391


imgx, imgy = 512,512 #all images are 512 by 512

image1 = Image.new("RGB", (imgx, imgy)) #creating all three images
image2 = Image.new("RGB", (imgx, imgy))
image3 = Image.new("RGB", (imgx, imgy))

image1 = image1.filter(ImageFilter.SMOOTH_MORE) #the first image has a filter that smoothes it



#-----------------------FIRST GRAPH----------------------------------------------------------------
for y in range(imgy): #goes through each column
	cy = y * (ymax-ymin) / (imgy-1 )+ ymin #each column is assigned a y component (imaginary part) of a complex number by mapping them
	for x in range(imgx): #goes through each row
		cx = x * (xmax-xmin) / (imgx-1) + xmin #same as ^^^^ but for x component (real part)
		c = complex(cx, cy) #putting the two components as 1 complex number
		z = 0 #Zsub0 is always 0 
		for i in range(maxIt): #loops through mandelbrot formula while always keeping track of the number of recursions. This loop will max out at 256 x through
			if abs(z) > 2.0: #if it is outside the circle, break, i is how many times it has looped up to this point
				break
			z = z**2 + c #the formula: the previous Z squared + the original complex number
		
		h = ((1.3*i**5)%256)/256 #setting the hue, keeping it between 1 and 0
		s = 1 - i/256 #setting the saturation, keeping it between 1 and 0
		v = 1 - i/500 #setting the value, keeping it between 1 and .5
		
		r,g,b = colorsys.hsv_to_rgb(h,s,v) #converting b/w hsv and rgb
		r,g,b = r*255, g*255, b*255 #to finish conversion, multiply by 255 to put in rgb scale
		
		image1.putpixel((x,y), (int(r),int(g),int(b))) #color pixels

	print("Graph 1 "+str(int(((y/512)*100)))+"% complete") #indicate % complete

image1.show() #display




#-----------------------SECOND GRAPH----------------------------------------------------------------

for y in range(imgy): #same process as the first graph, just a different scope
	cy = y * (ymax2-ymin2) / (imgy-1 )+ ymin2
	for x in range(imgx):
		cx = x * (xmax2-xmin2) / (imgx-1) + xmin2
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) > 2.0:
				break
			z = z**2 + c
		
		r = int(1/(math.sin(math.log(i))))%256 # color bases off some fancy math
		b = int(math.pow(i, math.e))%256 #^^
		g = int(1.1*math.sin(i))%256 #^^
		
		image2.putpixel((x,y), (int(r),int(g),int(b)))
	
	print("Graph 2 "+str(int(((y/512)*100)))+"% complete") #same as first graph

px = image2.load() #calling on the variable px[x, y] will give the rgb of pixel[x, y]

#This is my smoothing function, makes quite a difference on appearance
for y in range(imgy): #go through each pixel
	for x in range(imgx):
		
		m = 3 #with how many spaces in each direction do you want to smooth?
		
		mlx, mmx, mly, mmy = (-1*m), m, (-1*m), m #setting the smoothing ranges for each axis and direction. ml = mixing lower, mm = mixing max
		
		if mmx<x<(imgx + mlx) and mmy<y<(imgy+mly): #if pixels are out of theses range, will try to smooth and get values for pixels that are out of the picture, so let's keep the pixels in this range
			
			for t in range(mly, mmy+1): #b/w lower mix and max mix for y axis
				for r in range(mlx, mmx+1): #b/w lower mix and max mix for x axis
					
					a,b,c = px[(x+r), (y+t)] #rgb at nearby pixel
					w,e,u, = px[x, y] #rgb at exact pixel
					r,g,b = ((a+w)/2), ((b+e)/2), ((c+u)/2) #average the rgb values
					
					image2.putpixel((x,y), (int(r),int(g),int(b))) #reset pixel as this average
		else: #this deals with the pixels nearing the border I talked about before that were skipped
			
			yfup = y #amount of y space avaliable from the upper boundary (0) to the pixel
			yfdown = 512 - y #amount of y space avaliable from the down boundary(511) to the pixel
			xfleft = x #amount of x space avaliable from the left boundary(0) to the pixel
			xfright = 512 - x #amount of x space avaliable from the right boundary(511) to the pixel
			
			if (-1* yfup) >= mly: #if the pixel's y value is too close to the top, will change it
				if yfup == 0: #if pixel's  y value is 0 wont try to mix with pixels above it
					mly = 0
				else: 
					mly = yfup-1 #limits the pixels above mixed with
			
			if yfdown <= mmy: #if the pixel's y value is too close to the bottom, will change it
				if yfdown == 0: #if pixel's  y value is 512 wont try to mix with pixels below it
					mmy = 0
				else:
					mmy = yfdown -1 #limits the pixels below mixed with
			
			if (-1* xfleft) >= mlx: #same as y values but now limiting the right/left mixing ranges
				if xfleft == 0:
					mlx = 0
				else:
					mlx = xfleft -1
			
			if xfright <= mmx:
				if xfright == 0:
					mmx = 0
				else:
					mmx = xfright -1
			
			for t in range(mly, mmy+1): #using the new ranges for mixing, perform the same mixing function as from before
				for r in range(mlx, mmx+1):
					
					a,b,c = px[(x+r), (y+t)]
					w,e,u, = px[x, y]
					r,g,b = ((a+w)/2), ((b+e)/2), ((c+u)/2)
					
					image2.putpixel((x,y), (int(r),int(g),int(b)))

	print("Smoothing " +str(int(((y/512)*100)))+"% complete") #user - hang in there, it will finish


image2.show()



#-----------------------THIRD GRAPH----------------------------------------------------------------

#My third fractal looks like a tree. At the end of every vector, two new vectors in smaller length are generated at 45 degree angles of the first one.

for x in range(512): #color all pixels a nice yellow
	for y in range(512):
		image3.putpixel((x,y), (255,255,153))

def placingpixels(x, y): #I formulated my vectors in a cartesian plain, this converts it to python (flips the ys)
	y = 512 -y
	
	if 0<y<511 and 0<x<511: #makes sure in the range of the image
		image3.putpixel((x,y), (165,42,42)) #places a nice red
	else:
		pass

def drawnextbranch(xstart, ystart, p, length, sign): #my recursive function for drawing each line segment. Begins from the end of the one it was just called from. The line which it was called from determines its shape(p) and direction (sign) 
	newlength = int(length*(.72)) #the length of the new line will be 72% of the one before
	xcomp = int(math.cos((math.pi/4))*newlength) #in case the line is drawn at an angle, there is a count of how far x and y that would be. the ycomp is the same because the angle is 45 degrees
	if newlength < 2: #this will cut the recursion off at a certain point
		pass

#Below are the functions I used, and assigned each one to a certain number (See my handwritten notes for further explanation):

#1: x=c or x =-c
#2: y =x or y =-x
#3: y = |x| or y = -|x|
#4: y= +0 or y = -0

	elif p == 1: #y =c or y = -c
		for t in range(0, newlength +1): #since it is a vertical line, the length is equal to the change in y
			x = xstart
			y = ystart + sign*t #how you make a x=c graph parametrically, factoring in which direction it was called in
		
			placingpixels(x,y) #put a pixel here
		xstart = xstart #x value didnt change
		ystart = ystart + sign*newlength #new y value is just the old one + the length
		
		drawnextbranch(xstart, ystart, 2, newlength, sign*1) #calls upon two lines, each a different shape (see my attaches handnotes for how each next called line is determined)
		drawnextbranch(xstart, ystart, 3, newlength, sign*1)
	
	elif p == 2:
		for t in range(0, xcomp+1): #since this is a diagonal line, the change in x in terms of the total length is = the xcompt
			x = xstart +t #move x in positive direction
			y= ystart + sign*t #whether it is y = -x or y = x
			placingpixels(x,y)
		
		xstart = xstart + xcomp #both y and x moved over the sin(45 degrees)*total length
		ystart = ystart + sign*xcomp
		
		drawnextbranch(xstart, ystart, 1, newlength, sign*1)
		drawnextbranch(xstart, ystart, 4, newlength, 1)
	
	elif p == 3:
		for t in range(-xcomp, 1): #moves in the left direction
			x = xstart +t #moves left
			y= ystart + sign*abs(t) #moves up or down depending on how called, not on x value
			placingpixels(x,y)
		
		xstart = xstart- xcomp #same as p ==2
		ystart = ystart +sign*xcomp
		
		drawnextbranch(xstart, ystart, 1, newlength, sign*1)
		drawnextbranch(xstart, ystart, 4, newlength, -1)
	
	elif p == 4:
		for t in range(newlength+1): #straight line. horizontal.
			x = xstart + sign*t #only x changes
			y = ystart
			placingpixels(x,y)
		
		xstart = xstart + sign*newlength #only x has changed
		ystart = ystart
		
		if sign == -1: #this is the only set of lines where different signs call on completely different lines, not just a different signed line like the other sets. This accounts for that.
			drawnextbranch(xstart, ystart, 3, newlength, -1)
			drawnextbranch(xstart, ystart, 3, newlength, 1)
		else:
			drawnextbranch(xstart, ystart, 2, newlength, -1)
			drawnextbranch(xstart, ystart, 2, newlength, 1)

drawnextbranch(255, 0, 1, 200, 1) #how I kick off the whole graph

image3.show()














