from tkinter import *
window = Tk()
window.title("Getting started with widgets")
window.geometry("400x300")

Num1Label = Label(window, text="Enter first number:")
Num2Label = Label(window, text="Enter second number:")

Num1Entry = Entry(window, width=30)
Num2Entry = Entry(window, width=30)

def calculate():
    num1_value = Num1Entry.get()
    num2_value = Num2Entry.get()
    sum_result = int(num1_value) * int(num2_value)
    textbox.insert(END, f"The product is: {sum_result}\n")

textbox = Text(window, bg="#D3D3D3", fg="black")
button = Button(window, text="Calculate", command=calculate, bg="Gray")

Num1Label.place(x=20, y=20)
Num1Entry.place(x=180, y=20)    
Num2Label.place(x=20, y=60)
Num2Entry.place(x=180, y=60)
button.place(x=150, y=100)
textbox.place(y=140)

window.mainloop()