#I think it is better to switch boxes, because starting off you have a 2/3 chance of picking the pennies, so the box uneliminated but not choosen is more likely to be the car 

import random


#staying
winsStaying = 0 #keeps track of the # of wins with the staying method
for x in range(1000):
	carbox = random.randint(1,3) 
	firstchoice = random.randint(1,3)
	if firstchoice == carbox: 
		#since you will stick with your choice, this is the only scenario in which you win
		winsStaying += 1
	else:
		pass


#__________________________________________________________________________________________________

#switching boxes
winsSwitching = 0 #keeps track of the number of wins with the switching method
for x in range(1000): #repeat 1000 times
	carbox = random.randint(1,3) #there are three boxes
	firstchoice = random.randint(1,3) #random guess for which box
	if firstchoice == carbox:
		#because you will end up switching away from this choice, it is automatically a loss
		pass 
	else:
		#you have choosen a penny box, and so when the other one gets eliminated, it leaves only your choice (penny) and the box with the car (not your choice). So when you switch, you will win the car. 
		winsSwitching += 1 
	

#__________________________________________________________________________________________________

# #switching boxes - a more complicated code but shows gameplay - can uncomment if you want
# winsSwitchingp = 0
# secondchoice = 0
# for x in range(1000):

# 	list1 = [1,2,3] #list of original choices
# 	remaining = [1,2,3] #list of choices, one going to be eliminated


# 	carbox = random.randint(1,3)
# 	firstchoice = random.randint(1,3)

# 	#remove choice that is not a car and not the one you already picked, leaving two options
# 	for q in range(3):
# 		if list1[q] != carbox and list1[q] != firstchoice and len(remaining)==3:
# 			remaining.pop(q)

# 	#switch choices
# 	for y in range(len(remaining)):
# 		if remaining[y] != firstchoice:
# 			secondchoice = remaining[y]

# 	#track wins
# 	if secondchoice == carbox:
# 		winsSwitchingp += 1


#__________________________________________________________________________________________________



print('\nWins Staying with Original Box: ' +str(winsStaying) +'. This yields a winning rate of ' +str((winsStaying/10)) + '%')
print('\nWins Switching Boxes: ' +str(winsSwitching) +'. This yields a winning rate of ' +str((winsSwitching/10)) + '%\n')
#print('\nWins Switching Boxes: ' +str(winsSwitchingp) +'. This yields a winning rate of ' +str((winsSwitchingp/10)) + '%\n')


#On average, the chances of winning with the staying method were 1/3, and the chances of winning with the switching method were 2/3. I expected the switching to win more often, which it did, but I did not expect the fractions to be so simple.
#The fractions can be found very simply though, so it makes sense. With the staying method, you basically have to guess it on the first shot, so you have a clean one in three chance of guessing correctly.
#However, with the switching method, as long as you guess a penny with your first guess, you will win (see my comments above for why you automatically win if this is the case). The chances of guessing a penny are twice as likely, so you have a 2 in 3 shot of winning the car.






