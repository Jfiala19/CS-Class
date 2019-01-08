import random
list1 = [['Zeros:', 0],['Ones:', 0], ['Twos:',0,],['Threes:', 0], ['Fours:', 0],['Fives:', 0],['Sixes:', 0],['Sevens:', 0],['Eights:', 0],['Nines:', 0],['Tens:', 0]]

for x in range(1000000):
	heads = 0 
	tails = 0
	for i in range(10):
		z = random.randint(0,1)
		if z == 0:
			heads += 1
		else:
			tails += 1
	list1[heads][1] += 1
for x in list1:
	print(*x)