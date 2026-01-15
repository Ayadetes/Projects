from tkinter import *

window = Tk()
window.title("Age Storage App")
window.geometry("400x400")
NameLabel = Label(window, text="Enter your name:")
DateLabel = Label(window, text="Enter your day of birth:")
MonthLabel = Label(window, text="Enter your month of birth :")
YearLabel = Label(window, text="Enter your year of birth :")

NameEntry = Entry(window,width=30)
DateEntry = Entry(window,width=30)   
MonthEntry = Entry(window,width=30)
YearEntry = Entry(window,width=30)

def display():
    name_value = NameEntry.get()
    date_value = DateEntry.get()
    month_value = MonthEntry.get()
    year_value = YearEntry.get()
    greet = "Hello, " + name_value + "!"
    message = f"\nYour age is or is going to be: {2026 - int(year_value)}"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(window, bg="#BEBEBE", fg="black")
buton = Button(window, text="Submit", command=display, bg="red")

NameLabel.place(x=20, y=20)
NameEntry.place(x=180, y=20)
DateLabel.place(x=20, y=60)
DateEntry.place(x=180, y=60)
MonthLabel.place(x=20, y=100)
MonthEntry.place(x=180, y=100)
YearLabel.place(x=20, y=140)
YearEntry.place(x=180, y=140)
buton.place(x=150, y=180)
textbox.place(y=220)


window.mainloop()