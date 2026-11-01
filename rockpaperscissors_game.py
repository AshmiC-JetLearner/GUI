from tkinter import*
import tkinter.font as font
import random

player_score=0
computer_score=0
options=[('rock',0),('paper',1),('scissors',2)]

def computer_wins():
    global computer_score,player_score
    computer_score += 1
    winner_label.config(text='Computer Won!!')
    computer_score_lbl.config(text=f'Computer Score:{computer_score}')
    player_score_lbl.config(text=f'Player Score:{player_score}')

def player_wins():
    global computer_score,player_score
    player_score += 1
    winner_label.config(text='Player Won!!')
    computer_score_lbl.config(text=f'Computer Score:{computer_score}')
    player_score_lbl.config(text=f'Player Score:{player_score}')







#creating main window
game_window=Tk()
game_window.title('Rock paper scissor game')
game_window.config(background='blue')
app_font=font.Font(size=12)
game_title=Label(game_window,text='Rock Paper Scissor',
                  bg='black',fg='yellow',font=font.Font(size=20))
game_title.pack()


winner_label=Label(game_window,text="Let's Start the Game...",fg='white',bg='purple',
                   font=font.Font(size=13),pady=8)
winner_label.pack()

input_frame=Frame(game_window,bg='white')
input_frame.pack()

input_frame=Frame(game_window,bg='brown')
input_frame.pack()
player_options=Label(input_frame,text='Your Options:',
                     font=app_font,fg='purple',bg='green')
player_options.grid(row=0,column=0,pady=8)

rock_btn=Button(input_frame,text='Rock',width=15,bd=3,
                bg='pink',pady=5,command=None)
rock_btn.grid(row=1,column=1,padx=8,pady=5)

paper_btn=Button(input_frame,text='paper',width=15,bd=3,
                 bg='grey',pady=5,command=None)
paper_btn.grid(row=1,column=2,padx=8,pady=5)

scissors_btn=Button(input_frame,text='scissors',width=15,bd=3,
                    bg='white',pady=5,command=None)
scissors_btn.grid(row=1,column=3,pady=5,padx=8)

score_lbl=Label(input_frame,text='Score:',font=app_font,fg='blue',bg='white')
score_lbl.grid(row=2,column=0)



computer_choice_lbl=Label(input_frame,text='Computer Choice:___',
                          font=app_font,bg='white',fg='purple')
computer_choice_lbl.grid(row=2,column=3)

player_choice_lbl=Label(input_frame,text='Your Choice:___',
                        bg='white',font=app_font)
player_choice_lbl.grid(row=3,column=3)


player_score_lbl=Label(input_frame,text='Your Score:___',font=app_font,
                       bg='white',fg='green')
player_score_lbl.grid(row=2,column=1)

computer_score_lbl=Label(input_frame,text='Computer Score:___',
                         font=app_font,bg='white',fg='purple')
computer_score_lbl.grid(row=3,column=1)

game_window.geometry('700x300')
game_window.mainloop()

