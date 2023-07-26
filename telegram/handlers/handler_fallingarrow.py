import json

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from telegram.pdf.pdf_request import create_pdf
from telegram.fsm.fsm_fallingarrow import FSMFallingArrow
from telegram.keyboards.keybords_default import get_ok_kb, get_request_kb
from telegram.data_base.db_abcmodel import load_pdf_abcmodel_answers, load_pdf_abc_questions
from telegram.data_base.db_worklist import load_pdf_worklist_questions, load_pdf_worklist_answers
from telegram.data_base.db_fallingarrow import get_text_fallingarrow, get_question_fallingarrow, down_fallingarrow, \
    load_pdf_fallingarrow_answers, load_pdf_fallingarrow_questions


# @dp.message_handler(Text(equals='Так', ignore_case=True), state=None)
async def get_next(message: types.Message):
    await FSMFallingArrow.question_0.set()
    await message.answer(text=await get_text_fallingarrow(1), reply_markup=get_ok_kb())


# @dp.message_handler(state="*", commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(text="Переходь до мети", reply_markup=get_ok_kb())


# @dp.message_handler(state=FSMFallingArrow.question_0)
async def get_question_1(message: types.Message):
    await FSMFallingArrow.next()
    await message.answer(text=await get_question_fallingarrow(1))


# @dp.message_handler(state=FSMFallingArrow.question_1)
async def get_question_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_1'] = message.text
    await FSMFallingArrow.next()
    await message.answer(text=await get_question_fallingarrow(2))


# @dp.message_handler(state=FSMFallingArrow.question_2)
async def get_question_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_2'] = message.text
    await FSMFallingArrow.next()
    await message.answer(text=await get_question_fallingarrow(3))


# @dp.message_handler(state=FSMFallingArrow.question_3)
async def get_question_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_3'] = message.text
    await FSMFallingArrow.next()
    await message.answer(text=await get_question_fallingarrow(4))


# @dp.message_handler(state=FSMFallingArrow.question_4)
async def get_question_5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_4'] = message.text
    await FSMFallingArrow.next()
    question_5 = await get_question_fallingarrow(5)
    await message.answer(text=question_5)


# @dp.message_handler(state=FSMFallingArrow.question_5)
async def get_question_6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_5'] = message.text
    await FSMFallingArrow.next()
    await message.answer(text=await get_question_fallingarrow(6))


# @dp.message_handler(state=FSMFallingArrow.question_6)
async def get_question_7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_6'] = message.text
    await FSMFallingArrow.next()
    await message.answer(text=await get_question_fallingarrow(7))


# @dp.message_handler(state=FSMFallingArrow.question_7)
async def get_question_8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_7'] = message.text
    await FSMFallingArrow.next()
    await message.answer(text=await get_question_fallingarrow(8))


# @dp.message_handler(state=FSMFallingArrow.question_8)
async def get_question_9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_8'] = message.text
        data_dict = dict(data.items())
        await down_fallingarrow(message.from_user.id, data_dict)
    await FSMFallingArrow.next()
    await message.answer(text=await get_text_fallingarrow(8), reply_markup=get_request_kb())


# @dp.message_handler(state=FSMFallingArrow.push_pdf)
async def push_pdf(message: types.Message, state: FSMContext):
    work_list_answer = await load_pdf_worklist_answers(message.from_user.id)
    abc_model_answer = await load_pdf_abcmodel_answers(message.from_user.id)
    falling_arrow_answer = await load_pdf_fallingarrow_answers(message.from_user.id)
    work_list_questions = await load_pdf_worklist_questions()
    abc_model_questions = await load_pdf_abc_questions()
    falling_arrow_questions = await load_pdf_fallingarrow_questions()
    pdf = create_pdf(json.loads(work_list_answer), json.loads(abc_model_answer), json.loads(falling_arrow_answer),
                     work_list_questions, abc_model_questions, falling_arrow_questions)
    pdf_file = types.InputFile(pdf, filename=f"Запит {message.from_user.first_name}.pdf")
    await message.answer_document(pdf_file, caption="Дані у форматі PDF", reply_markup=get_ok_kb())
    await state.finish()


def register_handlers_fallingarrow(dp: Dispatcher):
    dp.register_message_handler(get_next, Text(equals='Так', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_message_handler(get_question_1, state=FSMFallingArrow.question_0)
    dp.register_message_handler(get_question_2, state=FSMFallingArrow.question_1)
    dp.register_message_handler(get_question_3, state=FSMFallingArrow.question_2)
    dp.register_message_handler(get_question_4, state=FSMFallingArrow.question_3)
    dp.register_message_handler(get_question_5, state=FSMFallingArrow.question_4)
    dp.register_message_handler(get_question_6, state=FSMFallingArrow.question_5)
    dp.register_message_handler(get_question_7, state=FSMFallingArrow.question_6)
    dp.register_message_handler(get_question_8, state=FSMFallingArrow.question_7)
    dp.register_message_handler(get_question_9, state=FSMFallingArrow.question_8)
    dp.register_message_handler(push_pdf, state=FSMFallingArrow.push_pdf)
