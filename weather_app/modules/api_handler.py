# api_handler.py
import requests
from config import API_KEY


def get_weather(city):
    """
    Fetch weather data from OpenWeatherMap API.

    Args:
        city (str): The name of the city to fetch weather for.

    Returns:
        dict: JSON response containing weather details,
          or None if an error occurs.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
