import os   # OS Библиотека для работы с операционной системой

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
weather_key = str(os.getenv("open_weather_key"))

# Список айдишников всех  администраторов
admins = [
   1234567890
]
