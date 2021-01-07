''' Create a function which takes a city name and returns the weather ID for that city,
    return City not found for failed requests '''

import requests


def today_weather(city):
    """
    Takes  and returns the
    """
    url = f"https://www.metaweather.com/api/location/search/?query={city}"
    response = requests.get(url)
    if not response.ok:
        print('City not found')

    city = response.json()
    return city['woeid']

