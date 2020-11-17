import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "" # прописать токен

admins = [
    "", # прописать id чата с админом
]

ip = os.getenv("ip")

MORSE_CODE = {"-.-.-.": ';', "-...-": "=", "---": "O", "----.": "9", "-..-.": "/", ".-...": "&", "...--": "3",
              ".--": "W", "--": "M", "--..": "Z", ".----.": "'", "-.-.--": "!", "-...": "B", "..-": "U", ".----": "1",
              "-.--.-": ")", ".-": "A", "-....-": "-", "...-": "V", "...---...": "SOS", "-.--": "Y", "..": "I",
              "--.-": "Q", "-.": "N", "..---": "2", "-....": "6", "---...": ",", ".-.-.": "+", ".--.-.": "@",
              "....-": "4", "-----": "0", ".-.-.-": ".", "-.-.": "C", ".": "E", "..-.": "F", ".---": "J", "-.-": "K",
              ".-..": "L", ".-.": "R", "...": "S", "--.": "G", "---..": "8", "..--..": "?", "-.--.": "(", ".--.": "P",
              ".....": "5", "..--.-": "_", "-..": "D", ".-..-.": "\"", "-": "T", "....": "H", "--..--": ",",
              "...-..-": "$", "--...": "7", "-..-": "X"}

MORSE_CODE_REVERSE = {}
for k, v in MORSE_CODE.items():
    MORSE_CODE_REVERSE[v] = k
