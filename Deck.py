from card import Card
import random

class Deck: 


	def __init__(self, blist): 
		self.blist = blist

	def drawtop(self, amount):
		pass
	def drawrandom(self, amount):
		pass
	def shuffle(self):
		self.blist = random.shuffle(self.blist)
	def fill52(self):
		for i in range(1,14, 1):
			self.blist.append(Card(i, "c"))
			self.blist.append(Card(i, "d"))
			self.blist.append(Card(i, "s"))
			self.blist.append(Card(i, "h"))
	def __str__(self):
		
		for x in range(len(self.blist)):
			self.blist[x]


jack = Deck([])
jack.fill52()
#jack.shuffle()
print(jack)