from PIL import Image

mainimg = Image.open("UNO.png")

card = Image.new("RGB",(240,360))

imgx = 1 + 240*13
imgy = 1
for xcard in range(0,240):
	for ycard in range(0,360):
		pixcolor = mainimg.getpixel((imgx+xcard,imgy+ycard))
		card.putpixel((xcard,ycard),pixcolor)
card.save("wild.png","PNG")

imgx = 1 + 240*13
imgy = 1 + 360*4
for xcard in range(0,240):
	for ycard in range(0,360):
		pixcolor = mainimg.getpixel((imgx+xcard,imgy+ycard))
		card.putpixel((xcard,ycard),pixcolor)
card.save("plus4.png","PNG")

for x in range(13):
	imgx = 1 + 240*x
	for y in range(4):
		imgy = 1 + 360*y
		for xcard in range(0,240):
			for ycard in range(0,360):
				pixcolor = mainimg.getpixel((imgx+xcard,imgy+ycard))
				card.putpixel((xcard,ycard),pixcolor)
		card.save(str(x) + " " + str(y) + ".png","PNG")