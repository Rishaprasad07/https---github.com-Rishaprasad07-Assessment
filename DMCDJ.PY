import tkinter as tk 

root = tk.Tk()
root.title("My GUI")

label = tk.label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="Click me!", command=root.quit)
button.pack()

root.mainloop()
