from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth=3)
e.grid(row=1, column=3, columnspan=60, padx=6, pady=5)


#e.insert(0,"")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()
    
#define the buttons

button_1 = Button(root, text="Customers name", padx=5, pady=5, command=myClick)   
button_2 = Button(root, text="Receipt number", padx=5, pady=5, command=myClick)    
button_3 = Button(root, text="Item hired", padx=5, pady=5, command=myClick)
button_4 = Button(root, text="Number hired", padx=5, pady=5, command=myClick)
button_5 = Button(root, text="Run", padx=5, pady=5, command=myClick)
button_6 = Button(root, text="Clear", padx=5, pady=5, command=myClick)
button_7 = Button(root, text="Exit", padx=5, pady=5, command=myClick)
#put the buttons on the screen 
button_1.grid(row=1, column=0)
button_2.grid(row=3, column=0)
button_3.grid(row=5, column=0)
button_4.grid(row=7, column=0)
button_5.grid(row=12, column=4)
button_6.grid(row=12, column=7)
button_7.grid(row=12, column=10)





root.mainloop()