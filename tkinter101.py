#! /usr/bin/python3

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='Goodday',message='You pressed me!')

window = Tk()
button = Button(window,text='press',command=reply)
button.pack()
window.mainloop()