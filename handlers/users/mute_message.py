from aiogram import types

from filters import IsPrivate
from loader import dp, Dispatcher

from keyboards.default import kb_menu


@dp.message_handler(IsPrivate(),content_types='text')
async def send_message(message: types.Message):
        await message.answer(f'Бот не видит что вы пишите, чтобы начать заного используйте меню' , reply_markup=kb_menu)



