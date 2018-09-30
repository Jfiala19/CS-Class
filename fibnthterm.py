import sys
x = int(sys.argv[1])
def fib(term_n):
	if term_n == 0:
		return 0
	elif term_n == 1:
		return 1
	else:
		q = fib(term_n-1) + fib(term_n-2)
		return q

z = fib(x)
print(z)