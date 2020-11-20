from aiogram.dispatcher.filters.state import StatesGroup, State


class Morse(StatesGroup):  # Определение состояний
    code_english_to_morse = State()  # Состояние для кодирования Английского в Азбуку Морзе
    code_morse_to_english = State()  # Состояние для декодирования Азбуки Морзе в Английский
