import streamlit as st
from modules.api_handler import get_weather
from modules.ui_components import display_weather,set_background

def main():
    set_background("assets/background.png")
    st.markdown('<h1 style="color: white;">Weather App</h1>', unsafe_allow_html=True)

    city = st.text_input("",placeholder="Enter city name:")

    if st.button("Get Weather"):
        data = get_weather(city)
        print(data)
        display_weather(data)

    st.markdown("<p style='color:white;'>Done by ---</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Geetha Akshay</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Anish Reddy</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Lahir Sai Vignesh</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:white;'>Harigovind</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()