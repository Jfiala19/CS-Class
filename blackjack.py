import random

bothBJ = "\nYou both got blackjack. Your bet has been returned to you\n"
playerBJ = "\nCongrats, you got Blackjack! You earned twice your bet. \n"
dealerBJ = "\nThe Dealer won. You lost your bet. \n"
rules = "Each round you and the dealer will take turns drawing card. The Dealer will draw to 16, will stand on 17+. Pays 3 to 2"
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
cards= {
1:{
	'name': 'a Ace',
	'value': '1',

},
0:{
	'name': 'nothing',
	'value': '0'
},
2:{
	'name': 'a 2',
	'value': '2',

},
3:{
	'name': 'a 3',
	'value': '3',

},
4:{
	'name': 'a 4',
	'value': '4',

},
5:{
	'name': 'a 5',
	'value': '5',

},
6:{
	'name': 'a 6',
	'value': '6',

},
7:{
	'name': 'a 7',
	'value': '7',

},
8:{
	'name': 'a 8',
	'value': '8',

},
9:{
	'name': 'a 9',
	'value': '9',

},
10:{
	'name': 'a 10',
	'value': '10',

},
11:{
	'name': 'a Jack',
	'value': '10',

},
12:{
	'name': 'a Queen',
	'value': '10',

},
13:{
	'name': 'a King',
	'value': '10',
},
14:{
	'name': 'a Ace',
	'value': '11',
}
}

def turn():
	input("\nPress Enter to Draw \n")
	Dealer1 = 10
	prRed("The Dealer Drew " +cardname(Dealer1))
	Player1 = drawcard()
	prGreen("You Drew "+cardname(Player1))
	input("\nPress enter to begin next round. \n")
	#Dealer2 = 5
	#prRed("The Dealer Drew " +cardname(Dealer2))
	Player2 = drawcard()
	prGreen("You Drew "+cardname(Player2))
	if naturalcheck(Player1, Player2) == 1:
		endplayer()
	#if Player1 == 1:
		#Player1 = acesetvalue(Player1, 1)
	#if Player2 == 1:
		#Player2 = acesetvalue(Player2, 2)
	#if checkfor21(Player1, Player2, 0, 0, 0, 0) == 1:
		#if dealercheck1(Dealer1, Dealer2, 0, 0, 0, 0) == 1:
			#input(bothBJ)
			#return bet value
		#else:
			#input(playerBJ)
			#double bet value
		#return
	#if dealercheck1(Dealer1, Dealer2) == 1:
		#input(dealerBJ)
		#return
	Player3 = drawagain()
	#checkturn3 = checkfor21(Player1, Player2, Player3, 0, 0, 0)
	#Dealer3 = dealermove(Dealer1, Dealer2, 0, 0, 0, 0)
	#prRed("The Dealer Drew " +cardname(Dealer3))
	#thedealer draws two cards along with you, then you keep going. Dealer will draw more cards if you havent busted and


def drawcard():
	cardDrawen = int(random.randrange (1, 14, 1))
	return cardDrawen
def cardvalue(card):
	return int(cards[card]['value'])
def naturalcheck(card1, card2): #if ace and a ten card are selected, ace will automatically trigger blackjack 
	if card1 + card2 == 11 and (cardvalue(card1) == 1 or cardvalue(card2) == 1):
		return 1
	else:
		return 2
def cardname(card):
	return cards[card]['name']
def checkfor21(card1, card2, card3, card4, card5, card6):
	cardsum = cardvalue(int(card1)) +cardvalue(int(card2)) +cardvalue(int(card3)) +cardvalue(int(card4)) +cardvalue(int(card5)) +cardvalue(int(card6)) 
	if cardsum == 21:
		return 1
	elif cardvalue(card1) +cardvalue(card2) < 21:
		return 2
	else:
		return 3
def acesetvalue(card, draw):
	Aceval1 = int(input("\nDo you want your Ace (draw "+str(draw)+") value to be 1 or 11?\n>>"))
	if Aceval1 == 1:
		return 1
	elif Aceval1 == 11:
		return 14
def dealermove(card1, card2, card3, card4, card5, card6):
	cardsum = cardvalue(card1) + cardvalue(card2) + cardvalue(card3) + cardvalue(card4) + cardvalue(card5) + cardvalue(card6)
	if cardsum < 16:
		return drawcard()
	if cardsum > 17:
		return 0
def staying(card1, card2, card3, card4, card5, card6):
	pass
def endplayer():
	pass
def drawagain():
	draw5 = input("\nHit or Stay?\n>>")
	draw5 = draw5.lower()
	if draw5 == "hit":
		hi = drawcard()
		prGreen("You Drew "+cardname(hi))
		return hi
	if draw5 == "stay":
		endplayer()

startBank = 100
#username = input("\n\n\nEnter username: \n>> ")
#print("\n\nHi "+username+". Welcome to Blackjack 2018 on Jack's Macbook!")
#print(" ")
#rules = input("Do you need to know the rules of the game? (Yes/No) ")
#rules = rules.lower()
#if rules == "yes":
	#{
	#print(rulebook)
	#}
#highscore = 0
#input("\nThe game is about to begin. You have $"+str(startBank)+" to bet. Press enter to continue")
#betValue = float(input("How much would you like to bet? :\n\n>> "))
#print("You have bet $"+str(betValue)+", and currently have $"+str(startBank - betValue)+" In the bank")
turn()
print('1234')






#the dealer will hit till 17, then stay