---
title: Weather Report App
emoji: 🌤️
colorFrom: blue
colorTo: indigo
sdk: streamlit
app_file: app.py
pinned: false
---

# Weather Report App

This is a simple weather report project for the AIPI 503 Week 5 API and
Streamlit challenges.

The project includes:

- `get_weather.py`: a command line weather app
- `app.py`: a Streamlit weather app
- `streamlit_app.py`: an alternate Streamlit entry point

Both versions ask the user for a US city, call the OpenWeatherMap API, and show:

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

## Run the Command Line App

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

## Run the Streamlit App

```bash
streamlit run app.py
```

Then enter a city in the text box and click **Get Weather**.

## Deploy on Streamlit Community Cloud

Deploy this GitHub repository on Streamlit Community Cloud:

1. Go to `https://streamlit.io/cloud`
2. Create a new app from this GitHub repository
3. Use `main` as the branch
4. Use `app.py` as the main file path
5. Add this app secret:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Streamlit Cloud will run `app.py` as the web app.

## Notes

The real API key is stored in `.env`, which is ignored by Git so it does not get
uploaded to GitHub.
