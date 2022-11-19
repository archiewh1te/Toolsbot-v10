import socket
from loader import dp
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from keyboards.default import kb_menu, kb_back
from utils.misc import rate_limit


@dp.message_handler(Text(equals="🌐Узнать IP сайта"))
async def ip_by_hostname(message: types.Message, state: FSMContext):
    await message.reply(f'пожалуйста, введите URL-адрес веб-сайта: ', reply_markup=kb_back)
    await state.set_state("get_ip")  # --- назначем состояние


@rate_limit(limit=5)
@dp.message_handler(text='⬅Назад', state='get_ip')
async def quit(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Для продолжения воспользуйтесь кнопками меню', reply_markup=kb_menu)

@dp.message_handler(state='get_ip')  # ---- получаем стейт get_ip (который назаначен выше)
async def get_ip_hostname(message: types.Message, state: FSMContext):
    try:
        await message.reply(f'Hostname: {message.text}\nIp адрес: {socket.gethostbyname(message.text)}',reply_markup=kb_menu)
        await state.finish()  # ------ Сбрасываем состояние
    except socket.gaierror as error:
        await message.reply(f'Неверный хост - {error}')


