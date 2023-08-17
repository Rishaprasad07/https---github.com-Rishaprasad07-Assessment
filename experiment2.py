from tkinter import *
from tkinter import ttk

root = Tk()

#e.insert(0, "")

def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()
    
#define the buttons

button_1 = Button(root, text="Customer name", padx=5, pady=5, command=myClick)
button_1.grid(row=0, column=0)
e = Entry(root, width=50, borderwidth=2)
e.grid(row=0, column=3, columnspan=60, padx=5, pady=5)
name_combobox = ttk.tkinter(row=0, column=0)


button_2 = Button(root, text="receipt number", padx=5, pady=5, command=myClick)
button_2.grid(row=1, column=0)
e = Entry(root, width=50, borderwidth=2)
e.grid(row=1, column=3, columnspan=60, padx=5, pady=5)


button_3 = Button(root, text="Item hired", padx=5, pady=5, command=myClick)
button_3.grid(row=2, column=0)
e = Entry(root, width=50, borderwidth=2)
e.grid(row=2, column=3, columnspan=60, padx=5, pady=5)

button_4 = Button(root, text="Number of items hired", padx=5, pady=5, command=myClick)
button_4.grid(row=3, column=0)
e = Entry(root, width=50, borderwidth=2)
e.grid(row=3, column=3, columnspan=60, padx=5, pady=5)


button_5 = Button(root, text="Run", padx=8, pady=5, command=myClick)
button_5.grid(row=8, column=10)

button_6 = Button(root, text="Clear", padx=8, pady=5, command=myClick)
button_6.grid(row=8, column=12)

button_7 = Button(root, text="Exit", padx=8, pady=5, command=myClick)
button_7.grid(row=8, column=14)


root.mainloop()