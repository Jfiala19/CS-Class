import random
cards= {
1:{
	'name': 'Ace',
	'value': '1',

},
2:{
	'name': '2',
	'value': '2',

},
3:{
	'name': '3',
	'value': '3',

},
4:{
	'name': '4',
	'value': '4',

},
5:{
	'name': '5',
	'value': '5',

},
6:{
	'name': '6',
	'value': '6',

},
7:{
	'name': '7',
	'value': '7',

},
8:{
	'name': '8',
	'value': '8',

},
9:{
	'name': '9',
	'value': '9',

},
10:{
	'name': '10',
	'value': '10',

},
11:{
	'name': 'Jack',
	'value': '10',

},
12:{
	'name': 'Queen',
	'value': '10',

},
13:{
	'name': 'King',
	'value': '10',
},
14:{
	'name': 'Ace',
	'value': '11',
}
}

def turn():
	input("\nPress Enter to Draw \n")
	Player1 = drawcard()
	print("You Drew a "+cardname(Player1))
	Dealer1 = drawcard()
	print("The Dealer Drew a " +cardname(Dealer1))
	input("\nPress enter to begin next round. \n")
	Player2 = drawcard()
	print("You Drew a "+cardname(Player2))
	Dealer2 = drawcard()
	print("The Dealer Drew a " +cardname(Dealer2))
	if Player1 == 1:
		Aceval1 = int(input("\nDo you want your Ace (draw 1) value to be 1 or 11?\n>>"))
		if Aceval1 == 1:
			Player1 = 1
		elif Aceval1 == 11:
			Player1 = 14
	if Player2 == 1:
		Aceval2 = int(input("\nDo you want your Ace (draw 2) value to be 1 or 11?\n>>"))
		if Aceval2 == 1:
			Player2 = 1
		elif Aceval2 == 11:
			Player2 = 14
	if checkfor21(Player1, Player2) == 1:
		if dealercheck1(Dealer1, Dealer2) == 1:
			input("\nYou both got blackjack. Your bet has been returned to you\n")
			#return bet value
		else:
			input("\nCongrats, you got Blackjack! You earned twice your bet. \n")
			#double bet value
		return
	if dealercheck1(Dealer1, Dealer2) == 1:
		input("\nThe Dealer won. You lost your bet. \n")
		return


def drawcard():
	cardDrawen = int(random.randrange (1, 14, 1))
	return cardDrawen
def cardvalue(card):
	return int(cards[card]['value'])
def dealercheck1(card1, card2):
	if cardvalue(card1) + cardvalue(card2) == cardvalue(card1) + 1 or cardvalue(card1) + cardvalue(card2) == cardvalue(card2) + 1:
		return 1
	else:
		return 2
def cardname(card):
	return cards[card]['name']
def checkfor21(card1, card2):
	if cardvalue(int(card1)) +cardvalue(int(card2)) == 21:
		return 1
	elif cardvalue(card1) +cardvalue(card2) < 21:
		return 2
	else:
		return 3

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