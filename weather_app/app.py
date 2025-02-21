import streamlit as st
from modules.api_handler import get_weather
from modules.ui_components import display_weather,set_background

def main():
    set_background("assets/background.png")
    st.title("🌤️ Weather App")

    city = st.text_input("Enter city name:", "")

    if st.button("Get Weather"):
        data = get_weather(city)
        print(data)
        display_weather(data)
    
    st.markdown("---")
    st.markdown("Done by--")
    st.markdown("Geetha Akshay")
    st.markdown("Anish Reddy")
    st.markdown("Lahir")
    st.markdown("Hari govind")

if __name__ == "__main__":
    main()