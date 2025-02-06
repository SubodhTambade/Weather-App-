Get real-time weather updates for any city directly from your terminal! This Python-based CLI tool fetches live weather data using the OpenWeatherMap API and displays key information like temperature, humidity, wind speed, and more in an easy-to-read format.

🚀 Features:
✅ Fetches current weather for any city worldwide
✅ Displays temperature, humidity, wind speed, and pressure
✅ Shows sunrise & sunset timings
✅ Simple and lightweight command-line interface
✅ Uses OpenWeatherMap API for accurate data

💻 How It Works:
This script reads an API key stored in api_key.txt and uses it to fetch real-time weather data from OpenWeatherMap. The user inputs a city name, and the app retrieves and presents weather details in a structured format. If the API key is missing, the program alerts the user and exits gracefully.

🔧 Setup Instructions:
1️⃣ Clone the repository
2️⃣ Install dependencies: pip install requests
3️⃣ Get an API key from OpenWeatherMap and store it in api_key.txt
4️⃣ Run the script: python weather-app.py
5️⃣ Enter a city name and get instant weather updates!

📊 Example Output:
yaml
Copy
Edit
🌦️ Current Weather 🌦️  
📍 Location: London, UK  
🌡️ Temperature: 18°C (Feels like 17°C)  
☁️ Weather: Cloudy  
💧 Humidity: 70%  
🌬️ Wind Speed: 5 m/s  
🌅 Sunrise: 06:45:30  
🌇 Sunset: 19:15:00  
