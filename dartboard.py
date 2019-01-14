 #Jack Fiala, 1/10/19, Monte Carlo Walk Simulation, OMH

#1) The longest walk you can take and still have a 50% chance of walking back is 22 blocks

#https://www.riskamp.com/files/RiskAMP%20-%20Monte%20Carlo%20Simulation.pdf
#https://www.palisade.com/risk/monte_carlo_simulation.asp
#2) Monte Carlo simulations are computer simulations based on statistic probability that show all possible outcomes and their likelihood, and can be then analyzed to determine risk or forecast for the future. It can provide a model for real life as it runs through certain tasks over and over again, using differing values for certain factors that change. It can be used in varying professional fields like finance, bussiness, and manufacturing, to provide insight into certain aspects of that field, such as how long a project is likely going to take.


import random 

z = 1000000 #the number of darts thrown
in_circle = 0 #keeps track of the number of darts that land inside circle

for x in range(z): #repeat for each dart
	xcord = (random.random()*2) -1 #gives a x random coordinate within the square (b/w -1 and 1)
	ycord = (random.random()*2) -1 #same as ^^ but for y
	if (xcord**2 +ycord**2) <= 1: #the equation for the circle in problem: x^2 + y^2 = 1. If if the left hand side of the equation is less than or equal to the right, the coordinates are within the circle
		in_circle += 1 

result = ((in_circle*4)/z)
print(result)

#with only 100 darts, the result seems to vary between about 2.8 and 3.4
#however, as the number of darts gets very large, the result seems to approach pi
#this makes sense b/c the probability of landing in the circle (found by dividing areas) is pi/4. So when you add a bunch of values that average to pi/4, and multiply by four, it should be pi.


#attempts per game (at least 140 on the season)
# attempts = [42.2,39.9,38,37.9,37.3,36.6,36.2,36,35.6,35.1,34.7,34.6,32.9,31.8,31.6,32.6,34.7,33.6,31,26.7,31.8,31,36.5,28.1,42.1,34.4,33.2,23.6,32.8,26.7,34.2,24.9,30.8,39]
# interceptions_percent_attempts = 2.4
# completions_percent_attempts = 64.9
# touchdowns_pecent_attempts = 4.9
