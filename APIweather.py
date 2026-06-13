import requests

headers = {"User-Agent": "(myweatherapp.com, contact@myweatherapp.com)"}

response = requests.get("https://api.weather.gov/points/38.8894,-77.0352", headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Full JSON response: {data}")
    print("")
    print(f"{data.get('timeZone')}:")
else: 
    print("failed to recieve data")
