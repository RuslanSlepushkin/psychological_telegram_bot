import json

from aiogram import types, Dispatcher
from telegram.fsm.fsm_bai import FSMBai
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from telegram.pdf.pdf_bai import create_pdf_bai
from telegram.keyboards.keyboard_inline import get_bai_kb
from telegram.keyboards.keybords_default import get_request_kb, get_ok_kb
from telegram.data_base.db_bai import get_question_bai, get_text_bai, down_bai, down_user, load_pdf_bai_answers, \
    load_pdf_bai_questions


# @dp.message_handler(Text(equals='Шкала Тривоги Бека', ignore_case=True), state=None)
async def get_request(message: types.Message):
    await FSMBai.question_1.set()
    await message.answer(text=await get_text_bai(1))
    await message.answer(text=await get_question_bai(1), reply_markup=get_bai_kb())


# @dp.message_handler(state="*", commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(text="Переходь до мети", reply_markup=get_ok_kb())


# @dp.callback_query_handler(state=FSMBai.question_1)
async def get_question_1(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_1"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(2), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_2)
async def get_question_2(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_2"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(3), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_3)
async def get_question_3(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_3"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(4), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_4)
async def get_question_4(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_4"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(5), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_5)
async def get_question_5(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_5"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(6), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_6)
async def get_question_6(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_6"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(7), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_7)
async def get_question_7(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_7"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(8), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_8)
async def get_question_8(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_8"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(9), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_9)
async def get_question_9(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_9"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(10), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_10)
async def get_question_10(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_10"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(11), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_11)
async def get_question_11(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_11"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(12), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_12)
async def get_question_12(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_12"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(13), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_13)
async def get_question_13(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_13"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(14), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_14)
async def get_question_14(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_14"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(15), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_15)
async def get_question_15(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_15"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(16), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_16)
async def get_question_16(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_16"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(17), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_17)
async def get_question_17(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_17"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(18), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_18)
async def get_question_18(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_18"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(19), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_19)
async def get_question_19(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_19"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(20), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_20)
async def get_question_20(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_20"] = callback.data
    await FSMBai.next()
    await callback.message.answer(text=await get_question_bai(21), reply_markup=get_bai_kb())


# @dp.callback_query_handler(state=FSMBai.question_21)
async def get_question_21(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["question_21"] = callback.data
        data_dict = dict(data.items())
        result = sum(int(value) for value in data_dict.values())
        await down_user(callback.from_user.id, callback.from_user.username,
                        callback.from_user.first_name)
        await down_bai(callback.from_user.id, data_dict, result)
    await FSMBai.next()
    if result <= 5:
        await callback.message.answer(text=f"Кількість балів - {result}")
        await callback.message.answer(text=await get_text_bai(2), reply_markup=get_request_kb())
    elif result <= 8:
        await callback.message.answer(text=f"Кількість балів - {result}")
        await callback.message.answer(text=await get_text_bai(3), reply_markup=get_request_kb())
    elif result <= 18:
        await callback.message.answer(text=f"Кількість балів - {result}")
        await callback.message.answer(text=await get_text_bai(4), reply_markup=get_request_kb())
    elif result > 18:
        await callback.message.answer(text=f"Кількість балів - {result}")
        await callback.message.answer(text=await get_text_bai(5), reply_markup=get_request_kb())


# @dp.message_handler(state=FSMBai.push_pdf)
async def push_pdf(message: types.Message, state: FSMContext):
    bai_list_answers, result, time = await load_pdf_bai_answers(message.from_user.id)
    bai_list_questions = await load_pdf_bai_questions()
    pdf = create_pdf_bai(json.loads(bai_list_answers), bai_list_questions, result, time)
    pdf_file = types.InputFile(pdf, filename=f"Шкала тривоги Бека результат {message.from_user.first_name}.pdf")
    await message.answer_document(pdf_file, caption="Дані у форматі PDF", reply_markup=get_ok_kb())
    await state.finish()


def register_handlers_bai(dp: Dispatcher):
    dp.register_message_handler(get_request, Text(equals='Шкала Тривоги Бека', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_callback_query_handler(get_question_1, state=FSMBai.question_1)
    dp.register_callback_query_handler(get_question_2, state=FSMBai.question_2)
    dp.register_callback_query_handler(get_question_3, state=FSMBai.question_3)
    dp.register_callback_query_handler(get_question_4, state=FSMBai.question_4)
    dp.register_callback_query_handler(get_question_5, state=FSMBai.question_5)
    dp.register_callback_query_handler(get_question_6, state=FSMBai.question_6)
    dp.register_callback_query_handler(get_question_7, state=FSMBai.question_7)
    dp.register_callback_query_handler(get_question_8, state=FSMBai.question_8)
    dp.register_callback_query_handler(get_question_9, state=FSMBai.question_9)
    dp.register_callback_query_handler(get_question_10, state=FSMBai.question_10)
    dp.register_callback_query_handler(get_question_11, state=FSMBai.question_11)
    dp.register_callback_query_handler(get_question_12, state=FSMBai.question_12)
    dp.register_callback_query_handler(get_question_13, state=FSMBai.question_13)
    dp.register_callback_query_handler(get_question_14, state=FSMBai.question_14)
    dp.register_callback_query_handler(get_question_15, state=FSMBai.question_15)
    dp.register_callback_query_handler(get_question_16, state=FSMBai.question_16)
    dp.register_callback_query_handler(get_question_17, state=FSMBai.question_17)
    dp.register_callback_query_handler(get_question_18, state=FSMBai.question_18)
    dp.register_callback_query_handler(get_question_19, state=FSMBai.question_19)
    dp.register_callback_query_handler(get_question_20, state=FSMBai.question_20)
    dp.register_callback_query_handler(get_question_21, state=FSMBai.question_21)
    dp.register_message_handler(push_pdf, state=FSMBai.push_pdf)
