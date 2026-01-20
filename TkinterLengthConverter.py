from tkinter import *

window = Tk()
window.title("Length Converter App")
window.geometry("400x400")

label = Label(window, text="Length Converter App")
inputlabel = Label(window, text="Enter length in inches:")
outputlabel = Label(window, text="Length in centimeters:")

inputentry = Entry(window, width=50)

def convert_length():
    inches = inputentry.get()
    centimeters = float(inches) * 2.54
    output.insert(END, f"{centimeters} cm")

output = Text(window, bg="#BEBEBE", fg="black")
button = Button(window, text="Convert", command=convert_length, bg="blue")

label.pack()
inputlabel.pack()
inputentry.pack()
button.pack()
output.pack()

window.mainloop()