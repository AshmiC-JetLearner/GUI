from tkinter import*
root=Tk()
root.geometry('300x400')
w= Label(root, text='Chocos and ice creams', font=55,)
w.pack() #by default side=top

#adding frames
frame=Frame(root)#top frame
frame.pack(pady=10)

#buttons added to frame
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM,pady=10)

b1_button = Button(frame,text='Choco',fg= 'pink',bg='purple',bd=5)
b1_button.pack(side=LEFT,padx=2)

b2_button = Button(frame,text='Dark choco',fg= 'purple',bg='pink',bd=5)
b2_button.pack(side=LEFT,padx=2)

b3_button = Button(frame,text='White choco',fg= 'blue',bg='purple',bd=5)
b3_button.pack(side=LEFT,padx=2)

b4_button = Button(bottomframe,text='Pastry',fg= 'purple',bg='pink',bd=3)
b4_button.pack(side=BOTTOM,pady=2)

b5_button = Button(bottomframe,text='Cupcake',fg= 'blue',bg='purple',bd=3)
b5_button.pack(side=BOTTOM,pady=2)

b6_button = Button(bottomframe,text='Cake pop',fg= 'pink',bg='purple',bd=3)
b6_button.pack(side=BOTTOM)

#adding a list into the root window
listbox_frame=Frame(root)
listbox_frame.pack(padx=10,pady=10)
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(listbox_frame,yscrollcommand=scrollbar.set)
listbox.pack(side=LEFT)

scrollbar.config(command=listbox.yview)

items=['Item 1','Item 2','Item 3','Item 4','Item 5',
       'Item 6','Item 7','Item 8','Item 9','Item 10',
       'Item 11','Item 12','Item 13','Item 14','Item 15',
       'Item 16','Item 17','Item 18','Item 19','Item 20']
for item in items:
    listbox.insert(END, item)


root.mainloop()
