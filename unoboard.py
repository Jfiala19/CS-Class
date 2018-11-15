
from tkinter import *

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
			self.shuffle()

	def shuffle(self): # Shuffle deck
		random.shuffle(self.cards)

	def numcards(self): # Returns number of cards in deck
		return len(self.cards)

	def deal(self, position): # Removes and returns the value of the card in position of the deck
		return self.cards.pop(position)

	def addcard(self, card): # Add card to end of deck
		self.cards.append(card)

	def addtotop(self, card): # Add card to front of deck
		self.cards = [card] + self.cards
    
	def cardid(self, position): # Returns the card in specified position in the deck
		return self.cards[position]

	def __str__(self):
		hand = ""
		for i in range(len(self.cards)):
			hand = hand + str(self.cards[i]) +"\n"
		return str(hand)