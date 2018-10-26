class Account: 

	def __init__(Name, Pin, Balance, OC, SQ, SA): 
		self.Name = Name
		self.Pin = Pin
		self.Balance = Balance
		self.OC = OC
		self.SQ = SQ
		self.SA = SA
	#Methods (A function within a class)
	def withdraw(amount):
		if self.balance > amount:
			self.balance -= amount 
			status = "You withdrew $" +str(amount) " and now have a balance of $" +str(self.balance) 
		else:
			status = "You balance is $" +self.balance " . You can't withdraw this much"
		return status
	def deposit(amount):
		self.balance += amount
		status = "Your balance is now $" +self.balance
		return status



def accountmanagement(account):
While True:	
	action = input("What would you like to do: \n\n1) View Balance\n2)Deposit\n3)Withdraw\n4)Exit")
	if action == 1:
		print(account.Balance)
	if action == 2:
		amount = input("How much would you like to Deposit?")
		print(account.deposit(amount))
	if action == 3:	
		amount = input("How much would you like to Withdraw?")
		print(account.withdraw(amount))
	if action == 4:
		break()


333444a = Account(Jack, 1234, 100, 1, "What was the name of your first pet?", "Cali")





while True:
	try1 = input("Enter your account number: ")
	try2 = input("Enter your Pin Number: ")
	if try2 == 333444a.pin:
		print("Hello "+333444a.Name)
		accountmanagement(333444a)
	else:
		try3 = input("Incorrect.\n Eneter your Pin Number: ")
		if try3 == 333444a.pin:
			print("Hello "+333444a.Name)
			accountmanagement(333444a)
		else:
			try4 = input("Incorrect.\n " +333444a.SQ)
			if try4 == 333444a.SA:
				print("Hello "+333444a.Name)
				accountmanagement(333444a)

