# Optimized by Saiom Patro
#CONGRATS FOR WINNING $10000

import requests
from dotenv import load_dotenv
import os

print("IMporting")
load_dotenv()
API_KEY = os.getenv("Token")
print("Imported T0KEN")

Model = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{Model}"
Headers = {"Authorization": f"Bearer {API_KEY}"}


def detect(message):
    Input = {
        "inputs": message,
        "parameters": {"candidate_labels": ["spam", "safe"]}
    }

    response = requests.post(API_URL, headers=Headers, json=Input, timeout=30)
    print(response)

    if not response.ok:
        raise RuntimeError(f"API error:{response.status_code}")
    
    data = response.json()

    results = list(zip(data["labels"], data["scores"]))
    print(f"results: {results}")

    return sorted(results, key=lambda x: x[1], reverse=True)

def show_results(message, results):

    label, score = results[0]

    print("\n" + "=" * 44)
    print("Spam vs Safe Message Classifier")
    print("=" * 44)

    print(f"Message: {message}")
    print(f"Result: {label} ({score*100:.1f}%)\n")

    print("Confidence scores:")
    for i, (lbl, scr) in enumerate(results, 1):
        print(f"{i}. {lbl}: {scr*100:.1f}%")

    if label == "Spam":
        print("\n⚠️  Warning: Don't click links or share personal info!")
    else:
        print("\n✅ Looks safe, but always stay alert!")

    print("=" * 44)

while True:
    print("Enter your email you want to check \nclick q to quit:")
    emailraw = input()
    if emailraw == "q":
        break
    else:
        emailresults = detect(emailraw)
        show_results(emailraw, emailresults)
