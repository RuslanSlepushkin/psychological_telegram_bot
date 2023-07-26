from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_choice_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Сформувати запит")
    button_2 = KeyboardButton("Домашнє завдання")
    button_3 = KeyboardButton("Більше про когнітивно-поведінкову терапію")
    button_4 = KeyboardButton("Переглянути попередні результати")
    button_5 = KeyboardButton("Видалити попередні результати")
    kb.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)
    return kb


def get_choice_homework_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Шкала Тривоги Бека")
    button_2 = KeyboardButton("Емоції, яких я уникаю")
    button_3 = KeyboardButton("Написання історії")
    kb.add(button_1).add(button_2).add(button_3)
    return kb


def get_ok_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("OK")
    kb.add(button_1)
    return kb


def get_next_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Далі")
    kb.add(button_1)
    return kb


def get_yes_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Так")
    kb.add(button_1)
    return kb


def get_request_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Отримати PDF файл із запитом")
    kb.add(button_1)
    return kb


def get_request_bai_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Отримати PDF файл із запитом")
    kb.add(button_1)
    return kb


def get_show_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Переглянути результати Шкалу Тривоги Бека")
    button_2 = KeyboardButton("Переглянути результати емоції, яких я уникаю")
    button_3 = KeyboardButton("Переглянути результати написання історії")
    kb.add(button_1).add(button_2).add(button_3)
    return kb


def get_delete_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = KeyboardButton("Видалити результати Шкали Тривоги Бека")
    button_2 = KeyboardButton("Видалити результати емоції, яких я уникаю")
    button_3 = KeyboardButton("Видалити результати написання історії")
    button_4 = KeyboardButton("Видалити результати запиту")
    kb.add(button_1).add(button_2).add(button_3).add(button_4)
    return kb