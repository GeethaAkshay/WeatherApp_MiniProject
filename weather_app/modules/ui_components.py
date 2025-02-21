import streamlit as st
import os
import base64

def set_background(image_path):
    """
    Sets a background image using base64 encoding.

    Args:
        image_path (str): Path to the background image file.
    """
    image_path = "assets/background.png"  # Ensure this file exists

    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()

    background_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Map weather conditions to appropriate image URLs
def get_weather_image(weather):
    """
    Maps weather conditions to an appropriate image.

    Args:
        weather (str): The main weather condition (e.g., 'Clear', 'Clouds').

    Returns:
        str: Path to the corresponding weather image.
    """
    image_folder = os.path.join(os.getcwd(), 'assets', 'weather_icons') 
    image_path="assets/weather_icons/"
    images = {
        'Clear': 'sunny.png',
        'Clouds': 'cloudy.png',
        'Rain': 'rainy.png',
        'Snow': 'snow.png',
        'Thunderstorm': 'thunder.png',
        'Mist': 'mist.png'
    }
    image_path+=images.get(weather, 'default.png')
    set_background(image_path)
    # Return the corresponding image path or a default image
    return os.path.join(image_folder, images.get(weather, 'default.png'))

def display_weather(weather_data):
    """
    Displays weather information in the Streamlit app.

    Args:
        weather_data (dict): JSON response from the weather API.
    """
    if not weather_data:
        st.error("❌ Failed to retrieve weather data. Please try again.")
        return

    city = weather_data['name']
    weather_main = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description'].title()

    # Get dynamic image based on weather condition
    image_url = get_weather_image(weather_main)
    set_background(image_url)

    # Display Weather Information
    col1, col2, col3 = st.columns([12,10,10])  # Create three columns

    with col1:
        st.markdown(
            """
            <div style="text-align: center; padding: 10px;
              background-color: #ff9e19;
              color: #ffffff; border-radius: 15px; height:215px">
                <h2>🌡️ Temperature</h2>
                <h3>{}°C</h3>
            </div>
            """.format(temp),
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="text-align: center; padding: 20px;
              background-color: #514c45; 
            color: #ffffff; border-radius: 15px;">
                <h2>💧   Humidity</h2>
                <h3>{}%</h3>
            </div>
            """.format(humidity),
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style="text-align: center; padding: 20px; 
            background-color: #64B5F6;
              color: #ffffff; border-radius: 15px;">
                <h2>🌬️ Wind Speed</h2>
                <h3>{} m/s</h3>
            </div>
            """.format(wind_speed),
            unsafe_allow_html=True
        )

    st.markdown(
    f"""
    <div style=" padding: 10px; border-radius: 5px;">
        <p style="color: white; font-weight: bold;">
        Description: {description}</p>
    </div>
    """,
    unsafe_allow_html=True
    )   
    st.image(image_url, caption=f"Current Weather in {city}", 
             use_container_width=True)


