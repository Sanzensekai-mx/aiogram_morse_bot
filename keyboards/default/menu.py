from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кодировать сообщение"),
        ],
        [
            KeyboardButton(text="Декодировать сообщение")
        ],
    ],
    resize_keyboard=True)
