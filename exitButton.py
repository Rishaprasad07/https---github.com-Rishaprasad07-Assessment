import tkinter as tk 
from tkinter import ttk


root = tk.Tk()
exit_button = ttk.Button(
    root,
    text="Exit",
    command=lambda: root.quit()
    
)