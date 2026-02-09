import requests

current = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-37.70&lon=144.93&units=metric&appid=d7825fad863b2100ac5ee5d26a00ac8b")


print(current.json())

#1769904000
#1770681600
