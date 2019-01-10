import random
import math
# import matplotlib.pyplot as plt

# walk_home = 0
# for x in range(1000):
# 	homex, homey = 0,0 #xcord, y cord
# 	x = 0
# 	y = 0
# 	status = []
# 	for z in range(10):
# 		direction = random.randint(0,3)
# 		if direction == 0: #North
# 			y += 1
# 		elif direction == 1: #East
# 			x += 1
# 		elif direction == 2: #South
# 			y += -1
# 		elif direction == 3:#West
# 			x += -1
# 		#status.append((x,y))
# 		#plt.plot(x,y, 'ro')
# 	distance_from_home = math.fabs(x) + math.fabs(y)
# 	# for x in status:
# 	# 	print(*x)
# 	#print(distance_from_home)
# 	# plt.show()
# 	if distance_from_home <= 4:
# 		walk_home += 1

#print(walk_home)

points = []
for q in range(50):
	walk_home = 0
	for x in range(2000):
		homex, homey = 0,0 #xcord, y cord
		x = 0
		y = 0
		status = []
		for z in range(q):
			direction = random.randint(0,3)
			if direction == 0: #North
				y += 1
			elif direction == 1: #East
				x += 1
			elif direction == 2: #South
				y += -1
			elif direction == 3:#West
				x += -1
			#status.append((x,y))
			#plt.plot(x,y, 'ro')
		distance_from_home = math.fabs(x) + math.fabs(y)
		# for x in status:
		# 	print(*x)
		#print(distance_from_home)
		# plt.show()
		if distance_from_home <= 4:
			walk_home += 1
	percent = walk_home/1000
	points.append([q, percent])
for x in points:
	print(*x)











