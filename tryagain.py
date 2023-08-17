import tkinter

root = tkinter.Tk()

customer_name_label = tkinter.Label(root, text="customer name", padx=20, pady=5)
customer_name_label.pack()
customer_name_label.grid(row=0, column=0)


root.mainloop()