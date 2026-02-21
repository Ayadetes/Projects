import colorama 
colorama.init()
color = colorama.Fore
cvHistory = []
name = str(input(f"{color.GREEN}Greetings, I am Amox and I am a chatbot, what is your name?\n{color.RESET}")).capitalize()
status = True
def leave():
    leave = str(input(f"{color.GREEN}what do you wanna do now?\n{color.RED}Leave{color.RESET}, {color.BLUE}Chat{color.RESET}\n")).lower()
    if leave == "leave":
        print("Goodbye!")
        return False
    else: 
        return True

mood = str(input(f"{color.GREEN}Hello {name}, how are you rn \n Good, or Bad \n{color.RESET}")).lower()
if mood == "good" or mood == "great" or mood == "amazing" or mood == "fantastic":
    print("Well its nice to hear that")
elif mood == "bad" or mood == "sad" or mood == "depressed" or mood == "unhappy":
    print("Sad to hear that. Anyways,")
else:
    print("Its sometimes hard to put our things into words")

while True:
    ReportInput = str(input(f"{color.GREEN}Would you like a report of whats happening?\n{color.BLUE}Yes{color.RESET} or {color.RED}No{color.RESET} \n{color.RESET}")).lower()
    if ReportInput == "yes" or ReportInput == "y" or ReportInput == "yeah" or ReportInput == "yep" or ReportInput == "sure" or ReportInput == "ok" or ReportInput == "okay":
        print("Today (1/1/1955) \n Weather \n High - 73* Low - 69*")
        print("Morning News \n The 67 meme died out why are we still doing this \n -Jeff Bezos")
        print("Pinned - \n India -- 9:00am \n Tampa -- 12:00pm \n Paris -- 1:00pm")
        cvHistory.append("Report")
    elif ReportInput == "no" or ReportInput == "n" or ReportInput == "nope" or ReportInput == "nah" or ReportInput == "not really":
        print("Alrighty then")
        cvHistory.append("No Report")
    else:
        print("I didnt understand that, but its ok")
        cvHistory.append("No Report")
    status = leave()
    if status == True:
        pass
    else:
        break