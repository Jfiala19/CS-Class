import random
from tkinter import *
from unoboard import *


# GUI SETUP

class Card: #Card Class
	def __init__(self, color, rank): #Take in color, rank, and image to make each card
		self.color = color
		self.rank = rank
		self.img = PhotoImage(file=str(rank)+" "+str(color)+".png")
		self.but = Button(playarea,image=self.img, command = self.clickCard, cursor = "pirate")
	def id(self):
		if 0<= self.rank <= 9: # If the card is a number card
			return self.rank
		if self.rank == 10: #a 10 rank card is a Skip
			return "Skip"
		if self.rank == 11:
			return "Reverse"
		if self.rank == 12:
			return "Draw 2"
		if self.rank == 13:#^^^
			return "Wild"
		if self.rank == 14:#^^^
			return "Draw 4" #when printing 
	def colorer(self):
		if self.color == 0:
			return "Red"
		if self.color == 1:
			return "Yellow"
		if self.color == 2:
			return "Green"
		if self.color == 3:
			return "Blue"
		if self.color == 4:
			return "Wild"
	def __str__(self):	
		return self.colorer() + " " + str(self.id())
	def clickCard(self):
		if self.rank == discard.cards[0].rank or self.color == discard.cards[0].color or self.color == 4: # If card is playable:
			useCard(self) # Play that card
			endClear() # End turn after playing a card

		# Incomplete
		else:
			print("You can't play that card.")

window = Tk() # Makes main tkinter window
infobar = Frame(window, width = 1200, height = 200) # Makes infobar at the top
infobar.pack_propagate(0) # Stop bar from shrinking
infobar.pack()
playarea = Frame(window, width = 1200, height = 800, bg = "black") # Makes playarea with the cards
playarea.pack_propagate(0)
playarea.pack()
topcard = Label(playarea)


def drawCard():
	playerhands[turncounter].addcard(drawpile.deal(0))
	drawbut.pack_forget()
	endbut.pack()

drawbut = Button(playarea, text = "Draw Card", command = drawCard)

def endPress():
	global turncounter
	turncounter = (turncounter + direction)%len(playernames)
	endClear()

def endClear():
	drawbut.pack_forget()
	endbut.pack_forget()
	topcard.pack_forget()
	#Unpack everything

endbut = Button(playarea, text = "End Turn", command = endPress)

# LISTS & VARIABLES SETUP

playernames = [] #this list will be used to call on the players names
playerhands = [] #this list will be used to call on each player's hand
drawpile = Deck(1) # Make a full deck
discard = Deck(0) # Create an initially empty discard pile
direction = 1 # Direction of the game, can be reversed with a reverse card
turncounter = 1
turnended = False

def makeHands():
	for i in range(len(playernames)): # Make an empty deck for each player in the game
		playerhands.append(Deck(0))

	for i in range(7): # For each player, deal 7 cards into their deck
		for x in playerhands:
			x.addcard(drawpile.deal(0))

def makeDiscard():
	while True: # Start the game off by adding a card to the discard pile
		discard.addtotop(drawpile.deal(0)) # Keep adding cards
		if discard.cards[0].rank <= 9: # Until a regular number card is on top, burning cards in the process
			break

infolist = [Label(infobar, text = "Player 1\nCards: ", bg = "blue"),Label(infobar, text = "Player 2", bg = "red"),Label(infobar, text = "Player 3", bg = "yellow"),Label(infobar, text = "Player 4", bg = "green")]

def refreshinfobar(turner): # Refreshes the infobar at the top when the next player goes
	for x in infolist: # Clear the infobar
		x.pack_forget()
	for i in range(4): # Add the number of cards other players are holding
		if i != turner:
			infolist[i].pack(side=LEFT)


#INCOMPLETE
def displayCards(start):
	for x in playerhands[turncounter].cards[start:start+3]:
		x.but.pack(side=LEFT)

def refreshDiscard():
	topcard.pack_forget()
	topcard.config(image = discard.cards[0].img)
	topcard.pack(side=RIGHT)

def showDraw():
	drawbut.pack()

def refreshboard(): # Refreshes the playboard
	displayCards(0) # Shows their first page of cards
	refreshDiscard() # Updates top of discard pile
	showDraw()

def useCard(card):
	global direction, turncounter
	cardindex = playerhands[turncounter].cards.index(card)
	discard.addtotop(playerhands[turncounter].deal(cardindex))
	print(playerhands[turncounter])
	if card.rank == 10: # Skip
		turncounter = (turncounter+(2*direction))%len(playernames)
	elif card.rank == 11: # Reverse
		direction = direction * (-1)
		turncounter = (turncounter + direction)%len(playernames)
	elif card.rank == 12: # Draw 2
		for i in range(2):
			playerhands[turncounter+direction].addcard(drawpile.deal(0))
		turncounter = (turncounter+(2*direction))%len(playernames)
	elif card.rank == 13: # Wild
		turncounter = (turncounter + direction)%len(playernames)
		colorPicker()
	elif card.rank == 14: # Draw 4
		for i in range(4):
			playerhands[turncounter+direction].addcard(drawpile.deal(0))
		turncounter = (turncounter+(2*direction))%len(playernames)
		colorPicker()
	else: # Regular number cards
		turncounter = (turncounter + direction)%len(playernames)
	print(turncounter) # testing
	endClear()


def colorPicker():
	pass # pass means I havent written the code for it yet. pass stops program from crashing

def nextTurn(): # Runs during a player's turn
	global turncounter
	refreshinfobar(turncounter)
	refreshboard()

def EnterName(): #if names are confirmed
	global listofentries, numberofplayers #import these two vars
	for i in range(numberofplayers): #repeat for as many users there are
		playernames.append(listofentries[i].get()) #add to the list playernames each entered name
		listofentries[i].pack_forget() #delete text entry
	confirmnamesbutton.pack_forget() #delete other aspects
	Namelabel.pack_forget()
	print(playernames)

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
		listofentries[i] = Entry(infobar)
		listofentries[i].pack()
	confirmnamesbutton.pack() #enter button

	
playerselection = Listbox(infobar, selectmode = BROWSE, width =5, height=4) #this is the listbox for selecting the number of players
confirmnamesbutton = Button(infobar, text = "Enter", command = EnterName) #this is the button to confirm the names typed in
Namelabel = Label(infobar, text = 'Enter Player Names')
Numberlabel = Label(infobar, text = 'Select Number of Users')
numberokaybutton = Button(infobar, text = "Okay", command = Confirm) #this is the button to confirm number of players selection
Numberlabel.pack(side=TOP) #ask how many users
playerselection.pack()#listbox to select ^^^
choices = ["2", "3", "4"]#choices for amount of users
for i in range(len(choices)): #add all choices to listbox
	playerselection.insert(i, choices[i])
numberokaybutton.pack() #display okay button





# makeHands()
# makeDiscard()
# nextTurn()

window.mainloop()






