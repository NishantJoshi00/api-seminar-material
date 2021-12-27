key = "fd05de4f336256ec996f75e85841bba4"
import requests

# Get the weather from the API

url = "http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=" + key

data = requests.get(url)
print(data.json())