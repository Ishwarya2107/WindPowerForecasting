!pip install requests
!pip install json
import requests
import json

api_key = "443182c924d37ea42547cbd6bfc5faf8"


latitude = 26.920860
longitude = -80.088188


endpoint = "https://api.openweathermap.org/data/2.5/onecall"


params = {
    "lat": latitude,
    "lon": longitude,
    "date":2023-11-13,
    "exclude": "minutely,daily",
    "appid": api_key,
}


response = requests.get(endpoint, params=params)

if response.status_code == 200:
    data = json.loads(response.text)

    print(data)
    wind_speed = []
    wind_direction = []
    for i in range(48):
      wind_speed.append(data['hourly'][i]['wind_speed'])
      wind_direction.append(data['hourly'][i]['wind_deg'])
    print(wind_speed)
    print(wind_direction)


