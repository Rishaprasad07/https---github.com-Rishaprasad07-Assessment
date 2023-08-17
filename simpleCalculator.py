from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "")

def button_click(number):
    e.delete(0, END)
    e.insert(0, number)
    
#Define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_1.click)    