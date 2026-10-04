from tkinter import*
from tkinter.ttk import *
import tkinter
root=Tk()
root.title("Mirror app")
root.geometry('300x400')

entry_box=Entry(root)
copy_txt=Button(root,text='Copy text',bd=5,bg='purple',var=Entry.get(entry_box))
copy_txt.pack(side=TOP)
