import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        print(f"Погода в {city}: {temperature} C, {weather_description}")
    else:
        print("Не удалось получить данные о погоде")

# Замените значение api_key на ваш собственный ключ API OpenWeatherMap
api_key = "YOUR_API_KEY"
city = "YOUR_CITY"

get_weather(api_key, city)
