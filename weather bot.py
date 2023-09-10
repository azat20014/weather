import os
import telegram
from telegram.ext import Updater, CommandHandler
import requests

# Получите API-ключ от OpenWeatherMap и API-токен от вашего телеграм-бота из секретов GitHub
owm_api_key = os.environ['OPENWEATHERMAP_API_KEY']
telegram_token = os.environ['TELEGRAM_BOT_TOKEN']

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я погодный бот. Введи название города, чтобы узнать погоду.")

def weather(update, context):
    city = context.args[0]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={owm_api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = round(data['main']['temp'] - 273.15, 2)
        weather_description = data['weather'][0]['description']
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Погода в городе {city}: {weather_description}\nТемпература: {temperature}°C")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Не удалось получить погоду для данного города.")

def main():
    bot = telegram.Bot(token=telegram_token)
    updater = Updater(token=telegram_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    weather_handler = CommandHandler('weather', weather)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(weather_handler)

    updater.start_polling()

if __name__ == "__main__":
    main()
