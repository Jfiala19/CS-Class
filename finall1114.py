import random
from tkinter import*


 class Card: #Card Class
 	def __init__(self, color, rank): #Take in color, rank, and image to make each card
 		self.color = color
 		self.rank = rank
 		self.img = PhotoImage(file=str(rank)+" "+str(color)+".png")
 		self.but = Button(playarea,image=self.img, command = self.clickCard, cursor = "pirate")

 	def clickCard(self):
 		if self.rank == discard.cards[0].rank or self.color == discard.cards[0].color or self.color == 4: # If card is playable:
 			useCard(self) # Play that card
 			endClear() # End turn after playing a card

 class Deck:
 	def __init__(self, present): # Make deck
 		self.cards = [] # Make an empty deck
 		self.present = present # If present == 1, make a full deck. If present == 0, make an empty deck
 		if self.present == 1:
 			for i in range(4): # For each color except "wild color"
 				self.cards.append(Card(i, 0)) # Make 1 zero card
 				for x in range(2): # Make 2 copies of the following cards
 					for z in range(0,9): # Numbered cards from 1 to 9
 						self.cards.append(Card(i, z))
 					self.cards.append(Card(i, 10))
 					self.cards.append(Card(i, 11))
 					self.cards.append(Card(i, 12))
 			for q in range(4): # Make 4 wild and draw 4 cards
 				self.cards.append(Card(4, 13))
 				self.cards.append(Card(4, 14))
 			random.shuffle(self.cards)

 	def deal(self, position): # Removes and returns the value of the card in position of the deck
 		return self.cards.pop(position)

 	def addtotop(self, card): # Add card to front of deck
 		self.cards = [card] + self.cards

 # Functions activated by button clicks

 def drawCard():
 	playerhands[turncounter].cards.append(drawpile.deal(0))
 	drawbut.pack_forget()
 	if len(drawpile.cards) == 0:
 		win(0)
 	else:
 		refreshCards()
 		endbut.pack()

 def endPress():
 	global turncounter
 	endClear()
 	turncounter = (turncounter + direction)%len(playernames)
 	showNext()

 def nextPress():
 	nextbut.pack_forget()
 	nextTurn()

 def leftPress():
 	global pagenum
 	pagenum -= 1
 	refreshCards()

 def rightPress():
 	global pagenum
 	pagenum += 1
 	refreshCards()

 def rClick():
 	discard.cards[0].color = 0
 	clearWheel()

 def yClick():
 	discard.cards[0].color = 1
 	clearWheel()

 def gClick():
 	discard.cards[0].color = 2
 	clearWheel()

 def bClick():
 	discard.cards[0].color = 3
 	clearWheel()

 def clearWheel():
 	colorinstructions.pack_forget()
 	for x in colorwheel:
 		x.pack_forget()
 	showNext()

 # Other functions

 def makeHands():
 	for i in range(len(playernames)): # Make an empty deck for each player in the game
 		playerhands.append(Deck(0))

 	for i in range(7): # For each player, deal 7 cards into their deck
 		for x in playerhands:
 			x.cards.append(drawpile.deal(0))

 def makeDiscard():
 	while True: # Start the game off by adding a card to the discard pile
 		discard.addtotop(drawpile.deal(0)) # Keep adding cards
 		if discard.cards[0].rank <= 9: # Until a regular number card is on top, burning cards in the process
 			break

 def refreshinfobar(): # Refreshes the infobar at the top when the next player goes
 	for i in range(len(playernames)): # Clear the infobar
 		infolist[i].pack_forget()
 		if i == turncounter:
 			infolist[i].config(text = playernames[i] + ". It's your turn!")
 		else:
 			infolist[i].config(text = playernames[i] + ". Cards in hand:" + str(len(playerhands[i].cards)))
 	infolist[4].pack_forget()
 	infolist[4].config(text = "Cards left in draw pile: " + str(len(drawpile.cards)))
 	for i in range(len(playernames)): # Add the number of cards other players are holding
 		infolist[i].pack(fill = Y, side=LEFT)
 	infolist[4].pack(fill = Y)

 def win(method):
 	infobar.pack_forget()
 	leftbox.pack_forget()
 	playarea.pack_forget()
 	rightbox.pack_forget()
 	butbox.pack_forget()
 	discardbox.pack_forget()
 	winbox.pack()
 	if method == 0: # Win by draw pile running out
 		winlabel.config("The drawpile is empty! The game cannot continue. No one wins!")
 		winlabel.pack(fill=BOTH)	
 	else:
 		winlabel.config(text = playernames[turncounter] + " wins!")
 		winlabel.pack(fill=BOTH)

 def refreshCards():
 	for x in playerhands[turncounter].cards:
 		x.but.pack_forget()
 	leftbut.pack_forget()
 	rightbut.pack_forget()
 	if pagenum > 0:
 		leftbut.pack(side=LEFT)
 	for x in playerhands[turncounter].cards[pagenum:pagenum+5]:
 		x.but.pack(side=LEFT)
 	if pagenum < len(playerhands[turncounter].cards)-5:
 		rightbut.pack(side=LEFT)

 def refreshDiscard():
 	if discard.cards[0].rank == 13 or discard.cards[0].rank == 14:
 		wildlabel.config(text = "This wild card is \n" + colorlist[discard.cards[0].color], fg = colorlist[discard.cards[0].color])
 		wildlabel.pack()
 	topcard.config(image = discard.cards[0].img)
 	topcard.pack(side=RIGHT)

 def showDraw():
 	drawbut.pack(anchor=CENTER)

 def refreshboard(): # Refreshes the playboard
 	refreshCards() # Shows their first page of cards
 	refreshDiscard() # Updates top of discard pile
 	showDraw()

 def useCard(card):
 	global direction, turncounter
 	cardindex = playerhands[turncounter].cards.index(card)
 	endClear()
 	discard.addtotop(playerhands[turncounter].deal(cardindex))
 	if len(playerhands[turncounter].cards) == 0:
 		win(1)
 	if card.rank == 10: # Skip
 		turncounter = (turncounter+(2*direction))%len(playernames)
 		showNext()
 	elif card.rank == 11: # Reverse
 		direction = direction * (-1)
 		turncounter = (turncounter + direction)%len(playernames)
 		showNext()
 	elif card.rank == 12: # Draw 2
 		for i in range(2):
 			playerhands[(turncounter+direction)%len(playernames)].cards.append(drawpile.deal(0))
 		turncounter = (turncounter+(2*direction))%len(playernames)
 		showNext()
 	elif card.rank == 13: # Wild
 		turncounter = (turncounter + direction)%len(playernames)
 		colorPicker()
 	elif card.rank == 14: # Draw 4
 		for i in range(4):
 			playerhands[(turncounter+direction)%len(playernames)].cards.append(drawpile.deal(0))
 		turncounter = (turncounter+(2*direction))%len(playernames)
 		colorPicker()
 	else: # Regular number cards
 		turncounter = (turncounter + direction)%len(playernames)
 		showNext()

 def showNext():
 	nextbut.config(text = playernames[turncounter] + ". Please click this button to begin your turn.")
 	nextbut.pack()

 def endClear():
 	global pagenum
 	pagenum = 0
 	drawbut.pack_forget()
 	endbut.pack_forget()
 	topcard.pack_forget()
 	leftbut.pack_forget()
 	rightbut.pack_forget()
 	wildlabel.pack_forget()
 	for x in playerhands[turncounter].cards:
 		x.but.pack_forget()
 	#Unpack everything

 def colorPicker():
 	colorinstructions.pack(side=TOP)
 	for x in colorwheel:
 		x.pack(side=TOP)

 def nextTurn(): # Runs during a player's turn
 	refreshinfobar()
 	refreshboard()


 def Gamesetup():
 	Numberlabel.pack(side=TOP) #ask how many users
 	playerselection.pack()#listbox to select ^^^
 	choices = ["2", "3", "4"]#choices for amount of users
 	for i in range(len(choices)): #add all choices to listbox
 		playerselection.insert(i, choices[i])
 	numberokaybutton.pack() #display okay button

 def EnterName(): #if names are confirmed
 	global listofentries, numberofplayers #import these two vars
 	for i in range(numberofplayers): #repeat for as many users there are
 		playernames.append(listofentries[i].get()) #add to the list playernames each entered name
 		listofentries[i].pack_forget() #delete text entry
 	confirmnamesbutton.pack_forget() #delete other aspects
 	Namelabel.pack_forget()
 	print(playernames)
 	makeHands()
 	makeDiscard()
 	nextTurn()

 def Confirm(): #after clicking okay to a selected amount of users
 	global listofentries, numberofplayers #make these two vars global
 	numberofplayers = [playerselection.get(i) for i in playerselection.curselection()] #the number of users is equal to the number from the listbox
 	numberofplayers = int(numberofplayers[0]) #convert from string to int
 	listofentries = [] #make a list for the different text entry boxes
 	numberokaybutton.pack_forget() #delete all number of users pieces
 	playerselection.pack_forget()
 	Numberlabel.pack_forget() #ask names of users
 	Namelabel.pack(side=TOP)
 	for i in range(numberofplayers): #create one text entry for each user
 		listofentries.append(0)
 		listofentries[i] = Entry(playarea)
 		listofentries[i].pack()
 	confirmnamesbutton.pack() #enter button

 	



 window = Tk() # Makes main tkinter window
 infobar = Frame(window, width = 1000, height = 50) # Makes infobar at the top
 infobar.pack_propagate(0) # Stop bar from shrinking
 infobar.pack()
 leftbox = Frame(window, width = 64, height = 300, bg = "black")
 leftbox.pack_propagate(0)
 leftbox.pack(side=LEFT)
 playarea = Frame(window, width = 620, height = 300, bg = "black") # Makes playarea with the cards
 playarea.pack_propagate(0)
 playarea.pack(side=LEFT)
 rightbox = Frame(window, width = 64, height = 300, bg = "black")
 rightbox.pack_propagate(0)
 rightbox.pack(side=LEFT)
 butbox = Frame(window, width = 128, height = 300, bg = "black")
 butbox.pack_propagate(0)
 butbox.pack(side=LEFT)
 discardbox = Frame(window, width = 124, height = 300, bg = "black")
 discardbox.pack_propagate(0)
 discardbox.pack(side=LEFT)
 topcard = Label(discardbox)
 winbox = Frame(window, width = 1000, height = 350)
 winlabel = Label(winbox)
 drawbut = Button(butbox, text = "Draw Card", command = drawCard)
 endbut = Button(butbox, text = "End Turn", command = endPress)
 nextbut = Button(playarea, text = "Next Player, please press this button to begin your turn.", command = nextPress)
 leftimg = PhotoImage(file="leftarrow.png")
 leftbut = Button(leftbox, image = leftimg, command = leftPress)
 rightimg = PhotoImage(file="rightarrow.png")
 rightbut = Button(rightbox, image = rightimg, command = rightPress)
 playernames = [] #this list will be used to call on the players names
 playerhands = [] #this list will be used to call on each player's hand
 drawpile = Deck(1) # Make a full deck
 discard = Deck(0) # Create an initially empty discard pile
 direction = 1 # Direction of the game, can be reversed with a reverse card
 turncounter = 0
 pagenum = 0
 infolist = [Label(infobar, bg = "blue"),Label(infobar, bg = "red"),Label(infobar, bg = "yellow"),Label(infobar, bg = "green"),Label(infobar)]
 colorwheel = [Button(butbox, text = "Red", fg = "red", command = rClick),Button(butbox, text = "Yellow", fg = "orange", command = yClick),Button(butbox, text = "Green", fg = "green", command = gClick),Button(butbox, text = "Blue", fg = "blue", command = bClick)]
 colorinstructions = Label(playarea, text = "Pick the color you would like your wild card to be.", bg = "black", fg = "white")
 wildlabel = Label(discardbox, bg = "black")
 colorlist = ["red","yellow","green","blue"]
 playerselection = Listbox(playarea, selectmode = BROWSE, width =5, height=8) #this is the listbox for selecting the number of players
 confirmnamesbutton = Button(playarea, text = "Enter", command = EnterName) #this is the button to confirm the names typed in
 Namelabel = Label(playarea, text = 'Enter Player Names')
 Numberlabel = Label(playarea, text = 'Select Number of Users')
 numberokaybutton = Button(playarea, text = "Okay", command = Confirm) #this is the button to confirm number of players selection





 window.title("UNO Game")

 Gamesetup()



 window.mainloop() 