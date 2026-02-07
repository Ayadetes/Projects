from tkinter import *

window = Tk()
window.geometry("600x300")
window.title("Calculator")
Label1 = Label(window, text="Principal Amount", bg="#BEBEBE", fg="black")
Principal = Entry(window, bg="#BEBEBE", fg="black")
Label2 = Label(window, text="Time", bg="#BEBEBE", fg="black")
Time = Entry(window, bg="#BEBEBE", fg="black")
Label3 = Label(window, text="Rate", bg="#BEBEBE", fg="black")
Rate = Entry(window, bg="#BEBEBE", fg="black")
Label4 = Label(window, text="Output", bg="#BEBEBE", fg="black")
Output = Text(window, bg="#BEBEBE", fg="black", width=50, height=2)


def Calculate():
    Principalc = float(Principal.get())
    Timec = float(Time.get())
    Ratec = float(Rate.get())
    if Principalc != "" or Timec != "" and Ratec !="":
        Interest = (Principalc * Timec * Ratec) / 100
        Output.delete("1.0", END)
        Output.insert(END, Interest)
        print(Interest)
    else:
        Output.insert(END, "You inputn should be valid")
    

CalculateButton = Button(window, text="Calculate",  bg="#BEBEBE", fg="black", command=Calculate)

Label1.place(x=15,y=15)
Principal.place(x=15, y=50)
Label2.place(x=200,y=15)
Time.place(x=200,y=50)
Label3.place(x=385,y=15)
Rate.place(x=385, y=50)
Label4.place(x=15, y=200)
Output.place(x=15, y=250)
CalculateButton.place(x=15, y=100)

window.mainloop()