import requests
import sys
from datetime import datetime

def get_api_key():
    try:
        with open("api_key.txt", "r") as key_file:
            return key_file.read().strip()
    except FileNotFoundError:
        print("Error: API key file not found. Create a file named 'api_key.txt' with your OpenWeatherMap API key.")
        sys.exit(1)

def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # For Celsius use "metric", for Fahrenheit use "imperial"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_weather(data):
    if data is None:
        return
    
    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return

    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]
    sys_info = data["sys"]
    
    print("\n🌦️ Current Weather 🌦️")
    print(f"📍 Location: {data['name']}, {sys_info.get('country', 'N/A')}")
    print(f"🌡️ Temperature: {main['temp']}°C (Feels like {main['feels_like']}°C)")
    print(f"☁️ Weather: {weather['description'].capitalize()}")
    print(f"📉 Min/Max Temp: {main['temp_min']}°C / {main['temp_max']}°C")
    print(f"💧 Humidity: {main['humidity']}%")
    print(f"🌬️ Wind Speed: {wind['speed']} m/s")
    print(f"🎐 Wind Direction: {wind.get('deg', 'N/A')}°")
    print(f"📊 Pressure: {main['pressure']} hPa")
    print(f"🌅 Sunrise: {datetime.fromtimestamp(sys_info['sunrise']).strftime('%H:%M:%S')}")
    print(f"🌇 Sunset: {datetime.fromtimestamp(sys_info['sunset']).strftime('%H:%M:%S')}")

def main():
    api_key = get_api_key()
    
    while True:
        city = input("\nEnter city name (or 'q' to quit): ").strip()
        if city.lower() == 'q':
            print("Goodbye! 👋")
            break
        
        weather_data = get_weather_data(city, api_key)
        if weather_data:
            display_weather(weather_data)

if __name__ == "__main__":
    main()