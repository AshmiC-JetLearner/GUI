from tkinter import*
root=Tk()
root.title("Menu bar")
menubar=Menu(root)

file=Menu(menubar)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open file',command=None)
file.add_command(label='Save As',command=None)
file.add_command(label='Exit',command=None)

edit=Menu(menubar)
menubar.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)
edit.add_command(label='Select All', command=None)
