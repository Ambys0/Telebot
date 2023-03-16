from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests


TOKEN = '5478265131:AAGBHvDuwi-NMgxSkQxe-_aBGUQcfmLQrYA'

# створюємо бота та диспетчера
bot = Bot("5478265131:AAGBHvDuwi-NMgxSkQxe-_aBGUQcfmLQrYA")
dp = Dispatcher(bot)


# обробка команди /weather
@dp.message_handler(commands=["weather"])
async def get_weather_command(message: types.Message):
    # виконуємо запит до API та повертаємо погодні дані
    api_key = "499612c952951b4ec1036569d9428a46"
    city = message.text.split("/weather ")[1]
    weather = get_weather(city, api_key)

    # відправляємо відповідь користувачу
    await message.answer(weather)


def get_weather(city: str, api_key: str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        return "Місто не знайдено"
    else:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        weather_description = data["weather"][0]["description"]
        return f"Температура в місті {city}: {temp:.0f}°C, відчувається як {feels_like:.0f}°C. "


# обробник події приєднання нових користувачів до групи
@dp.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS])
async def greet_new_members(message: types.Message):
    for user in message.new_chat_members:
        # відправка привітання новому користувачу
        await message.answer(f"Вітаємо, {user.full_name}! Ласкаво просимо в наш родинний чат.")

# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




