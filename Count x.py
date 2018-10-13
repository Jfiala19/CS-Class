def countx(a):
	y = a[0]
	if len(a) == 1:
		if y == "x":
			return 1
		else:
			return 0
	y = a[0]
	if y == "x":
		return 1 + countx(a[1:])
	else:
		return countx(a[1:])
def crazy(a):
	a = str(a)
	y = a[0]
	if len(a) == 1:
		if y == "8":
			return 1
		else:
			return 0
	y = a[0]
	if y == "8":
		return 1 + crazy(a[1:])
	else:
		return crazy(a[1:])
typer = input("8s or X\n\n>>")
q = input("Enter: \n\n>>")
if typer == "8":
	print(crazy(q))
else:
	print(countx(q))

