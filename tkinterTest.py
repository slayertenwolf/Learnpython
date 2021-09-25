#!/usr/bin/python
#from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='Zoom',message='You You You!')
win = tk.Tk() 
win.title("HelloWorld")
btn = tk.Button(win,text='press me!',command=reply)
btn.pack()
win.mainloop()