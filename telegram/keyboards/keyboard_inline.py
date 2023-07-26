from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_url_kb() -> InlineKeyboardMarkup:
    url_kb = InlineKeyboardMarkup(row_width=1)
    url_button_1 = InlineKeyboardButton(text="Центр когнітивного-поведінкової терапії",
                                        url='https://kpt-center.com.ua/ru/')
    url_button_2 = InlineKeyboardButton(text="Коло сім'ї", url='https://k-s.org.ua/')
    url_button_3 = InlineKeyboardButton(text="4help", url='https://4help.com.ua/')
    url_kb.add(url_button_1, url_button_2, url_button_3)
    return url_kb


def get_bai_kb() -> InlineKeyboardMarkup:
    bai_kb = InlineKeyboardMarkup(row_width=1)
    bai_button_1 = InlineKeyboardButton(text="0", callback_data="0")
    bai_button_2 = InlineKeyboardButton(text="1", callback_data="1")
    bai_button_3 = InlineKeyboardButton(text="2", callback_data="2")
    bai_button_4 = InlineKeyboardButton(text="3", callback_data="3")
    bai_kb.add(bai_button_1, bai_button_2, bai_button_3, bai_button_4)
    return bai_kb
