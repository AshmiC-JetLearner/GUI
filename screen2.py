from tkinter import *
root= Tk()
root.geometry("200x250")

#create a button
btn=Button(root, text="Click me", bd=6,bg= "pink",
           activebackground="purple", activeforeground="white",
           command= root.destroy)
btn.pack(side="top")

btn2=Button(root, text="Click me", bd=6,bg= "blue",
           activebackground="pink", activeforeground="white",
           command= root.destroy)
btn2.pack(side="bottom")

btn3=Button(root, text="Click me", bd=6,bg= "blue",
           activebackground="green", activeforeground="white",
           command= root.destroy)
btn3.pack(side="right")

btn4=Button(root, text="Click me", bd=6,bg= "blue",
           activebackground="green", activeforeground="white",
           command= root.destroy)
btn4.pack(side="left")


root.mainloop()
