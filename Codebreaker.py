lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
codea = input("Insert encrypted text: ")
letters = list(codea)

for y in range(len(letters)):
	current = letters[y]
	if current == ' ' or current == '(' or current == ')' or current == '.' or current == '/' or current == ':':
		new = current
	else:
		for x in range(len(lista)):
			if lista[x] == current:
				value = x
				break	
		value = (value + 2)%26
		new = lista[value]
	letters[y] = new
letters = ''.join(letters)
print(letters)