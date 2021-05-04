#from tkinter import *
import tkinter as tk

root = tk.Tk()

widgets = [ [ 0 for i in range(50) ] for j in range(50) ]
rowIndex = 1

def clickAddSymbol(x, y):

    if x > 48 or y > 48:
        return

    #Destroy the button and replace it with an input field
    widgets[x][y].destroy()
    widgets[x][y] = tk.Entry(root, width=5)
    widgets[x][y].grid(row=x,column=y)

    #Create a new button to the right (index: x, y+1)
    widgets[x][y+1] = tk.Button(root, text="+", command=lambda i=x,j=y+1: clickAddSymbol(i,j))
    widgets[x][y+1].grid(row=x, column=y+1)

def clickAddRow(index):
    pass


def addRow(index) -> None:

    widgets[index][0] = tk.Entry(root, width=5)
    widgets[index][0].grid(row=index, column=0)

    widgets[index][1] = tk.Label(root, text="->")
    widgets[index][1].grid(row=index, column=1)

    widgets[index][2] = tk.Entry(root, width=5)
    widgets[index][2].grid(row=index, column=2)

    widgets[index][3] = tk.Button(root, text="+", command=lambda i=index,j=3: clickAddSymbol(i,j))
    widgets[index][3].grid(row=index, column=3)


addRow(0)

#btn1 = Button(root, text="+", command=lambda i=1,j=1: click(i,j))
#btn1.grid(row=1, column=1)

if __name__ == "__main__":
    root.mainloop()