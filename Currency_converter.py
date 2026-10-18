from tkinter import *
root=Tk()
root.title('Currency converter')
root.geometry('800x300')
root.config(background='purple')

def from_dollar():
    pound=float(input_value.get()) * 0.75
    peso=float(input_value.get()) * 62.58
    euro=float(input_value.get()) * 0.89

    poundconversion.delete('1.0',END)
    poundconversion.insert(END,pound)

    pesoconversion.delete('1.0',END)
    pesoconversion.insert(END,peso)

    euroconversion.delete('1.0',END)
    euroconversion.insert(END,euro)

    
    




#designing app
dollar_lbl=Label(root,text='Dollar',bg='pink')
input_value=IntVar()
dollar_entry=Entry(root,textvariable=input_value)
pound_lbl=Label(root,text='Pound',bg='pink')
peso_lbl=Label(root,text='Peso',bg='pink')
euro_lbl=Label(root,text='Euro',bg='pink')
convert_btn=Button(root,text='Convert',bg='green',bd=7,command=from_dollar)

poundconversion=Text(root,height=2,width=25,fg='blue')
pesoconversion=Text(root,height=2,width=25,fg='blue')
euroconversion=Text(root,height=2,width=25,fg='blue')



dollar_lbl.grid(row=0,column=0,padx=50)
dollar_entry.grid(row=0,column=1,padx=30)

pound_lbl.grid(row=1,column=1,pady=10)
poundconversion.grid(row=2,column=1)

peso_lbl.grid(row=2,column=2,pady=10)
pesoconversion.grid(row=3,column=2)

euro_lbl.grid(row=0,column=2,pady=10)
euroconversion.grid(row=1,column=2)

convert_btn.grid(row=9,column=1)



root.mainloop()
