#9/27/18 Question 4, no sources
terms = []
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) #defining some fancy fonts
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b 
	return a
i = 1
while len(terms) < 50:
	if (fib(i))%2 != 0:
		terms.append(fib(i))
	i+=1
for i in range(0, 50):
	if i%2 == 0:
		prRed(fib(i))
	else:
		prCyan(fib(i))


