imgx = 9
imgy = 9
import math
xx = .5
yy = .5
for w in range(imgx):
	for q in range(imgy):
		xcord = -2 + (w*xx)
		ycord = 2 - (q*yy)
		c = complex(xcord, ycord)
		print(c)
		print(abs(pow(c, 2)))
		# z1 = complex(0, 0)
		# i = 0
		# while i < 25:
		# 	z2 = pow(z1, 2) + c #formula,
		# 	if abs(z2) > 2: #if the abs value of z2 is outside of circle, it escaped
		# 		break
		# 	z2 = z1
		# 	i += 1
		# print(i)
		print("\n")