
name = str(input("Greetings, I am Amox and I am a chatbot, what is your name?"))
while True:
    mood = str(input(f"Hello {name}, how are you rn \n Good, or Bad ")).lower()
    if mood == "good":
        print("Well its nice to hear that")
    elif mood == "bad":
        print("Sad to hear that. Anyways,")
    else:
        print("Its sometimes hard to put our things into words")
    hobbies = str(input("what are you hobbies?\n")) 
    print(f"I love doing {hobbies} too")
    leave = str(input("what do you wanna do now?\n Leave, Chat")).lower()
    if leave == "leave":
        print("Goodbye!")
        break
    else: 
        pass