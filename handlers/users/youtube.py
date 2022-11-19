from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from time import sleep

from youtubesearchpython import *

from keyboards.default import kb_menu, kb_back
from utils.misc import rate_limit




@dp.message_handler(text='⬅Назад', state='youtube')
async def quit(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Для продолжения воспользуйтесь кнопками меню', reply_markup=kb_menu)


@rate_limit(limit=5)
@dp.message_handler(Text(equals="🎥Поиск в YouTube"))
async def search_youtube(message: types.Message, state: FSMContext):
    await message.reply(f'Пожалуйста, введите название видео: \n'
                        f'Будет найдено 5 ссылок!', reply_markup=kb_back)
    await state.set_state("youtube")  # --- назначем состояние


@dp.message_handler(state="youtube")  # ---- получаем стейт youtube (который назаначен выше)
async def get_youtube(message: types.Message, state: FSMContext):
    try:
        customSearch = CustomSearch(f'{message.text.lower()}', VideoUploadDateFilter.thisYear, limit=20)
        for i in range(5):
            search = customSearch.result()['result'][i]['link']
            print(search)
            sleep(1.5)
            await message.answer(f'{search}', reply_markup=kb_menu)
            await state.finish()  # ------ Сбрасываем состояние
    except Exception:
        await message.reply("Проверьте правильно ли написано название")


