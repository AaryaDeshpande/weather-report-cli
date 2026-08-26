# Weather Report CLI

This is a simple command line weather report app for the AIPI 503 Week 5 API
Calls challenge.

The app asks the user for a US city, calls the OpenWeatherMap API, and prints:

- Temperature in Celsius
- Humidity
- Weather description

## Setup

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

Create a `.env` file in this folder:

```bash
cp .env.example .env
```

Open `.env` and replace the example value with your OpenWeatherMap API key:

```bash
OPENWEATHER_API_KEY=your_api_key_here
```

## Run

```bash
python3 get_weather.py
```

Example:

```text
Enter a US city: Durham

Weather report for Durham
Temperature: 25.4 C
Humidity: 61%
Description: Clear Sky
```

## Notes

The real API key is stored in `.env`, which is ignored by Git so it does not get
uploaded to GitHub.
