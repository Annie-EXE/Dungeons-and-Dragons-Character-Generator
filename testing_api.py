import requests
import json

response = requests.get("https://open5e.com/races/tiefling")
print(response.json)
