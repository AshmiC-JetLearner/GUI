from tkinter import *
root= Tk()
root.geometry("200x250")

#create a button
btn=Button(root, text='Click me', bd=6,background= "pink",
           activebackground='purple', activeforeground='white',
           command= root.destroy)
btn.pack(side='top')








root.mainloop()
