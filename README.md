---
title: Weather Report App
emoji: W
colorFrom: blue
colorTo: indigo
sdk: streamlit
app_file: streamlit_app.py
pinned: false
---

# Weather Report App

This is a simple weather report project for the AIPI 503 Week 5 API and
Streamlit challenges.

The project includes:

- `get_weather.py`: a command line weather app
- `app.py`: a Streamlit weather app
- `streamlit_app.py`: the Hugging Face Spaces entry point

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

## Deploy on Hugging Face Spaces

Create a new Hugging Face Space with the **Streamlit** SDK.

In the Space settings, add this repository secret:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Hugging Face will run `streamlit_app.py` automatically.

## Notes

The real API key is stored in `.env`, which is ignored by Git so it does not get
uploaded to GitHub.
