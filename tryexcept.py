#while True:
#	try:
#		x = int(input("Enter a number: "))
#		break
#	except ValueError:
#		x = int(input("Enter a number: "))
#count = 0
#while count < x:
#	print("Hello!")
#	count += 1
while True:
	try:
		x = int(input("Enter a number: "))
		if 1<=x<=5:
			break
		else:
			print("Not in my house")
	except ValueError:
		print("Nah")
	

print("Succcess")