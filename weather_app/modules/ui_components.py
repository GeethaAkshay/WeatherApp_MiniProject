import streamlit as st
import os
import base64

def set_background():
    """Sets a background image using base64 encoding."""
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
    image_folder = os.path.join(os.getcwd(), 'assets', 'weather_icons')   # Directory where images are stored
    images = {
        'Clear': 'sunny.jpg',
        'Clouds': 'cloudy.jpeg',
        'Rain': 'rainy.png',
        'Snow': 'snow.png',
        'Thunderstorm': 'thunder.jpg',
        'Mist': 'mist.jpg'
    }
    # Return the corresponding image path or a default image
    return os.path.join(image_folder, images.get(weather, 'default.jpg'))

def display_weather(weather_data):
    page_bg_img = '''
                    <style>
                    body {
                    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
                    background-size: cover;
                    }
                    </style>
                    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
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

    # Display Weather Information
    col1, col2, col3 = st.columns([12,10,10])  # Create three columns

    with col1:
        st.markdown(
            """
            <div style="text-align: center; padding: 10px; background-color: #FF6F61; border-radius: 15px;">
                <h2>🌡️ Temperature</h2>
                <h3>{}°C</h3>
            </div>
            """.format(temp),
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="text-align: center; padding: 20px; background-color: #4DB6AC; border-radius: 15px;">
                <h2>💧   Humidity</h2>
                <h3>{}%</h3>
            </div>
            """.format(humidity),
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style="text-align: center; padding: 20px; background-color: #64B5F6; border-radius: 15px;">
                <h2>🌬️ Wind Speed</h2>
                <h3>{} m/s</h3>
            </div>
            """.format(wind_speed),
            unsafe_allow_html=True
        )

    st.info(f"**Description:** {description}")
    st.image(image_url, caption=f"Current Weather in {city}", use_container_width=True)

    # Dynamic background image
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url('{image_url}');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
