from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("RED ALERT, VIRUS DETECTED, WAYNETECH PROTOCOLS ACTIVATED")

button = Button(root, text="Scan for virus", command=msg)

button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

root.mainloop()