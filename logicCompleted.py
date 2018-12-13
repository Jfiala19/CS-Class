# Partner 1: Jack 
# Partner 2: Scott
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''

''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
if str(grade.lower()) == "a":
   print("Good Work")


''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''

if int(yards) < 17:
   yards = yards*2

''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''

if success:
   print("Congratulations")

''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
if word[1].lower() == 'f':
   print("Fun")


''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''

if celsius:
   temp = temp*1.8 + 32


''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
if numItems == 0:
   print("No items")
else:
   averageCost = totalCost/numItems
   print(averageCost)


''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
if pollution < cutoff:
   print("Safe Condition")
if pollution >= cutoff:
   print("Unsafe Condition")


''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
if score<60:
   grade = "F"
elif 60<=score <70:
   grade = "D"
elif 70<= score <80:
   grade = "C"
elif 80<= score <90:
   grade = "B"
else:
   grade = "A"


''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''

while True:
   try:
      if 0<=int(letter)<=9:
         print("digit")
         break
   except ValueError:
      if letter.isalpha():
         if str(letter.lower()) == str(letter):
            print("Lowercase")
         elif str(letter.lower()) != str(letter):
            print("Uppercase")
      else:
         print("symbol")
      break



''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''

if neighbors >= 50:
   print("city")
elif 50 > neighbors >= 25:
   print("Suburbia")
elif 25 > neighbors > 0:
   print("rural")
else:
   print("middle of nowhere")

''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
if doesSignificantWork and makesBreakthrough:
   nobelPrizeCandidate = True
else:
   nobelPrizeCandidate = False


''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
if tax:
   price = price*(1+taxRate)


''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
if word[-2]+word[-1] == "ly":
   type = "adverb"
elif word[-3:-1]+word[-1] == "ing":
   type = "gerund"
elif word[-1] == "s":
   type = "plural"
else:
   type = "error"


''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
if currentNumber%2 == 1:
   currentNumber = 3*currentNumber + 1
else:
   currentNumber = currentNumber/2

''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
if year%4 == 0:
   leapYear = True
else:
   leapYear = False


''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
if a<b and a<c:
   result = a
elif b<a and b<c:
   result = b
else:
   result = c


''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
if number%2 ==0 and number%5 == 0 and -100<=number<=100:
   special = True
else:
   special = False


''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
list1 = ['a','e','i','o','u','y']
code = 0
for x in range(len(list1)): 
   if list1[x] == letter.lower():
      if list1[x] == 'y':
         code = -1
      else:
         code = 1


''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
if dayOfWeek.lower() == 'saturday' or dayOfWeek.lower() == 'sunday':
   isWeekend = True
else:
   isWeekend = False


''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
months = [['january', 31],['february',28],['march',31],['april', 30],['may',31],['june',30],['july',31],['august',31],['septemper',30],['october',31],['november',30],['december',31]]
for x in range(len(months)):
   if months[x][0] == month.lower():
      numDays = months[x][1]


''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
if angle1+angle2+angle3 == 180:
   validTriangle = True
else:
   validTriangle = False


''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
if electricity <= 50:
   payment = .50*electricity
elif 50<electricity<=150:
   payment = 25 + .75*(electricity -50)
elif 150< electricity<=250:
   payment = 100 + 1.2(electricity - 150)
else:
   payment = 1.2*(220 +1.5(electricity -250))


''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
if language.lower() == 'english':
   greeting = 'Hello'
elif language.lower() == 'french':
   greeting = 'Bonjour'
elif language.lower() == 'spanish':
   greeting = 'Hola'
else:
   greeting = '01001000 01100101 01101100 01101100 01101111 00100001' 


''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
if number == 1:
   phrase = str(number) + " " +str(noun)
else:
   phrase = str(number) + " " +str(noun) +"s"
 

''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''

if userInput == 'bacon':
   print('Why did you type bacon?')
else:
   print('I like bacon.')
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''

''' Task 1: Given three numbers, g, h, and o, find the average and then print out which number(s) are greater than that average

'''

# solution

g= 7
h = 76
o = 89
average = (g+h+o)/3
if g > average:
   print(g)
if h > average:
   print(h)
if o > average:
   print(o)


''' Task 2: if variable knowledgeOfShrek is greater than 5, print "You may enter the swamp.", otherwise print "Get out of me swamp!"

'''

# solution
knowledgeOfShrek = 4
if knowledgeOfShrek > 5:
   print("You may enter the swamp.")
else:
   print('Get out of me swamp!')




''' Task 3: Print all the prime numbers from 0 to t

'''

# solution
t = 100
for x in range(t):
   actual = x + 1
   for z in range(actual-1):
      real = z +1
      if real != 1:
         if actual%real == 0:
            break
      if real == actual-1:
         print(actual)


''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''