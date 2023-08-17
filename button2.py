from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()

def myClick():
    myLabel = Label(root, text="Have a nice day " + e.get())
    myLabel.pack()
    
myButton = Button(root, text="Enter a name", command=myClick, fg="purple", bg="white"  )
myButton.pack()
 

root.mainloop()

