from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with widgets :)")
root.geometry('400x300')

lbl = Label(text="Hey pal!", fg="white", bg="#072F5F", height=1, width=300)

name_lbl = Label(text="Full name", bg="#3895D3")

name_entry = Entry()

def display():
    global Message
    Message = "Welcome to my applictaion!! \n The Date and time are: "
    greet = "Hello "+name+"\n"

    Text_box.insert(END, greet)
    Text_box.insert(END, Message) 
    Text_box.insert(END, date.today()) 

Text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg= 'white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()

root.mainloop()

