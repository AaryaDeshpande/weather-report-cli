import os

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    """Fetch weather data for a city from OpenWeatherMap."""
    if not API_KEY:
        print("Missing OPENWEATHER_API_KEY. Add it to a .env file first.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        message = data.get("message", "Unable to fetch weather data.")
        print(f"Weather lookup failed: {message}")
        return

    city_name = data["name"]
    temp_celsius = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print()
    print(f"Weather report for {city_name}")
    print(f"Temperature: {temp_celsius} C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.title()}")


city = input("Enter a US city: ")
get_weather(city)
