import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "9ca9d39577bc1e0fc821c96856376eff"

weather_params = {
    "lat": 37.566536,
    "lon": 126.977966,
    "appid": api_key,
    "lang": "kr"

}
# tst
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response.json())

