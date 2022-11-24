**ToolsBot v1.0**

**Author:** @ArchieWh1te

**Language:** Python 3.8+

**library pypi:** python-dotenv, aiogram, requests, folium, google 

**License:** Free

[![PyPI](https://img.shields.io/pypi/v/folium?label=folium&logo=folium)](https://pypi.org/project/folium/)
[![PyPI](https://img.shields.io/pypi/v/aiogram?label=aiogram&logo=aiogram)](https://pypi.org/project/aiogram/)
[![PyPI](https://img.shields.io/pypi/v/requests?label=requests&logo=requests)](https://pypi.org/project/requests/)
[![PyPI](https://img.shields.io/pypi/v/google?label=google&logo=google&logoColor=yellow)](https://pypi.org/project/google/)
[![PyPI](https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv&logo=python-dotenv)](https://pypi.org/project/python-dotenv/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiogram?color=greem&logo=python)


### ToolsBot с функциями

**Описание:**

Бот имеет 5 функций: Поиск в Google, Поиск в YouTube, может узнать погоду, показывает информацию об IP и может определить IP сайта.  

Бот написан на асинхронной библиотеке **aiogram** в хорошей структуре и расположении файлов.

Для того чтобы работала погода вам надо зарегистрироваться на сайте https://openweathermap.org/ и получить **ТОККЕН**, далее записать его в файл *.env* в переменную *open_weather_key* (токен должен быть в двойных кавычках " ")

Для работы бота запускаем файл *app.py*.

В папке *location* хранится спарсиный html с картой IP адреса который мы вводим у бота. 

**Скриншоты**

*Клавиатура*

![kb](screen/kb.png)

*Поиск в Google(Выдаст 5 ссылок)*

![google](screen/google.png)

*Узнать IP сайта*

![ip](screen/ip.png)

*Узнать погоду*

![weather](screen/weather.png)

*Поиск в YouTube(Выдаст 5 ссылок)*

![youtube](screen/youtube.png)

*Узнать информацию об IP*

![infoip](screen/infoip.png)
