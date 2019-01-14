import random 
import matplotlib.pyplot as plt

list1 = [0 for i in range(80000)]



for x in range(1000000):
	total_calories = 0
	parties = random.randint(1, 10)
	for z in range(parties):
		desserts = random.randint(1,8)
		for y in range(desserts):
			total_calories += random.randint(40, 500)

	list1[total_calories+1] += 1
#40000 is max
plt.plot(list1)
plt.show()
