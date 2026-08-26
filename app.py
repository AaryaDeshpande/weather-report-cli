import streamlit as st

from get_weather import get_weather_data


st.set_page_config(page_title="Weather Report", page_icon="W")

st.title("Weather Report App")
st.write("Enter a US city to get the current weather.")

city = st.text_input("City", placeholder="Durham")

if st.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city.")
    else:
        try:
            weather = get_weather_data(city.strip())

            st.subheader(f"Current weather in {weather['city']}")

            col1, col2 = st.columns(2)
            col1.metric("Temperature", f"{weather['temperature']} C")
            col2.metric("Humidity", f"{weather['humidity']}%")

            st.info(f"Description: {weather['description'].title()}")
        except ValueError as error:
            st.error(error)
