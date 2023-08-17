from tkinter import *

root = Tk()
root.title("Customers name")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

#e.insert(0,"")

def button_click(number):
    return
#define

button_1 = Button(root, text="Customers name", padx=25, pady=15, lambdacommand= button_click)
button_2 = Button(root, text="Receipt number", padx=25, pady=15, Lambdacommand=button_click)
button_3 = Button(root, text="Item hired", padx=25, pady=15, Lambdacommand=button_click)
button_4 = Button(root, text="Number hired", padx=25, pady=15, Lambdacommand=button_click)







root.mainloop()