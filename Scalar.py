from PIL import Image

def Halfsize(Img):
	img = Image.open(Img)
	width, height = img.size
	img.resize((width//2, height//2)).save(Img)

def Imagescalar():
	for y in range(13):
		for x in range(4):
			Halfsize((str(y) + " " +str(x) +".png"))
	Halfsize("13 4.png")
	Halfsize("14 4.png")

Imagescalar()