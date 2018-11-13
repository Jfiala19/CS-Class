from PIL import Image
import colorsys
import math

dogpic = Image.open("lighthouse.jpg")

imgx, imgy = dogpic.size


px = dogpic.load() #calling on the variable px[x, y] will give the rgb of pixel[x, y]

for x in range(imgx):
	for y in range(imgy):
		

		a,b,c = px[(x), (y)]
		

		#if 150<c and ((0<x<1150 or x>1420) or (y<450 or y >1100)):
			#a = a + 100


		a,b,c = a/255, b/255, c/255

		h,s,v = colorsys.rgb_to_hsv(a,b,c) #converting b/w hsv and rgb
		s = s *2
		h = h
		if .585<h or h>.5 and ((0<x<1150 or x>1420) or (y<450 or y >1100)):
			h = (h+ .13)








		r,g,b = colorsys.hsv_to_rgb(h,s,v) #converting b/w hsv and rgb
		r,g,b = r*255, g*255, b*255 #to finish conversion, multiply by 255 to put in rgb scale
		
		dogpic.putpixel((x,y), (int(r),int(g),int(b)))
		
	print("Graph 1 "+str(int(((x/imgx)*100)))+"% complete") #indicate % complete

dogpic.show()
