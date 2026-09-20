from tkinter import*
import calendar

def show_calendar():
    new_root=Tk()
   # new_root.config('white')
    root.geometry('650x700')

    fetch_year=int(year_field.get())
    cal_content=calendar.calendar(fetch_year)
    cal_year=Label(new_root,text=cal_content,font='Consolas 10 bold')
    cal_year.pack(side='top')
    new_root.mainloop()
    

#design
if __name__ == '__main__':
    root=Tk()
    root.config(background='light pink')
    root.geometry('300x200')
    root.title('Calendar')

    cal=Label(root,text='Calendar',bg='white',font=('times',28,'bold'))
    year=Label(root,text='Enter year',bg='white',font=('times',13,'bold'))
    year_field=Entry(root)

    show_btn=Button(root,text='Show calendar',bd=5,bg='purple',command=show_calendar)
    exit_btn=Button(root,text='Exit',bd=5,bg='purple',command=exit)

    cal.pack(side='top')
    year.pack(side='top')
    year_field.pack(side='top')

    show_btn.pack(side='bottom')
    exit_btn.pack(side='bottom')



    root.mainloop()
