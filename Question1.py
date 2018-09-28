#9/27/18, Question1, https://wiki.python.org/moin/HowTo/Sorting
import random
x =[]
while len(x) < 10:
	y = random.randint(0, 100)
	if y%3 != 0:
		x.append(y)
x.sort()
print(x)
