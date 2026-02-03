from tkinter import *
import random

RPS = Tk()
RPS.geometry("600x500")
RPS.title("Rock Paper Scissors")

Input = Text(RPS, bg="#BEBEBE", fg="black")
resultOutput = Text(RPS, bg="#BEBEBE", fg="Black")
result = ""

def Show_Button_Rock():
    if Input.get("1.0", END).strip() != "":
        Input.delete("1.0", END)
    Input.insert(END, "Rock")
def Show_Button_Paper():
    if Input.get("1.0", END).strip() != "":
        Input.delete("1.0", END)
    Input.insert(END, "Paper")
def Show_Button_Scissors():
    if Input.get("1.0", END).strip() != "":
        Input.delete("1.0", END)
    Input.insert(END, "Scissors")

RockButton = Button(RPS, text="Rock", command=Show_Button_Rock, bg="#BEBEBE", fg="black")
PaperButton = Button(RPS, text="Paper", command=Show_Button_Paper, bg="#BEBEBE", fg="black")
ScissorsButton = Button(RPS, text="Scissors", command=Show_Button_Scissors, bg="#BEBEBE", fg="black")

def Play():
    Bot = random.randint(1,3)
    BotOutput = ""
    if Bot == 1:
        if output.get("1.0", END).strip() != "":
            return
        BotOutput = "Rock"
    if Bot == 2:
        if output.get("1.0", END).strip() != "":
            return
        BotOutput = "Paper"
    if Bot == 3:
        if output.get("1.0", END).strip() != "":
            return
        BotOutput = "Scissors"
    
    print(BotOutput)

    

    if BotOutput == "Rock":
        if Input.get("1.0", END) == "Rock\n":
            result = "It's a Tie!"
        elif Input.get("1.0", END) == "Paper\n":
            result = "You Win!"
        elif Input.get("1.0", END) == "Scissors\n":
            result = "You Lose!"
    elif BotOutput == "Paper":
        if Input.get("1.0", END) == "Rock\n":
            result = "You Lose!"
        elif Input.get("1.0", END) == "Paper\n":
            result = "It's a Tie!"
        elif Input.get("1.0", END) == "Scissors\n":
            result = "You Win!"
    elif BotOutput == "Scissors":
        if Input.get("1.0", END) == "Rock\n":
            result = "You Win!"
        elif Input.get("1.0", END) == "Paper\n":
            result = "You Lose!"
        elif Input.get("1.0", END) == "Scissors\n":
            result = "It's a Tie!"
    output.insert(END, BotOutput + "\n" + result)
    



output = Text(RPS, bg="#FFFFFF", fg="Black")

start = Button(RPS, text="Play", command=Play, bg="#BEBEBE", fg="black")

start.place(x=300  , y=10)
Input.place(x=0, y=50)
RockButton.place(x=10 , y=10)
PaperButton.place(x=100, y=10)
ScissorsButton.place(x=200   , y=10)
output.place(x=0, y=100)



RPS.mainloop()