from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp
from data.config import MORSE_CODE_REVERSE, MORSE_CODE


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выберите действие из меню ниже", reply_markup=menu)


@dp.message_handler(Text(equals=["Кодировать сообщение", "Декодировать сообщение"]))
async def get_answer(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо")  # reply_markup=ReplyKeyboardRemove()
    if message.text == 'Кодировать сообщение':
        await message.answer('Введите сообщение на английском, которое необходимо преобразовать в код морзе...')

        @dp.message_handler()
        async def code_english_to_morse(english_input: Message):
            english_input.text = english_input.text.upper() + ' '
            morse_code = ''
            char_text = ''
            for char in english_input.text:
                # if char not in MORSE_CODE_REVERSE.keys():
                #     await english_input.answer('Пожалуйста, напишите сообщение на английском)')
                if char != ' ':
                    i = 0
                    char_text += char
                    if char_text == 'SOS':
                        morse_code += MORSE_CODE_REVERSE[char_text]
                        return morse_code
                else:
                    i += 1
                    if i == 2:
                        morse_code += ' '
                    else:
                        try:
                            for c in char_text:
                                morse_code += MORSE_CODE_REVERSE[c]
                                morse_code += ' '
                        except KeyError:
                            continue
                        char_text = ''
                        morse_code += '   '
            await english_input.answer(morse_code)
    elif message.text == 'Декодировать сообщение':
        await message.answer('Введите сообщение на морзе, которое необходимо преобразовать в английское сообщение...')

        @dp.message_handler()
        async def decode_morse_to_english(morse_input: Message):
            morse_input.text += ' '
            decode_morse_code = ''
            char_text = ''
            for char in morse_input.text:
                # if char not in '-. ':
                #     await morse_input.answer('Пожалуйста, введите сообщение на азбуке морзе)')
                if char != ' ':
                    i = 0
                    char_text += char
                else:
                    i += 1
                    if i == 2:
                        decode_morse_code += ' '
                    else:
                        try:
                            decode_morse_code += MORSE_CODE[char_text]
                        except KeyError:
                            continue
                        char_text = ''
            await morse_input.answer(decode_morse_code)
