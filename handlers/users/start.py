from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu, cancel
from loader import dp
from data.config import MORSE_CODE_REVERSE, MORSE_CODE
from states.morse import Morse
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart())  # Старое: @dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(f'''
Привет, {message.from_user.full_name}!
Этот бот предназначен для кодирования английских сообщений в Азбуку Морзе и обратно''')
    await message.answer('Попробуй)')
    await message.answer("Выбери действие из меню ниже", reply_markup=menu)


@dp.message_handler(Text(equals=["Кодировать сообщение", "Декодировать сообщение"]))
async def get_answer(message: Message):
    await message.answer(f"Выбрано: {message.text}")  # reply_markup=ReplyKeyboardRemove()
    if message.text == 'Кодировать сообщение':
        await Morse.code_english_to_morse.set()
        await message.answer('Введи сообщение на английском, которое необходимо закодировать в Азбуку Морзе:',
                             reply_markup=ReplyKeyboardRemove())
    elif message.text == 'Декодировать сообщение':
        await Morse.code_morse_to_english.set()
        await message.answer('Введи сообщение на Азбуке Морзе, которое необходимо декодировать в простое английское '
                             'сообщение:',
                             reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=Morse.code_english_to_morse)
async def code_english_to_morse(english_input: Message, state: FSMContext):
    if english_input.text == "Отмена":
        await state.finish()
        await english_input.answer('Отмена.', reply_markup=menu)
    else:
        await english_input.answer('Ваше сообщение на Азбуке Морзе:', reply_markup=cancel)
    # async with state.proxy() as data:
    #     data['text'] = english_input.text
    #     user_message = data['text']
    english_input.text = english_input.text.upper() + ' '
    morse_code = ''
    char_text = ''
    for char in english_input.text:
        if char != ' ':
            i = 0
            char_text += char
            if char_text == 'SOS':
                morse_code += MORSE_CODE_REVERSE[char_text]
                await english_input.answer(morse_code)
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
    # await state.finish()


@dp.message_handler(state=Morse.code_morse_to_english)
async def decode_morse_to_english(morse_input: Message, state: FSMContext):
    if morse_input.text == "Отмена":
        await state.finish()
        await morse_input.answer('Отмена.', reply_markup=menu)
    else:
        await morse_input.answer('Ваше сообщение на Азбуке Морзе:', reply_markup=cancel)
    # async with state.proxy() as data:
    #     data['text'] = morse_input.text
    #     user_message = data['text']
    morse_input.text += ' '
    decode_morse_code = ''
    char_text = ''
    for char in morse_input.text:
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
    # await state.finish()

# Не работает, пока буду использовать конструкцию с if else
# Возможно надо ее поставить наверх и лучше продумать

# @dp.message_handler(state=Morse)
# async def cancel(message: Message):
#     await message.answer("Отмена.", reply_markup=menu)
