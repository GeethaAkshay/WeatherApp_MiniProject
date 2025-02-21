import streamlit as st
from modules.api_handler import get_weather
from modules.ui_components import display_weather,set_background

def main():
    """
    Streamlit-based Weather App.

    Features:
    - Users input a city name to get the weather forecast.
    - Fetches weather data using OpenWeatherMap API.
    - Displays temperature, humidity, wind speed, and weather condition.
    - Dynamically updates the background image based on weather conditions.
    - Lists contributors' names.

    Modules:
    - `api_handler`: Handles API requests for weather data.
    - `ui_components`: Manages UI elements like displaying weather 
    and setting the background.

    Usage:
    - Run the script to launch the Streamlit web app.
    - Enter a city name and click "Get Weather" to fetch details.
    """
    
    set_background("assets/background.png")
    st.markdown('<h1 style="color: white;">Weather App</h1>', 
                unsafe_allow_html=True)

    city = st.text_input("",placeholder="Enter city name:")

    if st.button("Get Weather"):
        data = get_weather(city)
        print(data)
        display_weather(data)

    st.markdown("<p style='color:white;'>Done by ---</p>",
                 unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Geetha Akshay</p>", 
                unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Anish Reddy</p>", 
                unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Lahir Sai Vignesh</p>",
                 unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Harigovind</p>", 
                unsafe_allow_html=True)

if __name__ == "__main__":
    main()