import json

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from telegram.fsm.fsm_emotions import FSMEmotions
from telegram.pdf.pdf_emotions import create_pdf_emotions
from telegram.keyboards.keybords_default import get_request_kb, get_ok_kb
from telegram.data_base.db_emotions import get_text_emotions, get_question_emotions, load_pdf_emotions_questions, \
    load_pdf_emotions_answers, down_user, down_emotions


# @dp.message_handler(Text(equals="Емоції, яких я уникаю", ignore_case=True), state=None)
async def get_request(message: types.Message):
    await FSMEmotions.question_1.set()
    await message.answer(text=await get_text_emotions(1))
    await message.answer(text=await get_question_emotions(1))


# @dp.message_handler(state="*", commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(text="Переходь до мети", reply_markup=get_ok_kb())


# @dp.message_handler(state=FSMEmotions.question_1)
async def get_question_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_1'] = message.text
    await FSMEmotions.next()
    await message.answer(text=await get_question_emotions(2))


# @dp.message_handler(state=FSMEmotions.question_2)
async def get_question_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_2'] = message.text
        data_dict = dict(data.items())
        await down_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await down_emotions(message.from_user.id, data_dict)
    await FSMEmotions.next()
    await message.answer(text="Дякую, шо поділився", reply_markup=get_request_kb())


# @dp.message_handler(state=FSMEmotions.push)
async def push_pdf(message: types.Message, state: FSMContext):
    emotions_list_answers, time = await load_pdf_emotions_answers(message.from_user.id)
    emotions_list_questions = await load_pdf_emotions_questions()
    pdf = create_pdf_emotions(json.loads(emotions_list_answers), emotions_list_questions, time)
    pdf_file = types.InputFile(pdf, filename=f"Емоції, яких я уникаю {message.from_user.first_name}.pdf")
    await message.answer_document(pdf_file, caption="Дані у форматі PDF", reply_markup=get_ok_kb())
    await state.finish()


def register_handlers_emotions(dp: Dispatcher):
    dp.register_message_handler(get_request, Text(equals="Емоції, яких я уникаю", ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_message_handler(get_question_1, state=FSMEmotions.question_1)
    dp.register_message_handler(get_question_2, state=FSMEmotions.question_2)
    dp.register_message_handler(push_pdf, state=FSMEmotions.push)
