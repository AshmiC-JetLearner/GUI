from tkinter import*
root=Tk()
root.title("My hobbies")
root.geometry('300x400')
w= Label(root, text='Things I like to do', font=75,)
w.pack()

frame=Frame(root)
frame.pack(pady=10)

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM,pady=10)

listbox_frame=Frame(root)
listbox_frame.pack(padx=10,pady=10)
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(listbox_frame,yscrollcommand=scrollbar.set,bg='yellow',fg='blue')
listbox.pack(side=LEFT)

scrollbar.config(command=listbox.yview)

items=['Arts and Crafts','sewing','soccer','painting']
for item in items:
    listbox.insert(END, item)



root.mainloop()
