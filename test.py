#9/10/18 Simple Chatbot
#Sources: https://www.geeksforgeeks.org/print-colors-python-terminal/

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
closing = "Boom. How do you like me now?!?!?!"
print(" ")
print(" ")
print(" ")
print(" ")
print("Hello Human being!")
username = input("What is your name? ")
print(" ")
print(" ")
print("Hi "+username+"!")
ask1 = input("Do you want to hear a joke? (Yes/No) ")
print(" ")
print(" ")
if ask1 == "Yes" : 
	print("What do you call a fake noodle? ")
	print(" ")
	print(" ")
	print(" ")
	print("An Impasta!")
else:
	ask2 = input("Fine.... Are you sure? (Yes/No) ")
	if ask2 == "No" : 
		print("What do you call a fake noodle? ")
		print(" ")
		print(" ")
		print(" ")
		print("An Impasta!")

	else: 
		print("Okay, I'm just trying to have a little fun  ; )")
print(" ")
print(" ")
weather = input("What is the weather like today? ")
print(" ")
print(" ")
print("Hmm... "+weather+"?? Same here, buckaroo!!!")
print(" ")
print(" ")
color = input("What is your favorite color? (Please say Red, Green, or Blue!!) ")
if color == "Red":
	prRed(closing)
elif color =="Blue":
	prCyan(closing)
else:
	prGreen(closing)
print(" ")
print("Well, "+username+", my Mom is calling so I have to say goodbye for now. Nice Chat! xoxoxoxoxx")
print(" ")
print(" ")
print(" ")
