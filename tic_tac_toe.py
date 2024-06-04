from tkinter import *
import random

def next_turn(row,col):
    pass


def check_winner():
    pass

def check_empty_spaces():
    pass

def start_new_game():
    pass


window =Tk()
window.title("tictactoe Yasmina")

players=["x" , "o"]
player=random.choice(players)
game_btns =[
[0,0,0],
[0,0,0],
[0,0,0]
]

label =Label(text=(player + "turn"),font=('console',40))
label.pack(side="top")
restart_btn =Button(text="restart",font=
                     ('console',20),command=start_new_game)
restart_btn.pack(side="top")
btns_frame=Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] =Button(btns_frame,text="",font=('consoles',50),width=4,height=1,
                                    command=lambda row=row ,col=col :next_turn(row,col))
        game_btns[row][col].grid(row=row,column=col)
window.mainloop()




