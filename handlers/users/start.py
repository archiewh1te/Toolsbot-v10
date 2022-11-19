from aiogram import types
from loader import dp

from keyboards.default import kb_menu

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    who = "@" + message.from_user.first_name
    await message.answer(f'Привет {who}! \n'
                         f'Ты попал в бота который может всё - воспользуйтесь кнопками меню', reply_markup=kb_menu)