from tkinter import*
from tkinter.ttk import *
import tkinter
root=Tk()

root.geometry('300x600')
progress=Progressbar(root,orient=HORIZONTAL,length=100, mode='determinate')

def probar():
    import time
    progress['value']=20
    root.update_idletasks()
    time.sleep(1)

    progress['value']=40
    root.update_idletasks()
    time.sleep(1)

    progress['value']=60
    root.update_idletasks()
    time.sleep(1)

    progress['value']=80
    root.update_idletasks()
    time.sleep(1)

    progress['value']=100


#designing
progress.pack(pady=50)
tkinter.Button(root,text='Start',bd=5,command=probar).pack(pady=10)



root.mainloop()
