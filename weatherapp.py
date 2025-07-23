import requests
import json
import os

city = input("Enter the city name: ")

url = f"https://api.weatherapi.com/v1/current.json?key=ab7b670c8ba980558252207&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)

w = wdic["current"]["temp_c"]
print(w)

text = f"The temperature in {city} is {w} degrees"
command = f'powershell -Command "Add-Type -AssemblyName System.Speech; ' \
          f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'

os.system(command)
