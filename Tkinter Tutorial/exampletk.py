'''
Date: 01/31/19 (Got an extension)
Description: Calculator Example

Sources:
http://effbot.org/tkinterbook/

Honor Pledge: On our honor, we have neither given nor received unauthorized aid. Anan Aramthanapon, Jackson Fiala
'''
from tkinter import * 

#Creating Tk window
window = Tk()
window.title("Calculator")

 # Class for number buttons
 # text is the number
 # command is numInput with the number as the input
 # cursor becomes a plus when hovering over buttons
class Number:
	def __init__(self,num):
		self.but = Button(calcframe, text = str(num), command = lambda:numInput(num), cursor = "plus", height = 3, width = 8)

# Class for operator buttons
# same as number buttons, but calls on the calculate function instead
class Ops:
	def __init__(self,op):
		self.but = Button(calcframe, text = op, command = lambda:calculate(op), cursor = "plus", height = 3, width = 8)

# MATH
# Number that can be edited by pressing number buttons
activestr = ""
# Number stored in memory used for calculations
storedstr = ""
# Last operator used
storedop = ""

def numInput(num): # Command when numbered buttons are clicked
	global activestr
	activestr = activestr + str(num) # add the number to the active string
	refresh()

def calculate(operator): # Command when operator buttons are clicked
	global activestr,storedstr,storedop
	if activestr != "": # If active string is not empty
		if operator != "=": # and operator is not =
			if storedstr == "": # If there is nothing stored (first input)
				storedstr = activestr # Store it
				activestr = "" # Clear active number
				storedop = operator # Store operator
			elif storedstr != "": # If there is a number stored
			# Perform previous mathematical operation
				if storedop == "+":
					storedstr = str(int(storedstr) + int(activestr))
				elif storedop == "-":
					storedstr = str(int(storedstr) - int(activestr))
				elif storedop == "*":
					storedstr = str(int(storedstr) * int(activestr))
				elif storedop == "/":
					storedstr = str(int(storedstr) // int(activestr))
				activestr = "" # Clear active number
		else: # If operator is equals
		# Do the same operation but put that as the active number instead
			if storedop == "+":
				activestr = str(int(storedstr) + int(activestr))
			elif storedop == "-":
				activestr = str(int(storedstr) - int(activestr))
			elif storedop == "*":
				activestr = str(int(storedstr) * int(activestr))
			elif storedop == "/":
				activestr = str(int(storedstr) // int(activestr))
			storedstr = "" # And clear the storedstr instead
	refresh()		


def clear(): # Clear button command
	global activestr,storedstr,storedop
	# Clears all values
	activestr = ""
	storedstr = ""
	storedop = ""
	refresh()

def refresh(): # Refreshes the display bar
	if activestr == "": # If the active number is empty
		display.config(text = storedstr) # Show the stored number
	else: # If it is not empty
		display.config(text = activestr) # Show active number

calcframe = Frame(window, bg = "orange", width = 300, height = 600) # Frame for buttons
dispframe = Frame(window, bg = "black", width = 300, height = 100) # Frame for display
spacer = Label(dispframe, bg = "black", height = 1) # Adds space between top of dispframe and display label
display = Label(dispframe, text = "", height = 3, width = 25) # Display label

butlist = [] # Making numbered buttons
for i in range(0,10):
	butlist.append(Number(i)) # Makes buttons numbered from 0 to 9

oplist = ["=","+","-","*","/"] # Making operator buttons
opbutlist = []
for i in oplist:
	opbutlist.append(Ops(i)) # Makes operator buttons for each operator in oplist

# Making clear button
clearbut = Button(calcframe, text = "C", command = clear, cursor = "plus", height = 3, width = 8)

# Packing frames, spacers and display bar
dispframe.pack()
dispframe.pack_propagate(0)
calcframe.pack()
calcframe.pack_propagate(0)
spacer.pack()
display.pack()

# Grid Layout
butlist[9].but.grid(row=0,column=0)
butlist[8].but.grid(row=0,column=1)
butlist[7].but.grid(row=0,column=2)
butlist[6].but.grid(row=1,column=0)
butlist[5].but.grid(row=1,column=1)
butlist[4].but.grid(row=1,column=2)
butlist[3].but.grid(row=2,column=0)
butlist[2].but.grid(row=2,column=1)
butlist[1].but.grid(row=2,column=2)
butlist[0].but.grid(row=3,column=0)
clearbut.grid(row=3,column=1)
opbutlist[0].but.grid(row=3,column=2)
opbutlist[1].but.grid(row=0,column=3)
opbutlist[2].but.grid(row=1,column=3)
opbutlist[3].but.grid(row=2,column=3)
opbutlist[4].but.grid(row=3,column=3)

# Mainloop
window.mainloop()
