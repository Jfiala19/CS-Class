from PIL import Image


def Halfsize(Img):
	img = Image.open(Img)
	width, height = img.size
	img.resize((width//2, height//2)).save(Img)

Halfsize("images.png")