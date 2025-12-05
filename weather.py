import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get("API_KEY")

emoji_map = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Fog": "🌫️",
    "Smoke": "💨",
    "Haze": "🌫️",
    "Dust": "🌪️",
    "Sand": "🌪️",
    "Ash": "🌋",
    "Squall": "💨",
    "Tornado": "🌪️",
}


while True:
    user_input = input("Enter city:  ")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}"
    )

    weather = weather_data.json()

    if weather["cod"] == "404":
        print("City not found, try with another!")
    else:
        city = weather["name"]
        condition = weather["weather"][0]["main"]
        emoji = emoji_map.get(condition, "")
        temperature = weather["main"]["temp"]
        feels_like = weather["main"]["feels_like"]
        humidity = weather["main"]["humidity"]

        print(f"City: {city}\nCondition: {condition} {emoji}\n")
        print(
            f"Temperature: {temperature}°C\nIt feels like: {feels_like}°C\nHumidity: {humidity}%\n"
        )

    again = input("Search another city? (yes/no):  ").strip().lower()

    if again not in ("yes", "y"):
        print("See you soon!!")
        break

    print()
