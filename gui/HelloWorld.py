#Use to test KTinker widgets on simple program
#REMEMBER KTinker is a 2 step process, define widget, 
#add into window
from tkinter import *

root = Tk()

#Lets create an entry

myEntry = Entry(root, width = 50)
myEntry.pack()

#Lets create a button

def myClick():
	myLabel2 = Label(root, text="Hello " + myEntry.get())
	myLabel2.pack()

myButton = Button(root, text="Enter your name.",command =myClick)
myButton.pack()

#creating a Label Widget
myLabel = Label(root, text="Hello World")
myLabel.pack()

#Using grid to put text onto the screen .grid(row=0, column=0)
#just pack data using .pack()

root.mainloop()