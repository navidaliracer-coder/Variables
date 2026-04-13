from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Main")

def topwin():

    top = Toplevel()
    top.geometry("180x100")
    top.title("TopLevel")

    l2 = Label(top, text="This is the crasher window")
    l2.pack()

    top.mainloop()

l =Label(root, text="This is a base window")
btn = Button(root, text="SPAM ME!!", command=topwin)

l.pack()
btn.pack()

root.mainloop()


