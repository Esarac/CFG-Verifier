from tkinter import *

root = Tk()

def click():
    lbl = Label(root, text="test")
    lbl.pack()

btn = Button(root, text="+", command=click)
btn.pack()

root.mainloop()