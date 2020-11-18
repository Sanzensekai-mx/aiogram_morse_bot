from aiogram.dispatcher.filters.state import StatesGroup, State


class Morse(StatesGroup):
    code_english_to_morse = State()
    code_morse_to_english = State()
