import random
dealerbust = "\nThe Dealer busted and you Won! Way to gain from other's losses!!! \n"
playerBJ = "\nCongrats, you got Blackjack! Winner Winner Chicken Dinner!! \n"
dealerBJ = "\nThe Dealer got blackjack. Tough bid. \n"
bustuser = "\nYou busted. Tough way to go out. Be more smarter. "
rules = "\nEach round you and the dealer will take turns drawing cards trying to get a hand worth 21. Cards 2-10 are worth their face value, and all face cards are worth ten except aces, which are worth 1 or 11. Dealer's aces will count high for his first two draws, and then drop low along with any newly drawn aces. You will go first, drawing more cards until you bust, hit 21, or stay. After that the dealer will draw until they bust, hit 21, or beat your hand."
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
h = "hit"
z = "stay"
endMessage = "\nThanks for playing!!!!\n"
Dealer1 = 0
Dealer2 = 0
Dealer3 = 0
Dealer4 = 0
Dealer5 = 0
Dealer6 = 0
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
	Player1 = 0
	Player2 = 0
	Player3 = 0
	Player4 = 0
	Player5 = 0
	Player6 = 0
	Player1 = drawcard()
	prGreen("You Drew "+cardname(Player1))
	input("\nPress enter to begin next round. \n")
	Player2 = drawcard()
	prGreen("You Drew "+cardname(Player2))
	naturalcheck(Player1, Player2)
	Player3 = drawagain(Player1, Player2, 0, 0, 0, 0)
	checkforinstant(Player1, Player2, Player3, 0, 0, 0)
	Player4 = drawagain(Player1, Player2, Player3, 0, 0, 0)
	checkforinstant(Player1, Player2, Player3, Player4, 0, 0)
	Player5 = drawagain(Player1, Player2, Player3, Player4, 0, 0)
	checkforinstant(Player1, Player2, Player3, Player4, Player5, 0)
	Player6 = drawagain(Player1, Player2, Player3, Player4, Player5, 0)
	checkforinstant(Player1, Player2, Player3, Player4, Player5, Player6)
def drawcard():
	cardDrawen = int(random.randrange (1, 14, 1))
	return cardDrawen
def cardvalue(card):
	return int(cards[card]['value'])
def naturalcheck(card1, card2): #if ace and a ten card are selected, ace will automatically trigger blackjack 
	if cardvalue(card1) + cardvalue(card2) == 11 and (cardvalue(card1) == 1 or cardvalue(card2) == 1):
		endplayer(14, 14, 14, 14, 14, 14)
	else:
		return
def dealercheck(card1, card2): #if ace and a ten card are selected, ace will automatically trigger blackjack 
	if cardvalue(card1) + cardvalue(card2) == 11 and (cardvalue(card1) == 1 or cardvalue(card2) == 1):
		return 1 
	else:
		return 2
def cardname(card):
	return cards[card]['name']
def acecheck(card, draw):
	if card != 1:
		return card
	if card == 1:
		while True:
			try:
				acer = int(input("\nDo you want your Ace (draw "+str(draw)+") value to be 1 or 11?\n>>"))
				if acer == 1 or acer == 11:
					break
				else:
					print("Not in my house")
			except ValueError:
				print("\nPlease enter a 1 or 11")
		if acer == 1:
			return 1
		elif acer == 11:
			return 14
def endplayer(card1, card2, card3, card4, card5, card6):
	cardsum = cardvalue(card1) + cardvalue(card2) + cardvalue(card3) + cardvalue(card4) + cardvalue(card5) + cardvalue(card6)
	if cardsum == 66:
		prCyan(playerBJ)
		print(endMessage)
		exit()
	if cardsum > 21:
		prCyan(bustuser)
		print(endMessage)
		exit()
	if cardsum == 21:
		prCyan(playerBJ)
		print(endMessage)
		exit()
	if cardsum < 21:
		print("\nYou sit at "+str(cardsum)+". Let's see what the dealer has.\n")
		dealerfinisher(Dealer1, cardsum)
