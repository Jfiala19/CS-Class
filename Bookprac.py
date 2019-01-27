from tkinter import* 

master = Tk()

master.aspect(1,1,1,1)
master.geometry('400x400')
master.title("My First Window")


def click(button):
	label1 = Label(master, text = button.lower()+ " wins", bg = button)
	label1.grid(row =2, column =0, columnspan = 2)

list1 = ['Red', 'Green', 'Blue', 'Yellow']
button = [0,0,0,0]
for x in range(4):
	button[x] = Button(master, text = str(list1[x]), command = lambda x=x:click(str(list1[x])))

button[0].grid(row=0, column = 0)
button[1].grid(row=1, column = 0)
button[2].grid(row=0, column = 1)
button[3].grid(row=1, column = 1)

mainloop()





























# draw_area = Canvas(master, width =400, height =400)
# draw_area.pack()

# draw_area.create_rectangle(150, 25,250,300, fill = 'RED')
# draw_area.create_oval(150,25,200,75, fill = 'BLUE')
# draw_area.create_text(200, 310, text="I'm right here")



# changeable_string = StringVar()
# entry1 = Entry(master,textvariable = changeable_string)

# draw_area.create_window(200, 10, window=entry1)

# mainloop()






















# smallerframe = Frame(width = 400, height = 100, background = "RED")
# smallerframe.pack()

# labe1 = Label(text = )

# mainloop()



























# from tkinter import* 

# myframe = Tk()

# myframe.aspect(1,1,1,1)
# myframe.geometry('400x400')
# myframe.title("My First Window")


# changeable_string = StringVar()
# entry1 = Entry(myframe, textvariable = changeable_string)
# entry1.pack()

# def click():
# 	label1 = Label(myframe, text = changeable_string.get(), cursor = 'pirate', background = 'RED')
# 	label1.pack()

# button1 = Button(myframe,text="Cool Button", command = click)
# button1.pack()

# mainloop()



