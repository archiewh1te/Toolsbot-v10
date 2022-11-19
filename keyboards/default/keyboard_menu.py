from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# kb_menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#
#             KeyboardButton(text='🌐Узнать IP сайта'),
#             KeyboardButton(text='🌤Узнать погоду'),
#             KeyboardButton(text='🎥Поиск в YouTube'),
#             KeyboardButton(text='🔍Поиск в Google')
#         ]
#     ],
#     resize_keyboard=True
# )

kb_back = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='⬅Назад'),

        ]
    ],
    resize_keyboard=True
)

button1 = KeyboardButton(text='🌐Узнать IP сайта')
button2 = KeyboardButton(text='🌤Узнать погоду')


kb_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(
    button1, button2
)


button6 = KeyboardButton(text='📄Информация об IP')

kb_menu.row(button6)


button4 = KeyboardButton(text='🎥Поиск в YouTube')
button5 = KeyboardButton(text='🔍Поиск в Google')

kb_menu.row(button4, button5)
