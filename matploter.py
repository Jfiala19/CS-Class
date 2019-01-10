import random
import matplotlib.pyplot as plt

list1 = [[0, 0],[1, 0], [2,0,],[3, 0], [4, 0],[5, 0],[6, 0],[7, 0],[8, 0],[9, 0],[10, 0]]

for x in range(1000):
	heads = 0 
	tails = 0
	for i in range(10):
		z = random.randint(0,1)
		if z == 0:
			heads += 1
		else:
			tails += 1
	list1[heads][1] += 1


results = []
for j in range(1000):
	total = 0
	for i in range(10):
		flip = random.randint(0,1)
		total += flip
	results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1

x_axis = [x for x in range(11)]
data2 = [y for y in range(5,16)]

plt.plot(x_axis, display, 'r', x_axis, data2, 'r^')
plt.bar(x_axis, display)
plt.ylabel("Frequency")
plt.xlabel("Number of Heads")
# plt.plot(x_axis, display, 'r--')
# plt.plot(x_axis, display, 'b^')
# plt.plot(x_axis, display, 'gs')

plt.show()




