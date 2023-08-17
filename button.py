from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()
    
myButton = Button(root, text="Click Me!", command=myClick, fg="black", bg="purple"  )
myButton.pack()
  
font = ("font name", "font_size")
font= ("Arial", 14)    
root.mainloop()