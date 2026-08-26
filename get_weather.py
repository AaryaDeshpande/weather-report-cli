import os

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather_data(city):
    """Fetch weather data for a city from OpenWeatherMap."""
    if not API_KEY:
        raise ValueError("Missing OPENWEATHER_API_KEY. Add it to a .env file first.")

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
        raise ValueError(f"Weather lookup failed: {message}")

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
    }


def print_weather_report(city):
    """Print a simple weather report to the command line."""
    weather = get_weather_data(city)

    print()
    print(f"Weather report for {weather['city']}")
    print(f"Temperature: {weather['temperature']} C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Description: {weather['description'].title()}")


if __name__ == "__main__":
    city = input("Enter a US city: ")
    try:
        print_weather_report(city)
    except ValueError as error:
        print(error)
