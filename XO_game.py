from math import lgamma
from pickle import TRUE
import tkinter as tk


color = "yellow"
count = 0


def start_game ():
    global count 
    global color 
    color= "yellow"
    count= 0
    
    player1_score.config(bg = "green") 
    player2_score.config(bg = "black") 
    player1_score["text"] = "player 1"
    player2_score["text"] = "player 2"
    
    block1.config(state= "normal")
    block2.config(state= "normal")
    block3.config(state= "normal")
    block4.config(state= "normal")
    block5.config(state= "normal")
    block6.config(state= "normal")
    block7.config(state= "normal")
    block8.config(state= "normal")
    block9.config(state= "normal")
    block1.config(bg= "black")
    block2.config(bg= "black")
    block3.config(bg= "black")
    block4.config(bg= "black")
    block5.config(bg= "black")
    block6.config(bg= "black")
    block7.config(bg= "black")
    block8.config(bg= "black")
    block9.config(bg= "black")
    start.config(state= "disabled")
def game_finish ():
    
    block1.config(state= "disabled")
    block2.config(state= "disabled")
    block3.config(state= "disabled")
    block4.config(state= "disabled")
    block5.config(state= "disabled")
    block6.config(state= "disabled")
    block7.config(state= "disabled")
    block8.config(state= "disabled")
    block9.config(state= "disabled")    
    start.config(state= "normal")

    
def game_logic (thisColour):
    
    if count > 8 :
        player1_score["text"] = "no one"
        player2_score["text"] = "no one"
        game_finish()
    if block1.cget("background") == thisColour and block2.cget("background") == thisColour and block3.cget("background") == thisColour or \
    block4.cget("background") == thisColour and block5.cget("background") == thisColour and block6.cget("background") == thisColour or \
    block7.cget("background") == thisColour and block8.cget("background") == thisColour and block9.cget("background") == thisColour or \
    \
    block1.cget("background") == thisColour and block4.cget("background") == thisColour and block7.cget("background") == thisColour or \
    block2.cget("background") == thisColour and block5.cget("background") == thisColour and block8.cget("background") == thisColour or \
    block3.cget("background") == thisColour and block6.cget("background") == thisColour and block9.cget("background") == thisColour or \
    \
    block1.cget("background") == thisColour and block5.cget("background") == thisColour and block9.cget("background") == thisColour or \
    block3.cget("background") == thisColour and block5.cget("background") == thisColour and block7.cget("background") == thisColour:
    
        print("win")
        if thisColour == "blue":
            player1_score["text"] = "blue win"
        else:
            player2_score["text"] = "yellow win"
            
        game_finish()
        
def game(block):
    global color 
    global count
    count +=1
    
    if color == "yellow":
        color = "blue"
        player2_score.config(bg= "green")
        player1_score.config(bg= "black")
    else :
        color = "yellow"
        player1_score.config(bg= "green")
        player2_score.config(bg= "black")
        
    
    block.config(bg = color, state= "disabled")

    if count > 4 :
        game_logic(color)
                         
root = tk.Tk()

root.title("X O game")
root.geometry("300x300+500+350")
root.resizable(False,False)
h = 5
w = 9
buttoncolor = "black"
block1 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block1))
block2 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block2))
block3 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block3))
block4 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block4))
block5 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block5))
block6 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block6))
block7 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block7))
block8 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block8))
block9 = tk.Button(root, height= h, width= w, bg = buttoncolor, state= "disabled", command= lambda : game(block9))

start = tk.Button(root, height= 3, width = 10, bg = "gray", text= "start", command= lambda : start_game())

player1_score = tk.Label(root, height= 3, width= 10, bg= "black", text= "player 1", fg= "blue")
player2_score = tk.Label(root, height= 3, width= 10, bg= "black", text= "player 2", fg= "yellow")

block1.place(x = 0 , y = 0)
block2.place(x= 73, y = 0)
block3.place(x= 146, y = 0)

block4.place(x= 0, y =86)
block5.place(x= 73, y =86)
block6.place(x= 146, y =86)

block7.place(x= 0, y =172  )
block8.place(x= 73, y =172)
block9.place(x= 146, y =172)

player1_score.place(x = 220, y = 0)
player2_score.place(x = 220, y = 55)

start.place(x = 220 , y = 110 )

root.mainloop()