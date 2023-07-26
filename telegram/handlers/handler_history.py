import json

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from telegram.fsm.fsm_history import FSMHistory
from telegram.pdf.pdf_history import create_pdf_history
from telegram.keyboards.keybords_default import get_request_kb, get_ok_kb
from telegram.data_base.db_history import get_text_history, get_question_history, down_user, down_history, \
    load_pdf_history_questions , load_pdf_history_answers


# @dp.message_handler(Text(equals="Написання історії", ignore_case=True), state=None)
async def get_request(message: types.Message):
    await FSMHistory.question_1.set()
    await message.answer(text=await get_text_history(1))
    await message.answer(text=await get_question_history(1))


# @dp.message_handler(state="*", commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(text="Переходь до мети", reply_markup=get_ok_kb())


# @dp.message_handler(state=FSMHistory.question_1)
async def get_question_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_1'] = message.text
    await FSMHistory.next()
    await message.answer(text=await get_question_history(2))


# @dp.message_handler(state=FSMHistory.question_2)
async def get_question_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_2'] = message.text
    await FSMHistory.next()
    await message.answer(text=await get_question_history(3))


# @dp.message_handler(state=FSMHistory.question_3)
async def get_question_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_3'] = message.text
    await FSMHistory.next()
    await message.answer(text=await get_question_history(4))


# @dp.message_handler(state=FSMHistory.question_4)
async def get_question_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_4'] = message.text
    await FSMHistory.next()
    await message.answer(text=await get_question_history(5))


# @dp.message_handler(state=FSMHistory.question_5)
async def get_question_5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_5'] = message.text
    await FSMHistory.next()
    await message.answer(text=await get_question_history(6))


# @dp.message_handler(state=FSMHistory.question_6)
async def get_question_6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_6'] = message.text
        data_dict = dict(data.items())
        await down_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
        await down_history(message.from_user.id, data_dict)
    await FSMHistory.next()
    await message.answer(text="Дякую, шо поділився", reply_markup=get_request_kb())


# @dp.message_handler(state=FSMHistory.push)
async def push_pdf(message: types.Message, state: FSMContext):
    history_list_answers, time = await load_pdf_history_answers(message.from_user.id)
    history_list_questions = await load_pdf_history_questions()
    pdf = create_pdf_history(json.loads(history_list_answers), history_list_questions, time)
    pdf_file = types.InputFile(pdf, filename=f"Моя історія {message.from_user.first_name}.pdf")
    await message.answer_document(pdf_file, caption="Дані у форматі PDF", reply_markup=get_ok_kb())
    await state.finish()


def register_handlers_history(dp: Dispatcher):
    dp.register_message_handler(get_request, Text(equals="Написання історії", ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_message_handler(get_question_1, state=FSMHistory.question_1)
    dp.register_message_handler(get_question_2, state=FSMHistory.question_2)
    dp.register_message_handler(get_question_3, state=FSMHistory.question_3)
    dp.register_message_handler(get_question_4, state=FSMHistory.question_4)
    dp.register_message_handler(get_question_5, state=FSMHistory.question_5)
    dp.register_message_handler(get_question_6, state=FSMHistory.question_6)
    dp.register_message_handler(push_pdf, state=FSMHistory.push)