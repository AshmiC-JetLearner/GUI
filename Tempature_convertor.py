from tkinter import *
root=Tk()
root.title('Tempature')
root.geometry('400x200')
root.config(background='pink')

def from_fahrenheit(self):
     celsius=float(input_value.get()) -32  * 5/9

     celsius_lbl.delete('1.0',END)
     celsius_lbl.insert(END,celsius)

celsius_lbl=Label(root,text='Celsius',bg='white')
input_value=IntVar()
convert_btn=Button(root,text='Convert',bg='green',bd=7,command=NONE)

fahrenheit_lbl=Label(root,text='Fahrenheit',bg='pink')
fahrenheit_entry=Entry(root,textvariable=input_value)

fahrenheit_lbl.grid(row=0,column=0,padx=35)
fahrenheit_entry.grid(row=0,column=1,padx=5)

celsius_lbl.grid(row=1,column=1,pady=20)
convert_btn.grid(row=11,column=1,pady=40)

root.mainloop()
