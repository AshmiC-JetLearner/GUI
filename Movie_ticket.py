from tkinter import*
from tkinter.ttk import *
import tkinter

root=Tk()
root.title("Cinema Booking")
root.geometry('300x600')
label = tkinter.Label(root, text="How many tickets would you like?")
label.pack(pady=70)

w=Spinbox(root,from_=1,to= 10,increment=1,format='%00.3f')
w.pack(pady=5)



tkinter.Button(root,text='Book now',bd=5,command= root.destroy).pack(pady=100)







root.mainloop()

