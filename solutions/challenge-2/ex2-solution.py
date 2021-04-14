''' Create a function which takes a city name and returns the weather ID for that city,
    return City not found for failed requests '''
import requests

BASE_URL = "https://www.metaweather.com/api/location/search/"

def today_weather(city):
    """
    Takes a city name and returns the weather ID for that city
    """
    params = {'query':city}
    response = requests.get(BASE_URL, params=params)
    if not response.ok:
        return 'City not found'

    return response.json()[0]['woeid']


