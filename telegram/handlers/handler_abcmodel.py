from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from telegram.fsm.fsm_abcmodel import FSMABCModel
from telegram.keyboards.keybords_default import get_yes_kb, get_ok_kb
from telegram.data_base.db_abcmodel import get_question_abcmodel, get_text_abcmodel, down_abcmodel


# @dp.message_handler(Text(equals='Далі', ignore_case=True), state=None)
async def get_abc(message: types.Message):
    await FSMABCModel.question_1.set()
    await message.answer(text=await get_text_abcmodel(1))
    await message.answer(text=await get_question_abcmodel(1))


# @dp.message_handler(state="*", commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer(text="Переходь до мети", reply_markup=get_ok_kb())


# @dp.message_handler(state=FSMABCModel.question_1)
async def get_question_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_1'] = message.text
    await FSMABCModel.next()
    await message.answer(text=await get_question_abcmodel(2))
    await message.answer(text=await get_text_abcmodel(2))


# @dp.message_handler(state=FSMABCModel.question_2)
async def get_question_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_2'] = message.text
    await FSMABCModel.next()
    await message.answer(text=await get_question_abcmodel(3))
    await message.answer(text=await get_text_abcmodel(3))


# @dp.message_handler(state=FSMABCModel.question_3)
async def get_question_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_3'] = message.text
    await FSMABCModel.next()
    await message.answer(text=await get_text_abcmodel(4))
    await message.answer(text=await get_question_abcmodel(4))


# @dp.message_handler(state=FSMABCModel.question_4)
async def get_question_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_4'] = message.text
    await FSMABCModel.next()
    await message.answer(text=await get_question_abcmodel(5))


# @dp.message_handler(state=FSMABCModel.arrow)
async def go_arrow(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_5'] = message.text
        data_dict = dict(data.items())
        await down_abcmodel(message.from_user.id, data_dict)
    await state.finish()
    await message.answer(text=await get_text_abcmodel(5), reply_markup=get_yes_kb())


def register_handlers_abcmodel(dp: Dispatcher):
    dp.register_message_handler(get_abc, Text(equals='Далі', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_message_handler(get_question_1, state=FSMABCModel.question_1)
    dp.register_message_handler(get_question_2, state=FSMABCModel.question_2)
    dp.register_message_handler(get_question_3, state=FSMABCModel.question_3)
    dp.register_message_handler(get_question_4, state=FSMABCModel.question_4)
    dp.register_message_handler(go_arrow, state=FSMABCModel.arrow)