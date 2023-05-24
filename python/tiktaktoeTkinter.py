import tkinter as tk
import pandas as pd
border=50

XO={"A":["","",""],"B":["","",""],"C":["","",""]}
game=pd.DataFrame(XO, index=[1,2,3])

window=tk.Tk()
window.title("Tic Tac Toe game")
canvas = tk.Canvas (window, bg="white" , width=600 , height =600)

line1 = canvas.create_line(200,20,200,580, fill='black', width=4)
line2 = canvas.create_line(400,20,400,580, fill='black', width=4)
line3 = canvas.create_line(20,200,580,200, fill='black', width=4)
line4 = canvas.create_line(20,400,580,400, fill='black', width=4)
label_error=tk.Label(window, text= "")
win_label=tk.Label(window, text= "")
i=0
def write_value_into_board(i,j,player,event):
    global game ,canvas
    if player%2==0:
        if game[i][j]=="":
            line_x=canvas.create_line(event.x-50, event.y-50, event.x+50,event.y+50, fill="blue", width=5)+canvas.create_line(event.x+50, event.y-50, event.x-50,event.y+50, fill="blue", width=5)
            game[i][j]="X"
    else:
        if game[i][j]=="":
            line_o=canvas.create_oval(event.x-50, event.y-50, event.x+50,event.y+50,outline = 'red', width=5)
            game[i][j]="O"
def tictactoe(event):
    global i, line1, line2, line3, line4, canvas, border, game
    line1_x0,line1_y0,line1_x1, line1_y1 = canvas.coords(line1)
    line2_x0,line2_y0,line2_x1, line2_y1 = canvas.coords(line2)
    line3_x0,line3_y0,line3_x1, line3_y1 = canvas.coords(line3)
    line4_x0,line4_y0,line4_x1, line4_y1 = canvas.coords(line4)
    if ((event.x>=border and event.x<=600-border) and (event.y>=border and event.y<=600-border)) and ((event.x<line1_x0-border or event.x>line1_x0+border) and (event.x<line2_x0-border or event.x>line2_x0+border)) and ((event.y<line3_y0-border or event.y>line3_y0+border) and (event.y<line4_y0-border or event.y>line4_y0+border)):
        if ((event.x>=0 and event.x<=200) and (event.y>=0 and event.y<=200)):
            write_value_into_board("A",1,i, event)
        elif ((event.x>=200 and event.x<=400) and (event.y>=0 and event.y<=200)):
            write_value_into_board("B",1,i, event)
        elif ((event.x>=400 and event.x<=600) and (event.y>=0 and event.y<=200)):
            write_value_into_board("C",1,i, event)
        elif ((event.x>=0 and event.x<=200) and (event.y>=200 and event.y<=400)):
            write_value_into_board("A",2,i, event)
        elif ((event.x>=200 and event.x<=400) and (event.y>=200 and event.y<=400)):
            write_value_into_board("B",2,i, event)
        elif ((event.x>=400 and event.x<=600) and (event.y>=200 and event.y<=400)):
            write_value_into_board("C",2,i, event)
        elif ((event.x>=0 and event.x<=200) and (event.y>=400 and event.y<=600)):
            write_value_into_board("A",3,i, event)
        elif ((event.x>=200 and event.x<=400) and (event.y>=400 and event.y<=600)):
            write_value_into_board("B",3,i, event)
        elif ((event.x>=400 and event.x<=600) and (event.y>=400 and event.y<=600)):
            write_value_into_board("C",3,i, event)
        i+=1
        label_error.config(text=" ")
    else:
        label_error.config(text="not in range")
    chech_win(game)


def chech_win(game):
    global canvas
    for j in range(1,4):
            if(game["A"][j]!="" and game["B"][j]!="" and game["C"][j]!="" and game["A"][j]==game["B"][j] and game["B"][j]==game["C"][j] and game["A"][j]==game["C"][j]):
                win_label.config(text=f'{game["A"][j]} won')
                if j == 1:
                    line = canvas.create_line(40,100,560,100, fill='green', width=4)
                elif j == 2:
                    line = canvas.create_line(40,300,560,300, fill='green', width=4)
                elif j == 3:
                    line = canvas.create_line(40,500,560,500, fill='green', width=4)
                break
    if check_equalizations(game,"A"):
        line = canvas.create_line(100,40,100,560, fill='green', width=4)
    elif check_equalizations(game,"B"):
        line = canvas.create_line(300,40,300,560, fill='green', width=4)
    elif check_equalizations(game,"C"):
        line = canvas.create_line(500,40,500,560, fill='green', width=4)
    if(game["A"][1]!="" and game["B"][2]!="" and game["C"][3]!="" and game["A"][1]==game["B"][2] and game["A"][1]==game["C"][3] and game["B"][2]==game["C"][3]):
        line = canvas.create_line(40,40,560,560, fill='green', width=4)
        win_label.config(text=f'{game["A"][1]} won')
    elif(game["A"][3]!="" and game["B"][2]!="" and game["C"][1]!="" and game["A"][3]==game["B"][2] and game["A"][3]==game["C"][1] and game["B"][2]==game["C"][1]):
        line = canvas.create_line(40,560,560,40, fill='green', width=4)
        win_label.config(text=f'{game["A"][1]} won')

def check_equalizations(game,x):
      if (game[x][3]!="" and game[x][1]!="" and game[x][2]!="" and game[x][1]==game[x][2] and game[x][1]==game[x][3] and game[x][2]==game[x][3]):
            win_label.config(text=f'{game[x][3]} won')
            return game[x][3]
  

window.bind("<Button-1>", tictactoe)
canvas.pack()
label_error.pack(pady= 25)
win_label.pack(pady= 25)
window.mainloop()