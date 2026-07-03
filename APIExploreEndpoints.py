import requests

Choice = input("Which genre: science, history or technology?\n")

if Choice.lower() == "science":
    API = "https://uselessfacts.jsph.pl/category/Science.json?language=en"
elif Choice.lower() == "history":
    API = "https://uselessfacts.jsph.pl/category/History.json?language=en"
elif Choice.lower() == "technology":
    API = "https://uselessfacts.jsph.pl/category/Technology.json?language=en"
else:
    print("error: invalid genre")

output = requests.get(API)
if output.status_code == 200:
    data = output.json()
    print(data)
else:
    print("Error:", output.status_code)

