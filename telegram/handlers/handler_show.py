import json

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from telegram.pdf.pdf_bai import create_pdf_bai
from telegram.pdf.pdf_history import create_pdf_history
from telegram.pdf.pdf_emotions import create_pdf_emotions
from telegram.keyboards.keybords_default import get_show_kb, get_ok_kb
from telegram.data_base.db_bai import load_allpdf_bai_answers, load_pdf_bai_questions
from telegram.data_base.db_history import load_pdf_history_questions, load_allpdf_history_answers
from telegram.data_base.db_emotions import load_pdf_emotions_questions, load_allpdf_emotions_answers


# @dp.message_handler(Text(equals="Переглянути попередні результати", ignore_case=True))
async def choose_show(message: types.Message):
    await message.answer(text="Зроби вибір", reply_markup=get_show_kb())


# @dp.message_handler(Text(equals="Переглянути результати Шкалу Тривоги Бека", ignore_case=True))
async def get_show_bai(message: types.Message):
    bai_list = await load_allpdf_bai_answers(message.from_user.id)
    bai_list_questions = await load_pdf_bai_questions()
    for data in bai_list:
        answers = data['answers']
        result = data['result']
        time = data['date']
        pdf = create_pdf_bai(json.loads(answers), bai_list_questions, result, time)
        pdf_file = types.InputFile(pdf, filename=f"Шкала тривоги Бека результат {message.from_user.first_name} "
                                                 f"{time}.pdf")
        await message.answer_document(pdf_file, caption="Дані у форматі PDF")
        await message.answer(text="Твій попередній результат", reply_markup=get_ok_kb())


# @dp.message_handler(Text(equals="Переглянути результати емоції, яких я уникаю", ignore_case=True))
async def get_show_emotions(message: types.Message):
    emotions_list = await load_allpdf_emotions_answers(message.from_user.id)
    emotions_list_questions = await load_pdf_emotions_questions()
    for data in emotions_list:
        answers = data['answers']
        time = data['date']
        pdf = create_pdf_emotions(json.loads(answers), emotions_list_questions, time)
        pdf_file = types.InputFile(pdf, filename=f"Шкала тривоги Бека результат {message.from_user.first_name} "
                                                 f"{time}.pdf")
        await message.answer_document(pdf_file, caption="Дані у форматі PDF")
        await message.answer(text="Твій попередній результат", reply_markup=get_ok_kb())


# @dp.message_handler(Text(equals="Переглянути результати написання історії", ignore_case=True))
async def get_show_history(message: types.Message):
    history_list = await load_allpdf_history_answers(message.from_user.id)
    history_list_questions = await load_pdf_history_questions()
    for data in history_list:
        answers = data['answers']
        time = data['date']
        pdf = create_pdf_history(json.loads(answers), history_list_questions, time)
        pdf_file = types.InputFile(pdf, filename=f"Історія {message.from_user.first_name} {time}.pdf")
        await message.answer_document(pdf_file, caption="Дані у форматі PDF")
        await message.answer(text="Твій попередній результат", reply_markup=get_ok_kb())


def register_handlers_show(dp: Dispatcher):
    dp.register_message_handler(choose_show, Text(equals="Переглянути попередні результати", ignore_case=True))
    dp.register_message_handler(get_show_bai, Text(equals="Переглянути результати Шкалу Тривоги Бека",
                                                   ignore_case=True))
    dp.register_message_handler(get_show_emotions, Text(equals="Переглянути результати емоції, яких я уникаю",
                                                        ignore_case=True))
    dp.register_message_handler(get_show_history, Text(equals="Переглянути результати написання історії",
                                                       ignore_case=True))