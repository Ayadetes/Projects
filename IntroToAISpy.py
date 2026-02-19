import colorama 
from colorama import * 
from textblob import TextBlob

colorama.init()

print(f"{Fore.LIGHTGREEN_EX}🔎👾 I am the Sentimental Spy 👾🔎{Style.RESET_ALL}")
user_name = str(input(f"{Fore.CYAN}Username: "))

if not user_name:
    user_name = "Mumbo Jumbo"

Conversation_History = []

print(f"{Fore.LIGHTGREEN_EX}Hello Agent {user_name},")
print(f"{Fore.LIGHTGREEN_EX}I can find sentiments using TextBlob. \n Type a sentence in to try me{Style.RESET_ALL}")
print(f"{Fore.LIGHTMAGENTA_EX}Type in exit, history, or reset to access those commands {Style.RESET_ALL}")

while True: 
    user_input = input(f"{Fore.LIGHTGREEN_EX}>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.CYAN}We need some text{Style.RESET_ALL}")
        continue
    elif user_input.lower() =="exit":
        print("Mission Report:")
        for i in range(len(Conversation_History)):
                if v == "Positive":
                    color = Fore.GREEN
                    emoji = "😁"
                elif v == "Negative":
                    color = Fore.RED
                    emoji = "😭"
                else: 
                    color = Fore.YELLOW
                    emoji = "😑"

                print(f"{i + 1}: {color}{v} emotions {emoji}{Style.RESET_ALL}")

        print("Closing...")
        break
    elif user_input.lower() == "reset":
        Conversation_History.clear()
        print(f"{Fore.CYAN}Resetting...{Style.RESET_ALL}")
    elif user_input.lower() == "history":
        if not Conversation_History:
            print(f"{Fore.YELLOW}Theres no history yet{Style.RESET_ALL}")
        else: 
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")

            for i in range(len(Conversation_History)):
                if v == "Positive":
                    color = Fore.GREEN
                    emoji = "😁"
                elif v == "Negative":
                    color = Fore.RED
                    emoji = "😭"
                else: 
                    color = Fore.YELLOW
                    emoji = "😑"

                print(f"{i + 1}: {color}{v} emotions {emoji}{Style.RESET_ALL}")

        continue
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        v = "Positive"
        color = Fore.GREEN
        emoji = "😁"  
    if polarity < -0.25:
        v = "Negative"  
        color = Fore.RED
        emoji = "😭"
    elif 0.24 > polarity > -0.24:
        v = "Neutral"
        color = Fore.YELLOW
        emoji = "😑"

    Conversation_History.append((user_input, polarity, v))
    print(f"{color}{emoji} {v} sentiment detected! "
          f"Polarity: {polarity:.2f}")