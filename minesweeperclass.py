import random as r
import sys
w = int(sys.argv[1]) #input width
h = int(sys.argv[2]) #input heigh
b = int(sys.argv[3]) #input bomb
var = 0 #holding variable for later
board = [[0]*w for x in range(h)] #makes games board to be displayed
board2 = [[0]*(w+2) for x in range(h+2)] #makes larger gameboard with a cushion of zeros all the way around for when searching for bombs with edge guys

def yet(space):
	if space == "*":
		return
	else:
		space += 1
for x in range(b): #repeat b times
	z = r.randint(0, (w-1)) #give a random width
	y = r.randint(0, (h-1)) #give random height
	board[y+1][z+1] = "*" #set in game board
	yet(board[x-1][y+1])
	yet(board[x][y+1])
	yet(board[x+1][y+1])
	yet(board[x-1][y])
	yet(board[x+1][y])
	yet(board[x-1][y-1])
	yet(board[x][y-1])
	yet(board[x+1][y-1])

for x in board:
	print(*x)

