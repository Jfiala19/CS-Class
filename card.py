class Card: 

	def __init__(self, rank, suit): 
		self.suit = suit
		self.rank = int(rank)
	#Methods (A function within a class)
	def suiter(self):
		if self.suit == "h":
			return "Hearts"
		if self.suit == "d":
			return "Diamonds"
		if self.suit == "c":
			return "Cloves"
		if self.suit == "s":
			return "Spades"
	def __str__(self):
		if 2<=self.rank<=10:
			return str(self.rank)+ " of " + self.suiter()
		if self.rank == 1:
			return "Ace of " + self.suiter()
		if self.rank == 11:
			return "Jack of " +self.suiter()
		if self.rank == 12:
			return "Queen of " +self.suiter()
		if self.rank == 13:
			return "King of " +self.suiter()