def dealerfinisher(card1, playerstatus):
	Dealer1 = drawcard()
	Dealer2 = drawcard()
	Dealer3 = 1
	Dealer4 = drawcard()
	Dealer5 = drawcard()
	Dealer6 = drawcard()
	dealerprint(Dealer1)
	dealerprint(Dealer2)
	if dealercheck(Dealer1, Dealer2) == 1:
		comparerer(66, playerstatus)
	cardsum = cardvalue(Dealer1) + cardvalue(Dealer2)
	if cardsum < playerstatus:
		cardsum += cardvalue(Dealer3)
		dealerprint(Dealer3)
		if cardsum < playerstatus:
			cardsum += cardvalue(Dealer4)
			dealerprint(Dealer4)
			if cardsum < playerstatus:
				cardsum += cardvalue(Dealer5)
				dealerprint(Dealer5)
				if cardsum < playerstatus:
					cardsum += cardvalue(Dealer6)
					dealerprint(Dealer6)
	if cardsum == 21:
		comparerer(66, playerstatus)
	if cardsum != 21:
		comparerer(cardsum, playerstatus)
def comparerer(dealerstatus, playerstatus):
	if dealerstatus == 66:
		prCyan(dealerBJ)
		print(endMessage)
		exit()
	if dealerstatus > 21:
		prCyan(dealerbust)
		print(endMessage)
		exit()
	if dealerstatus > playerstatus:
		prCyan("\nThe Dealer's "+str(dealerstatus)+" beats your "+str(playerstatus)+" and you lost. Let me break out the world's smallest violin!!\n")
		print(endMessage)
		exit()
	if playerstatus > dealerstatus:
		prCyan("\nThe Dealer's "+str(dealerstatus)+" is no match to your "+str(playerstatus)+" and you won! You are the smartest human being I know!!\n")
		print(endMessage)
		exit()
	if playerstatus == playerstatus:
		PrCyan("\nYou tied the dealer! Not bad but not good! But especially not good\n")
		print(endMessage)
		exit()
def dealerprint(card):
	input("\nPress enter to continue. \n")
	prRed("The Dealer Drew " +cardname(card))

def drawagain(card1, card2, card3, card4, card5, card6):
	draw5 = input("\nHit or Stay?\n>>")
	draw5 = draw5.lower()
	while str(draw5) != str(z) and str(draw5) != str(h):
		draw5 = input("\nHit or Stay?\n>>")
		draw5 = draw5.lower()
	if draw5 == "hit":
		hi = drawcard()
		prGreen("\nYou Drew "+cardname(hi))
		return hi
	if draw5 == "stay":
		card1 = acecheck(card1, 1)
		card2 = acecheck(card2, 2)
		card3 = acecheck(card3, 3)
		card4 = acecheck(card4, 4)
		card5 = acecheck(card5, 5)
		card6 = acecheck(card6, 6)
		endplayer(card1, card2, card3, card4, card5, card6)

def checkforinstant(card1, card2, card3, card4, card5, card6):
	cardsum = cardvalue(card1) + cardvalue(card2) + cardvalue(card3) + cardvalue(card4) + cardvalue(card5) + cardvalue(card6)
	if cardsum >= 21:
		endplayer(card1, card2, card3, card4, card5, card6)

username = input("\n\n\nEnter username: \n>> ")
print("\n\nHi "+str(username)+". Welcome to Blackjack 2021 brought to you by your computer's Terminal!!\n")
ruler = input("\nDo you need to know the rules of the game? (Yes/No) \n >>")
ruler = ruler.lower()
while str(ruler) != "yes" and str(ruler) != "no":
	ruler = input("Do you need to know the rules of the game? (Yes/No) \n>>")
	ruler = ruler.lower()
if ruler == "yes":
	print(rules)
turn()