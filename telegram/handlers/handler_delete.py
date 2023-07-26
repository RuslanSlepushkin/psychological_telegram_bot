from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from telegram.data_base.db_bai import delete_allpdf_bai_answers
from telegram.data_base.db_history import delete_allpdf_history_answers
from telegram.keyboards.keybords_default import get_delete_kb, get_ok_kb
from telegram.data_base.db_emotions import delete_allpdf_emotions_answers
from telegram.data_base.db_fallingarrow import delete_allpdf_fallingarrow_answers


# @dp.message_handler(Text(equals="Видалити попередні результати", ignore_case=True))
async def choose_delete(message: types.Message):
    await message.answer(text="Зроби вибір", reply_markup=get_delete_kb())


# @dp.message_handler(Text(equals="Видалити результати Шкали Тривоги Бека", ignore_case=True))
async def get_delete_bai(message: types.Message):
    await delete_allpdf_bai_answers(message.from_user.id)
    await message.answer(text="Твои предыдущие результаты удалены", reply_markup=get_ok_kb())


# @dp.message_handler(Text(equals="Видалити результати емоції, яких я уникаю", ignore_case=True))
async def get_delete_emotions(message: types.Message):
    await delete_allpdf_emotions_answers(message.from_user.id)
    await message.answer(text="Твои предыдущие результаты удалены", reply_markup=get_ok_kb())


# @dp.message_handler(Text(equals="Видалити результати написання історії", ignore_case=True))
async def get_delete_history(message: types.Message):
    await delete_allpdf_history_answers(message.from_user.id)
    await message.answer(text="Твои предыдущие результаты удалены", reply_markup=get_ok_kb())


# @dp.message_handler(Text(equals="Видалити результати запиту", ignore_case=True))
async def get_delete_request(message: types.Message):
    await delete_allpdf_fallingarrow_answers(message.from_user.id)
    await message.answer(text="Твои предыдущие результаты удалены", reply_markup=get_ok_kb())


def register_handlers_delete(dp: Dispatcher):
    dp.register_message_handler(choose_delete, Text(equals="Видалити попередні результати", ignore_case=True))
    dp.register_message_handler(get_delete_bai, Text(equals="Видалити результати Шкали Тривоги Бека",
                                                     ignore_case=True))
    dp.register_message_handler(get_delete_emotions, Text(equals="Видалити результати емоції, яких я уникаю",
                                                          ignore_case=True))
    dp.register_message_handler(get_delete_history, Text(equals="Видалити результати написання історії",
                                                         ignore_case=True))
    dp.register_message_handler(get_delete_request, Text(equals="Видалити результати запиту",
                                                         ignore_case=True))