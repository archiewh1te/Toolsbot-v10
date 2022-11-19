from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
import requests
import folium

from keyboards.default import kb_menu, kb_back
from utils.misc import rate_limit



@dp.message_handler(text='⬅Назад', state='infoip')
async def quit(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Для продолжения воспользуйтесь кнопками меню', reply_markup=kb_menu)


@rate_limit(limit=5)
@dp.message_handler(Text(equals="📄Информация об IP"))
async def search_info(message: types.Message, state: FSMContext):
    await message.reply(f'Пожалуйста введите IP: ', reply_markup=kb_back)
    await state.set_state("infoip")  # --- назначем состояние


@dp.message_handler(state="infoip")  # ---- получаем стейт infoip(который назаначен выше)
async def get_ip(message: types.Message, state: FSMContext, ):
    try:
        ip = message.text
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Provider]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Почта]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
        }

        query_IP = data['[IP]']
        provider = data['[Provider]']
        Org = data['[Org]']
        country = data['[Страна]']
        regionName = data['[Регион]']
        city = data['[Город]']
        zips = data['[Почта]']
        lat = data['[Широта]']
        lon = data['[Долгота]']

        await message.reply(f"IP: {query_IP}\n"
                            f"Provider: {provider}\n"
                            f"Org: {Org}\n"
                            f"Страна: {country}\n"
                            f"Регион: {regionName}\n"
                            f"Город: {city}\n"
                            f"Почта: {zips}\n"
                            f"Широта: {lat}\n"
                            f"Долгота: {lon}", reply_markup=kb_menu)



        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'location/{response.get("query")}_{response.get("city")}.html')

        await state.finish()


    except requests.exceptions.ConnectionError:
       await message.reply('[!] Проверьте ваше соединение')


