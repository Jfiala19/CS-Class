from PIL import Image
import colorsys
import math

dogpic = Image.open("Dog89.JPG")

imgx, imgy = dogpic.size


px = dogpic.load() #calling on the variable px[x, y] will give the rgb of pixel[x, y]

for x in range(imgx):
	for y in range(imgy):
		

		a,b,c = px[(x), (y)] #get rgb values


		#increase contrast: if value are high, make them higher, if values low, make them lower
		if a > 200: 
			a = a*1.05
		if a <100:
			a = .95*a

		if 200 < b:
			b = 1.05*b
		if b <100:
			b = b *.95

		if c > 200:
			c = c*1.05
		if c <100:
			c = c*.95


		#make entire picture more red
		a = a**1.05


		#make sure rgb values within limits
		if a> 255:
			a = 255
		if a < 0:
			a = 0

		if b> 255:
			b = 255
		if b < 0:
			b = 0

		if c> 255:
			c = 255
		if c < 0:
			c = 0


		a,b,c = a/255, b/255, c/255 #need to be a value b/w 0 and 1 for conversion

		h,s,v = colorsys.rgb_to_hsv(a,b,c) #converting b/w hsv and rgb
		s = s *2 #increase saturation


		r,g,b = colorsys.hsv_to_rgb(h,s,v) #converting b/w hsv and rgb
		r,g,b = r*255, g*255, b*255 #to finish conversion, multiply by 255 to put in rgb scale
		
		dogpic.putpixel((x,y), (int(r),int(g),int(b))) #place new values
		
	print("Filter "+str(int(((x/imgx)*100)))+"% complete") #indicate % complete

dogpic.save("Filter68.JPG")
