global counter

class Account: 

	def __init__(self, number, name, pin, balance, OC, SQ, SA): 
		self.name = name
		self.number = number
		self.pin = pin
		self.balance = balance
		self.OC = OC
		self.SQ = SQ
		self.SA = SA
	#Methods (A function within a class)
	def withdraw(self, amount):
		if self.balance >= int(amount):
			self.balance -= int(amount) 
			status = "\nYou withdrew $" +amount+  " and now have a balance of $" +str(self.balance) +"\n"
		else:
			status = "\nYou balance is $" +str(self.balance) +". You can't withdraw this much \n"
		return status
	def deposit(self, amount):
		self.balance +=int(amount)
		status = "\nYour balance is now $" +str(self.balance) +"\n"
		return status



def accountmanagement(account):

	while True:	
		action = input("\nWhat would you like to do: \n\n1)View Balance\n2)Deposit\n3)Withdraw\n4)Exit\n>>")
		if action == "1":
			print("\nYour Balance: $"+str(account.balance)+"\n")
		if action == "2":
			amount = input("\nHow much would you like to Deposit?\n>>")
			print("\n"+str(account.deposit(amount))+"\n")
		if action == "3":	
			amount = input("\nHow much would you like to Withdraw?\n>>")
			print("\n"+str(account.withdraw(amount))+"\n")
		if action == "4":
			break


A1 = Account(a44a, "Jack", "1234", 100, 1, "What was the name of your first pet?", "Cali")
A2 = Account(g668, "Qin", "5768", 1000, 1, "What is your favorite team?", "Browns")
Users[] = [A1, A2]



for i in range(3):
	try1 = input("Enter your account number: ")
	try2 = input("Enter your Pin Number: ")
	for z in range(len(Users)):
		y = Users[z]
		r = y.number
		q = y.pin
		if try1 == y and try2 == q:
			accountmanagement(y)
counter = 0			
for z in range(len(Users)):
	x = Users[z]
	if x.number == try1:
		counter += 1
if counter == 1:
	answer = input()
else:
	print("Invalid Number/Pin. Goodbye\n\n")



	if try2 == a44a.pin:
		print("\nHello "+a44a.name)
		accountmanagement(a44a)
	else:
		try3 = input("\nIncorrect.\n Eneter your Pin Number: ")
		if try3 == a44a.pin:
			print("\nHello "+a44a.name)
			accountmanagement(a44a)
		else:
			try4 = input("\nIncorrect.\n " +a44a.SQ)
			if try4 == a44a.SA:
				print("\nHello "+a44a.name +"\n")
				accountmanagement(a44a)

