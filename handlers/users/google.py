from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from time import sleep
from googlesearch import search

from keyboards.default import kb_menu, kb_back
from utils.misc import rate_limit


@dp.message_handler(text='⬅Назад', state='google')
async def quit(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Для продолжения воспользуйтесь кнопками меню', reply_markup=kb_menu)


@rate_limit(limit=5)
@dp.message_handler(Text(equals="🔍Поиск в Google"))
async def search_google(message: types.Message, state: FSMContext):
    await message.reply(f'Пожалуйста, введите текст для поиска: \n'
                        f'Будет найдено 5 ссылок!', reply_markup=kb_back)
    await state.set_state("google")  # --- назначем состояние


@dp.message_handler(state="google")  # ---- получаем стейт google (который назаначен выше)
async def get_google(message: types.Message, state: FSMContext):
    src_google = f'{message.text.lower()}'
    for item in search(src_google, num=5, stop=5, pause=2):
        print(item)
        sleep(2)
        await message.answer(f'{item}', reply_markup=kb_menu)
        await state.finish()  # ------ Сбрасываем состояние